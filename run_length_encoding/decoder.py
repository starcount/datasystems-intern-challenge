def decode(encoded):
    return ''.join([symbol * run_length
        for (run_length, symbol) in encoded])

