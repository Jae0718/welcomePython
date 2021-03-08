#리스트

subway = [10,20,30]
print(subway)

subway = ["1번", "2번", "3번"]

print(subway.index("2번"))

subway.append("5번")
print(subway)

subway.insert(3, "4번")
print(subway)


#꺼내기

print(subway.pop())
print(subway)


#같은 이름 확인

#정렬

num_list = [5,4,7,2,4,0]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)


#다양한 자료형 함께 사용가능 + 확장
mix_list = ["조세호", '1' , 3]

num_list.extend(mix_list)
print(num_list)




