#!/bin/bash

# начальный таймстемп в миллисекундах
start_time=$(date +%s%3N)

# Путь к директориям
log_directory="/home/rusov/Downloads/"

# Счетчик
match_count=0

# Проходим по всем файлам в указанной директории
for file in "$log_directory"/*
do
  # Проверяем, что это файл
  if [[ -f $file ]]; then
    match_count=$((match_count + $(grep -c 'php7.4' "$file")))
  fi
done

end_time=$(date +%s%3N)

# Вычисляем время выполнения скрипта
execution_time=$((end_time - start_time))

# Выводим результаты и перенаправляем в файл
{
  echo "Количество строк с 'php7.4': $match_count"
  echo "Время выполнения скрипта: $execution_time миллисекунд"
} > output.txt
