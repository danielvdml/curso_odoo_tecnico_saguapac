from odoo.tests.common import TransactionCase
from odoo.tests import tagged
import logging
from odoo.addons.sg_sale_descuentos_sucesivos.utils.utils import validar_carnet_identidad,validar_nit
_logger = logging.getLogger(__name__)


@tagged('post_install','-at_install')
class TestValidacionContactos(TransactionCase):

    def setUp(self):
        super(TestValidacionContactos,self).setUp()

    def test_validacion_carnet_de_identidad(self):
        self.assertTrue(validar_carnet_identidad("5377567"))
        self.assertFalse(validar_carnet_identidad("53"))
        self.assertFalse(validar_carnet_identidad("5398632A"))
        self.assertFalse(validar_carnet_identidad(False))
        self.assertFalse(validar_carnet_identidad([]))
        self.assertFalse(validar_carnet_identidad("53986323238764"))

    def test_validacion_nit(self):
        self.assertTrue(validar_nit("537756715"))
        self.assertTrue(validar_nit("1537756715"))
        self.assertFalse(validar_nit("537756715A"))
        self.assertFalse(validar_nit("5377567152323"))
        self.assertFalse(validar_nit(False))