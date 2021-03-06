def encrypt(plaintext: str, keyword: str):
    """encrypting text using vigenere encryption"""

    # Preparing variables for later
    plaintext = prepare_string(plaintext)
    keyword = prepare_string(keyword)
    keyword = [ord(x) - 64 for x in keyword]
    encrypted = ''
    key = 0

    for char in plaintext:
        # If keyword ends go to the begin
        if key == len(keyword):
            key = 0

        # Appending encrypted letter
        if keyword:
            encrypted += encrypt_letter(char, keyword[key])

        # Select next key for shifting
        key += 1

    # Returns encrypted text or None if there's none
    return encrypted if encrypted != '' else None


def encrypt_letter(char, shift):
    # Returns shifted character for encryption
    return chr((ord(char) + shift - 65) % 26 + 65)


def decrypt(text: str, keyword: str):
    """decrypting text using vigenere decryption knowing they key"""

    # Preparing variables for later
    text = prepare_string(text)
    keyword = prepare_string(keyword)
    keyword = [ord(x) - 64 for x in keyword]
    decrypted = ''
    key = 0

    for char in text:
        # If keyword ends go to the begin
        if key == len(keyword):
            key = 0

        # Appending decrypted letter
        if keyword:
            decrypted += decrypt_letter(char, keyword[key])

        # Select next key for shifting
        key += 1

    # Returns decrypted text or None if there's none
    return decrypted if decrypted != '' else None


def decrypt_letter(char, shift):
    # Returns back shifted character for decryption
    return chr((ord(char) - shift - 65) % 26 + 65)


def prepare_string(string: str) -> str:
    # Deletes non-alphabetic characters and turning to uppercase
    return ''.join(c.upper() for c in string if c.isalpha())
