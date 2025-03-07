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




    





