import random

def solve(n):
    total = 0
    suc = 0
    for m in range(10000):
        a=[]
        for i in range(4):
            a.append(0)

        for i in range(n):
            b=random.randrange(0,52)
            a[int(b/13)] = 1

            if sum(a) == 4:
                suc += 1
                break

        total += 1
    print 1.0*suc/total
    return 1.0*suc/total

solve(10)