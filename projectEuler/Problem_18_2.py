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

def move(l1,l2,addr):
    l1 = [int(l1[i]) for i in range(0,len(l1))]
    l2 = [int(l2[i]) for i in range(0,len(l2))]
    if len(l1) <= 1:
        return [l1[l1.index(max(l1))],l1.index(max(l1))]
    elif len(l1) == 2:
        return [l1[addr-1],addr-1]
    else:
        if addr == -1:
            max_num = l1[l1.index(max(l1))]
            addr = [i for i, x in enumerate(l1) if x == max_num]
            if len(addr) <= 2:
                h1 = [l2[x] for x in range(addr[0],addr[0]+2)]
                h1_max = h1[h1.index(max(h1))]+max_num
                h2 = [l2[x] for x in range(addr[-1],addr[-1]+2)]
                h2_max = h2[h2.index(max(h2))]+max_num
                if h1_max > h2_max:
                    return [l1[addr[0]],addr[0]]
                else:
                    return [l1[addr[-1]],addr[-1]]
        else:
            addr = addr -1
            base = [l1[x] for x in range(addr,addr+2)]
            print(base)
            max_num = base[base.index(max(base))]
            sub_addr = [i for i, x in enumerate(l1) if x == max_num]
            for i in range(0,len(sub_addr)):
                if addr == sub_addr[i] or addr == sub_addr[i] - 1:
                    return [l1[sub_addr[i]],sub_addr[i]]

a = []
print(a)
for i in reversed(range(0, 15)):
    if len(a) == 0:
        a.append(move(get_arr[i],get_arr[i-1],-1))
    else:
        a.append(move(get_arr[i],get_arr[i-1],a[-1][1]))

print(a)

