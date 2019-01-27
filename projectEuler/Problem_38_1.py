'''
2019/1/26

Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
'''
def pan():
    base = set('123456789')
    num = 0
    for x in range(1,10000):
        s = ''
        i = 1
        while True:
            s += str(i * x)
            if len(s) > 9 or len(s) != len(set(s)):
                break
            if set(s) == base and int(s) > num:
                num = int(s)
                break
            i += 1
    return num

print(pan())
'''

num = str('123456789')

def pan(n):
    check = list(str(n))
    for ch in range(len(check)):
        if '0' in check[ch]:
            return False

    arr = []
    nl = []
    for x in range(1,10):
        nl.append(str(n * x))
        a = sorted(list(str(n * x)))
        for y in range(len(a)):
            print(a)
            if a[y] not in arr:
                arr.append(a[y])
            else:
                return False

        fix = ''.join(sorted(arr))

        if fix == num and x != 1:
            ans = ''.join(nl)
            return [n,ans]

numFix = [pan(x) for x in range(1,10000) if pan(x) != False]
print(numFix)
