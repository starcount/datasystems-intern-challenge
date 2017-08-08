from functools import reduce
from run_length_encoding.constants import DIGIT_CHARACTERS
from run_length_encoding.exceptions import DeserializationError


class _Deserializer:


    def _deserialize_character(self, deserialized, character):

        if self.deserializing_pair:
            (run_length_string, _) = deserialized.pop()
            if character in DIGIT_CHARACTERS:
                deserialized.append((run_length_string + character, None))
            else:
                deserialized.append((run_length_string, character))
                self.deserializing_pair = False

        else:
            if character in DIGIT_CHARACTERS:
                deserialized.append((character, None))
            else:
                context = ''.join([run_length_string + symbol
                    for (run_length_string, symbol) in  deserialized])
                raise DeserializationError("No run length for symbol {} in context {}".format(
                    character,
                    context))
            self.deserializing_pair = True

        return deserialized


    def deserialize(self, serialized):
        self.deserializing_pair = False
        deserialized = reduce(self._deserialize_character, serialized, [])

        if self.deserializing_pair:
            self.deserializing_pair = False
            context = ''.join([run_length_string + (symbol or "")
                for (run_length_string, symbol) in  deserialized[:-1]])
            (run_length_string, _) = deserialized[-1]
            raise DeserializationError("No symbol for run length {} in context {}".format(
                run_length_string,
                context))

        return [(int(run_length_string), symbol)
            for (run_length_string, symbol) in deserialized]
 

def deserialize(serialized):
    return _Deserializer().deserialize(serialized)

