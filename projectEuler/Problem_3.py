'''
2018/11/30

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''

def prFact():
    baseNUm = 600851475143
    primefactor = 3

    while primefactor < baseNUm:
        iN, fL = divmod(baseNUm,primefactor)
        if fL == 0:
            baseNUm = iN
        else:
            primefactor += 2
    print(primefactor)

prFact() 



