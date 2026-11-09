# Django Fundamentals – Complete Beginner's Guide

## 1. What is Django?

Django is a high-level, open-source Python web framework used to build secure, scalable, and maintainable web applications quickly.

It follows the **Model-Template-View (MTV)** architectural pattern and provides built-in functionality for common web development tasks.

Django helps developers build websites without having to implement everything from scratch.

### What can we build with Django?

- E-commerce websites
- Social media platforms
- Blog applications
- Learning management systems
- Hospital management systems
- University management systems
- REST APIs
- Business management applications

### Why is Django important?

Building a website from scratch requires many things:

- User authentication
- Database management
- URL routing
- Security
- Request and response handling
- Form processing
- Admin interfaces

Django provides built-in tools for many of these tasks, reducing development time and effort.

---

## 2. Why Choose Django Over Other Technology Stacks?

There are several web development frameworks and technology stacks available.

For example:

| Technology  | Language   | Main purpose                          |
| ----------- | ---------- | ------------------------------------- |
| Django      | Python     | Full-featured web development         |
| Flask       | Python     | Lightweight web development           |
| FastAPI     | Python     | APIs and asynchronous applications    |
| Express.js  | JavaScript | Backend web development               |
| Laravel     | PHP        | Full-featured web development         |
| Spring Boot | Java       | Enterprise application development   |

### Why choose Django?

**1. Built-in features**

Django provides many features out of the box:

- Authentication system
- Admin dashboard
- ORM (Object Relational Mapper)
- URL routing
- Security protection
- Database migrations

**2. Faster development**

You don't need to build every feature manually.

**3. Security**

Django provides protection against common vulnerabilities, including:

- SQL injection
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF)
- Clickjacking

Security still depends on how you configure and use the framework.

**4. Scalability**

Django can support applications ranging from small websites to large production systems when properly designed and deployed.

**5. Python ecosystem**

Python provides extensive libraries for:

- Artificial intelligence
- Machine learning
- Data science
- Automation
- Backend development

Django can integrate with these technologies.

### Is Django better than every other framework?

No. Each framework has different strengths.

Django is particularly useful when you need a structured backend with authentication, database operations, admin functionality, and many built-in features.

---

## 3. Understanding Django Architecture (MTV)

Django follows the Model-Template-View architecture.

The three main components are:

### Model

Responsible for handling application data and database structure.

Example:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

### Template

Responsible for presenting information to users.

Example:

```html
<h1>Welcome to My Website</h1>
<p>Hello, {{ name }}</p>
```

### View

Responsible for processing requests and returning responses.

Example:

```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to Django!")
```

### How do they work together?

1. A user visits a URL.
2. Django matches the URL.
3. The corresponding view executes.
4. The view may retrieve data through a model.
5. The view may render a template.
6. Django returns an HTTP response to the browser.

---

## 4. Installing Django

Before creating a Django project, install Python and Django.

**Step 1: Check Python installation**

```bash
python --version
```

**Step 2: Create a virtual environment**

```bash
python -m venv venv
```

A virtual environment isolates your project's Python packages from other projects.

**Step 3: Activate the virtual environment**

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

**Step 4: Install Django**

```bash
pip install django
```

**Step 5: Check Django version**

```bash
django-admin --version
```

---

## 5. What Is a Django Project?

A Django project represents the entire web application.

It contains the overall configuration and connects different Django applications.

For example, imagine building an e-commerce website called `myshop`.

The project manages:

- Website configuration
- Database settings
- URL configuration
- Security settings
- Application integration

### Creating a Django project

```bash
django-admin startproject config .
```

Let's understand the command:

| Part            | Meaning                                       |
| --------------- | --------------------------------------------- |
| `django-admin`  | Django's command-line utility                 |
| `startproject`  | Creates a Django project                      |
| `config`        | Name of the project configuration package     |
| `.`             | Creates the project files in the current directory |

### Why use the dot (.)?

Suppose you already created a folder:

```text
myshop/
```

You navigate inside it:

