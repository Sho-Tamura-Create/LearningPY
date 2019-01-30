'''
2019/1/27
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p ≤ 1000, is the number of solutions maximised?

'''
import math
import collections

collect_arr = []
mydict = []
for i in range(1,1000):
    for j in range(1,1000):
        a = i ** 2
        b = j ** 2
        c = a + b
        if math.sqrt(c).is_integer() == True and math.sqrt(a)+math.sqrt(b)+math.sqrt(c)<=1000:
            fix = math.sqrt(a)+math.sqrt(b)+math.sqrt(c)
            check_arr = sorted([math.sqrt(a),math.sqrt(b),math.sqrt(c)])

            if check_arr not in mydict:
                mydict.append(check_arr)
                collect_arr.append(str(fix))

print(collections.Counter(collect_arr))
