#집합 (set) : 중복이 안되고, 순서가 없음

my_set = {1,2,3,3,3,3}
print(my_set)


java = {1,2,3,4,5,6}
python = set([4,5,6,7,8])

#교집합
print(java&python)
print(java.intersection(python))

#합집합
print(java | python)
print(java.union(python))

#차집합
print(java-python)
print(java.difference(python))

#추가
python.add(11)

#삭제
java.remove(1)


