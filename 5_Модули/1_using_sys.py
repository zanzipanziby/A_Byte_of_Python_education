import sys

print("Аргументы командной строки")

for i in sys.argv:
    print(i)


print("\n\n переменная PYTHONPATH содержит", sys.path, "\n\n")
