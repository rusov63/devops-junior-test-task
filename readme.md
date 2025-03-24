# Выполнение тестового задания на позицию junior DevOps

## 1. Задание - Ansible. Реализацию задачи смотрите папку "Task_№1_ansible".

- Что использовал, и в чем разница with_items от loop, 
- запустил и что-то не работает как узнать подробнее? 

Использовал fileglob, будет искать все файлы в указанной директории, и цикл loop переберет каждый из них, 
что может быть полезно для выполнения задач, таких как копирование файлов.

Команда предоставит больше информации о том, где именно произошла ошибка и какие данные были переданы
(-v, -vv, -vvv или -vvvv)
```
ansible-playbook -i hosts.ini site.yml -vvv
```
Это предоставит больше информации о том, где именно произошла ошибка и какие данные были переданы в модуль.


- **`with_items`**: 
  - это старый способ работы с циклами в Ansible. 
  Работает медленнее, но прост в использовании для базовых списков.

- **`loop`**:
  - появился в Ansible 2.5, более быстрый и гибкий. Поддерживает сложные структуры данных и фильтры. 
  Сейчас это рекомендуемый подход.

loop считается более современным и рекомендуется к использованию вместо with_items для новых проектов.

ссылка на документацию в Ansible:
- https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_loops.html



## 2. Задание - bash. Реализацию задачи смотрите папку "Task_№2_bash".
Написал два варианта решения - на bash (count_php_logs.sh) и python (script.py). 
Python-скрипт оказался быстрее: 0.041с против 0.070с на bash.

В Unix-системах Python поставляется по умолчанию. Для работы с Python я использовал встроенные библиотеки 
os и glob, которые доступны сразу и не требуют дополнительной установки. Хотя для асинхронной обработки 
можно было бы применить aiofiles, в данном случае это не является необходимым.
Для запуска python-скрипта нужна версия 3.0+:
```
python --version
python scripts.py
```

## 3. Задание - docker. Реализацию задачи смотрите папку "Task_№3_docker".

- Запуск в фоновом режиме:

```
docker-compose up -d
```
- Вопрос: Если файл default.conf в системе поменяется, изменится ли он внутри контейнера?

- Ответ: Да, изменится. При изменении default.conf в хост-системе файл автоматически обновится в 
контейнере благодаря volume-монтированию:

```
volumes:
  - ./default.conf:/etc/nginx/conf.d/default.conf
```

- Вопрос: Нужен ли рестарт при изменении файла default.conf?

- Ответ: Да, нужен рестарт nginx контейнера, чтобы применить новую конфигурацию.
Перезагружает конфигурацию без полного рестарта контейнера
```
docker-compose exec nginx nginx -s reload
```

- Вопрос: Если в docker-compose внесли изменения?

- Ответ: Нужно пересоздать контейнеры:

```
docker-compose up -d --force-recreate
```

- Вопрос: Что нравится больше docker-compose или docker-swarm?

- Ответ: Что касается docker-compose vs docker-swarm - для небольших проектов и разработки использую compose как более 
простой инструмент. Для прода с высокой нагрузкой больше подойдут swarm или kubernetes.

