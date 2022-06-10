import random
import string


def get_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def get_random_string(y):
    return ''.join(random.choice(string.ascii_letters) for _ in range(y))


gen_login = get_random_string(9)
gen_password = get_random_password(5)
gen_gardenName = get_random_string(11)
gen_email = get_random_string(7) + "@gmailx.com"
