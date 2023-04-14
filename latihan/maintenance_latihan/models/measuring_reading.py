import re
import datetime
import calendar

from odoo import _, api, fields, models



class MeasuringReading(models.Model):
    _name = 'measuring.reading'
    _description = 'Measuring Reading for Equipment'

    
    unit_id = fields.Many2one(
        comodel_name='maintenance.equipment', string='Unit ID/Component ID', realate='unit_id.name')

    accumulative_hourmeter = fields.Integer(string='Accumulative Hourmeter', stored=False , compute='_compute_run_time_total')
    accumulative_kilomater = fields.Integer(string='Accumulative Kilometer', stored=False, compute='_compute_run_time_total_yes')

    measuring_utilization_ids = fields.One2many('measuring.utilization', 'utilization_id')
    
    @api.depends('measuring_utilization_ids.run_time', 'measuring_utilization_ids.measuring_type')
    def _compute_run_time_total(self):
        for record in self:
            accumulative_hourmeter = 0
            for utilization in record.measuring_utilization_ids:
                if utilization.measuring_type == 'hourmeter':
                    accumulative_hourmeter += utilization.run_time
            record.accumulative_hourmeter = accumulative_hourmeter
            if record.unit_id:
                record.unit_id.accumulative_hourmeter_id = accumulative_hourmeter


    @api.depends('measuring_utilization_ids.run_time', 'measuring_utilization_ids.measuring_type')
    def _compute_run_time_total_yes(self):
        for record in self:
            accumulative_kilomater = 0
            for utilization in record.measuring_utilization_ids:
                if utilization.measuring_type == 'kilometer':
                    accumulative_kilomater += utilization.run_time
            record.accumulative_kilomater = accumulative_kilomater
            if record.unit_id:
                record.unit_id.accumulative_kilometer_id = accumulative_kilomater

    def write(self, vals):
        result = super(MeasuringReading, self).write(vals)
        if 'accumulative_hourmeter' in vals:
            for record in self:
                if record.unit_id:
                    record.unit_id.accumulative_hourmeter_id = record.accumulative_hourmeter
        return result
    
    def write(self, vals):
        result = super(MeasuringReading, self).write(vals)
        if 'accumulative_kilomater' in vals:
            for record in self:
                if record.unit_id:
                    record.unit_id.accumulative_kilometer_id = record.accumulative_kilomater
        return result