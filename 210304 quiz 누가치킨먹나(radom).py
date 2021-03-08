# shuffle, sample - random
from random import *


# setComment = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
setComment = range(1,21)
lstComment = list(setComment)
print(shuffle(lstComment))

selectList = sample(lstComment,4)
print("치킨" + str(selectList[0]))
print("커피" + str(selectList[1:]))

# 출력시 Str로 감싸야함. List도... 
