import math

def solve(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i) == 0:
            return False

    return True