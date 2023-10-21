from odoo import models,fields,api
from odoo.addons.sg_sale_descuentos_sucesivos.utils.utils import validar_carnet_identidad,validar_nit
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    check_numero_identidad = fields.Boolean("Check Número Identidad")

    def __validar_numero_identidad(self):
        return validar_carnet_identidad(self.vat)
    
    def validacion_masiva(self):
        for record in self:
            record.check_numero_identidad = record.__validar_numero_identidad()

        """
        msg = "Usted ha seleccionado los siguentes elementos:\n"
        for record in self:
            msg += f"{record.name} el numero de identidad: {record.vat or ''} es {'válido' if record.__validar_numero_identidad() else 'inválido'} \n"
        
        raise UserError(msg)
        """