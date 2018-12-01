'''
2018/12/01

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

'''
def palindrome(minN,maxN):
    numlist = []
    reNum = []
    getNum = 0

    for i in range(minN,maxN):
        l = i
        for n in range(minN,maxN):
            getNum = l * n
            getNum = str(getNum)
            list_num = list(getNum)
            list_num = [int(s) for s in list_num]
            reNum = [int(s) for s in list_num]
            reNum.reverse()
            
            if list_num == reNum and int(getNum) not in numlist:
                numlist.append(int(getNum))

            numlist.sort()

    print(numlist[-1])

palindrome(100,999)