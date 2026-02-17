from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Sesion(models.Model):
    _name = 'edu.sesion'
    _description = 'Sesión de Curso'
    _rec_name = 'fecha_inicio'

    # Relación Many2one: Una sesión pertenece a un curso
    curso_id = fields.Many2one('edu.curso', string='Curso', required=True, ondelete='cascade')
    
    fecha_inicio = fields.Datetime(string='Fecha de Inicio', required=True)
    duracion_horas = fields.Float(string='Duración (horas)', required=True, default=1.0)
    num_asientos = fields.Integer(string='Número de Asientos', required=True, default=1)
    
    # Relación Many2one: Una sesión tiene un profesor
    profesor_id = fields.Many2one('edu.profesor', string='Profesor', ondelete='set null')
    
    # Relación Many2many: Una sesión tiene muchos alumnos
    alumno_ids = fields.Many2many('edu.alumno', string='Alumnos Inscritos')
    
    # Relación Many2one: Una sesión pertenece a una clase
    clase_id = fields.Many2one('edu.clase', string='Clase', required=True, ondelete='cascade')

    color = fields.Integer(string='Color', default=0)

    # --- CAMPOS COMPUTADOS ---
    
    asientos_ocupados = fields.Integer(
        string='Asientos Ocupados', 
        compute='_compute_asientos_ocupados', 
        store=True
    )
    porcentaje_ocupacion = fields.Float(
        string='Porcentaje de Ocupación', 
        compute='_compute_porcentaje_ocupacion', 
        store=True
    )

    @api.depends('alumno_ids')
    def _compute_asientos_ocupados(self):
        for record in self:
            record.asientos_ocupados = len(record.alumno_ids)

    @api.depends('asientos_ocupados', 'num_asientos')
    def _compute_porcentaje_ocupacion(self):
        for record in self:
            if record.num_asientos > 0:
                record.porcentaje_ocupacion = (record.asientos_ocupados / record.num_asientos) * 100
            else:
                record.porcentaje_ocupacion = 0.0

    # --- VALIDACIONES (@api.constrains) ---

    @api.constrains('profesor_id', 'fecha_inicio', 'duracion_horas')
    def _check_profesor_disponibilidad(self):
        for record in self:
            if not record.profesor_id or not record.fecha_inicio:
                continue
            
            # Calcular fin de la sesión actual
            inicio_actual = record.fecha_inicio
            fin_actual = inicio_actual + timedelta(hours=record.duracion_horas)
            
            # Buscar otras sesiones del mismo profesor que se solapen
            # Una sesión se solapa si empieza antes de que termine la actual O termina después de que empiece la actual
            # Excluimos la sesión actual de la búsqueda
            overlapping_sessions = self.env['edu.sesion'].search([
                ('id', '!=', record.id),
                ('profesor_id', '=', record.profesor_id.id),
                ('fecha_inicio', '<', fin_actual),
            ])
            
            for session in overlapping_sessions:
                inicio_otra = session.fecha_inicio
                fin_otra = inicio_otra + timedelta(hours=session.duracion_horas)
                
                # Comprobar solapamiento real
                if inicio_actual < fin_otra and inicio_otra < fin_actual:
                    raise ValidationError(
                        f"El profesor {record.profesor_id.nombre} ya tiene una sesión programada ({session.fecha_inicio}) "
                        f"que se solapa con este horario."
                    )

    @api.constrains('alumno_ids', 'num_asientos')
    def _check_asientos_disponibles(self):
        for record in self:
            if len(record.alumno_ids) > record.num_asientos:
                raise ValidationError(
                    f"No hay suficientes asientos disponibles. Inscritos: {len(record.alumno_ids)}, "
                    f"Plazas totales: {record.num_asientos}."
                )
