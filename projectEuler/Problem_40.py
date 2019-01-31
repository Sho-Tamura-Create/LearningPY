'''
2019/1/31

An irrational decimal fraction is created by concatenating the positive integers:
0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If dn represents the nth digit of the fractional part, find the value of the following expression.
d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

'''
from functools import reduce
from operator import mul

n = 1
pickup = []
arr = ''.join(list(str(i) for i in range(0,200000)))

while True:
    pickup.append(int(arr[n]))
    n *= 10
    if len(pickup) == 7:
        ans = reduce(mul,pickup)
        break

print(pickup)
print(ans)
print(len(arr))