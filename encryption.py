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
    if hex_dig == '309c0255d1d68ac4c1fd595e82ec9274895c2d1b76ff613b7e93486bb6e2edcf':
        return True


def master_pin(pin):
    hash_object = hashlib.sha256(pin)
    hex_dig = hash_object.hexdigest()
    if hex_dig == '3849ba084da2faea804918e8d999dee3f176659e0216debcccbf86b3e6b769ef':
        return True
