Project Documentation: A Comprehensive Staff Tracking System: A Web-Based Solution for Real-Time Attendance and Duty Management

Table of Contents

1. Project Overview
2. Technology Stack
3. Project Setup
4. Application Structure
5. Database Models
6. Views and URL Configuration
7. User Authentication
8. Testing the Application
9. Deployment
10. Conclusion

1. Project Overview

The Staff Tracking System is a web-based application designed to streamline the process of tracking employee attendance and managing duty posts in real time. Built using the Django framework, the system enables organizations to manage their staff efficiently by monitoring attendance, assigning duty posts, and generating relevant reports. This project is backend centred. 

2. Technology Stack

- Programming Language -  Python
- Framework - Django
- Database - SQLite (Django default)
- Version Control - Git
- Deployment - GitHub

3. Project Setup

3.1. Prerequisites

Ensure you have the following installed on your system:

- Python 3.x
- Pip (Python package installer)
- Virtual environment tool (`venv` or `virtualenv`)
- Git
- Visual Studio Code (or any other preferred IDE)

3.2. Setting Up the Project

1. Create a Virtual Environment and Install Django
   ```command prompt 
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install django
   ```

2. Create the Django Project and Application
   ```command prompt
   django-admin startproject staff_tracking_system
   cd staff_tracking_system
   django-admin startapp tracking
   ```

3. Update `settings.py` to Include the `tracking` App
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'tracking',  # Add the tracking app
   ]
   ```

4. Application Structure

```
staff_tracking_system/
│
├── staff_tracking_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tracking/
│   ├── migrations/
│   │   └── tracking/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│
├── manage.py
└── venv/
```

5. Database Models

5.1. Staff Model

The `Staff` model represents an employee in the organization.

```python
# tracking/models.py
from django.db import models
from django.contrib.auth.models import User

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
```

5.2. Attendance Model

The `Attendance` model tracks the attendance of each staff member.

```python
class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time_in = models.TimeField()
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.staff.user.username} - {self.date}"
```

5.3. DutyPost Model

The `DutyPost` model represents different duty posts within the organization.

```python
class DutyPost(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
```

5.4. Applying Migrations

After defining the models, run the following commands to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

5.5. Registering Models in the Admin Interface

To manage the models via Django's admin interface, register them in `admin.py`:

```python
# tracking/admin.py
from django.contrib import admin
from .models import Staff, Attendance, DutyPost

admin.site.register(Staff)
admin.site.register(Attendance)
admin.site.register(DutyPost)
```

6. Views and URL Configuration

6.1. Creating Views

Views are functions that handle requests and return responses. Below are the views for this project:

```python
# tracking/views.py
from django.shortcuts import render, redirect
from .models import Staff, Attendance, DutyPost

def dashboard(request):
    staff = Staff.objects.all()
    return render(request, 'dashboard.html', {'staff': staff})

def mark_attendance(request):
    if request.method == 'POST':
        # Handle attendance marking logic
        pass
    return render(request, 'mark_attendance.html')

def duty_post_list(request):
    duty_posts = DutyPost.objects.all()
    return render(request, 'duty_post_list.html', {'duty_posts': duty_posts})

def duty_post_detail(request, pk):
    duty_post = DutyPost.objects.get(pk=pk)
    return render(request, 'duty_post_detail.html', {'duty_post': duty_post})

def create_duty_post(request):
    if request.method == 'POST':
        # Handle duty post creation logic
        pass
    return render(request, 'create_duty_post.html')
```

6.2. URL Configuration

URLs map the views to specific paths. Define the URLs for the application:

```python
# tracking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('attendance/', views.mark_attendance, name='mark_attendance'),
    path('duty-posts/', views.duty_post_list, name='duty_post_list'),
    path('duty-posts/<int:pk>/', views.duty_post_detail, name='duty_post_detail'),
    path('duty-posts/new/', views.create_duty_post, name='create_duty_post'),
]
```

Include the `tracking` app's URLs in the project's main URL configuration:

```python
# staff_tracking_system/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracking.urls')),
]
```
9. Testing the Application

9.1. Running the Development Server

Start the development server to test the application:

```bash
python manage.py runserver
```

9.2. Manual Testing

- Access the dashboard and verify that all staff members are displayed correctly.
- Test the attendance marking feature by submitting the attendance form.
- Navigate through duty posts and ensure the creation, listing, and detail views work as expected.

10. Deployment

10.1. Deploying to GitHub

Below is a structured and detailed documentation of the deployment process of the Staff Tracking System of the  backend of the Django application to GitHub. This documentation includes all necessary steps used to facilitate the deployment.

Step 1.0: Initialize a Git Repository on my already created GitHub account. 

1.1 Initialize Git

1. Open a terminal or command prompt.
2. Navigate to the root directory of your Django project.
3. Initialize a new Git repository using the following command:

   ```bash
git init
git add .
git commit -m "Initial commit: Add backend for Staff Tracking System"
git remote add origin https://github.com/IdorenyinInoh/capstone_project
git push -u origin master
   ```

By following the steps outlined in this documentation, I successfully deployed the backend part of the Django application to GitHub. This process allows for version control, collaboration, and easy sharing of your codebase.


11. Conclusion

This documentation provides a comprehensive guide to building a Staff Tracking System using Django. By following the steps outlined in this document, you will have a fully functional backend application that tracks employee attendance and manages duty posts. The project is designed to be beginner-friendly, with clear instructions for each stage of development, from setting up the environment to deploying the application on GitHub.

