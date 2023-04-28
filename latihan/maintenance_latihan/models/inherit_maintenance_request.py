from odoo import _, api, fields, models


class InheritMaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'


    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')
    
    equipment_master_list = fields.Many2one(comodel_name='maintenance.equipment', 
                                            string='Equipment Master List')
    
    work_order_type1 = fields.Selection(
        string='Work Order Type', selection=[('1', 'Pre - Maintenance(Schedule)'), ('2', 'Repair(Unschedule)'), 
                                             ('3', 'Servicing(Schedule)'), ('4', 'Backlog(Schedule)')])
    site_id = fields.Many2one(comodel_name='site', string='Site')
    demage_id = fields.Char(string='Demage') #sementara
    cause_id = fields.Char(string='Cause') #sementara

    planning_wo_ids = fields.One2many('planning', 'planning_wo', string='Planning')

    schedule_start = fields.Datetime('Schedule Start')
    schedule_finish = fields.Datetime('Schedule Finish')
    actual_start = fields.Datetime('Actual Start')
    actual_finish = fields.Datetime('Actual Finish')

    measuring_reading_ids = fields.One2many('measuring.reading', 'unit_id')

    kilometer = fields.Integer(string="Kilometer")
    hourmeter_1 = fields.Integer('Hourmeter' )

    
    # def _compute_fields(self):
    #     for yes in self:
    #         reading_ids = self.env['measuring.reading'].sudo().search([('unit_id', '=', yes.id)])
    #         for reading in reading_ids:
    #             hour_util = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', reading.id), ('measuring_type', '=', 'hourmeter')], order="date_measuring desc", limit=1)
    #             yes.hourmeter_1 = hour_util.end_measuring
    #             km_util = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', reading.id), ('measuring_type', '=', 'kilometer')], order="date_measuring desc", limit=1)
    #             yes.kilometer = km_util.end_measuring
    

class Planning (models.Model):
    _name = 'planning' 
    _description = 'Maintenance Request Tab'


    schedule_start = fields.Datetime('Schedule Start')
    schedule_finish = fields.Datetime('Schedule Finish')
    actual_start = fields.Datetime('Actual Start')
    actual_finish = fields.Datetime('Actual Finish')

    planning_wo = fields.Many2one(comodel_name='maintenance.request', 
                                            string='Planning')