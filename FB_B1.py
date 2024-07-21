import sys
#import math
from functools import reduce
from itertools import combinations_with_replacement

#sys.stdout=open(r'C:\Users\parim\Downloads\FB_B1.txt','wt')


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def product(array):
    return reduce(lambda x, y: x * y, array, 1)


def calc_res(f_reduced, P):
    res = []
    s = 41
    while s > 0 and len(f_reduced) > 0:
        if P % f_reduced[-1] == 0 and 1 not in res and s - f_reduced[-1] >= 0:
            P = P // f_reduced[-1]
            s -= f_reduced[-1]
            res.append(f_reduced[-1])
        else:
            f_reduced.pop()
    if s == 0 and P == 1:
        return res
    else:
        return -1


for case in range(int(input())):
    P = int(input())
    f = factors(P)
    f_reduced = list(filter(lambda a: a <= 41, f))
    #print(P)
    #print(f_reduced)
    f_reduced.sort()
    res = calc_res(f_reduced, P)

    if res == -1 or P == 41:
        print(f'Case #{case + 1}: -1')
    else:
        print(f'Case #{case + 1}: {len(res)}', end=" ")
        for k in res:
            print(k, end=" ")
        print()