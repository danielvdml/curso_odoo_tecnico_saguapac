

def descuento_sucesivos(descuentos):
    producto_descuentos = 1
    cantidad_descuentos = len(descuentos)
    for dsct in descuentos:
        producto_descuentos*=(100-dsct)

    return 100-(producto_descuentos/100**(cantidad_descuentos-1))