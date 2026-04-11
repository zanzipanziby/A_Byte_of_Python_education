address_book = {
    "Swaroop": "swaroop@swaroopch.com",
    "Larry": "larry@wall.org",
    "Matsumoto": "matz@ruby-lang.org",
    "Spammer": "spammer@hotmail.com",
}

print(address_book)
print("Адрес Swaroop'а:", address_book["Swaroop"])

del address_book["Spammer"]
print(address_book)

print(f"\nВ адресной книге {len(address_book)} контактов\n")

for name, address in address_book.items():
    print(f"Контакт {name} с адресом {address}")

address_book["Guido"] = "guido@python.org"

if "Guido" in address_book:
    print("\nАдрес Guido: ", address_book["Guido"])
