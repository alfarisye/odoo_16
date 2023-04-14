from odoo import _, api, fields, models


class MeasuringUtilization(models.Model):
    _name = 'measuring.utilization'
    _description = 'Measuring Utilization for Equipment'

    date_measuring = fields.Date('Date Measuring')
    measuring_type = fields.Selection(string='Measuring Type', 
                                      selection=[('hourmeter', 'Hourmater'), ('kilometer', 'Kilometer')])
    start_measuring = fields.Integer('Start')
    end_measuring = fields.Integer('End')
    run_time = fields.Integer(string='Run Time', compute='_compute_run_time')

    utilization_id = fields.Many2one(comodel_name='measuring.reading', 
                                                 string='Mater Utilization')
   
    @api.depends('start_measuring', 'end_measuring')
    def _compute_run_time(self):
        for record in self:
            record.run_time = record.end_measuring - record.start_measuring
    