from odoo import _, api, fields, models


class MachineType(models.Model):
    _name = 'machine.type'
    _description = 'Machine type for Equipment'

    name = fields.Char(string='Machine type')
    active = fields.Boolean(string='Active', default=True)
   
