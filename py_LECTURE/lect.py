"""
a = 5
b = 5

print(a is b)  
print(a is not b)  
"""
"""
a = 3
b = 3.0

print(a == b)
print( a is b)
print(a is not b)
"""

"""
a = [3 , 5, 1]
b = a

print(a is b)

a[0] = 2

print(a, b)

print(a is b)
"""
"""
a = 2 + 3 * 4
a = 10 / 5 / 2
a = 2 ** 3 ** 2
a = 10 % 3 % 2
a = 1 + 2 > 3 and 4 - 1 < 2
a = not False and True
a = not True or False and True
a = 1 * 2 | 3 ^ 4
a = 5 in [3, 4, 5] or 2 not in [1, 2, 3]
a = 2 * -3 // 2
a = 1==2
a = False != 3

print(a)
"""
"""
#x = 10 
#x = -1 
x = 0 

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero") 
    
"""

# if 짝수, 홀수
"""
num = 26
num = 21

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")
"""

# if 두수 비교
"""
a = 2
b = 3
if a == b:
    print("같아요")
else:
    print("달라요")
"""  
    
# if a or b 인지
"""  
char = "a"
if char == "a" or char == "b":
    print("'a' 또는 'b'입니다.")
    
else:
    print("'a' 또는 'b'가 아닙니다.")
"""        

#for 예시
""" 
fruits = ["apple", "banana", "cherry"]

for fruitin in fruits:
    print(fruits)
""" 

# 이중 for문 예시
""" 
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_list:
    for num in row:
        print(num)
""" 
""" 
# fot 0 ~ 9 출력

for i in range(10) :
    print(1)
"""     
    
# fot 낱말 출력
"""   
for char in "python" :
    print(char)
"""       
# fot 역순출력 reversed
"""  
fruits = ["apple", "banana"< "cherry"] 

for fruit in reversed(frits):
    print(fruit)
"""
# fot 역순출력 sorted
"""
for fruit in sorted(fruits, reverse=True):
    print(fruit)
"""
# fot 구구단
"""
for i in range(1, 10):
    for j in range(1,10):
        print(i, "x", j, "=", i*j)
"""

# for ~ else 문
"""
rang = [5, 8, 3, 1, 6]

for i in rang:
	print("element : ", i)
else :
	print("end process")
"""
"""
for i in range(10):
    if i == 7:
        print("break", i)
        break
    elif i == 1:
        print("continue", i)
        continue
    else:
        print("pass", i)
        pass

    print(i)
"""

# while 1 ~ 5 출력
"""
i = 1

while i <= 5:
    print(i)
    i += 1
"""


# while 0 ~ 9 출력
"""
i = 0

while i <= 9:
    print(i)
    i += 1
"""


# while 문자열을 한글자씩 출력
""" 
str_word = "python"
i = 0

while i < len(str_word):
    print(str_word[i])
    i += 1
"""


#1부터 10까지의 총합 출력
"""
sum = 0
i = 1

while i <= 10:
    sum += i
    i += 1
    
print (sum)
"""

#1에서 100까지의 짝수, 홀수 출력하기

i = 1


while i <= 100:
    if i % 2 == 0:
        print("짝수 : ", i)
    elif i % 2 == 1:
        print("홀수 : ", i)
    i += 1




#1에서 100까지의 7의 배수만 출력하기
"""
i = 1
while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1
"""

