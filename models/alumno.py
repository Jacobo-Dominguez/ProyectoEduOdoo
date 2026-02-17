from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'edu.alumno'
    _description = 'Alumno'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    email = fields.Char(string='Email', required=True)
    
    # Relación Many2many: Un alumno está inscrito en muchos cursos
    curso_ids = fields.Many2many('edu.curso', string='Cursos')
    
    # Relación Many2many: Un alumno asiste a muchas sesiones
    sesion_ids = fields.Many2many('edu.sesion', string='Sesiones')
    
    # Relación One2many: Un alumno puede tener muchas facturas
    facturacion_ids = fields.One2many('edu.facturacion', 'alumno_id', string='Facturas')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
