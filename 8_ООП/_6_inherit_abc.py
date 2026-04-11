from abc import ABCMeta, abstractmethod


class SchoolMember(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Создан SchoolMember: {self.name}")

    @abstractmethod
    def tell(self):
        print(f"Имя: {self.name}, Возраст: {self.age}", end=" ")


class Teacher(SchoolMember):
    """Представляет преподавателя."""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Создан Teacher: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Зарплата: {self.salary:d}")


class Student(SchoolMember):
    """Представляет студента."""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Создан Student: {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Оценки: {self.marks:d}")


t = Teacher("Mrs. Shrividya", 40, 30000)
s = Student("Swaroop", 25, 75)

# m = SchoolMember('abc', 10)
# Это приведёт к ошибке: "TypeError: Can't instantiate abstract class
# SchoolMember with abstract methods tell"
print()  # печатает пустую строку

members = [t, s]

for member in members:
    member.tell()  # работает как для преподавателя, так и для студента
