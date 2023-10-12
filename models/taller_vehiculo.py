from odoo import models, fields

class TallerVehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Vehículo'
	
    name = fields.Char(string='Placa del vehículo')
    marca = fields.Many2one('taller.marca',string="Marca")
    linea = fields.Many2one('taller.linea',string="Linea")
    modelo = fields.Integer(string='Modelo')
    transmision = fields.Selection([('mecanico', 'Mecánico'), ('automatico', 'Automático')], 'Transmisión')
    motor = fields.Char(string='Motor')
    vin = fields.Char(string='Vin')
    
class TallerVehiculo(models.Model):
    _name = 'taller.taller_vehiculo'
    _description = 'Vehículo 2'
