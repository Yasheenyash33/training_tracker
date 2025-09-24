# 🏫 Training Tracker System

A comprehensive training management system built with Django REST API backend and React frontend. Designed to streamline the management of training programs, batches, trainers, and trainees with role-based access control.

## ✨ Features

### 🔐 Authentication & Authorization
- JWT-based authentication with refresh tokens
- Role-based access control (Admin, Trainer, Trainee)
- Password reset functionality
- Secure user registration and login

### 👥 User Management
- Multi-role user system (Admin, Trainer, Trainee)
- User profile management
- Role-specific dashboards and permissions
- Audit logging for all user actions

### 📚 Training Programs
- Create and manage training programs
- Program categorization and descriptions
- Topic-wise program structure
- Program status tracking (Active/Inactive)

### 👨‍👩‍👧‍👦 Batch Management
- Create and manage training batches
- Assign programs to batches
- Trainer and trainee assignments
- Batch progress tracking

### 📊 Progress Tracking
- Individual trainee progress monitoring
- Topic-wise completion tracking
- Progress reports and analytics
- Performance metrics

### 🎓 Classes & Sessions
- Schedule and manage training classes
- Class attendance tracking
- Trainer session management
- Class materials and resources

### 🔧 Admin Features
- Complete user management
- System configuration
- Data export and reporting
- Audit trail monitoring

## 🛠 Technology Stack

### Backend
- **Django 5.2** - Python web framework
- **Django REST Framework** - API development
- **Simple JWT** - JSON Web Token authentication
- **SQLite** - Database (development)
- **MySQL** - Database (production ready)
- **Django CORS Headers** - Cross-origin resource sharing

### Frontend
- **React 19** - Frontend framework
- **Material-UI (MUI)** - Component library
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **React Hook Form** - Form management

### Development Tools
- **Python 3.8+** - Backend language
- **Node.js 14+** - Frontend runtime
- **Git** - Version control
- **VS Code** - Recommended IDE

## 📁 Project Structure

```
training_tracker/
├── training/                    # Main Django app
│   ├── models.py               # Database models
│   ├── views.py                # API views and logic
│   ├── serializers.py          # API serializers
│   ├── urls.py                 # URL routing
│   ├── permissions.py          # Custom permissions
│   ├── management/             # Django management commands
│   └── migrations/             # Database migrations
├── frontend/                   # React frontend
│   ├── src/
│   │   ├── components/         # React components
│   │   │   ├── auth/           # Authentication components
│   │   │   ├── dashboard/      # Dashboard components
│   │   │   ├── programs/       # Program management
│   │   │   ├── batches/        # Batch management
│   │   │   ├── users/          # User management
│   │   │   ├── progress/       # Progress tracking
│   │   │   └── layout/         # Layout components
│   │   ├── contexts/           # React contexts
│   │   ├── services/           # API services
│   │   └── App.js             # Main app component
│   ├── public/                # Static assets
│   └── package.json           # Frontend dependencies
├── training_tracker/          # Django project settings
│   ├── settings.py           # Project configuration
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── requirements.txt          # Python dependencies
├── manage.py               # Django management script
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- Git

### Backend Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd training_tracker
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create sample users (optional)**
   ```bash
   python manage.py create_sample_users
   ```

6. **Start Django development server**
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Start React development server**
   ```bash
   npm start
   ```

4. **Access the application**
   - Frontend: http://localhost:3001
   - Backend API: http://localhost:8000
   - Admin Panel: http://localhost:8000/admin/

## 🔑 Default Credentials

### Admin User
- **Username:** admin
- **Email:** admin@example.com
- **Password:** (set during user creation)

### Sample Users
Run `python manage.py create_sample_users` to create sample users with different roles.

## 📡 API Endpoints

### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token
- `POST /api/register/` - User registration
- `POST /api/password-reset/` - Request password reset
- `GET /api/auth/user/` - Get current user info

### Users
- `GET /api/users/` - List all users (Admin only)
- `POST /api/users/` - Create new user (Admin only)
- `GET /api/users/{id}/` - Get user details
- `PUT /api/users/{id}/` - Update user
- `DELETE /api/users/{id}/` - Delete user

### Programs
- `GET /api/programs/` - List all programs
- `POST /api/programs/` - Create new program (Admin only)
- `GET /api/programs/{id}/` - Get program details
- `PUT /api/programs/{id}/` - Update program
- `DELETE /api/programs/{id}/` - Delete program

### Batches
- `GET /api/batches/` - List all batches
- `POST /api/batches/` - Create new batch (Trainer/Admin)
- `GET /api/batches/{id}/` - Get batch details
- `PUT /api/batches/{id}/` - Update batch
- `DELETE /api/batches/{id}/` - Delete batch

### Progress Records
- `GET /api/progress-records/` - List progress records
- `POST /api/progress-records/` - Create progress record
- `GET /api/progress-records/{id}/` - Get progress details
- `PUT /api/progress-records/{id}/` - Update progress
- `DELETE /api/progress-records/{id}/` - Delete progress

## 👤 User Roles & Permissions

### Super Admin
- Full system access
- User management
- System configuration
- All CRUD operations

### Trainer
- Manage assigned batches
- View trainee progress
- Create and update classes
- Update progress records

### Trainee
- View own profile
- View enrolled batches
- View own progress
- Update personal information

## 🗄 Database Models

### User
- Custom user model with roles
- Profile information
- Authentication fields

### Program
- Training program details
- Topics and descriptions
- Status management

### Batch
- Training batch information
- Program associations
- Trainer assignments

### BatchTrainee
- Trainee-batch relationships
- Enrollment status
- Completion tracking

### ProgressRecord
- Individual progress tracking
- Topic-wise completion
- Performance metrics

### Class
- Training session details
- Schedule management
- Attendance tracking

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:3000
```

### Django Settings
Key settings in `training_tracker/settings.py`:
- Database configuration
- CORS settings
- Authentication settings
- Static files configuration

## 🧪 Testing

### Backend Testing
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test training

# Run with coverage
pip install coverage
coverage run manage.py test
coverage report
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 🚀 Deployment

### Backend Deployment
1. Set `DEBUG=False` in settings.py
2. Configure production database (MySQL/PostgreSQL)
3. Set up static files serving
4. Configure CORS for production domains
5. Use a production WSGI server (Gunicorn + Nginx)

### Frontend Deployment
1. Build the production version
   ```bash
   cd frontend
   npm run build
   ```
2. Serve the `build` folder with a web server
3. Configure API base URL for production



## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint for React code
- Write meaningful commit messages
- Add tests for new features
- Update documentation

## 📝 API Documentation

### Authentication
All API requests (except login/register) require authentication via JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

### Response Format
```json
{
  "status": "success",
  "data": { ... },
  "message": "Operation completed successfully"
}
```

### Error Handling
```json
{
  "status": "error",
  "message": "Error description",
  "errors": { ... }
}
```

## 🔍 Troubleshooting

### Common Issues

1. **CORS Errors**
   - Ensure CORS_ALLOWED_ORIGINS includes your frontend URL
   - Restart Django server after CORS changes

2. **Database Connection Issues**
   - Check database settings in settings.py
   - Ensure database server is running
   - Run migrations if needed

3. **Authentication Issues**
   - Verify JWT token is valid
   - Check token expiration
   - Ensure user has required permissions

4. **Frontend Build Issues**
   - Clear node_modules and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies are installed

### Debug Mode
Enable debug logging by setting `DEBUG=True` in settings.py and checking Django console output.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Support

For support, please contact the development team or create an issue in the repository.

---


