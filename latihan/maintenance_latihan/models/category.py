from odoo import _, api, fields, models


class Category(models.Model):
    _name = 'category'
    _description = 'Category for Maintenance'

    name = fields.Char(string='Category')
    active = fields.Boolean(string='Active', default=True)
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
    