```bash
cd myshop
```

Then execute:

```bash
django-admin startproject config .
```

Django creates its files directly inside `myshop`.

Without the dot:

```bash
django-admin startproject config
```

Django creates another directory named `config` inside the current directory.

Remember:

- `myshop` = Main project directory.
- `config` = Django project configuration package.
- `.` = Current directory.

Using `config` is a common naming convention, but it is not mandatory.

---

## 6. Django Project Folder Structure

After creating your project, the structure looks like this:

```text
myshop/
│
├── manage.py
│
└── config/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Let's understand every file.

### manage.py

`manage.py` is the command-line entry point for executing Django management commands.

For example:

```bash
python manage.py runserver
python manage.py startapp core
python manage.py migrate
python manage.py createsuperuser
```

A simplified version of `manage.py`:

```python
import os
import sys

from django.core.management import execute_from_command_line

def main():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'config.settings'
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
```

When you execute:

```bash
python manage.py runserver
```

The following happens:

1. Python executes `manage.py`.
2. The `main()` function runs.
3. Django receives the command-line arguments.
4. Django identifies `runserver`.
5. Django executes the corresponding management command.

The actual implementation of the built-in command is available in Django's installed package under:

```text
django/core/management/commands/runserver.py
```

### settings.py

Contains the main configuration of your Django project.

For example:

```python
DEBUG = True

INSTALLED_APPS = []

DATABASES = {}

ROOT_URLCONF = 'config.urls'
```

It controls:

- Installed applications
- Database configuration
- Middleware
- Templates
- Static files
- Security settings

### urls.py

Responsible for URL routing.

It tells Django which view should handle a particular URL.

Example:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

### \_\_init\_\_.py

Makes the directory a Python package.

### wsgi.py

Provides the WSGI application entry point for compatible web servers.

### asgi.py

Provides the ASGI application entry point for compatible web servers.

---

## 7. What Is runserver?

The `runserver` command starts Django's built-in development server.

Command:

```bash
python manage.py runserver
```

Django starts a local development server.

You will see an address similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open your browser: <http://127.0.0.1:8000/>

### Understanding the URL

| Part         | Meaning                 |
| ------------ | ----------------------- |
| `http://`    | Communication protocol  |
| `127.0.0.1`  | Your local computer     |
| `8000`       | Port number             |
| `/`          | Root URL path           |

### What happens when runserver executes?

1. Django starts its development server.
2. The browser sends an HTTP request.
3. Django receives the request.
4. Django checks the URL configuration.
5. The matching view processes the request.
6. Django returns a response.

### Other runserver commands

Start on the default port:

```bash
python manage.py runserver
```

Start on port 8080:

```bash
python manage.py runserver 8080
```

Start listening on all network interfaces:

```bash
python manage.py runserver 0.0.0.0:8000
```

> **Important:** `runserver` is intended for development and testing, not production hosting.

### What is the first Django page?

When you visit the root URL of a newly created project with the default URL configuration, Django may display its development-mode 404 page with the installation-success message.

This is not a homepage that you have created.

You can create your own homepage by defining a URL pattern and a view.

---

## 8. What Is a Django App?

A Django app is a smaller component inside a Django project that handles a specific functionality.

Imagine an e-commerce website.

You might create:

| App        | Responsibility                  |
| ---------- | ------------------------------- |
| `accounts` | User registration and login     |
| `products` | Product management              |
| `cart`     | Shopping cart                   |
| `orders`   | Order management                |
| `payments` | Payment processing              |

### Creating a Django app

Command:

```bash
python manage.py startapp core
```

Let's understand:

| Part         | Meaning                          |
| ------------ | -------------------------------- |
| `python`     | Runs Python                      |
| `manage.py`  | Django management entry point    |
| `startapp`   | Creates a Django application     |
| `core`       | Application name                 |

### What happens?

Django automatically creates this structure:

