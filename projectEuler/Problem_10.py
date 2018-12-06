'''
2018/12/7

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
'''
import math
range_num = 2000000
num_list =[]

def primeNum(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

for h in range(2,range_num):
    if primeNum(h):
        num_list.append(h)
    
eqNum = sum(num_list)
print(eqNum)