# 비밀번호 만들어주는 프로그램

temp = "http://naver.com"

str2 = temp.replace("http://", "")


index = str2.find('.')
str3 = str2[:index]
print(str3) 

my_str = str3[:3] + str(len(str3)) + str(str3.count("e")) + "!"

print(my_str)
