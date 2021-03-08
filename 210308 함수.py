# 함수

# 함수의 매개변수가 몇개인지 모를때 -> * (Choice 매개변수)
# 키워드 파라미터 ** (kwargs) -> 매개변수를 dictionary로 저장함
function(a=1, b=2)
# {a:1, b:2} 로 저장됨

# 함수의 결과값은 항상 하나이다
return a+b, a*b 
#  -> 튜플형태로 반환됨 (a+b, a*b)
# 따로 값을 받고 싶다면 
val1, val2 = function(3,4)

# 매개변수를 초기화 해놓을려면 맨끝에 해야함
function(a, b, c = true): # ~~~

# 함수 안에서 함수밖의 변수를 변경하는 방법
# 1) return 이용해서 결과값으로 돌려주기
def function(a):
       a= a+1
       return a

   a = function(1)

# 2) globla 명령어 사용하기 (X)
# def funtion():
#     global a
#     a = a+1

# 람다식 : return 이 없어도 항상 값을 돌려줌
add = lamda a, b : a+b
# lamda = 매개변수 ... : 표현식
