def rot13_core(text: str=None, shift=13) -> str|list:

    cipher_core_output = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + 13) % 26 + base)
            cipher_core_output.append(new_char)
        else:
            cipher_core_output.append(char)

    return ''.join(cipher_core_output)


def rot47_core(text: str=None, shift=47) -> str|list:

    cipher_core_output = []
    for char in text:
        code = ord(char)
        if 33 <= code <= 126:  # tylko znaki drukowalne ASCII
            new_char = chr(33 + ((code - 33 + 47) % 94))
            cipher_core_output.append(new_char)
        else:
            cipher_core_output.append(char)  # inne znaki zostają bez zmian

    return ''.join(cipher_core_output)


