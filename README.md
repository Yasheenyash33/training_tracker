# Training Tracker Backend
## Quick start

### 1. Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Database Setup (SQLite - Currently Active)
The project is currently configured to use SQLite (easier for development):
- Database file: `db.sqlite3`
- No credentials required
- Migrations are already applied

### 3. Run Migrations (if needed)
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Sample Users
```bash
python manage.py create_sample_users
```

### 5. Start Development Server
```bash
python manage.py runserver
```

### 6. Access Points
- **API Base:** http://127.0.0.1:8000/
- **Admin Interface:** http://127.0.0.1:8000/admin/
- **Admin Login:** username: `admin`, email: `admin@example.com`

### 7. For Production (MySQL)
To switch back to MySQL for production:
1. Update `.env` with MySQL credentials
2. Change `training_tracker/settings.py` database configuration
3. Run migrations: `python manage.py migrate`

## 📁 Project Structure
- `training/` - Main Django app
- `frontend/` - React frontend
- `training_tracker/` - Django project settings
