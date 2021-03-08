# 파일 입출력

# 파일생성
f = open("새파일.txt", 'w') # 파일 열기보다 -> W 쓰기(r,w,a 읽, 쓰, 추)
for i in range(1,11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


# # readline()
# # 한줄씩 읽기
f = open("C:\python\.vscode\새파일.txt", 'r')
while True:
    line = f.readline()
    if not line : break  # 조건이 아닐때까지, readline은 읽은게 없으면 빈칸을 return함
                         # if, if not으로 널체크 가능함
    print(line)
f.close()


# readlines()
# 모든 줄을 읽어 각줄을 리스트로 돌려줌


# read() 
# -> 모든 내용을 문자열로 돌려줌



# # 파일에 새로운 내용 추가하기 - 'a' 모드로 틀어서 write!!

# # 자동으로 파일을 여닫아줌 - with 문을 벗어나면 열린 파일 객체가 닫힘
with open("foo.txt",'w') as f:
    f.write("Lisr is tooo short, you need python")


# # sys module 이용
 
import sys
args = sys.argv[1:]   # 0번째에는 파일의 경로를 담고 있음 나머지 명령어 입력은 순서대로 들어감


# 연습문제



# 1 주어진 자연수가 홀수인지 짝수인지
def is_odd(val):
    if val%2 == 0:
        return "짝수"
    else:
        return "홀수"

print(is_odd(3))        



# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# 파이썬에서는 전역변수쓸때는 되도록 함수안에 파라메타로 가져와서 쓰기

def calc_avg(*vals, sum = 0):
    for i in vals:
        sum += int(i)
    return sum/len(vals)

print(calc_avg(1,2,3,4,5,3,4,2,3))

# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
data = f2.read()
print(data)
f2.close()

#   OR
# close를 해줄 필요없는 with 사용

with open("test.txt", "w") as f:
    f.write("Life is too short")

with open("test.txt", "r") as f:
    str = f.read()
    print(str)







# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

str = input()

f1 = open("inputTest.txt", 'a')
f1.write(str + '\n')
f1.close()


#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

str = """Life is too short
you need java"""

f2 = open("replaceTest.txt", 'a')
str = str.replace("java", 'python')
f2.write(str)
f2.close()
