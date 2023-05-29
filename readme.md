# install
- python
- python, python extention, gitignore, gitlab
- django, venv, Pillow
- 

# git


…or create a new repository on the command line

``` batch
echo "# io-list-check" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/engineer-jinho/io-list-check.git
git push -u origin main
```

…or push an existing repository from the command line

``` batch
git remote add origin https://github.com/engineer-jinho/io-list-check.git
git branch -M main
git push -u origin main
```

…or import code from another repository

You can initialize this repository with code from a Subversion, Mercurial, or TFS project.

# Django 

## initialize project
``` batch
django-admin startproject config .
python manage.py startapp io_list
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
## settings.py
``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'io_list',  # 여기에 앱을 추가합니다.
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## admin

``` batch
python manage.py createsuperuser
```

``` python
#io_app/admin.py
from django.contrib import admin
from .models import AIModel, AOModel, DIModel, DOModel

admin.site.register(AIModel)
admin.site.register(AOModel)
admin.site.register(DIModel)
admin.site.register(DOModel)
```

``` batch
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```

## urls
```python
#io_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ai/<int:pk>/', views.ai_detail, name='ai_detail'),
    path('ai_hmi/<int:pk>/', views.ai_detail_hmi, name='ai_detail_hmi'),
    
    path('di/<int:pk>/', views.di_detail, name='di_detail'),
    path('do/<int:pk>/', views.do_detail, name='do_detail'),
    path('ao/<int:pk>/', views.ao_detail, name='ao_detail'),
]
```


## view
``` python
from django.shortcuts import render, get_object_or_404
from .models import AIModel, DIModel, DOModel, AOModel

def home(request):
    ais = AIModel.objects.all()
    dis = DIModel.objects.all()
    dos = DOModel.objects.all()
    aos = AOModel.objects.all()
    return render(request, 'io_app/home.html', {'ais': ais, 'dis': dis, 'dos': dos, 'aos': aos})

def ai_detail(request, pk):
    ai = get_object_or_404(AIModel, pk=pk)
    next_ai = AIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ai = AIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ai_detail.html', {'ai': ai, 'next_ai': next_ai, 'prev_ai': prev_ai})

def ai_detail_hmi(request, pk):
    ai = get_object_or_404(AIModel, pk=pk)
    next_ai = AIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ai = AIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ai_detail_hmi.html', {'ai': ai, 'next_ai': next_ai, 'prev_ai': prev_ai})

def di_detail(request, pk):
    di = get_object_or_404(DIModel, pk=pk)
    next_di = DIModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_di = DIModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/di_detail.html', {'di': di, 'next_di': next_di, 'prev_di': prev_di})

def do_detail(request, pk):
    do = get_object_or_404(DOModel, pk=pk)
    next_do = DOModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_do = DOModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/do_detail.html', {'do': do, 'next_do': next_do, 'prev_do': prev_do})

def ao_detail(request, pk):
    ao = get_object_or_404(AOModel, pk=pk)
    next_ao = AOModel.objects.filter(pk__gt=pk).order_by('pk').first()
    prev_ao = AOModel.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'io_app/ao_detail.html', {'ao': ao, 'next_ao': next_ao, 'prev_ao': prev_ao})



```


``` batch
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```


## html

### base
<!DOCTYPE html>
<html>
<head>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        {% block content %}
        <!-- 이 부분은 하위 템플릿에서 오버라이드됩니다. -->
        {% endblock %}
    </div>

    <!-- Bootstrap JS and jQuery -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</body>
</html>


### home
```html
{% extends "io_app/base.html" %}

{% block content %}
<h1>IO List Overview</h1>

<h2>AI List</h2>
<table class="table table-striped">
    <tr>
        <th>Field tag</th>
        <th>PLC tag</th>
        <th>For more detail</th>
        <th>For more detail(HMI)</th>
    </tr>
    {% for ai in ais %}
    <tr>
        <td>{{ ai.field_tag }}</td>
        <td>{{ ai.plc_tag }}</td>
        <td><a href="{% url 'ai_detail' ai.pk %}">Everythings</a></td>
        <td><a href="{% url 'ai_detail_hmi' ai.pk %}">HMIs</a></td>
    </tr>
    {% endfor %}
</table>

<h2>DI List</h2>
<table class="table table-striped">
    <tr>
        <th>Field tag</th>
        <th>PLC tag</th>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>

    {% for di in dis %}
    <tr>
        <td><a href="{% url 'di_detail' di.pk %}">{{ di.field_tag }}</a></td>
        <td>{{ di.plc_tag }}</td>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>
    {% endfor %}
</table>


<h2>DO List</h2>
<table class="table table-striped">
    <tr>
        <th>Field tag</th>
        <th>PLC tag</th>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>

    {% for do in dos %}
    <tr>
        <td><a href="{% url 'do_detail' do.pk %}">{{ do.field_tag }}</a></td>
        <td>{{ do.plc_tag }}</td>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>
    {% endfor %}
</table>

<h2>AO List</h2>
<table class="table table-striped">
    <tr>
        <th>Field tag</th>
        <th>PLC tag</th>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>

    {% for ao in aos %}
    <tr>
        <td><a href="{% url 'ao_detail' ao.pk %}">{{ ao.field_tag }}</a></td>
        <td>{{ ao.plc_tag }}</td>
        <!-- 추가로 필요한 필드를 여기에 추가하십시오. -->
    </tr>
    {% endfor %}
</table>


{% endblock %}

```


