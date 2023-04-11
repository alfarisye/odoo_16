from odoo import _, api, fields, models


class MachineGroup(models.Model):
    _name = 'machine.group'
    _description = 'Machine Group for Equipment'

    name = fields.Char(string='Machine group')
    active = fields.Boolean(string='Active', default=True)
   
