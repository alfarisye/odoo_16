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