from odoo import _, api, fields, models


class ModelMainten(models.Model):
    _name = 'model.mainten'
    _description = 'Model for Equipment'

    name = fields.Char(string='Model')
    active = fields.Boolean(string='Active', default=True)
