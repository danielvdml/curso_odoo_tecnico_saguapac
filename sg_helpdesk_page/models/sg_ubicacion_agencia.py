from odoo import models,fields

class SGUbicacionAgencia(models.Model):
    _name = "sg.ubicacion.agencia"
    _description = "Ubicación de la agencia"
    
    name = fields.Char(string="Nombre",required=True)