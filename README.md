# django_blog_website

Create views
Add template
Link url

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

# User creation
Need to add a csrf_token when creating a form
from django.contrib import messages can be used to create flash messages
To create new fields in the form we can create a new form.py and inherit the class UserCreationForm to it
user.is_authenticated  :  to check the user is logged in or not
@login_required : to control a router to open only after authentication
LOGIN_REDIRECT_URL='blog_home'
LOGIN_URL='login' 

# profile
MEDIA_ROOT=os.path.join(BASE_DIR,'media')
MEDIA_URL='/media/'

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

def ready(self):
        import users.signals