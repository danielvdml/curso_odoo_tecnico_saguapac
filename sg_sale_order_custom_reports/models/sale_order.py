from odoo import models,fields

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def saludo(self,cliente):
        return f"Holaaaa {cliente}"


    footer_page_sale = fields.Html(compute="compute_footer_page")

    def compute_footer_page(self):
        for record in self:
            ICP = self.env["ir.config_parameter"].sudo()
            record.footer_page_sale =  ICP.get_param("footer_page_sale",default="")
