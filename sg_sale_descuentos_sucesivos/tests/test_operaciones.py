from odoo.tests.common import TransactionCase
from odoo.tests import tagged
from odoo.addons.sg_sale_descuentos_sucesivos.utils.utils import descuento_sucesivos
import logging
_logger = logging.getLogger(__name__)


@tagged('post_install','-at_install')
class TestOperaciones(TransactionCase):

    def setUp(self):
        super(TestOperaciones,self).setUp()

    def test_1(self):
        self.assertTrue(True)

    def test_2(self):
        self.assertTrue(True)

    def test_descuentos_sucesivos(self):
        lista_descuentos = [20]
        res = descuento_sucesivos(lista_descuentos)
        self.assertEqual(res, 20, msg="El descuento resultante es 20.")

    def test_descuentos_sucesivos_2(self):
        lista_descuentos = [20,20]
        res = descuento_sucesivos(lista_descuentos)
        self.assertEqual(res, 36, msg="El descuento resultante es 36.")

    def test_descuentos_sucesivos_3(self):
        lista_descuentos = []
        res = descuento_sucesivos(lista_descuentos)
        self.assertEqual(res, 0, msg="El descuento resultante es 36.")

    def test_descuentos_sucesivos_valores_diferentes_a_numerico(self):
        with self.assertRaises(ValueError):
            lista_descuentos = [20,20,"a"]
            res = descuento_sucesivos(lista_descuentos)
            #self.assertEqual(res, 36, msg="El descuento resultante es 36.")

    def test_descuentos_sucesivos_error_valores_menores_a_cero(self):
        with self.assertRaises(ValueError):
            lista_descuentos = [-10,-20]
            res = descuento_sucesivos(lista_descuentos)

    def test_descuentos_sucesivos_valores_mayores_a_100(self):
        with self.assertRaises(ValueError):
            lista_descuentos = [110,150]
            res = descuento_sucesivos(lista_descuentos)

    def test_descuentos_sucesivos_entrada_diferente_a_lista(self):
        with self.assertRaises(ValueError):
            lista_descuentos = False
            res = descuento_sucesivos(lista_descuentos)