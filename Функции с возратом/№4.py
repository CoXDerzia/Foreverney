def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_number = False

    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_number = True

    return has_upper and has_lower and has_number

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))