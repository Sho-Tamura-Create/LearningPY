'''
2018/11/27
'''

#replace
name = "UheUhe.net"
name2 = name.replace("U", "Mo")
print(name2)

#slice
charCode = "abcdefghijklmnopqrstuvwxyz"
print(charCode[2:8:2])
print(charCode[::-1])

#length
print(len(charCode))

#( 'A')
second_per_hour = 60 * 60
day = second_per_hour * 24
second_per_day = day
day1_second = second_per_day/second_per_hour
day2_second = second_per_day//second_per_hour

print(day1_second)
print(day2_second)