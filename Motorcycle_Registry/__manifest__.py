{
    'name' : 'Motorcycle Registry',
    'summary' : """Manage Registration of Motorcycles""",
    'description' : """Motorcycle Registry
        ====================
        This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license' : 'OPL-1',
    'author' : 'EIRM-Odoo',
    'website' : 'https://github.com/EIRM-Odoo/Technical_Onboarding',
    'category' : 'Custom Modules/Kawiil',
    'depends' : ['stock', 'website'],
    'data' : [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'data/registry_data.xml',
        'views/registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_views_inherit.xml',
        'views/registry_web_templates.xml',
    ],
    'demo' : [
        'demo/registry_demo.xml',
    ],
    'application' : True,
}