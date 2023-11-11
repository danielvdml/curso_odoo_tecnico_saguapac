{
    "name":"Webiste Helpdesk",
    "depends":["base","website"],
    "data":[
        "security/ir_model_access.xml",
        "templates/helpdesk_page.xml",
        "views/helpdesk_ticket.xml"
    ],
    "assets":{
        "web.assets_frontend": [
            'sg_helpdesk_page/static/src/scss/style.scss',
        ]
    }
}