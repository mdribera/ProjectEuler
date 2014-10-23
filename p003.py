# PROBLEM THREE
# https://projecteuler.net/problem=3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
def prime(x):
    num = x
    cur = 2
    
    while cur <= (num/2):
        if not num % cur:
            num /= cur
            cur = 2
        else:
            cur += 1
    return num


print 'highest prime factor of 13195 is ' + str(prime(13195))
print 'highest prime factor of 600851475143 is ' + str(prime(600851475143))
        