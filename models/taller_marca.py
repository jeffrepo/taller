from odoo import models, fields

class TallerMarca(models.Model):
    _name = 'taller.marca'
    _description = 'Marca del vehículo'
    
    name = fields.Char('Nombre')
