# PROBLEM ONE
# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def find_sum_of_multiples(max):
    total = 0
    for x in range(1, max):
        if not(x % 3) or not(x % 5):
            total += x
    return total

print find_sum_of_multiples(1000)
