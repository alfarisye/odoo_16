from odoo import _, api, fields, models


class Brand(models.Model):
    _name = 'service.type'
    _description = 'Service Type for Equipment'

    service_type = fields.Char(string='Service Type')
    active = fields.Boolean(string='Active', default=True)
  
   
