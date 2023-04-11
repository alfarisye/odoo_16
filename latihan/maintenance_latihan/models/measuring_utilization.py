from odoo import _, api, fields, models


class MeasuringUtilization(models.Model):
    _name = 'measuring.utilization'
    _description = 'Measuring Utilization for Equipment'

    
    hourmeter = fields.Integer(string='Hourmeter')
    kilometer = fields.Integer(string='Kilometer')
    

    measuring_reading_id = fields.Many2one(comodel_name='measuring.reading', string='Measuring Reading')