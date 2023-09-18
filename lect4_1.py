#input
"""
num = input("4")
#print("nmber", num)
print("nmber", int(num))
"""
#type
"""
a = 12
print(type(a))


a = 12.01
print(type(a))


a = "a"
print(type(a))


a = "abcd"
print(type(a))


a = [3, 2, 1,]
print(type(a))
"""

#행변환
"""
a = 65
# a = "65"
print(int(a))
print(str(a))
print(hex(a))  #str 자료형 변환
print(oct(a))  #정수를 8진수 문자열 반환
print(chr(a))  #정수를 문자로 반환 하기 ASCII Code 확인
print(ord("A"))  # 문자로 반환 하기 ASCII Code 확인
"""

# pow 거듭제곱을 계산
"""
print(pow(2, 2))
print(pow(2, 6))
print(pow(3, 4))
print(3 ** 4)
"""

#print(divmod(10, 3)) #나누기 몫과 나머지를 반환

#print(round(3.14))  #올림된 값 출력

# alt shift a 주석처리

""" 
a = (3, 5, 7)
b = list(a)
c = tuple(b)

print(b)
print(a)

print(type(a))
print(type(b))
print(type(c))

"""

# rarge
"""
for i in range(2,7):
    print(i)
"""
"""
for i in range(6):
    print(i)
"""
"""  
for i in range(1, 20, 3):
    print(i)
""" 

# max, min, sum

""" 
a = [3, 5, 6, 9]
print(max(a))
print(min(a))
print(sum(a)) 
"""

# abs 절댓값 변환

""" 
print(abs(-3))
print(abs(3.0))
print(abs(-3.0))
"""

# sorted 데이터 타입내 정렬

""" 
a = [5, 3, 1, 9, 4]
print(sorted(a))
print(sorted(a, reverse=True)) 
"""

# enumerate 데이터타입내 인덱스와 값 반환
""" 
a = [5, 3.14, False, 9, "string"]
print(*enumerate(a)) 
"""

# zip 여러 데이터타입내 데이터를 합쳐서 반환

""" 
a = [1, 2, 3]
b = [4, 5, 6]

print(zip(a,b))
print(*zip(a,b)) 
"""


#any, all
""" 
a = [True, True, False]
b = [True, True, True]
print(any(a))
print(all(a))
print(all(b))
"""

# format 문자열 포맷팅 처리

""" 
a = 20
b = 23
c = "a는 (), b 는 {}, {}".format(a, b, "pyhon")

print(c) 
"""
"""

a = 3
# print(globals())
# print(locals())

print(dir(a))

print(callable(a))
"""

#lambda
""" 
add = lambda a, b : a + b
print(add(2, 3))
"""


""" 
add = lambda a, b : a + b
sud = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print(add(2,3))
print(sud(2,3))
print(mul(2,3))
print(div(2,3)) 
"""

#사용자 정의
""" def add_numbers(x, y):
    return x + y """

# 함수 호출
""" result = add_numbers(4,5)
print(result) """

""" 
def greet(name):
    print(name)
    print("hello," + name + ", how are you")
    
greet("pyton")
"""
""" def add(a, b) : 
	print(a + b)

def sub(a, b) :
	return a - b

def mul() :
	return 2 * 4

def div() :
	print(4 / 2)

add(3, 5)
sub(3, 5)
mul()
div() """

# 입력값 홀/짝수

""" def is_even(n):
    if n % 2 == 0:
        print("짝수")
    else :
        print("홀수")
        
num = input("숫자를 입력하세요 : ")

is_even(int(num)) """

# 문자열 반전

""" def reverse_string(msg):
    return msg[::-1]

in_str = input("문자열 : ")
print(reverse_string(in_str)) """

#두수를 입력받아 사칙연산


""" def add(a,b) :
    return int(a) + int(b)

def add(a,b) :
    return int(a) - int(b)

def add(a,b) :
    return int(a) * int(b)

def add(a,b) :
    return int(a) / int(b)

a = input("a 를 입력하세요")
b = input("b 를 입력하세요") """

""" def calc(a,b):
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) * int(b))
    print(int(a) / int(b))

a = input("a 를 입력하세요")
b = input("b 를 입력하세요") 

calc = (a,b) """


# 5개 수 입력

def sum_num(num):
    return sum(num)

nums = []

for i in range(1,6):
    innum = int(input(f"{i} 번째 숫자 입력 :"))
    nums.append(innum)
    
print(sum_num(nums))
