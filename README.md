# Cистема управления заказами в кафе

## Описание
Полнофункциональное веб-приложение на Django для управления заказами в кафе. Приложение
позволяет добавлять, удалять, искать, изменять и отображать заказы.

## Установка

1. Клонируйте репозиторий:
   
   git clone https://github.com/eskealexey/Cafe_management_system.git

2. Создайте виртуальное окружение (рекомендуется):
   python3 -m venv venv

3. Активируйте его:
  На Windows:
  venv\Scripts\activate

  На macOS/Linux:
  source venv/bin/activate

4. Установите зависимости:
  pip install -r requirements.txt

5. Перейдите в каталог проекта kafe

6. Запусите миграцию:
   python3 manage.py makemigrations
   python3 manage.py makemigrations menu
   python3 manage.py makemigrations order
   python3 manage.py migrate

7. Создайте суперпользователя:
   python3 manage.py createsuperuser

8. Запустите проект на выполнение:
   python3 manage.py runserver

9. В браузере перейдите по адресу: http://127.0.0.1:8000

## Работа в приложении:
Гавная страница:
![изображение](https://github.com/user-attachments/assets/3612df7e-9d89-4176-9121-4649f97860e7)

Страница заполнения меню:
![menu](https://github.com/user-attachments/assets/69efb8f1-dd9f-42b0-aafa-b2fdf0a2d2e0)

Страница добавления заказов:
![addorder](https://github.com/user-attachments/assets/24328e3a-4a6c-4504-a506-0be25b17aced)

Страница показа заказов:
![vieworder](https://github.com/user-attachments/assets/72cf45d2-347d-4169-8540-ffeea0caeeb3)

Страница изменения статуса заказа:
![changestatus](https://github.com/user-attachments/assets/61833411-dbea-408e-8efa-ab6e1fa5754f)

Просмотр выручки за смену:
![revenue](https://github.com/user-attachments/assets/b4ce0631-704c-43ec-897f-eb2fd3f736c5)




    





