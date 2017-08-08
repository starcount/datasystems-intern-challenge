from validation.run_length_encoding.base import TestBase
from validation.util import with_skip_not_implemented
from run_length_encoding.encoder import encode
from run_length_encoding.decoder import decode
from run_length_encoding.serializer import serialize
from run_length_encoding.deserializer import deserialize
from run_length_encoding.exceptions import SerializationError


class TestSerialization(TestBase):


    def _run_test_case(self, unencoded_symbols):
        self.assertEqual(
            unencoded_symbols,
            decode(deserialize(serialize(encode(unencoded_symbols)))))


    @with_skip_not_implemented
    def test_bad_symbol(self):
        with self.assertRaises(SerializationError):
            decode(deserialize(serialize(encode("AAAAA11BBBB"))))