```text
core/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

### Purpose of each file

**admin.py** – Registers database models with Django's admin panel.

**apps.py** – Contains application configuration.

**models.py** – Defines database models.

**tests.py** – Contains automated tests.

**views.py** – Contains functions and classes that process HTTP requests.

**migrations/** – Stores database migration files.

**\_\_init\_\_.py** – Makes the directory a Python package.

---

## 9. Project vs App

This is one of the most important concepts in Django.

| Project                            | App                                  |
| ---------------------------------- | ------------------------------------ |
| Represents the entire website      | Represents a specific functionality  |
| Created using `startproject`       | Created using `startapp`             |
| Manages overall configuration      | Manages a particular feature         |
| Usually one main project           | Can contain multiple apps            |

Example: University Management System

```text
university/
│
├── manage.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│
├── teachers/
│
├── courses/
│
├── attendance/
│
└── fees/
```

Here:

- `university` = Main project.
- `students` = Students application.
- `teachers` = Teachers application.
- `courses` = Courses application.
- `attendance` = Attendance application.
- `fees` = Fees application.

A project can contain multiple apps.

---

## 10. Registering an App in Django

After creating an application, you generally need to register it in `settings.py`.

Open:

```text
config/settings.py
```

Find `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Add your application:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]
```

Now Django recognizes your application.

---

## 11. What Is URL Routing in Django?

URL routing is the process of connecting a URL to a particular view.

The `urls.py` file contains URL patterns.

Example:

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

### Understanding path()

The general syntax:

```python
path(route, view, kwargs=None, name=None)
```

For example:

```python
path('home/', home_page, name='home')
```

| Argument | Meaning                                  |
| -------- | ---------------------------------------- |
| `route`  | URL pattern                              |
| `view`   | Function or class-based view             |
| `kwargs` | Optional additional arguments            |
| `name`   | Optional name for the URL pattern        |

### Example

When someone visits:

```text
http://127.0.0.1:8000/home/
```

Django searches the URL patterns for a match.

If it finds:

```python
path('home/', home_page)
```

Django executes the `home_page` view.

---

## 12. What Is a View in Django?

A view is responsible for processing an HTTP request and returning an HTTP response.

Django supports two main types of views:

- Function-Based Views (FBV)
- Class-Based Views (CBV)

### Function-Based View (FBV)

A function-based view is a normal Python function that accepts an HTTP request and returns an HTTP response.

Example:

```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Hello Welcome to Django!")
```

Here:

- `home_page` = View function.
- `request` = HTTP request object.
- `HttpResponse` = HTTP response returned to the browser.

### Connecting the view with urls.py

```python
from django.contrib import admin
from django.urls import path
from core.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
]
```

Now visit:

```text
http://127.0.0.1:8000/home/
```

Output:

```text
Hello Welcome to Django!
```

---

## 13. Is home_page a Callback Function?

Consider:

```python
def home_page(request):
    return HttpResponse("Welcome!")
```

And:

```python
path('home/', home_page)
```

Yes! `home_page` is a callback in this context.

A callback is a function passed to another function or component so that it can be called later.

Django calls the view when a matching HTTP request arrives.

### Why don't we write parentheses?

Correct:

```python
path('home/', home_page)
```

Incorrect for registering the view:

```python
path('home/', home_page())
```

Understand the difference:

| Expression     | Meaning                              |
| -------------- | ------------------------------------ |
| `home_page`    | Passes the function reference        |
| `home_page()`  | Executes the function immediately    |

Django needs the function reference because the view should execute when a matching request arrives.

---

## 14. Can We Define a View Inside urls.py?

Yes.

Python allows you to define a function directly inside `urls.py`.

Example:

```python
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def contact_page(request):
    return HttpResponse("Welcome to Contact Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_page),
]
```

This works.

However, the recommended approach is to define views inside `views.py` and import them into `urls.py`.

### Can we define a function directly inside path()?

A normal `def` function definition cannot be placed directly inside a function call as an argument.

This is invalid Python syntax:

```python
path('contact/', def contact_page(request):
)
```

However, Python supports lambda functions.

---

## 15. What Is a Lambda Function?

A lambda function is a small anonymous function in Python.

Anonymous means that the function does not have a declared function name.

It allows you to create a function in one line without using `def`.

### Syntax

```python
lambda arguments: expression
```

Example:

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

### Understanding the syntax

| Part      | Meaning                                    |
| --------- | ------------------------------------------ |
| `lambda`  | Keyword for creating a lambda function     |
| `a, b`    | Function parameters                        |
| `:`       | Separates parameters and expression        |
| `a + b`   | Expression whose result is returned        |

### Normal function vs Lambda function

Normal function:

```python
def square(x):
    return x * x
