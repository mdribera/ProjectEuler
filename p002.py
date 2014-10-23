def find_sum_of_even_fibs():
    fibs = [1,2]
    i = 1
    while (fibs[i] + fibs[i-1]) < 4000000:
        fibs.append(fibs[i] + fibs[i-1])
        i += 1
    return sum([x for x in fibs if is_even(x)])

def is_even(num):
    return not(num % 2)

print find_sum_of_even_fibs()