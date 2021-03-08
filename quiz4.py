from random import *;

# 5분 ~ 15분
time = random() * 50 +1  # 1~50까지의 랜덤한 값
# 반복문을 50번 돌면서 난수를 그때그때 생성해서 출력, 그게 범위이내인지 판별?
count = 0

for i in range(1,51):
    time = random()*50 +1
    print("{0} 번째 손님 / 소요시간 {1}분".format(i,time))
    if time < 15 and time > 5 :count += 1

print("총 {0}분 태웠습니다".format(count))

# 완료 된걸까?