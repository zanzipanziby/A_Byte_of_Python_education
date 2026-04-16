poem = """\
Программировать весело.
Если работа скучна,
Чтобы придать ей весёлый тон -
используй Python!
"""

f = open("poem.txt", "w", encoding="utf-8")

f.write(poem)

f.close()

f = open("poem.txt", encoding="utf-8")


while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end="")

f.close()
