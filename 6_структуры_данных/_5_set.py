bri = set(["Бразилия", "Беларусь", "Индия"])

print("bri", bri)
print("Индия" in bri)

print("США" in bri)

bric = bri.copy()
print("bric", bric)

bric.add("Китай")
print("bric", bric)

print(bric.issuperset(bri))
print("bric", bric)
print("bri", bri)
