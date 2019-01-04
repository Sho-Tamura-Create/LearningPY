'''
2019/1/4

Euler discovered the remarkable quadratic formula:
n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.
The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n2+an+b, where |a|<1000 and |b|≤1000
where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

'''
import math
def primeNum(n):
    if n % 2 == 0 and n > 2 or n < 1:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

def formula(a,b):
    n = 0
    count = 0
    while True:
        if primeNum(n**2 + a*n + b):
            n += 1
            count += 1
        else:
            return [n,a,b]

itemList = []
for a in range(-1000,1000):
    for b in range(-1001,1001):
        itemList.append(formula(a,b))
a = max(itemList)
fix = a[1]*a[2]

print(a)
print(fix)


