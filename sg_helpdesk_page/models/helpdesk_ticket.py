from odoo import models,fields


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    ubicacion_agencia_id = fields.Many2one("sg.ubicacion.agencia",string="Ubicación de la agencia   ")