```

Lambda function:

```python
square = lambda x: x * x
```

Both perform the same operation.

### More examples

Addition:

```python
add = lambda a, b: a + b
```

Square:

```python
square = lambda x: x ** 2
```

Even or odd:

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"
```

Uppercase:

```python
uppercase = lambda name: name.upper()
```

### Lambda in Django URL routing

```python
from django.urls import path
from django.http import HttpResponse

urlpatterns = [
    path(
        'contact/',
        lambda request: HttpResponse("Welcome to Contact Page")
    ),
]
```

This works because Django expects a callable view.

However, normal named functions are recommended for actual application views because they are easier to maintain, test, and reuse.

---

## 16. How Django Request and Response Work

Understanding request and response handling is essential.

Consider:

```python
def home_page(request):
    return HttpResponse("Hello Django!")
```

The execution flow:

1. User enters a URL in the browser.
2. Browser sends an HTTP request.
3. Django receives the request.
4. URL dispatcher checks `urlpatterns`.
5. Django calls the matching view.
6. View processes the request.
7. View returns an HTTP response.
8. Browser displays the response.

### Request

The request object contains information about the incoming HTTP request.

For example:

```python
def home_page(request):
    print(request.method)

    return HttpResponse("Welcome!")
```

### Response

`HttpResponse` sends content back to the browser.

Example:

```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to my website!")
```

---

## 17. What Are WSGI and ASGI?

These are interfaces that allow web servers to communicate with Python web applications.

They act as entry points between your Django application and compatible application servers.

### WSGI

WSGI stands for:

**Web Server Gateway Interface**

It is a standard interface for synchronous Python web applications.

Django automatically generates a `wsgi.py` file.

Example:

```python
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

application = get_wsgi_application()
```

#### Understanding the code

**`import os`** – Imports Python's operating system module.

**`DJANGO_SETTINGS_MODULE`** – Tells Django where the project settings are located.

**`get_wsgi_application()`** – Creates the WSGI application callable.

A WSGI-compatible server can use this callable to communicate with Django.

Example production server command:

```bash
gunicorn config.wsgi:application
```

### ASGI

ASGI stands for:

**Asynchronous Server Gateway Interface**

It is a newer interface supporting both synchronous and asynchronous application handling.

It is useful for:

- WebSockets
- Real-time notifications
- Asynchronous HTTP handling
- Long-lived connections

Django automatically generates an `asgi.py` file.

Example:

```python
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'config.settings'
)

application = get_asgi_application()
```

#### Understanding the code

**`get_asgi_application()`** – Creates the ASGI application callable.

An ASGI-compatible server can use it to communicate with Django.

Example server command:

```bash
uvicorn config.asgi:application
```

### WSGI vs ASGI

| Feature            | WSGI                          | ASGI                                |
| ------------------ | ----------------------------- | ----------------------------------- |
| Full form          | Web Server Gateway Interface  | Asynchronous Server Gateway Interface |
| Programming model  | Synchronous                   | Synchronous and asynchronous        |
| HTTP               | Supported                     | Supported                           |
| WebSockets         | Not natively supported        | Supported                           |
| Async capabilities | Limited                       | Yes                                 |
| Common server      | Gunicorn                      | Uvicorn                             |

> **Important:** ASGI does not automatically make every Django view asynchronous. You must use asynchronous-compatible code and appropriate components.

---

## 18. Complete Django Project Structure

After creating your project and an application named `core`, your structure should look like this:

