'''
2019/1/2

https://projecteuler.net/problem=22

'''
with open('projectEuler/Problem_22_name.txt') as f:
    nameList = [s.split(',') for s in f.readlines()]

nameList = [nameList[0][i].strip('"') for i in range(0,len(nameList[0]))]
nameList.sort()
score = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

nameScore = []

for x in range(0,len(nameList)):
    nameScore.append(sum([score[nameList[x][i]] for i in range(0,len(nameList[x]))])*(x+1))

print(sum(nameScore))