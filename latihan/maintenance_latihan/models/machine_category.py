from odoo import _, api, fields, models


class MachineCategory(models.Model):
    _name = 'machine.category'
    _description = 'Machine Category for Equipment'

    name = fields.Char(string='Machine category')
    active = fields.Boolean(string='Active', default=True)
   
