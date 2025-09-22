# Training Tracker Backend
## Quick start
Create a Python virtualenv and install requirements:

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt


Create the MySQL database and user, update .env with credentials (or set env vars).

Run migrations:

python manage.py makemigrations

python manage.py migrate


Create sample users:

python manage.py create_sample_users


Start server:

python manage.py runserver
