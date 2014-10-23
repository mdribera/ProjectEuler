
def find_sum_of_multiples(max):
    total = 0
    for x in range(1,max):
        if not(x % 3) or not(x % 5):
            total += x;
    return total

print find_sum_of_multiples(1000);