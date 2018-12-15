'''
2018/12/15

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 21000?

'''
num_arr = str(max([2 ** i for i in range(1,1001)]))

n = 0
arr = []
while True:
    arr.append(int(num_arr[n]))
    if len(arr) >= len(num_arr):
        break
    n += 1
print (sum(arr))
