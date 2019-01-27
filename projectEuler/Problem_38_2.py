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
