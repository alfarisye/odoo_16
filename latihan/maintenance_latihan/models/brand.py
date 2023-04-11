from odoo import _, api, fields, models


class Brand(models.Model):
    _name = 'brand'
    _description = 'Brand for Equipment'

    name = fields.Char(string='Brand')
    active = fields.Boolean(string='Active', default=True)
   
