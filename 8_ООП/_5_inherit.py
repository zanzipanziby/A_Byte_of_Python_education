class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Создан SchoolMember: {self.name}")

    def tell(self):
        print(f"Имя: {self.name}, Возраст: {self.age}", end=", ")


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Создан Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Зарплата: {self.salary}")


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Создан Student: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Оценки: {self.marks}")


t = Teacher("Марк", 40, 30000)
s = Student("Андрей", 25, 75)

print()

members = [t, s]

for member in members:
    member.tell()
