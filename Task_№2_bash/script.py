import glob
import os
import time

# Записываем начальный таймстемп
start_time = time.time()

# Путь к директории с логами
log_directory = "/home/rusov/Downloads/"

# Счетчик для количества строк с совпадением
match_count = 0

# Получаем список всех файлов .txt в указанной директории и поддиректориях
contents = glob.glob(os.path.join(log_directory, "**/*.txt"), recursive=True)

# Проходим по каждому файлу
for file_path in contents:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if 'php7.4' in line:
                match_count += 1


end_time = time.time()

# Вычисляем время выполнения скрипта
execution_time = end_time - start_time

output = f"Количество строк с 'php7.4': {match_count}\nВремя выполнения скрипта: {execution_time:.3f} секунд\n"

# Выводим результаты в файл
with open('output_python.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(output)

print("Результат в файле output_bash.txt")