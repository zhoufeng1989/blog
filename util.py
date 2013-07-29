import random
import hashlib


def gen_salt(length=6):
    ALPHABET = (
        r'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chars = []
    for i in xrange(6):
        chars.append(random.choice(ALPHABET))
    return ''.join(chars)


def gen_password(password):
    salt = gen_salt()
    password = hashlib.md5(
        salt + hashlib.md5(password).hexdigest()).hexdigest()
    return password, salt
