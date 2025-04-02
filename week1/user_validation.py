import re


def validate_username(username):
    if 3 <= len(username) <= 20 and re.match(r'^\w+$', username):
        return True
    return False


def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    return True
