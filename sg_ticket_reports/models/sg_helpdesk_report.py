from odoo import models,fields,tools

class sg_helpdesk_report(models.Model): 
    _name = "sg.helpdesk.report"
    _description = "Reporte personalizado para Helpdesk"
    _auto = False

    name = fields.Char("Nombre")
    team_id = fields.Many2one("helpdesk.team",string="Equipo")
    user_id = fields.Many2one("res.users",string="Usuario")
    employee_id = fields.Many2one("hr.employee",string="Empleado")
    partner_id = fields.Many2one("res.partner",string="Cliente")
    unit_amount = fields.Float(string="Cantidad")
    ticket_create_date = fields.Date("Fecha de creación del ticket")
    timesheet_date = fields.Date("Fecha de Parte de horas")


    def init(self):
        tools.drop_view_if_exists(self.env.cr,self._table)

        self.env.cr.execute(f"""
            CREATE OR REPLACE VIEW {self._table} AS (
                select  concat(ht.id,'/',aal.id) as id,
                    ht.team_id,
                    ht.user_id,
                    ht.partner_id,
                    aal.employee_id ,
                    aal.unit_amount,
                    concat(ht.ticket_ref,' - ',ht."name") "name",
                    ht.create_date "ticket_create_date",
	                aal.date "timesheet_date"
                from helpdesk_ticket ht
                left join account_analytic_line aal on aal.helpdesk_ticket_id = ht.id
                left join helpdesk_team ht2 on ht2.id = ht.team_id 
            )
        """)