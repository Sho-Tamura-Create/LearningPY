'''
2019/01/16

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)

'''

def numTo(n):
    t = n
    num = []
    arr = []

    strNum = list(map(int, str(n)))
    strArr = [str(j) for j in (reversed(strNum))]
    a = ''.join(strArr)
    a = int(a)

    while True:
        t,b = divmod(t,2)
        num.append(b)
        if t < 1:
            break

    arr = [i for i in (reversed(num))]
    if arr == num and n == a:
        return n

fix = [numTo(x) for x in range(1,1000001,2) if numTo(x) != None]
print(fix)
print(sum(fix))
