import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    cleaned_text = re.sub(r"[^a-zA-Z0-9а-яА-ЯёЁ]", "", text).lower()
    return cleaned_text == reverse(cleaned_text)


somthing = input("Введите текст: ").lower()

if is_palindrome(somthing):
    print("Это полиндром")
else:
    print("Это не полиндром")
