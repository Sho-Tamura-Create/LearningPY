'''
2019/1/26

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import math
def primeNum(n):
    if n % 2 == 0 and n > 2 or n<=1:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

def checker(x):
    if primeNum(x):
        arr_a = list(map(str, str(x)))
        arr_b = list(map(str, str(x)))
        while True:
            arr_a.pop(0)
            arr_b.pop()

            a = ''.join(arr_a)
            b = ''.join(arr_b)
                
            a = int(a)
            b = int(b)

            if primeNum(a) == False or primeNum(b) == False:
                return False
            if len(arr_a) <= 1 and len(arr_b) <= 1:
                return x
    else:
        return False

arr = [checker(z) for z in range(10,1000000) if checker(z) != False]
fix = sum(arr)
print(arr,fix)