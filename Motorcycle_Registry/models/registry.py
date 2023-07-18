from odoo import fields,models

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"


    registry_number = fields.Char(string="Registry Number", required=True)
    active = fields.Boolean(string="Active", default=True)

    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image("Picture", max_width=740, max_height=620)
    current_mileage = fields.Float("Current Mileage", digits="Miles")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Binary("Certificate Title")
    register_date = fields.Date(string="Register Date")

