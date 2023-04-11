import re
import datetime
import calendar

from odoo import _, api, fields, models



class HitConditionMonitoring(models.Model):
    _name = 'hit.condition.monitoring'
    _description = 'Hit Condition Monitoring for Equipment'

    name = fields.Char(string='Name')
    active = fields.Boolean(string='Active', default=True)
    brand_id = fields.Many2one(
        comodel_name='brand', string='Brand')
    category_iid = fields.Many2one(
        comodel_name='category', string='Category')
    class_mainten_id = fields.Many2one(
        comodel_name='class.mainten', string='Class')
    model_mainten_id = fields.Many2one(
        comodel_name='model.mainten', string='Model')
    site_id = fields.Many2one(
        comodel_name='site', string='Site')
    description = fields.Char(string='Description')
    height = fields.Float(string='Height')
    length = fields.Float(string='Length')
    width = fields.Float(string='Width')
    weight = fields.Float(string='Weight')
    machine_code_id = fields.Many2one(
        comodel_name='machine.code', string='Machine Code')
    machine_type_id = fields.Many2one(
        comodel_name='machine.type', string='Machine Type')
    machine_category_id = fields.Many2one(
        comodel_name='machine.category', string='Machine Category')
    machine_group_id = fields.Many2one(
        comodel_name='machine.group', string='Machine Group')
    serial_number_id = fields.Char(string='Serial Number')
    manufacturing_year = fields.Integer(string='Manufacturing Year')
    target_id = fields.Many2one(
        comodel_name='service.type', string='Target')
    equipment_master_list_ids = fields.One2many('maintenance.request', 'equipment_master_list', string='Work Order Type')
    transfer_unit_ids = fields.One2many('transfer.unit', 'transfer_unit_master', string='Transfer Unit')
    parent_id = fields.Selection(
        string='Parent', selection=[('Pre - Maintenance', 'Schedule'), ('Repair', 'Unschedule'),
                                                     ('Servicing', 'Schedule'),  ('Backlog', 'Schedule')])
    category_text = fields.Char(string='Category')
    brand_text = fields.Char(string='Brand')
    model_text = fields.Char(string='Model')
    class_text = fields.Char(string='Class')
    name_text = fields.Char(string='Name')

    warranty_type = fields.Selection(
        string='warranty_type', selection=[('Pre - Maintenance', 'Schedule'), ('Repair', 'Unschedule')])
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    hourmater_ids = fields.Float(string='Hourmater')
    Kilometer_ids = fields.Float(string='Kilometer')

    tire_information_ids = fields.One2many('maintenance.equipment', 'equipment_tire_information', string='Tire Information')


    age_id = fields.Integer(string='Age', compute='_compute_age')

    @api.depends('manufacturing_year')
    def _compute_age(self):
        for record in self:
            if record.manufacturing_year:
                now = fields.Date.today()
                age = now.year - record.manufacturing_year
                record.age_id = age
            else:
                record.age_id = 0

    hourmater_id = fields.Many2one(
        comodel_name='measuring.utilization', string='Hourmater')
    kilometer_id = fields.Many2one(
        comodel_name='measuring.utilization', string='Kilometer')
    
    hourmater = fields.Integer(string="Hourmater", related='hourmater_id.hourmeter')
    kilomater = fields.Integer(string="Kilometer", related='kilometer_id.kilometer')

    accumulative_hourmeter = fields.Integer(string='Accumulative Hourmeter')
    accumulative_kilomater = fields.Integer(string='Accumulative Kilometer')

    stage_id = fields.Selection(string='warranty_type', selection=[('draf', 'Draf'), ('inprogress', 'In Progress'), ('done', 'Done')])


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            seq = self.env['ir.sequence'].next_by_code('equipment.master.list.seq')
            category = self.env['category'].browse(vals.get('category_iid', False))
            site = self.env['site'].browse(vals.get('site_id', False))
            name = '{}-{}-{}'.format(category.name or '', site.name or '', seq)
            vals.update({'name': name})
        return super(HitConditionMonitoring, self).create(vals_list)



    # breakpoint()
   
