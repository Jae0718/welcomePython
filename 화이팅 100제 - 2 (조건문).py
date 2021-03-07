# 화이팅 100제 -2 if문

# val1 = 1;
# val2 = 2;

# if val1 > val2 :
#     print(">")
# elif val1 < val2:
#     print("<")
# else :
#     print("==")    





#윤년
# year = 2000

# #연도가 4의 배수이면서, 100의 배수가 아닐때 또는 400의 배수일때

# if (year%4 == 0 and year%100 != 0) or year%400 :
#     print(1)
# else:
#     print(0)





# 알람시계

timeH = int(input())
timeM = int(input())

if timeM - 45 < 0 : 
    timeH -= 1
    timeM = 60 - abs(timeM - 45)

print("{0} 시 {1} 분 알람 설정".format(timeH, timeM))
    








