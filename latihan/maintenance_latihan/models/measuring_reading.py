import re
import datetime
import calendar

from odoo import _, api, fields, models



class MeasuringReading(models.Model):
    _name = 'measuring.reading'
    _description = 'Measuring Reading for Equipment'

    hourmater_id = fields.Many2one(
        comodel_name='measuring.utilization', string='Hourmater', compute='_compute_hourmater_id')
    kilometer_id = fields.Many2one(
        comodel_name='measuring.utilization', string='Kilometer', compute='_compute_kilometer_id')

    accumulative_hourmeter = fields.Integer(string='Accumulative Hourmeter')
    accumulative_kilomater = fields.Integer(string='Accumulative Kilometer')

    # unit_id = fields.Integer(string="Hourmater", related='hourmater_id.unit_id')
    # unit_id = fields.Integer(string="Hourmater", related='kilometer_id.unit_id')

    # @api.depends('hourmeter')
    # def _compute_hourmater_id(self):
    #     for record in self:
    #         record.hourmater_id = self.env['measuring.utilization'].search([('unit_id', '=', record.hourmeter)], limit=1, order='create_date DESC').id

    # @api.depends('kilometer')
    # def _compute_kilometer_id(self):
    #     for record in self:
    #         record.kilometer_id = self.env['measuring.utilization'].search([('kilometer', '=', record.kilometer)], limit=1, order='create_date DESC').id