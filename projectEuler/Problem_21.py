'''
2019/1/1

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def yaku(m):
    return sum([i for i in range(1,m-1) if m % i == 0])

dl = []
for i in range(1,10000):
    a = yaku(i)
    b = yaku(a)

    if i == b and i != a:
        dl.append(i)
        set(dl)

print(sum(dl))
   
