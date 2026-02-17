{
    'name': "EduOdoo - Sistema Integral de Gestión para Academia",

    'summary': "Sistema completo para gestión de cursos, sesiones, alumnos y facturación",

    'description': """
Sistema Integral de Gestión para una Academia de Cursos (EduOdoo)
============================================================
Módulo educativo que permite gestionar:
- Cursos con diferentes niveles (A1-C2)
- Sesiones y horarios de clases
- Registro de alumnos
- Matrículas con flujo de estados
- Facturación y control de pagos
- Relaciones entre componentes (alumnos, cursos, sesiones)
    """,

    'author': "Jacob - DAM",
    'website': "https://www.tuempresa.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

