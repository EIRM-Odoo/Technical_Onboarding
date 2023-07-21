from odoo import api,fields,models
from odoo.exceptions import ValidationError
import re

class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"


    registry_number = fields.Char(string="Registry Number", default="MRN0000", copy=False, required=True, readonly=True)

    active = fields.Boolean(string="Active", default=True)

    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    picture = fields.Image("Picture", max_width=240, max_height=180)
    current_mileage = fields.Float("Current Mileage", digits="Miles")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Binary("Certificate Title")
    register_date = fields.Date(string="Register Date")

    _sql_constraints= [("unique_vin", "unique(vin)", "VIN already registred.")]

    partner_id = fields.Many2one(comodel_name="res.partner", string="Owner")

    phone = fields.Char(string="Phone", related="partner_id.phone")
    email = fields.Char(string="Email", related="partner_id.email")

    make = fields.Char(string="Make", compute="_compute_calculate_make")
    model = fields.Char(string="Model", compute="_compute_calculate_model")
    year = fields.Char(string="Year", compute="_compute_calculate_year")


    @api.model_create_multi
    def create(self, num_list):
        for num in num_list:
            if num.get('registry_number', ('MRN0000')) == ('MRN0000'):
                num['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(num_list)
    
    @api.constrains('vin')
    def _check_vin(self):
        for registry in self:
            if(re.search("^[A-Z]{4}\d\d[A-Z0-9]{2}[0-9]{6}", registry.vin) == None):
                raise ValidationError('The VIN does not have the correct format.')
            
    @api.constrains('license_plate')
    def _check_license_plate(self):
        for registry in self:
            if(re.search("^[A-Z]{1,4}[\d]{1,3}[A-Z]{0,3}$", registry.license_plate) == None):
                raise ValidationError('The License Plate does not have the correct format.')

    @api.depends("vin")        
    def _compute_calculate_make(self):
        for record in self:
            if record.vin:
                record.make = record.vin[0:2]
    
    @api.depends("vin")        
    def _compute_calculate_model(self):
        for record in self:
            if record.vin:
                record.model = record.vin[2:4]
    
    @api.depends("vin")        
    def _compute_calculate_year(self):
        for record in self:
            if record.vin:
                record.year = record.vin[4:6]
    