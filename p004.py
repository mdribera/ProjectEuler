# PROBLEM FOUR
# https://projecteuler.net/problem=4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindromic(num):
    num = str(num)
    first, second = num[:len(num)/2], num[len(num)/2:][::-1]
    if len(first) != len(second):
        second = second[:-1]
    return first == second


def largest_three_digits():
    possible = (x*y for x in xrange(110, 1000, 11) for y in xrange(x, 1000))

    return max(x for x in possible if is_palindromic(x))

print largest_three_digits()
