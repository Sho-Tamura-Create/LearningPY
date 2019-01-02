'''
2019/1/2

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''

numList = [0,1,2,3,4,5,6,7,8,9]
numAddr = 999999
a = []
for i in range(1,len(numList)+1):
    numAddr,c = divmod(numAddr,i)
    a.append(c)
    print(numAddr,c)

a = [x for x in reversed(a)]
fn = list(map(str,[numList.pop(a[x]) for x in range(0,len(a))]))
fn = ''.join(fn)

print(a)
print(fn)
print(numList)