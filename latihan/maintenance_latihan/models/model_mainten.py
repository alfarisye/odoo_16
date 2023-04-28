from odoo import _, api, fields, models


class ModelMainten(models.Model):
    _name = 'model.mainten'
    _description = 'Model for Equipment'

    name = fields.Char(string='Model')
    active = fields.Boolean(string='Active', default=True)
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
