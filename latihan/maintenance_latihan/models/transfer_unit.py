from odoo import _, api, fields, models


class TransferUnit(models.Model):
    _name = 'transfer.unit'
    _description = 'Transfer Unit for Equipment'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    site_id = fields.Many2one(comodel_name='site', string='Site Origin')
    effective_date = fields.Date('Effective Date')

    transfer_unit_master = fields.Many2one(comodel_name='maintenance.equipment', 
                                            string='Transfer Master List')
    
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
