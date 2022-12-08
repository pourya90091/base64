alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def encode(input):
    value_encoded = ""

    def append(b6):
        nonlocal value_encoded

        alphabet_index = int(b6, 2)
        value_encoded += alphabet[alphabet_index]

    binary = ""
    for char in input:
        if type(char) is int:
            byte = f"{char:0>8b}"
        elif type(char) is str:
            byte ="{0:08b}".format(ord(char))
        else:
            byte = ""

        binary += byte

    i = 1
    while i <= len(binary) // 6:
        n = 6 * i
        b6 = binary[n - 6:n]
        append(b6)

        i += 1
    else:
        if len(binary) % 6 != 0:
            b6 = binary[-(len(binary) % 6):]
            b6 += ((6 - len(b6)) * "0")
            append(b6)

            if len(binary) % 6 == 2:
                value_encoded += "=="
            elif len(binary) % 6 == 4:
                value_encoded += "="

        return value_encoded


def decode(input):
    value_decoded = ""

    def append(b8):
        nonlocal value_decoded

        ordinal = int(b8, 2)
        value_decoded += chr(ordinal)

    padding = 0
    binary = ""
    for char in input:
        if char == "=":
            padding += 1
            continue

        alphabet_index = alphabet.index(char)
        b6 = f"{alphabet_index:0>6b}"
        binary += b6
    else:
        if padding > 0:
            binary = binary[:(-2 * padding)]

    i = 1
    while i <= len(binary) // 8:
        n = 8 * i
        b8 = binary[n - 8:n]
        append(b8)

        i += 1
    else:
        return value_decoded
