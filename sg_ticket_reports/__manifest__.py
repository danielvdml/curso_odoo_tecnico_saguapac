{
    "name":"Reportes personalizados para Helpdesk",
    "depends":[
        "base",
        "helpdesk",
    ],
    "data":[
        #Parámetros de sistema
        #Security (grupos, accesos de modelo, reglas de accesos)
        #Acciones (de Servidor, automatización, Informes)
        #Vistas (tree,form, kanbak...)
        #Acciones de ventana
        #Menus
        "security/ir_model_access.xml",
        "views/sg_helpdesk_report.xml"
    ]
}