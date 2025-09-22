# Training Tracker Backend
## Quick start
1. Create virtualenv and install requirements: `pip install -r requirements.txt`
2. Create MySQL DB and set credentials in .env (see .env.example)
3. Run `python manage.py makemigrations` and `python manage.py migrate`
4. Create sample users: `python manage.py create_sample_users`
5. Run server: `python manage.py runserver`
