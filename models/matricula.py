from odoo import models, fields, api


class Matricula(models.Model):
    _name = 'edu.matricula'
    _description = 'Matrícula de Alumno'
    _rec_name = 'alumno_id'

    alumno_id = fields.Many2one('edu.alumno', string='Alumno', required=True, ondelete='cascade')
    curso_id = fields.Many2one('edu.curso', string='Curso', required=True, ondelete='cascade')
    fecha_matricula = fields.Date(string='Fecha de Matrícula', default=fields.Date.today, readonly=True)
    
    state = fields.Selection(
        [
            ('borrador', 'En borrador'),
            ('confirmada', 'Confirmada'),
            ('pagada', 'Pagada'),
        ],
        string='Estado',
        default='borrador',
        required=True
    )

    def action_confirmar(self):
        for record in self:
            if record.state == 'borrador':
                record.state = 'confirmada'

    def action_pagar(self):
        for record in self:
            if record.state == 'confirmada':
                record.state = 'pagada'

    def action_borrador(self):
        for record in self:
            record.state = 'borrador'
