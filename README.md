# django_blog_website

python -m django --version
django-admin : to list the available django soft commands
django-admin startproject name_of_project
python manage.py runserver

Create super user
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Database
python manage.py shell
from django.contrib.auth.models import User
from blog_app.models import Posts

User.objects.all()
user=User.objects.filter(username='name')
user.id
post_1=Posts(title='title',content='content',author=user)
user.posts_set
user.posts_set.create(title='title',content='content')