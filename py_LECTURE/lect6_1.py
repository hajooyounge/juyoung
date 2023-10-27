# 파일 생성하기
# f = open("new.txt", 'w')
"""
f = open("temp.txt" , 'w+')
f.close()
"""
#파일 쓰기
"""
file = open("temp.txt", 'w')

file.write("hello\n")
file.write("world")

file.close
"""
"""

file = open("temp.txt", 'w')

for i in range(100):
    file.write(f"{i}\n")
    
file.close
"""


#c:/User/Catholic/temp.txt
"""
f = open("c:\\Users\\Catholic\\temp.txt","w")
for i in range(100):
    f.write(f"{i}\n")
    
f.close
"""

# 추가 쓰기
"""
file = open("c:\\Users\\Catholic\\temp.txt", "a")

file.write("hello\n")
file.write("world")

file.close
"""
#파일 읽기
"""
f = open("temp.txt", "r")
res = f.read()
print(res)

f.close()
"""

#다른경로 파일 읽기
"""
f = open("c:\\Users\\Catholic\\temp.txt", "r")
res = f.read()
print(res)

f.close()
"""

#readline
"""
f = open("temp.txt", "r")

for i in range(110):
    res = f.readlines()
    print(res)

f.close()
"""

#readline 전체 읽기
"""
f = open("temp.txt", "r")
res = f.readlines()
print(res)

f.close()
"""

#readline 읽기
"""
f = open("temp.txt", "r")
line = f.readlines()
for i in line:
    print(i)

f.close()
"""

#file object

f = open("temp.txt", "r")
for line in f:
    print(line)

f.close()
