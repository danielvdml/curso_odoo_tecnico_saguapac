{
    "name":"Seguimiento de inmuebles",
    "description":"""
Este módulo permite al corredor administrar inmuebles, y dar seguimientos a los interesados.
Los tipos de inmuebles que te permitirá administrar son: ....
    """,
    "author":"Daniel Moreno <daniel@bigodoo.com>",
    "depends":[
        "base",
        "mail"
    ],
    "data":[
        "securitic/res.groups.xml",
        "securitic/ir.model.access.xml",
        "securitic/ir.rules.xml",
        "demo/inmuebles.xml",
        "data/sg_tipo_inmueble.xml",
        "views/sg_inmueble.xml",
        "views/res_partner.xml"
    ]
}