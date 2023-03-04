# track

Консольная утилита для трэкинга времени на работу на проектами.

### Описание
Данная утилита позволяет добавлять время затраченное на работу над проектом с сохранением текущей даты, а также вывода статистики в консоль по затраченному времени на запрошенный проект.

### Установка

1. Клонируйте данный репозиторий `git clone https://github.com/mikhail-mmm/track_task.git`.
2. Создайте виртуальное окружение `python -m venv <name_env>`.
3. Установите зависимости `pip install -r requirements.txt`.

### Запуск

1. Для добавления времени работы над проектом `python <path_to_directory_track.py> track --project=<name_project> <time in minutes>`.
2. Для вывода статистика по затраченному времени на работу над проектом `python <path_to_directory_track.py> stat --project=<name_project> --days=<amount_of_days>`.
3. Для получения справки основной утилиты `python <path_to_directory_track.py> -h`.
4. Для получения справки по подпрограммам `python <path_to_directory_track.py> track -h` и `python <path_to_directory_track.py> stat -h`.
