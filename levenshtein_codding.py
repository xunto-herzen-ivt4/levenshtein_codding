from base_numeral_system import base_ns
from unary_codding import unary


def encode_word(item):
    k = []
    c = 0

    m = item
    while m != 0:
        c += 1
        code = base_ns.convert(m, 2).integer[1:]
        k = code + k
        m = len(code)

    k = unary.encode([c]) + k
    return k


def encode(data: list):
    # Encode phrase
    result = []
    for item in data:
        result += encode_word(item)
    return result


def decode(k: list):
    k = k[:]

    result = []

    while (len(k)) > 0:
        c = 0
        for item in k:
            if item == 0:
                break
            c += 1

        k = k[c + 1:]
        if c == 0:
            result.append(0)
        else:
            n = 1
            for p in range(c-1, 0, -1):
                a = [1] + k[:n]
                k = k[n:]
                n = int(base_ns.convert_to_dec(base_ns.NumberBased(2, a)))
            result.append(n)
    return result
