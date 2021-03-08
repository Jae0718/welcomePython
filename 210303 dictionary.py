cabinet = {3:"유재석", 100:"김태호"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#없는 값을 참조할때
# print(cabinet[5]) # 멈춤
print(cabinet.get(5)) # 킵고잉

print(cabinet.get(5, "사용가능"))  

#자료가 있는지 확인
print(3 in cabinet) # key in 변수 true or false

#새로운 값 넣기
print(cabinet)
cabinet[200] = "이재영"
print(cabinet)

#값삭제
del cabinet[100]
print(cabinet)

#키/값/쌍 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
