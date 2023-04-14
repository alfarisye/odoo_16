from odoo import _, api, fields, models


class InheritMaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    equipment_master_list = fields.Many2one(comodel_name='maintenance.equipment', 
                                            string='Equipment Master List')
    work_order_type = fields.Selection(
        string='Work Order Type', selection=[('maintenance', 'Schedule'), ('Repair', 'Unschedule'),
                                                     ('Servicing', 'Schedule'),  ('Backlog', 'Schedule')])
    site_id = fields.Many2one(comodel_name='site', string='Site')
    demage_id = fields.Char(string='Demage') #sementara
    cause_id = fields.Char(string='Cause') #sementara

    planning_wo_ids = fields.One2many('planning', 'planning_wo', string='Planning')

    schedule_start = fields.Datetime('Schedule Start')
    schedule_finish = fields.Datetime('Schedule Finish')
    actual_start = fields.Datetime('Actual Start')
    actual_finish = fields.Datetime('Actual Finish')

class Planning (models.Model):
    _name = 'planning' 
    _description = 'Maintenance Request Tab'


    schedule_start = fields.Datetime('Schedule Start')
    schedule_finish = fields.Datetime('Schedule Finish')
    actual_start = fields.Datetime('Actual Start')
    actual_finish = fields.Datetime('Actual Finish')

    planning_wo = fields.Many2one(comodel_name='maintenance.request', 
                                            string='Planning')