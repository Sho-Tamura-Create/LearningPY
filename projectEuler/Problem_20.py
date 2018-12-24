'''
2018/12/24

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''
from functools import reduce
from operator import add, mul

a = str(reduce(mul,[i for i in reversed(range(1,101))]))
arr = sum([int(a[x]) for x in range(0,len(a))])
print(arr)