'''
2018/12/01

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
prime = []
checker = 0
base = 232700000
success = 0

while success < 1:
    base += 1 
    prime.clear()

    for i in range(1,21):
        prime.append(base / i)

    for n in range(len(prime)):
        if prime[n].is_integer() == True:
            checker += 1
        else:
            checker = 0
    
    if checker == 20:
        print("成功！")
        print(checker)
        print(base)
        success = 1
    else:
        print("失敗！")
        print(checker)
        print(base)
