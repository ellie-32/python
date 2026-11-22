##"{}".format(10)
##"{}{}".format(10,20)
##"{}{}{}{}{}".format(101,202,303,404,505)
##
##string_a = "{}".format(10)
##
##print(string_a)
##print(type(string_a))
##
##
##format_a = "{}만 원".format(5000)
##format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기.".format(5000)
##format_c = "{}{}{}".format(3000,4000,5000)
##format_d = "{}{}{}".format(1,"문자열",True)
##
##print(format_a)
##print(format_b)
##print(format_c)
##print(format_d)

##"{}{}".format(1,2,3,4,5)
##
##output_a = "{:d}".format(52)
##output_b = "{:5d}".format(52)
##output_c = "{:10d}".format(52)
##output_d = "{:05d}".format(52)
##output_e = "{:05d}".format(-52)
##
##print("#기본")
##print(output_a)
##print("#특정 칸에 출력하기")
##print(output_b)
##print(output_c)
##print("#빈칸을 0으로 채우기")
##print(output_d)
##print(output_e)
##
##output_f = "{:+d}".format(52)
##output_g = "{:+d}".format(-52)
##output_h = "{: d}".format(52)
##output_i = "{: d}".format(-52)
##
##print("#기호와 함께 출력하기")
##print(output_f)
##print(output_g)
##print(output_h)
##print(output_i)
##
##output_j = "{:+5d}".format(52)
##output_k = "{:+5d}".format(-52)
##output_l = "{:=+5d}".format(52)
##output_m = "{:=+5d}".format(-52)
##output_n = "{:+05d}".format(52)
##output_o = "{:+05d}".format(-52)
##
##print("#조합하기")
##print(output_j)
##print(output_k)
##print(output_l)
##print(output_m)
##print(output_n)
##print(output_o)
##
##output_a = "{:f}".format(52.273)
##output_b = "{:15f}".format(52.273)
##output_c = "{:+15f}".format(52.273)
##output_c = "{:+015f}".format(52.273)
##
##
##print(output_a)
##print(output_b)
##print(output_c)
##print(output_d)
##
##
##output_a = "{:15.3f}".format(52.273)
##output_b = "{:15.2f}".format(52.273)
##output_c = "{:15.1f}".format(52.273)
##
##print(output_a)
##print(output_b)
##print(output_c)
##
##
##output_a = 52.0
##output_b = "{:g}".format(output_a)
##
##print(output_a)
##print(output_b)

a = "Hello Python Programming...!"
a.upper()
a.lower()


input_a = """
    안녕하세요
문자열의 함수를 알아봅니다
"""

print(input_a)

print(input_a.strip())


print("TrainA10".isalnum())
print("10".isdigit())

output_a = "안녕안녕하세요".find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)

print("안녕"in"안녕하세요")
print("잘자"in"안녕하세요")

a = "10 20 30 40 50".split(" ")
print(a)


"3 + 4 = " +str(3 + 4)
"3 + 4 = {}".format(3 + 4)

"{}".format(10)
f"{10}"

f'{10}'

f"3 + 4 = {3+4}"
f"""1 + 2 = {1 + 2}
2 + 3 = {2 + 3}
3 + 4 = {3 + 4}"""



















