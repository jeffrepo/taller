from odoo import models, fields

class TallerLinea(models.Model):
    _name = 'taller.linea'
    _description = 'Línea del vehículo'
    
    name = fields.Char('Nombre')
