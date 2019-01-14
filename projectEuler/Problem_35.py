'''
2019/1/14


'''
import math
def primeNum(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3,int(math.sqrt(n))+1,2))

def prim(n):
    if n % 2 == 0 and n > 2:
        return False
    elif all(n % i for i in range(3,int(math.sqrt(n))+1,2)):
        a = 0
        arr = []
        arrnum = 0
        hantei = []

        strnum = str(n)
        strnum = [strnum[x] for x in range(len(strnum))]
        for i in range(0,len(strnum)):
            a = strnum.pop(0)
            strnum.append(a)
            arrnum = ''.join(strnum)
            arr.append(int(arrnum))
            
        for j in range(0,len(arr)):
            hantei.append(primeNum(arr[j]))
        if False not in hantei:
            return n
        else:
            return False

num = [prim(x) for x in range(2,1000001) if prim(x)]
print(num)
print(len(num))