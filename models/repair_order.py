from odoo import models, fields

class Repair(models.Model):
    _inherit = 'repair.order'
    _description = 'Repair Order'

    vehiculo_id = fields.Many2one('taller.vehiculo', 'Vehiculo')
