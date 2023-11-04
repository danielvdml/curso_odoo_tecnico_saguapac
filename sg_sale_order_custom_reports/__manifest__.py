{
    "name":"Reportes en Ventas",
    "depends":["base","sale"],
    "data":[
        "views/res_config_settings.xml",
        "data/paperformat.xml",
        "reports/external_layout_sg_custom.xml",
        "reports/report_sale_order.xml"
    ],
    "assets":{
        "web.report_assets_common":[
            "sg_sale_order_custom_reports/static/src/scss/styles.scss",
        ]
    }
}