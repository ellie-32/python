##str1 = "파이썬, C언어, HTML/CSS, java"
##logic1 = "파이썬" in str1
##print(logic1)
##logic2 = "C#" in str1
##print(logic2)
##
##poison = "이 파이썬 문장에는 독이 있어"
##print("독" in poison)
##print("약"not in poison)

##number = 12345678
##print(1 in number)
##
##number = "12345678"
##print(1 in number)

##print("1" in number)

##message = "다른 연산자끼리 섞어쓰는 것도 가능해"
##print("연산자" in message[2:10])
##print("연산자" not in "정말 다양한 방법으로" + "연산자를 쓸 수 있어")

##string = "문자열 함수 & 문자열 함수"
##print(string.find("자열"))
##print(string.find("함수"))
##print(string.rfind("자열"))
##print(string.rfind("함수"))

##string = "HelloPython"
##number = "12345"
##print(string.isalpha())
##print(string.isnumeric())
##print(number.isalpha())
##print(number.isnumeric())

##bab = "국밥 컵밥 초밥 김밥 비빔밥"
##print("가장 앞에 있는 밥은 "+str(bab.find("밥"))+"번째!")
##print("가장 뒤에 있는 밥은 "+str(bab.rfind("밥"))+"번째!")

##eng = "FunnyPython"
##kor = "신나는파이썬"
##black = "B L A C K"
##
##print(eng.isalpha())
##print(kor.isalpha())
##print(black.isalpha())

##num = "20240505"
##date = "202.05.05"
##
##print(num.isnumeric())
##print(date.isnumeric())








Q_1 = """강낭콩 옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고
완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다"""

##print("첫 번째 완두콩은 "+str(Q_1.find("완두콩"))+"번째에 있습니다")
##print("두 번째 완두콩은 "+str(Q_1.rfind("완두콩"))+"번째에 있습니다")

index1 = Q_1.find('')
one = Q_1[13:24]

#two = Q_1.rfind 39:50

print(one)
##print(two)

##print("완두콩 깐 빈 콩깍지" in Q_1[13:24])
##print("강낭콩 깐 빈 콩깍지" in Q_1[39:50])


























