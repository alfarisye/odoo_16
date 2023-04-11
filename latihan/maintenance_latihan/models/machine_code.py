from odoo import _, api, fields, models


class MachineCode(models.Model):
    _name = 'machine.code'
    _description = 'Machine Code for Equipment'

    name = fields.Char(string='Machine Code')
    active = fields.Boolean(string='Active', default=True)
   
