from odoo import models,fields,api


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    ubicacion_agencia_id = fields.Many2one("sg.ubicacion.agencia",string="Ubicación de la agencia   ")


    def hace_algo(self,valor):
        results = []
        for record in self:
            results.append(f"{record.name} - {valor}")
        return results

    @api.model
    def busqueda_por_cliente(self,keyword):
        results = self.search_read([("partner_id.name","ilike",f"%{keyword}%")],["id","name","description"])
        return results