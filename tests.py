from levenshtein_codding import encode, decode
import random

for i in range(100):
    print(i, 'is started')
    array = [random.randint(0, 10) for _ in range(5)]
    print(array)
    encoded = encode(array)
    decoded = decode(encoded)
    print(decoded)
    print(encoded)
    assert array == decoded
    print(i, 'is completed')
