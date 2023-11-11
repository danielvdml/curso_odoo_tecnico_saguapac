from odoo import http
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)



class HelpdeskPage(http.Controller):

    @http.route("/soporte",type="http", auth="user", website=True,method=["GET"])
    def soporte_page(self, **kwargs):
        my_tasks = request.env["helpdesk.ticket"].sudo().search([("user_id","=",request.env.user.id)])
        return request.render("sg_helpdesk_page.helpdesk_soporte_page_main",{'tasks':my_tasks,"attributo_extra":"attr"})
    
    @http.route("/soporte/<model('helpdesk.ticket'):ticket>",type="http", auth="user", website=True,method=["GET"])
    def ticket_page(self,ticket,**kwargs):
        return request.render("sg_helpdesk_page.ticket_page",{"ticket":ticket})

    @http.route("/soporte/new",type="http", auth="user", website=True,method=["GET"])
    def create_ticket_page(self):
        agencias = request.env["sg.ubicacion.agencia"].search([])
        return request.render("sg_helpdesk_page.helpdesk_soporte_page_create_ticket",{"agencias":agencias})
    
    @http.route("/soporte/new",type="http", auth="user", website=True,method=["POST"],csrf=False)
    def new_ticket(self,**post):
        _logger.info("POST: %r",post)
        request.env["helpdesk.ticket"].sudo().create({"name":post.get("name")})
        return request.redirect("/soporte")