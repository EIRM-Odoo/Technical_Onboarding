from odoo import fields,models

class Course(models.Model):
    _name = "academy.course"
    _description = "Course Info"
   
    # Other way to define a name without reserved word
    # _rec_name = "course_name"

    # course_name = fields.Char(string="Title", required=True)
    
    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)
    
    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner', 'Beginner'),
                                 ('intermediate', 'Intermediate'),
                                 ('advanced', 'Advanced'),
                             ],
                             copy=False)
    


