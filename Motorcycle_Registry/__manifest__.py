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
    'depends' : ['base'],
    'data' : [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'views/registry_menuitems.xml',
        'views/registry_views.xml'
    ],
    'demo' : [
        'demo/registry_demo.xml',
    ],
    'application' : True,
}