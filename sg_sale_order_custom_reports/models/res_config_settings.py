from odoo import fields,models,api


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    footer_page_sale = fields.Html("Pie de página para reporte de venta")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICP = self.env["ir.config_parameter"]
        footer_page_sale = ICP.get_param("footer_page_sale",default="")
        res.update(footer_page_sale=footer_page_sale)
        return res
    
    def set_values(self):
        super(ResConfigSettings, self).set_values() 
        ICP = self.env["ir.config_parameter"]
        ICP.set_param("footer_page_sale",self.footer_page_sale)
        