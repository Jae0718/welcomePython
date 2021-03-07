# 화이팅 100제 - 1 (입력, 출력, 사칙연산)

# 고양이
# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")




# 입력받은 숫자 사칙연산 : 
# 입력받은 값은 항상 string으로 들어오기 때문에 int로 바꿔줬음
# 1
# val1 = input()
# val2 = input()
# print(int(val1) + int(val2))






# 나머지 구하기
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

# valA = int(input())
# valB = int(input())
# valC = int(input())

# comp1 = (valA + valB)%valC
# comp2 = ((valA%valC) + (valB%valC))%valC

# print("비교1) {0} 와 {1} 는 같나요?".format(comp1, comp2))






# 곱하기
val1 = int(input())
val2 = input()

#세자리로 정해져있음
calc1 = val1 * int(val2[0:1]) 
calc2 = val1 * int(val2[1:2]) 
calc3 = val1 * int(val2[2:3])

print("(3) : {0}".format(calc1))
print("(4) : {0}".format(calc2))
print("(5) : {0}".format(calc3))
print("(6) : {0}".format(calc1*100 + calc2*10 + calc3))
