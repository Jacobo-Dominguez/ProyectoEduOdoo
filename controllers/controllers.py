# from odoo import http


# class ProyectoEduOdoo(http.Controller):
#     @http.route('/proyecto_edu_odoo/proyecto_edu_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto_edu_odoo/proyecto_edu_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto_edu_odoo.listing', {
#             'root': '/proyecto_edu_odoo/proyecto_edu_odoo',
#             'objects': http.request.env['proyecto_edu_odoo.proyecto_edu_odoo'].search([]),
#         })

#     @http.route('/proyecto_edu_odoo/proyecto_edu_odoo/objects/<model("proyecto_edu_odoo.proyecto_edu_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto_edu_odoo.object', {
#             'object': obj
#         })

