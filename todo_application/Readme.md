# Todo Application

A Django todo app with custom user accounts. Each user has their own private task list.

## Features
- Custom user model (phone, address, date of birth)
- Register, login, logout
- Create, edit, delete and complete tasks
- Task priority and due date
- Profile page
- Users can only see and edit their own tasks

## Setup

```bash
git clone <your-repo-url>
cd todo_application
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/