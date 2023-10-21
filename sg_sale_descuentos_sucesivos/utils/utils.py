
from functools import reduce
import re

def descuento_sucesivos(descuentos):
    #return reduce(lambda x, y: x * (1 - y / 100), descuentos, 100)
    if type(descuentos) != list:
        raise ValueError("El atributos descuentos debe ser una lista")
    
    for descuento in descuentos:
        if type(descuento) not in [float,int]:
            raise ValueError("Los valores del descuento deben ser de tipo numérico")
        if  descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe ser un valor entre 0 y 100")

    producto_descuentos = 1
    cantidad_descuentos = len(descuentos)
    for dsct in descuentos:
        producto_descuentos*=(100-dsct)

    return 100-(producto_descuentos/100**(cantidad_descuentos-1))
    
    
def validar_carnet_identidad(numero_carnet_identidad):
    return bool(re.match("\d{4,8}$",numero_carnet_identidad or ""))

def validar_nit(nit):
    return bool(re.match("\d{9,10}$",nit or ""))