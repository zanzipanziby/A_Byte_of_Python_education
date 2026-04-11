def print_max(x, y):
    """Выводит максимальное из двух чисел.
    Оба аргумента должны быть целыми числами.
    """
    x = int(x)
    x = int(y)

    if x > y:
        print(x, "наибольшее")
    else:
        print(y, "наибольшее")


print_max(10, 20)
print(print_max.__doc__)
