from odoo import _, api, fields, models


class InheritEquipment(models.Model):
    _inherit = 'maintenance.equipment'

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
    tire_s_n = fields.Char(string='Tire S/N')
    position = fields.Char(string='Position')

    equipment_tire_information = fields.Many2one(comodel_name='hit.condition.monitoring', 
                                                 string='Equipment Tire Information')
    
    target_id = fields.Many2one(comodel_name='service.type', string='Target')
    transfer_unit_ids = fields.One2many('transfer.unit', 'transfer_unit_master', string='Transfer Unit')


    eqip_parent_ids = fields.Many2one(comodel_name='maintenance.equipment', string='Parent ID')
    
    # category_text = fields.Many2one(
    #     comodel_name='category', related='eqip_parent_ids.category_iid')
    # brand_text = fields.Many2one(comodel_name='brand', related='eqip_parent_ids.brand_id')
    # model_text = fields.Many2one(comodel_name='model.mainten', related='eqip_parent_ids.model_mainten_id')
    # class_text = fields.Many2one(comodel_name='class.mainten', related='eqip_parent_ids.class_mainten_id')

    category_text = fields.Many2one(comodel_name='category')
    brand_text = fields.Many2one(comodel_name='brand')
    model_text = fields.Many2one(comodel_name='model.mainten')
    class_text = fields.Many2one(comodel_name='class.mainten')

    attachment_id = fields.Binary('attachment')
    
    

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
    
    accumulative_hourmeter_id = fields.Integer(string='Accumulative Hourmeter', compute='_compute_accumulative_hourmeter')
    accumulative_kilometer_id = fields.Integer(string='Accumulative Kilometer', compute='_compute_accumulative_kilomater')

    stage_id = fields.Selection(string='warranty_type', selection=[('draf', 'Draf'), ('inprogress', 'In Progress'), ('done', 'Done')])

    measuring_reading_ids = fields.One2many('measuring.reading', 'unit_id')
    
    kilometer = fields.Integer(string="Kilometer", compute="_compute_fields")
    hourmeter_1 = fields.Integer('Hourmeter', compute="_compute_fields")

    equipment_master_list_ids = fields.One2many('maintenance.request', 'equipment_master_list', string='Work Order Type', compute='_compute_work_order')
    transfer_unit_ids = fields.One2many('transfer.unit', 'transfer_unit_master', string='Transfer Unit', compute='_compute_transfer_information')

    def _compute_work_order(self):
        for yes in self:
            reading_ids = self.env['maintenance.request'].sudo().search([('equipment_id', '=', yes.id)], order="actual_start desc", limit=5)
            yes.equipment_master_list_ids = reading_ids

    def _compute_transfer_information(self):
        for yes in self:
            transfer_info = self.env['transfer.unit'].sudo().search([('unit_id', '=', yes.id)])
            yes.transfer_unit_ids = transfer_info

    def _compute_fields(self):
        for equipment in self:
            reading_ids = self.env['measuring.reading'].sudo().search([('unit_id', '=', equipment.id)])
            if not reading_ids:
                equipment.hourmeter_1 = 0
                equipment.kilometer = 0
                continue

            hour_util = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', reading_ids[0].id), ('measuring_type', '=', 'hourmeter')], order="date_measuring desc", limit=1)
            if not hour_util:
                equipment.hourmeter_1 = 0
            else:
                equipment.hourmeter_1 = hour_util.end_measuring

            km_util = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', reading_ids[0].id), ('measuring_type', '=', 'kilometer')], order="date_measuring desc", limit=1)
            if not km_util:
                equipment.kilometer = 0
            else:
                equipment.kilometer = km_util.end_measuring 

    # def _compute_hourmeter1(self):
    #     reading_ids = self.env['measuring.reading'].sudo().search([('unit_id', '=', self.id)])
    #     for raeding in reading_ids:
    #         util_ids = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', raeding.id), ('measuring_type', '=', 'hourmeter')], order="date_measuring desc", limit=1)
    #         self.hourmeter_1 = util_ids.run_time
            
    # def _compute_kilomater(self):
    #     reading_ids = self.env['measuring.reading'].sudo().search([('unit_id', '=', self.id)])
    #     for raeding in reading_ids:
    #         util_ids = self.env['measuring.utilization'].sudo().search([('utilization_id', '=', raeding.id), ('measuring_type', '=', 'kilometer')], order="date_measuring desc", limit=1)
    #         self.kilomater = util_ids.run_time

    @api.depends('measuring_reading_ids.accumulative_hourmeter')
    def _compute_accumulative_hourmeter(self):
        for equipment in self:
            hourmeter_total = 0
            for measuring_reading in equipment.measuring_reading_ids:
                hourmeter_total += measuring_reading.accumulative_hourmeter
            equipment.accumulative_hourmeter_id = hourmeter_total

    @api.depends('measuring_reading_ids.accumulative_kilomater')
    def _compute_accumulative_kilomater(self):
        for equipment in self:
            kilometer_total = 0
            for measuring_reading in equipment.measuring_reading_ids:
                kilometer_total += measuring_reading.accumulative_kilomater
            equipment.accumulative_kilometer_id = kilometer_total




    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            seq = self.env['ir.sequence'].next_by_code('equipment.master.list.seq')
            category = self.env['category'].browse(vals.get('category_iid', False))
            site = self.env['site'].browse(vals.get('site_id', False))
            name = '{}-{}-{}'.format(category.name or '', site.name or '', seq)
            vals.update({'name': name})
        return super(InheritEquipment, self).create(vals_list)

    @api.onchange('eqip_parent_ids')
    def onchange_eqip_parent_ids(self):
        if self.eqip_parent_ids:
            
            perent = self.eqip_parent_ids

            self.brand_text = perent.brand_id.id
            self.category_text = perent.category_iid.id
            self.class_text = perent.class_mainten_id.id
            self.model_text = perent.model_mainten_id.id

    # breakpoint()