import string

def crypt(message):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = ''.join(chr(ord(char) + 1) for char in message if char in caracteres)
    return encrypted_message