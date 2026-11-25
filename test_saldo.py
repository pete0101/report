"""justus"""
import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):

    def test_liian_kallis_ostos(self):
        kortti = Maksukortti(12.00)

        kortti.osta(12.80)

        self.assertEqual(kortti.saldo, 12.00)


if __name__ == "__main__":
    unittest.main()