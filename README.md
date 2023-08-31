Тестовое задание Api


Задание. Описание тест-кейса:
Предусловие:

● Авторизоваться в сервисе Yandex

Шаги:

● Выполнить запрос на получение всех папок и файлов на диске 

● Вывести список доступных папок и файлов

Ожидаемый результат:  ● Отображается список доступных папок и файлов

Постусловие: ● Разлогиниться


Вывод выглядит так : 

['%2f', '/gfd.gdfg.jpeg', '/test', '/test/egerge', '/test/egerge/gerge', '/test/egerge/gerge/trhtrh.pptx', '/test/egerge/gerger.pptx', '/test/egerge/gger.docx', '/test/egerge/gregerger.xlsx', '/test/egerge/rge.docx', '/test/egerge/rgerge', '/test/egerge/rgerge/kuyk.xlsx', 
'/test/fdewd.docx', '/test/fhgdh.docx', '/test/rfhf.docx', '/Горы.jpg', '/Зима.jpg', '/Мишки.jpg', '/Море.jpg', '/Москва.jpg', '/Новая папка', '/Приложения', '/Приложения/test_api', '/Санкт-Петербург.jpg', '/Хлебные крошки.mp4', '/апаувп', '/еенккн', '/еенккн/Новая папка', '/еенккн/Новая папка/Новая папка', '/кацук']

Язык программирования/версия : Python 3.11.2 Основные библиотеки : Requests 4, pytest - (Полный список можно посмотреть в файл recruitment.txt) Паттерн - Page object(Попытка)

Углублённая информация по проекту: 

Использовалось Api яндекс диска : https://yandex.ru/dev/disk/

Base_APP.py - содержит методы requests 

main.py - запуск тестов 

conftest.py - содержит фикстуры нужные для тестов в папке Test

папка Test - содержит файлы тестов 

_test.py - содержит сам тест


Инструкции по запуску: 1 Установить библиотеки из файла recruitment.txt 2. В файле start.bat - написать путь к pytest 3. Запустить start.bat или main

P.s Если задание воспринято мной не корректно, прошу прощения.
