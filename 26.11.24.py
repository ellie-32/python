##Q_1 = """강낭콩옆 빈 콩깍지는 완두콩 깐 빈 콩깍지고
##완두콩 옆 빈 콩깍지는 강낭콩 깐 빈 콩깍지다"""

##print("첫 번째 완두콩은 "+str(Q_1.find("완두콩"))+"번째에 있습니다")
##print("두 번째 완두콩은 "+str(Q_1.rfind("완두콩"))+"번째에 있습니다")

##index1 = Q_1.find('완두콩')
##one = Q_1[index1:24]
##
##index2 = Q_1.rfind('강낭콩')
##two = Q_1[index2:50]
##
##print(one)
##print(two)

##이메일 = input("이메일을 입력해주세요 : ")
##one1 = 이메일.find('@')
##one = 이메일[0:one1]
##print("이이메일의 아이디는 "+(one)+"입니다.")

##string = "문자열_함수는_참_다양해요"
##split_string = string.split("_")
##print(split_string)
##
##string = string.replace("다양해","멋져")
##print(string)

##string = "Python Upper Lower"
##print(string.upper())
##print(string.lower())

##dessert = "초코케이크 녹차마카롱 모카라떼"
##cake, macaron, coffee = dessert.split(" ")
##print("[ 오늘 먹을 간식 목록 ]")
##print("케이크 :", cake)
##print("마카롱 :",macaron)
##print("커피 :", coffee)

##n1,n2 = input("int 둘 입력 : ").split()
##print(n1)
##print(n2)
##
##print(n1+n2)
##print(int(n1)+int(n2))

##a,b,c = input("알파벳 셋 입력 : ").split()
##print(c,b,a,sep=">")

##r1,r2 = input("float 둘 입력 : ").split()
##r1 =float(r1)
##r2 =float(r2)
##
##print(r1*r2)

##message = """대공원에 보 벚꽃 놀이는
##낮 봄 벚꽃 놀이보다
##밤 봄 벚꽃 놀이니라."""
##
##print(message.replace("벚꽃","개나리"))

##win = "WindowXP"
##update = win.replace("XP","11")
##
##print(update + "로 업데이트 됐습니다.")


##japangi = """이 자판기 안에는
##포도맛 사이다,
##포맛 쥬스,
##포도맛 슬러쉬,
##가 있습니다."""
##
##taste = input("무슨 맛 자판기로 바꿀까요 : ")
##
##print(japangi.replace("포도",taste))

##message = input("영어로 문장을 적어주세요 : ")
##print(message.upper())
##print(message.lower())

##message = "abcD 1234 ..@@ !!!"
##
##trans = message.upper()
##
##print(trans)

##n1, n2,n3= input("전화번호 입력 : ").split("-")
##print(n1) 
##print(n2) 
##print(n3) 

##파일 = input("파일명을 입력해주세요 : ")
##update = 파일.replace("jpg","png")
##
##print(파일 + "파일을"+ update +"파일로 벼경하였습니다")
##
##
##string = "Hello, Python! Hello, String"
##print(string.upper())
##print(string.lower())

##string = "이 문장안에 있는 글자의 수는 몇개일까요?"
##print(len(string))
##
##string1 = "파이썬 {0}번 복습하기".format(10)
##print(string1)
##
##string2 = f"문자열도 {10:8.2f}번 복습하기"
##print(string2)

##tips = "len함수로 문자열의 갯수를 세봅시다"
##print(len(tips))
##number = 15335
##print(len(number))

##year = input("태어난 해를입력해주세요 : ")
##month = input("태어난 월을 입력해주세요 : ")
##day = input("태어난 일을 입력해주세요 : ")
##date = "{}년 {}월 {}일".format(year,month,day)
##print("당신의 생일은" + date + "입니다. Happy birthday!")

##num1 = f'{10}/{20}'
##num2 = f'[{10.10}/{20.20}]'
##print(num1)
##print(num2)
##
##pi = 3.14
##num3 = f'[{pi:4.1}/{pi:010.0f}]'
##print(num3)
##
##str1 = "Python"
##str2 = f'[{str1:10s}/{str1:010s}]'
##print(str2)

##
##movie = input("영화 제목을 입력하세요 : ")
##year = input("개봉 연도를 입력하세요 : ")
##actor = input("주연 배우를 입력하세요 : ")
##date = "{}은(는) {}년에 개봉한 {}".format(movie,year,actor)
##print(date + "주연의 영화입니다.")
##
##
##ID = input("""
##아이디를 입력해주세요(6글자 이상) : """)
##SID = ID[:3]
##print('암호화된 아이디 :' + SID +"*****")

##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"num1 + num2 = {num1 + num2}")
##print(f"num1 - num2 = {num1 - num2}")
##print(f"num1 * num2 = {num1 * num2}")
##print(f"num1 / num2 = {num1 / num2:.2f}")

##number = int(input("숫자를 입력해주세요 : "))
##
##print(f"number + 50 = {number + 50}")
##print(f"number - 50 = {number - 50}")
##print(f"number * 50 = {number * 50}")
##print(f"number / 50 = {number / 50:.3f}")
##
##w1 = 3
##w2 = 4
##h = 5
##
##answer1 = '(w1 + w2) * h / 2'
##answer2 = (w1 + w2) * h / 2
##
##answer = "{} = {}".format(answer1,answer2)
##
##print("사다리꼴의 넓이는 " + answer) 


##num1 = int(input("첫 번째 숫자 입력 : "))
##num2 = int(input("두 번째 숫자 입력 : "))
##
##print(f"num1 // num2 = {num1 // num2}")
##print(f"num1 % num2 = {num1 % num2}")
##print(f"num1 ** num2 = {num1 ** num2}")

##num1 = int(input("숫자를 입력해주세요 : "))
##
##print(f"{num1 // 4}")
##print(f"{num1 % 4}")
##print(f"{num1 ** 4}")





kg = input("몸무게(kg)을/를입력하세요 : ")
m = input("키(m)를 입력하세요 : ")

num = int(kg)
num1 = int(m)
num2 =m**2
num3 = kg / num
num4 = num1

print("BMI 지수는 " + num2)












