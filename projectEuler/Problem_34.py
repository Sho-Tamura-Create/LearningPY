'''
2019/1/14

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def kai(n):
    arr = []
    a = 1
    num = str(n)
    num = [int(num[x]) for x in range(len(num))]

    for i in range(0,len(num)):
        for j in reversed(range(1, num[i]+1)):
            a *= j
        arr.append(a)
        a = 1
    if n == sum(arr):
        return sum(arr)

fix = [kai(x) for x in range(3,99999) if kai(x) != None]
print(sum(fix))