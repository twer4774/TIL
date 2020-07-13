# Django Intro

- 파이썬 웹 프레임워크
- Flask와 더불어 가장 많이 사용되는 프레임워크
- Admin 구성 등 빠르게 틀이 만들어져 개발할 수 있는 장점
- SQLite라는 경량의 DB를 가지고 있어 별도로 DB설정이 필요없음
- 필요한 부분을 제외하고 제거해야 하는 단점(좀 무거운 느낌)

## 설치

- 가상환경 준비

```
python3 -m venv djangoStudy
source djangoStudy/bin/activate <-> deactivate
```

- Miniconda 이용 - python 패키지관리가 잘되므로 이용
  - https://docs.conda.io/en/latest/miniconda.html

```
bash ./Miniconda3-latest-MacOSX-x86_64.sh
conda create --name djangoStudy python=3.7
conda activate djangoStudy <-> conda deactivate
conda env list => 가상환경리스트
```

```
#mac 기준
pip3 install Django
python3 -m django version #3.0.8
django-admin startproject djangoStudyProject
python3 manage.py runserver
```

http://localhost:8000 실행 확인

- 위에 것이 안된다면 아래것 실행

  python manage.py startapp 에서 에러가 나와서 아래것으로 대체함 

```
python -m pip install django 
```



## GIT 설정

- github에 repository 생성

```
git config —global user.name "name"
git config —global user.email "email"
git init
echo "#TodowithDjango" >> README.md
git remote add origin https://github.com/twer4774/TodowithDjango
git add .
git commit -m "crate: Init Project"
git push -u origin master
```

- nano를 이용하여 .gitignore 만들기

```
*pyc
__pycache__
```

## Application 구성하기

```
python manage.py startapp my_to_do_app
```

1. ToDoList/settings.py 수정
   1. 앱을 만들때 마다 아래 파일에 추가해줘야한다

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_to_do_app'
]
```

2. URL 설정

   1. ToDoList/urls.py 수정

   ```python
   from django.contrib import admin
   from django.urls import path, include #include 추가
   
   urlpatterns = [
       path('', include('my_to_do_app.urls')),
       path('admin/', admin.site.urls),
   ]
   ```

   2. my_to_do_app/urls.py 생성

   ```python
   from django.urls import path
   from . import views #사용자에게 보여줄 화면 처리
   
   urlpatterns = [
       path('', views.index)
   ]
   ```

   3. my_to_do_app/views.py 수정

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   def index(request):
       return HttpResponse("my_to_do_app first page")
   
   ```

3. HTML파일 이용하기

   - HTML 파일을 템플릿으로 사용하려고 할 때, 장고는 해당 앱에서 templates라는 폴더를 탐색함
   - 따라서 앱의 이름과 동일한(my_to_do_app)이름의 폴더 templates폴더에 만들고 그 안에 html파일을 넣는다.
   - 구조
     - ToDoList
       - my_to_do_app
         - templates
           - my_to_do_app
             - index.html
         - migrations
         - ...

4. views.py 수정

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'my_to_do_app/index.html')

```

- render함수에서 request를 전달하여 user나 session같은 중요한 값들을 전달

5. 실행

```
python manage.py runserver
localhost:8000접속
```

