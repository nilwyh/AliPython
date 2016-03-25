import math

def get():
    prime = list()
    prime.append(2)
    prime.append(3)

    for i in range(5, 100000, 2):
        is_prime = True
        for j in prime:
            if i % j == 0:
                is_prime = False
                break
            elif j > math.sqrt(i):
                break
        if is_prime:
            prime.append(i)
    res = []
    for i in range(100):
        res.append([i+1])
    return res
