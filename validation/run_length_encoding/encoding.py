from validation.run_length_encoding.base import TestBase
from run_length_encoding.encoder import encode
from run_length_encoding.decoder import decode


class TestEncoding(TestBase):


    def _run_test_case(self, unencoded_symbols):
        self.assertEqual(
            unencoded_symbols,
            decode(encode(unencoded_symbols)))

