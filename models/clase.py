from odoo import models, fields, api


class Clase(models.Model):
    _name = 'edu.clase'
    _description = 'Clase'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre de la Clase', required=True)
    descripcion = fields.Text(string='Descripción')
    horario = fields.Char(string='Horario', required=True)
    grupo = fields.Char(string='Grupo', required=True)
    
    # Relación Many2one: Una clase está asociada a un curso
    curso_id = fields.Many2one('edu.curso', string='Curso', required=True, ondelete='cascade')
    
    # Relación One2many: Una clase tiene muchas sesiones
    sesion_ids = fields.One2many('edu.sesion', 'clase_id', string='Sesiones')
    
    # Relación Many2many: Una clase tiene muchos alumnos
    alumno_ids = fields.Many2many('edu.alumno', string='Alumnos de la Clase')

    def __str__(self):
        return self.nombre
