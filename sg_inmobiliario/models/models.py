from odoo import models,fields,api
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)


class TipoInmueble(models.Model):
    _name = "sg.tipo.inmueble"
    _description = "Tipo de Inmueble"

    name = fields.Char("Nombre")


class Inmuebles(models.Model):
    _name = "sg.inmueble"
    _description = "Inmuebles"
    
    name = fields.Char("Nombre")
    tag_ids = fields.Many2many("sg.tag",string="Etiquetas")
    value = fields.Float(string="Valor de propiedad")
    currency_id = fields.Many2one("res.currency",string="Moneda")
    street = fields.Text(string="Dirección")
    partner_ids = fields.Many2many("res.partner",string="Interesados")
    operation = fields.Selection(selection=[('venta','Venta'),('compra','Compra'),('alquiler','Alquiler')],default="venta")
    image = fields.Binary("Imagen")
    type = fields.Many2one("sg.tipo.inmueble",string="Tipo de Inmueble")

    user_id = fields.Many2one("res.users",string="Responsable",default=lambda self:self.env.user.id)
    company_id = fields.Many2one("res.company",string="Compañía",default=lambda self:self.env.company.id,required=True)
    owner_id = fields.Many2one("res.partner",string="Propietario")
    date = fields.Date("Fecha de alta")
    codigo_catastral = fields.Char("Código catastral",required=True)
    codigo_catastral_2 = fields.Char("Código catastral_2",required=True)

    
    _sql_constraints = [
        (
            'unique_codigo_catastral',
            'UNIQUE(codigo_catastral)',
            'El código catastral es único por inmueble'
        )
    ]
    
    @api.constrains('codigo_catastral_2')
    def _check_codigo_catastral_2(self):
        for record in self:
            exist = self.search_count([("codigo_catastral_2","=",record.codigo_catastral_2),('id','!=',record.id)]) > 0
            if exist:
                raise UserError("El código catastral 2 es único por inmueble")
    

    def action_view_detail(self):
        #_logger.info("=========================action_view_detail")
        #_logger.info(self.read())
        return {
            "name":self.name,
            "type":"ir.actions.act_window",
            "res_model":"sg.inmueble",
            "view_mode":"form",
            "res_id":self.id
        }


class Tags(models.Model):
    _name = "sg.tag"
    _description = "Etiquetas de Inmueble"

    name = fields.Char("Nombre")