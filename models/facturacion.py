from odoo import models, fields, api


class Facturacion(models.Model):
    _name = 'edu.facturacion'
    _description = 'Facturación'
    _rec_name = 'numero_factura'

    numero_factura = fields.Char(string='Número de Factura', readonly=True, copy=False, tracking=True)
    
    # Relación Many2one: Una factura pertenece a un alumno
    alumno_id = fields.Many2one('edu.alumno', string='Alumno', required=True, ondelete='cascade')
    
    # Relación Many2one: Una factura está asociada a un curso
    curso_id = fields.Many2one('edu.curso', string='Curso', required=True, ondelete='cascade')
    
    cantidad = fields.Float(string='Cantidad', required=True)
    concepto = fields.Char(string='Concepto', required=True)
    fecha_pago = fields.Date(string='Fecha de Pago')
    estado_pago = fields.Selection(
        [
            ('pendiente', 'Pendiente'),
            ('pagado', 'Pagado'),
            ('cancelado', 'Cancelado'),
        ],
        string='Estado de Pago',
        default='pendiente'
    )
    fecha_creacion = fields.Date(string='Fecha de Creación', default=fields.Date.today, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        # Generar número de factura automáticamente si no existe
        for vals in vals_list:
            if not vals.get('numero_factura'):
                vals['numero_factura'] = self.env['ir.sequence'].next_by_code('edu.facturacion') or 'FAC-0001'
        return super().create(vals_list)

    def __str__(self):
        return self.numero_factura
