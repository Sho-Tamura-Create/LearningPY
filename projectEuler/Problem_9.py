'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math

def is_pythagorean(a,b):
    return a**2 + b**2

for i in range(1,1000):
    for n in range(i+1,1000):
        a = i
        b = n
        c = is_pythagorean(a,b)

        if math.sqrt(c).is_integer() == True:
            if a + b + math.sqrt(c) == 1000:
                print('True Hit!!' , a  , b , int(math.sqrt(c)))
                print('答え' , int(a * b * math.sqrt(c)))                
                break
