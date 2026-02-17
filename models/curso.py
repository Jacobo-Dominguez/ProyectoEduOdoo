from odoo import models, fields, api


class Curso(models.Model):
    _name = 'edu.curso'
    _description = 'Curso'
    _rec_name = 'titulo'

    titulo = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    nivel = fields.Selection(
        [
            ('A1', 'A1 - Principiante'),
            ('A2', 'A2 - Elemental'),
            ('B1', 'B1 - Intermedio'),
            ('B2', 'B2 - Intermedio-Alto'),
            ('C1', 'C1 - Avanzado'),
            ('C2', 'C2 - Maestría'),
        ],
        string='Nivel',
        required=True
    )
    precio = fields.Float(string='Precio', required=True)
    
    # Relación Many2many: Un curso tiene muchas sesiones
    sesion_ids = fields.One2many('edu.sesion', 'curso_id', string='Sesiones')
    
    # Relación Many2many: Un curso tiene muchos alumnos
    alumno_ids = fields.Many2many('edu.alumno', string='Alumnos')

    def __str__(self):
        return self.titulo
