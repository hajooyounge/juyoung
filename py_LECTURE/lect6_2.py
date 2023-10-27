#속성 출력
"""
class Person :
	name = "python"
	age = 23
	number = "01012345678"
 
 
p = Person()
print(p.name)
print(p.age)
print(p.number)


pl = Person
print(pl.name)
print(pl.age)
print(pl.number)
"""

# 메서드, 셀프
"""

class Person :
	name = "python"
	age = 23
	number = "01012345678"

	def getIntroduce(self):
		return f"My name is {self.name}"

p = Person()
print(p.name)
print(p.age)
print(p.number)
print(p.getIntroduce())
"""

# 클래스 초기화
"""
class Person :
	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.number = number
  
p = Person("hello", 24, "01087654321")
p1 = Person("he", 21, "0108")
p2 = Person("hee", 24, "0287654321")

print(p.name)
print(p1.name)
print(p2.name)
"""

# 클래스 함수
"""
class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

p = Person("hello", 24, "01087654321")
print(p.name)
print(p.count)

p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.count)

p2 = Person("hee", 24, "0287654321")
print(p2.name)
print(p2.count)

print(p.count)
print(p1.count)
print(p2.count)
"""

# 클래스 메서드
class Person :
	count = 0

	def __init__(self, name, age, number):
		self.name = name
		self.age = age
		self.nmuber = number
		Person.count += 1

	@classmethod
	def getCount(cls) : 
		return cls.count

p = Person("hello", 24, "01087654321")
print(p.name)
print(p.getCount())
p1 = Person("he", 21, "0108")
print(p1.name)
print(p1.getCount())
p2 = Person("hee", 24, "0287654321")
print(p2.name)
print(p2.getCount())
