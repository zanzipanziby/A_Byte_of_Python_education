import pickle

# имя файла, в котором мы сохраним объект
shop_list_file = "shoplist.data"

# список покупок
shop_list = ["яблоки", "манго", "морковь"]

# Запись в файл
file = open(shop_list_file, "wb")
pickle.dump(shop_list, file)  # помещаем объект в файл
file.close()

del shop_list

# Считываем из хранилища
file = open(shop_list_file, "rb")
stored_list = pickle.load(file)  # загружаем объект из файла

print(stored_list)
