# 화이팅 100제 - 3 (반복문)


#구구단
# var = int(input())

# for i in range(1,10) :
#     print("{0} * {1} = {2}".format(var, i, var * i))




# N찍기
# varN = int(input())
# for i in range(1,varN+1):
#     print(i)




# 별찍기  : print 에 개행없애기
# varN = int(input())
# for j in range(0,varN):
#     for i in range(0,j+1) :
#         print("*", end='')
#     print("")    



# 별찍기2

varN = 5
for i in range(0,varN): # 1,2,3,4
    for j in range(0,varN-i): 
        print(" ", end='')
    for k in range(0,i+1) :  
            print("*", end='')    
    print("")




    


