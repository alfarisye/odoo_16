from odoo import _, api, fields, models


class Site(models.Model):
    _name = 'site'
    _description = 'Site for Equipment'

    name = fields.Char(string='site')
    active = fields.Boolean(string='Active', default=True)
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
  