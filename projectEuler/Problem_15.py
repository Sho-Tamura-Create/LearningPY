'''
2018/12/15

https://projecteuler.net/problem=15

'''
from functools import reduce
from operator import add, mul
#
def girdRoot(m,n):
    #階乗計算
    child = reduce(mul,[(m + n) - i for i in range(0,m+n)])
    mother = reduce(mul,[m - j for j in range(0,m)]) * reduce(mul,[n - j for j in range(0,n)])

    return child / mother

print(int(girdRoot(20,20)))

#child = reduce(mul,[(4 + 3) - i for i in range(0,7)])
#mother = reduce(mul,[4 - j for j in range(0,4)]) * reduce(mul,[3 - j for j in range(0,3)])
#print(child)
#print(mother)

