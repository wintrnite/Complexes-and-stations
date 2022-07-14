# Ближайшие остановки к ЖК

### Описание:

    Сервис для нахождения ближайших остановок к ЖК 
    на расстоянии не более, чем за 1000 метров 
    с ответом в формате CSV.

### Как использовать:

Необходимо иметь установленный PostgreSQL, PostGIS.
Также нужно предварительно загрузить в базу данных
данные (в таблицу
complexes [отсюда](https://docs.google.com/spreadsheets/d/1bPYa85nthsvZJO4MhjktTk0QrGYs5Rns/edit?rtpof=true&sd=true)
и в таблицу
stations [отсюда](https://data.mos.ru/opendata/7704786030-ostanovki-nazemnogo-gorodskogo-passajirskogo-transporta/data/table?versionNumber=7&releaseNumber=335)) или воспользоваться готовым дампом из файла postgres_db.dump

После загрузки данных необходимо создать виртуальное окружение

    make venv

а затем запустить приложение

    make app

(make работает для Linux и Mac OS).

Результат работы приложения будет лежать в файле

    answer.csv

___

### Для разработки:

Запустить линтеры

    make lint

Автоматически отформатировать код

    make format


    
