class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}, I am {self.age}")


p = Person("Dima", 36)

say_hi = p.say_hello
p.say_hello()  # Hello, my name is Dima, I am 36
say_hi()  # Hello, my name is Dima, I am 36
