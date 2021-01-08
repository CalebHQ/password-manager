import hashlib

possible_characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
key = 19


def encrypt(password):
    result = ''
    for char in password:
        position = possible_characters.find(char)
        new_position = (position + key) % 94
        result += possible_characters[new_position]
    return result


def decrypt(password):
    decrypted_message = ""
    for c in password:
        if c in possible_characters:
            position = possible_characters.find(c)
            new_position = (position - key) % 94
            new_character = possible_characters[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
    return decrypted_message


def master_key(master):
    hash_object = hashlib.sha256(master)
    hex_dig = hash_object.hexdigest()
    if hex_dig == 'ENTER MASTER KEY HASH':
        return True


def master_pin(pin):
    hash_object = hashlib.sha256(pin)
    hex_dig = hash_object.hexdigest()
    if hex_dig == 'ENTER MASTER PIN HASH':
        return True
