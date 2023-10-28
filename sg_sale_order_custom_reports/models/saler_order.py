from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def saludo(self,cliente):
        return f"Holaaaa {cliente}"