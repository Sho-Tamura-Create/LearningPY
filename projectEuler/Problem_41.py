'''
2019/02/23

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
'''

base = set('1234567')
arr = []

import math
def primeNum(n):
    if n % 2 == 0 and n > 2 or n<=1:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

for i in reversed(range(7654321)):
    if primeNum(i):
        a = list(str(i))
        a = set(a)
    
        if a == base:
            arr.append(i)
            break

print(arr)