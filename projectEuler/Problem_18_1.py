'''
2018/12/16

https://projecteuler.net/problem=18

'''
pyramid = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

get_arr = pyramid.splitlines()
get_arr = [get_arr[i].split() for i in range(1,len(get_arr))]

def move(n,m):
    n = [int(n[i]) for i in range(0,len(n))]
    if len(n) <= 2:
        return [n[n.index(max(n))],n.index(max(n))]
    else:
        base = [n[x] for x in range(m,m+2)]
        max_num = base[base.index(max(base))]
        addr = n.index(max_num)

        if addr < m:
           addr = [i for i, x in enumerate(n) if x == max_num]
           if len(addr) <= 2:
               addr = addr[-1]
               
        return[max_num,addr]

a = []
for i in range(0,len(get_arr)):
    if i <= 2:
       a.append(move(get_arr[i],0))
    else:
       a.append(move(get_arr[i],a[i-1][1]))

#a = [move(get_arr[i]) for i in range(0,2)]
print(a)
print(sum(a[i][0] for i in range(0,len(a))))
