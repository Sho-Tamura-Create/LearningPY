'''
2018/11/28

f we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def mathSum(minN,maxN):
    sumNum = 0
    for num in range(minN,maxN):
        ft = num / 3
        ff = num / 5
        if ft.is_integer() == True or ff.is_integer() == True:
            sumNum += num
    return sumNum

n = mathSum(1 ,1000)
print (n)


