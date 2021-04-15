import unittest
from pluralcode import decode_pluralcode

class TestPluralcode(unittest.TestCase):
    def test_decode(self):
        plural = decode_pluralcode(
            "PX0.1 N2 D9 C5 Q8 W4 <Lara: Gf Sh A1 Oi> <Go S~ Ax Ot>"
        )
        self.assertIsNotNone(plural)