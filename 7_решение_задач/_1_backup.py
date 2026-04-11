import os
import shutil
import time

source = "../tmp/"
target_dir = "../tmp/backup"

# Убедимся, что папка backup существует
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# Пользовательский комментарий
comment = input("Введите комментарий: ")

# Формируем имя целевого файла

if len(comment) == 0:
    target_name = time.strftime("%Y%m%d%H%M%S")
else:
    target_name = time.strftime("%Y%m%d%H%M%S") + "_" + comment.replace(" ", "_")

target_path = os.path.join(target_dir, target_name)

print(f"Создаю архив: {target_path}")

try:
    # shutil.make_archive(base_name, format, root_dir)
    # base_name: полный путь к архиву БЕЗ расширения .zip
    # format: 'zip'
    # root_dir: папка, которую архивируем

    shutil.make_archive(target_path, "zip", source)

    print("Резервная копия успешно создана в", target_path)
except Exception as e:
    print("Создание резервной копии НЕ УДАЛОСЬ")
    print("Ошибка:", e)
