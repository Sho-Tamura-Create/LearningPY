'''
2019/1/8

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''

limit = 200
pat = 8

for a in range(0,limit,100):
    for b in range(0,limit,50):
        for c in range(0,limit,20):
            for d in range(0,limit,10):
                for e in range(0,limit,5):
                    for f in range(0,limit,2):
                        for g in range(0,limit):
                            if a+b+c+d+e+f+g == 200:
                                pat += 1
print(pat)