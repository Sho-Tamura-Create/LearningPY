'''
2018/12/11

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''
#import math
#def is_prime(n):
#    if n % 2 == 0 and n > 2:
#        return False
#    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

def is_collaz(n):
    get_arr = []
    while True:
        if n % 2 == 0:
            get_arr.append(n / 2)
        else:
            get_arr.append((3 * n) + 1)

        n = get_arr[-1]

        if get_arr[-1] == 1:
            return len(get_arr)

def is_rank(new,old):
    if new > old:
        return True
    return False

i = 1000000
n_ans = 0
o_ans = 0
fix_arr = []

while True:
#    if is_prime(i):
    n_ans = is_collaz(i)
    if is_rank(n_ans,o_ans):
        o_ans = n_ans

        fix_arr = n_ans,i
        print(fix_arr)

    i -= 1
    if i == 1:
        break
