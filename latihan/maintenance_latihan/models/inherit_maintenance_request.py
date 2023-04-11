from odoo import _, api, fields, models


class InheritMaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    equipment_master_list = fields.Many2one(comodel_name='hit.condition.monitoring', 
                                            string='Equipment Master List')
    work_order_type = fields.Selection(
        string='Work Order Type', selection=[('Pre - Maintenance', 'Schedule'), ('Repair', 'Unschedule'),
                                                     ('Servicing', 'Schedule'),  ('Backlog', 'Schedule')])
    site_id = fields.Many2one(comodel_name='site', string='Site')
    demage_id = fields.Char(string='Demage') #sementara
    cause_id = fields.Char(string='Cause') #sementara