from django.test import TestCase
from .utils import *


class RealEstateTest(TestCase):
    def test_remove_accents(self):
        vn_str = 'Hôm qua đi trên những con đường ngoằn ngoèo.'
        non_accent_str = 'Hom qua di tren nhung con duong ngoan ngoeo.'
        self.assertEqual(remove_accents(vn_str), non_accent_str)
