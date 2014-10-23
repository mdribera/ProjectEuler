import math
def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    
    for x in range(3, int(math.sqrt(num))):
        if not num % x:
            return False
    return True

def highest_prime_below(x):
    return [x for x in range(x) if is_prime(x)][-1]

print highest_prime_below(100)
print highest_prime_below(600851475143)