# PROBLEM FIVE
# https://projecteuler.net/problem=5

# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?


def lcm(a, b):
    return a * b // gcd(a, b)


def gcd(a, b):
    # https://en.wikipedia.org/wiki/Euclidean_algorithm
    while b > 0:
        a %= b
        if a == 0:
            return b
        b %= a
    return a

print reduce(lcm, range(11, 21))
