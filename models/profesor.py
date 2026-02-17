from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'edu.profesor'
    _description = 'Profesor'
    _rec_name = 'nombre'

    nombre = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    email = fields.Char(string='Email', required=True)
    titulacion = fields.Char(string='Titulación', required=True)
    
    # Relación One2many: Un profesor imparte muchas sesiones
    sesion_ids = fields.One2many('edu.sesion', 'profesor_id', string='Sesiones')
    
    # Relación Many2many: Un profesor puede enseñar muchos cursos
    curso_ids = fields.Many2many('edu.curso', string='Cursos que Imparte')

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
