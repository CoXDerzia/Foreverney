def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

def get_next_prime(num):
    prime = num + 1
    while not is_prime(prime):
        prime += 1
    return prime

print(get_next_prime(6))
print(get_next_prime(7))
print(get_next_prime(14))
