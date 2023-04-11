from odoo import _, api, fields, models


class Site(models.Model):
    _name = 'site'
    _description = 'Site for Equipment'

    name = fields.Char(string='site')
    active = fields.Boolean(string='Active', default=True)
  