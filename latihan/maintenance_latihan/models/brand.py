from odoo import _, api, fields, models


class Brand(models.Model):
    _name = 'brand'
    _description = 'Brand for Equipment'

    name = fields.Char(string='Brand')
    active = fields.Boolean(string='Active', default=True)
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
   
