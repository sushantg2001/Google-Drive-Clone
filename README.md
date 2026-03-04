# Google Drive Clone

A full-stack web application that replicates core features of Google Drive, allowing users to upload, manage, and share files and folders across the cloud. Built with Django REST Framework backend and React frontend.

![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)
![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)
![MIT License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📋 Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Contributing](#contributing)
- [License](#license)

---

## ✨ Features

### Core File Management
- ✅ **Upload & Store Files** - Upload files to personal cloud storage
- ✅ **Create Folders** - Organize files in hierarchical folder structure
- ✅ **File Operations** - View, download, delete, and move files
- ✅ **Folder Management** - Create, rename, delete, and navigate folders
- ✅ **File Preview** - View file details and metadata

### Sharing & Access Control
- ✅ **Share Files & Folders** - Share with specific users
- ✅ **Access Control** - Manage permissions for shared resources
- ✅ **Shared with Me** - View resources shared by other users
- ✅ **User Management** - Create accounts and manage user profiles

### Authentication & Security
- ✅ **User Authentication** - Secure signup and login
- ✅ **Email Verification** - Verify user email addresses
- ✅ **Password Management** - Secure password hashing (Argon2)
- ✅ **CORS Support** - Cross-Origin Resource Sharing configured

### Developer Features
- ✅ **REST API** - Fully documented REST API with DRF
- ✅ **API Documentation** - Interactive API docs with drf-spectacular
- ✅ **Test Coverage** - Comprehensive pytest test suite
- ✅ **Type Checking** - MyPy for static type checking
- ✅ **Environment Management** - Multiple environment configurations

---

## 🛠 Technology Stack

### Backend
- **Framework**: Django 4.0.8
- **API**: Django REST Framework 3.14.0
- **Database**: PostgreSQL
- **Cache**: Redis
- **Authentication**: Django-allauth 0.51.0
- **API Documentation**: drf-spectacular 0.24.2
- **CORS**: django-cors-headers
- **Testing**: pytest, coverage
- **Type Checking**: mypy

### Frontend
- **Framework**: React 18.2.0
- **Routing**: React Router DOM 6.4.5
- **HTTP Client**: Axios 1.2.1
- **UI Library**: Material-UI (MUI 5.10.16)
- **Build Tool**: Create React App

### DevOps & Tools
- **Environment Management**: Python 3.x + conda
- **Package Management**: pip, npm
- **Code Style**: Black, Flake8

---

## 📁 Project Structure

```
.
├── drive_backend/                  # Django Backend Application
│   ├── config/                     # Django settings & configuration
│   │   ├── settings/               # Environment-specific settings
│   │   │   ├── base.py             # Base configuration
│   │   │   ├── local.py            # Local development settings
│   │   │   ├── production.py       # Production settings
│   │   │   └── test.py             # Testing settings
│   │   ├── api_router.py           # DRF router configuration
│   │   ├── urls.py                 # URL routing
│   │   └── wsgi.py                 # WSGI configuration
│   │
│   ├── drive_backend/              # Main application package
│   │   ├── file_system/            # File & folder management app
│   │   │   ├── models.py           # File, Folder models
│   │   │   ├── views.py            # ViewSets for files/folders
│   │   │   ├── api/                # API endpoints
│   │   │   ├── migrations/         # Database migrations
│   │   │   ├── signals.py          # Django signals
│   │   │   └── tests.py            # Test suite
│   │   │
│   │   ├── users/                  # User authentication app
│   │   │   ├── models.py           # Custom User model
│   │   │   ├── views.py            # User ViewSets
│   │   │   ├── forms.py            # User forms
│   │   │   ├── api/                # User API endpoints
│   │   │   ├── adapters.py         # Social auth adapters
│   │   │   ├── context_processors.py
│   │   │   └── tests/              # User tests
│   │   │
│   │   ├── utils/                  # Utility functions
│   │   │   └── storages.py         # Storage configuration
│   │   │
│   │   ├── contrib/                # Contrib modules
│   │   └── conftest.py             # Pytest configuration
│   │
│   ├── docs/                       # Sphinx documentation
│   ├── scripts/                    # Utility scripts
│   │   ├── delete_folders_files.py
│   │   ├── view_access.py
│   │   ├── view_files_in_folder.py
│   │   └── view_user_details.py
│   │
│   ├── requirements/               # Dependency specifications
│   │   ├── base.txt                # Base requirements
│   │   ├── local.txt               # Local development
│   │   └── production.txt          # Production
│   │
│   ├── static/                     # Static files (CSS, JS, images)
│   ├── media/                      # User uploaded files
│   ├── templates/                  # HTML templates
│   ├── manage.py                   # Django management script
│   └── pytest.ini                  # Pytest configuration
│
├── frontend/                       # React Frontend Application
│   ├── src/
│   │   ├── Components/             # Reusable React components
│   │   │   ├── filecard.js         # File display card
│   │   │   ├── fileitem.js         # File list item
│   │   │   ├── Header.js           # Header navigation
│   │   │   ├── login.js            # Login page
│   │   │   ├── NewFile.js          # File upload
│   │   │   ├── privateroute.js     # Protected routes
│   │   │   └── showfiles.js        # File listing
│   │   │
│   │   ├── Services/               # API service calls
│   │   ├── styles/                 # Component styles
│   │   ├── App.js                  # Main App component
│   │   ├── App.css                 # App styles
│   │   ├── index.js                # React entry point
│   │   └── index.css               # Global styles
│   │
│   ├── public/                     # Static public files
│   ├── package.json                # NPM dependencies
│   └── README.md                   # Frontend documentation
│
└── drive.code-workspace            # VS Code workspace config
```

---

## 📋 Prerequisites

Before running the application, ensure you have:

- **Python 3.8+** - Backend runtime
- **Node.js 14+** & **npm 6+** - Frontend runtime
- **PostgreSQL 12+** - Database
- **Redis** (optional) - Caching layer
- **Git** - Version control

### Verify Installations
```bash
python --version
node --version
npm --version
psql --version
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sushantg2001/Google-Drive-Clone.git
cd Google-Drive-Clone
```

### 2. Backend Setup

#### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies
```bash
cd drive_backend
pip install -r requirements/local.txt
```

#### Create Database
```bash
# Create PostgreSQL database
createdb drive_backend

# Run migrations
python manage.py migrate
```

#### Create Superuser
```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

---

## ⚙️ Configuration

### Backend Configuration

#### Environment Variables
Create a `.env` file in the `drive_backend/` directory:

```env
# Database
DATABASE_URL=postgres://username:password@localhost:5432/drive_backend

# Django
DEBUG=True
SECRET_KEY=your-super-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Email (for verification)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Redis (optional)
REDIS_URL=redis://localhost:6379/0

# AWS/Storage (if using S3)
USE_S3=False
```

#### Settings Files
- **Local Development**: `config/settings/local.py`
- **Production**: `config/settings/production.py`
- **Testing**: `config/settings/test.py`
- **Base Settings**: `config/settings/base.py`

### Frontend Configuration

Update API endpoint in your components:
```javascript
// In Services files
const API_BASE_URL = 'http://localhost:8000/api/v1';
```

---

## 🏃 Running the Application

### Backend Server

```bash
cd drive_backend
python manage.py runserver
```

**Backend runs on**: `http://localhost:8000`

#### Useful Management Commands
```bash
# Create superuser
python manage.py createsuperuser

# Run migrations
python manage.py migrate

# Create migrations
python manage.py makemigrations

# Run tests
pytest

# Run tests with coverage
coverage run -m pytest
coverage html

# Type checking
mypy drive_backend
```

### Frontend Development Server

```bash
cd frontend
npm start
```

**Frontend runs on**: `http://localhost:3000`

#### Frontend Commands
```bash
# Development
npm start

# Build for production
npm run build

# Run tests
npm test

# Eject configuration (one-way operation)
npm run eject
```

### Access the Application
- **Frontend**: http://localhost:3000
- **Admin Panel**: http://localhost:8000/admin/
- **API Documentation**: http://localhost:8000/api/schema/swagger-ui/ (after installing drf-spectacular)

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/login/` | User login |
| POST | `/auth/logout/` | User logout |
| POST | `/auth/signup/` | User registration |
| POST | `/auth/email/verify/` | Verify email |
| POST | `/auth/password/reset/` | Reset password |

### Files
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/files/` | List all files |
| POST | `/api/files/` | Upload file |
| GET | `/api/files/{id}/` | Get file details |
| PATCH | `/api/files/{id}/` | Update file |
| DELETE | `/api/files/{id}/` | Delete file |
| GET | `/api/files/{id}/download/` | Download file |

### Folders
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/folders/` | List all folders |
| POST | `/api/folders/` | Create folder |
| GET | `/api/folders/{id}/` | Get folder details |
| PATCH | `/api/folders/{id}/` | Update folder |
| DELETE | `/api/folders/{id}/` | Delete folder |

### Sharing & Access
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/utility/shared_with_me/` | Get shared resources |
| POST | `/api/utility/share/file/` | Share file with user |
| POST | `/api/utility/share/folder/` | Share folder with user |
| GET | `/api/utility/share/file/` | List file access |
| GET | `/api/utility/share/folder/` | List folder access |

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users/` | List all users |
| GET | `/api/users/{id}/` | Get user profile |
| PATCH | `/api/users/{id}/` | Update profile |

### Utility
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/utility/get_entities/` | Get files & folders |

**Full API Documentation**: Available at `/api/schema/swagger-ui/` when running locally

---

## 🗄️ Database Models

### User Model
```python
class User (AbstractBaseUser, PermissionsMixin):
    username: str (unique)
    email: str (unique)
    first_name: str
    last_name: str
    is_staff: bool
    is_active: bool
    date_joined: datetime
    updated: datetime
```

### Folder Model
```python
class Folder:
    name: str (max_length=100)
    owner: ForeignKey(User)
    parent: ForeignKey(Folder, self-referential)
    created: datetime
    updated: datetime
    users: ManyToMany(User, through FolderAccess)

    @property
    def path: str  # Returns full folder path
```

### File Model
```python
class File:
    name: str (max_length=100)
    file: FileField()
    owner: ForeignKey(User)
    parent: ForeignKey(Folder)
    created: datetime
    updated: datetime
    users: ManyToMany(User, through FileAccess)

    @property
    def path: str  # Returns full file path
```

### FileAccess Model
```python
class FileAccess:
    file: ForeignKey(File)
    user: ForeignKey(User)
    can_view: bool
    can_download: bool
    can_share: bool
    created: datetime
```

### FolderAccess Model
```python
class FolderAccess:
    folder: ForeignKey(Folder)
    user: ForeignKey(User)
    can_view: bool
    can_create: bool
    can_delete: bool
    can_share: bool
    created: datetime
```

---

## 🧪 Testing

### Backend Tests

Run all tests:
```bash
cd drive_backend
pytest
```

Run with coverage report:
```bash
coverage run -m pytest
coverage html
open htmlcov/index.html
```

Run specific test file:
```bash
pytest path/to/test_file.py
```

Run with verbose output:
```bash
pytest -v
```

### Frontend Tests

```bash
cd frontend
npm test
```

---

## 📚 Additional Documentation

- **Backend Docs**: [drive_backend/README.md](drive_backend/README.md)
- **Frontend Docs**: [frontend/README.md](frontend/README.md)
- **API Documentation**: Available at `/api/schema/swagger-ui/`
- **Django Documentation**: https://docs.djangoproject.com/
- **React Documentation**: https://reactjs.org/

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Backend: Follow PEP 8, use Black formatter
- Frontend: Use ESLint and Prettier
- Commit messages: Use clear, descriptive messages

### Running Quality Checks

```bash
# Backend
cd drive_backend
black .
flake8
mypy drive_backend
pytest

# Frontend
cd frontend
npm run lint
npm test
```

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 Authors

- **Sushant G** - Initial work - [sushantg2001](https://github.com/sushantg2001)

---

## 📞 Support

For issues, questions, or suggestions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Include:
   - Environment details (OS, Python/Node versions)
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots/logs if applicable

---

## 🙏 Acknowledgments

- Built with [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django/)
- API framework: [Django REST Framework](https://www.django-rest-framework.org/)
- Frontend: [Create React App](https://create-react-app.dev/)
- UI Components: [Material-UI](https://mui.com/)

---

**Last Updated**: March 2026
**Repository**: [Google-Drive-Clone](https://github.com/sushantg2001/Google-Drive-Clone)
