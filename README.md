# Social Media Project

Проста соцмережа на Django 5 (SQLite). Є профілі, друзі та підписки, пости з коментарями, лайками й репостами, групи та канали.

Застосунки: `accounts` (вхід/реєстрація), `profiles`, `posts`, `groups`, `requests` (запити в друзі).

## Запуск

```
python -m venv venv
venv\Scripts\activate        # Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Сайт буде на http://127.0.0.1:8000/

## Адмін

Вхід за email. Команда `createsuperuser` працює, вхід в адмінку за username
