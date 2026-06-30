def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def is_valid_password(password):
    parts = password.split(':')
    if len(parts) != 3:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        a, b, c = int(parts[0]), int(parts[1]), int(parts[2])
        return is_palindrome(a) and is_prime(b) and c % 2 == 0

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))