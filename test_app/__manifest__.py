{
    'name' : 'First Module',
    'summary' : """Module to test and learn Odoo""",
    'description' : """Module to Learn:
        -Odoo
        """,
    'license' : 'OPL-1',
    'author' : 'Edgar Rostro',
    'website' : 'www.odoo.com',
    'category' : 'Custom Modules/Tech Training',
    'depends' : ['sale', 'website'],
    'data' : [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/academy_web_templates.xml',
    ],
    'demo' : [
        'demo/course_demo.xml',
    ],
    'application' : True,
}