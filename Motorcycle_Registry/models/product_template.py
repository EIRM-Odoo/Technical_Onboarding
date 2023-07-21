from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    make = fields.Char(string="Make")
    model = fields.Char(string="Model")
    year = fields.Char(string="Year")
    curbw = fields.Float(string="Curb Weight")
    date = fields.Date(string="Launch Date")

    batteryc = fields.Char(string="Battery Capacity")
    char_time = fields.Float(string="Charge Time")
    range = fields.Float(string="Range")

    hp = fields.Float(string="Horsepower")
    tspeed = fields.Float(string="Top Speed")
    torque = fields.Float(string="Torque")


    detailed_type = fields.Selection(selection_add=[('motorcycle', 'Motorcycle'),], ondelete={'motorcycle': 'set product'})

    def _detailed_type_mapping(self):
        return {'motorcycle':'product'}
    

    