```text
mywebsite/
│
├── manage.py
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── core/
    ├── migrations/
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### Responsibilities

| File          | Responsibility                    |
| ------------- | --------------------------------- |
| `manage.py`   | Executes Django management commands |
| `settings.py` | Project configuration             |
| `urls.py`     | URL routing                       |
| `views.py`    | Request handling                  |
| `models.py`   | Database structure                |
| `admin.py`    | Admin registration                |
| `apps.py`     | Application configuration         |
| `tests.py`    | Automated testing                 |
| `wsgi.py`     | WSGI entry point                  |
| `asgi.py`     | ASGI entry point                  |

---

## 19. Complete Practical Example

Let's build a very simple Django application.

**Step 1: Create a project**

```bash
mkdir mywebsite
cd mywebsite

django-admin startproject config .
```

**Step 2: Create an app**

```bash
python manage.py startapp core
```

**Step 3: Register the app**

In `config/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]
```

**Step 4: Create a view**

In `core/views.py`:

```python
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("Welcome to My Website!")

def about_page(request):
    return HttpResponse("This is the About Page.")

def contact_page(request):
    return HttpResponse("Contact Us!")
```

**Step 5: Create app-level URLs**

Create a new file named `core/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),
]
```

**Step 6: Connect app URLs to project URLs**

In `config/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
```

**Step 7: Start the server**

```bash
python manage.py runserver
```

**Step 8: Visit the pages**

- Homepage: <http://127.0.0.1:8000/>
- About: <http://127.0.0.1:8000/about/>
- Contact: <http://127.0.0.1:8000/contact/>

Congratulations! You have created your first Django application with multiple URL routes.

---

## 20. Important Django Commands Cheat Sheet

| Command                                | Purpose                       |
| -------------------------------------- | ----------------------------- |
| `pip install django`                   | Installs Django               |
| `django-admin --version`               | Checks Django version         |
| `django-admin startproject config .`   | Creates a Django project      |
| `python manage.py startapp core`       | Creates an application        |
| `python manage.py runserver`           | Starts development server     |
| `python manage.py runserver 8080`      | Starts server on port 8080    |
| `python manage.py makemigrations`      | Creates migration files       |
| `python manage.py migrate`             | Applies database migrations   |
| `python manage.py createsuperuser`     | Creates admin user            |
| `python manage.py shell`               | Opens Django Python shell     |
| `python manage.py showmigrations`      | Lists migrations              |
| `python manage.py check`               | Checks project configuration  |

---

## 21. Important Concepts to Remember

- Django is a Python web framework.
- **Project** represents the entire web application.
- **App** represents a particular functionality.
- `manage.py` executes Django management commands.
- `runserver` starts the development server.
- `urls.py` connects URLs to views.
- `views.py` handles HTTP requests and returns responses.
- `models.py` defines database models.
- `settings.py` contains project configuration.
- **FBV** means Function-Based View.
- **CBV** means Class-Based View.
- **Callback** is a function passed to another component to be called later.
- **Lambda** is an anonymous, single-expression function.
- **WSGI** provides a synchronous application-server interface.
- **ASGI** supports synchronous and asynchronous application-server communication.

---

## 22. Recommended Learning Roadmap

After understanding these fundamentals, learn Django in this order:

1. Python fundamentals and OOP
2. Django installation and project creation
3. Django project vs app
4. URL routing
5. Function-Based Views
6. Class-Based Views
7. Templates and template inheritance
8. Static files (CSS, JavaScript, images)
9. Django models
10. Database migrations
11. Django ORM
12. Django admin panel
13. Forms and ModelForms
14. User authentication
15. Sessions and cookies
16. Django REST Framework
17. API development
18. Testing
19. Deployment

---

## Conclusion

Django provides a structured way to build web applications using Python.

The most important concept to understand is how these components work together:

**Project → App → URL → View → Model → Template → Response**

Once you understand this flow, building Django applications becomes much easier.

Keep practicing by building small projects before moving to complex applications.