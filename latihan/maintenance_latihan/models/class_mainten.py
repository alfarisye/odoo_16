from odoo import _, api, fields, models


class ClassMainten(models.Model):
    _name = 'class.mainten'
    _description = 'class for Equipment'

    name = fields.Char(string='Class')
    active = fields.Boolean(string='Active', default=True)
  