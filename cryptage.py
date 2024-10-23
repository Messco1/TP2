import string

def crypt(message, pas):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    encrypted_message = ''.join(chr(ord(char) + 1) for char in message if char in caracteres)
    return f"{encrypted_message} {pas}"

def decrypt(message):
    parts = message.rsplit(" ", 1)
    encrypted_message = parts[0]
    pas = int(parts[1])
    decrypted_message = ''.join(chr(ord(char) - pas) for char in encrypted_message)
    return decrypted_message
