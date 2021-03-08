#자료구조의 변경

menu = {1,2,3}
print(menu, type(menu))

#리스트로 감싸서 형식을 변경함
menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


