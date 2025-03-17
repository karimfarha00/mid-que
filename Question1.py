class Person:
	def __init__(self, name):
		self.name = name

class Student(Person):
	def __init__(self, name, grade):
		super().__init__(name)
		self.grade = grade

	def displayGrade(self):
		print(f"{self.name}: {self.grade}")

p = Student("Nabiha", 10)
p.displayGrade()
