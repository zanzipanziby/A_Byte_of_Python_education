x = 50


def func(x):
    print("x равен", x)
    x = 2
    print("Замена локальной переменной x на", x)


func(x)
print("x по-прежннему", x)
