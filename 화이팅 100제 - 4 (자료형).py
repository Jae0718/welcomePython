# 화이팅 100제 - 4 (자료형)
# python 자료구조

# 리스트 -> [] 
# 리스트 고유 append, insert, pop, remove, sort
# 서로 다른 자료형 가능
# 비어있는 리스트 가능
# 인덱스로 접근
# 인덱스 마이너스 값은 리스트의 마지막 값에서부터 시작하는 인덱스임
# 인덱스 슬라이싱 : [0:5] 범위를 이용해서 리스트를 자름
# 데이터 삽입 : append(가장 끝에), insert(위치지정해서 삽입가능)

 # 튜플 -> ()
# 수정 불가!
# 슬라이싱 가능 : 를 이용해서 가능..!! (리스트랑 동일)
# 곱하기 : 반복해서 추가됨 t2 *3 = 1,2,3,1,2,3,1,2,3
# 길이 : len
# a, b = ('python, life') -> 튜플로 a,b에 값을 대입함

# 딕셔너리 -> {key:value, key2:value2 ...} 쉼표로 구분, value에 리스트로 가능함
# a[2] = 'b'  -> a:b 로 추가됨
# key는 고유값이므로 중복되는 값을 설정해 놓으면 나머지가 무시됨.
# 리스트는 key값으로 쓸 수 없지만, 튜플은 가능함 -> 변할 수 있는 값인지 아닌지가 기준임
# a.keys() -> dictionary a의 key값만 모아서 dict_keys 객체를 돌려준다.
# 3.0 부터는 list가 아닌 dict_keys 객체로 반환하기 때문에 list로 받아야할 경우에는 list(a.keys())를 사용
# dict_keys는 리스트로 변환하지 않아도 기본적인 반복문등은 가능함
# a.values() -> dict_values 객체
# a.items() -> dict_items 객체 (쌍)
# key, vlaue 모두 지우기 : clear
# key로 calue 얻기 -> get , a[1]과 같음, 존재하지 않는 값을 호출할때 get은 None, []는 에러발생함
# key가 있는지 조사 -> in


# 집합 자료형 set
# 리스트, 튜플은 순서가 있어서 인덱싱 가능, 딕셔너리와 set은 X
# 교 &, intersection
# 합 |, union
# 차 -, difference
# add, update(여러개 추가), remove



# (중요)변수

# a = [1,2,3] 일때 b=a라고 하면 b와 a는 같은 주소값을 갖게 되어, a를 변경하면 b도 변경된다
# 다른 주소를 가리키도록 하는 방법
# 1) [:] (리스트 전체를 가리킴) 이용
# 2) copy 모듈이용 -> 모듈추가 후 사용








# 연습문제

# 리스트 sort 쓰기
# list = [1,2,3,4,5]
# list.sort(reverse=True)
# print(list)

# 리스트를 문자열로 만들기
# list = ['Life', 'is', 'too', 'short']

# val = ""
# print(val.join(list))

# 튜플에 값더하기, 항이 하나인 튜플 -> a= (1,)
# tuple1 = (1,2,3)  
# tuple2 = (4,)
# print(tuple1 + tuple2)

# # 딕셔너리 값 가져오기
# a = { 'A':12, 'B': 13, 'C':14}
# result = a.pop('B')  # pop에 아무것도 안넣으면 안된다..?
# print(a)

# 리스트 중복제거 -> 중복이 없는 자료형 : set, dictionary의 key
a = [1,1,1,2,2,3,3,4,5]
b = set(a)
# b = a.copy
print(b)