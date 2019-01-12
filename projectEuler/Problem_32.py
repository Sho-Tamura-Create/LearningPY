'''
2019/1/10

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

'''
def pandigital(num1,num2,num3,num4):
    nl = list('123456789')
    pl = []

    for x in range(num1,num2):
        for y in range(num3,num4):
            ans = x * y
            if sorted(list(str(ans) + str(x) + str(y))) == nl:
                pl.append(ans)
    return pl

fix_s = set(pandigital(1,9,1234,9876))
fix_b = set(pandigital(12,98,123,987))
print(fix_s)
print(fix_b)
print(sum(fix_s) + sum(fix_b))