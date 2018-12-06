'''
2018/12/01

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''
import math

counter = 0
pn = 2

def primeNum(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

while counter < 10001:
    if primeNum(pn):
        counter += 1
    if counter == 10001:
        print(pn)
        break
    pn += 1

