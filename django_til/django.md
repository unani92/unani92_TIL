## django

> 파이썬 웹 프레임워크



### 설치

```bash
$ pip install django==2.1.15
```



### 프로젝트 생성

```bash
$ django-admin startproject {프로젝트 명}
```



### 서버실행

- `django_intro` 폴더의 `settings.py`에서 다음과 같이 설정한다. 

```python
ALLOWED_HOST = [*]
```



```bash
~/ $ cd django_intro
~django_intro/$ python manage.py runserver 8080
```

- 서버종료 : `ctrl+c`



### 앱 생성

- 장고는 여러개의 앱을 가진 하나의 프로젝트로 구성된다. 
  - 커뮤니티
    - 회원과 관련된 앱
    - 게시글과 관련된 앱

```bash
$ python manage.py startapp pages # 프로젝트의 하위 앱 생성
```

#### 기본 흐름

1. `settings.py`에서 앱 주민등록을 한다.(앱 생성 시 최초 1회 반드시!!!) 
2. `views.py`에서 함수를 설정해준다. 
3. `urls.py`에서 url을 등록해준다.
4. templates



#### 파이썬 코드를 실행해보기(로또번호 생성기)

```python
def lotto(request) :
    import random
    pick = random.sample(range(1,46),6)
    pick.sort()
    context = {
        'pick':pick
    }
    return render(request,'lotto.html',context)
```

- 함수를 정의할 때에 반드시 첫 인자는 `request` 이다. 

  - 하지만 로또생성기처럼 내부적으로 요청을 처리할 시에는 요청 정보가 담긴 context 객체 삽입

- `render` 함수를 통해 반환

  - 세번째 인자 context는 딕셔너리 형태

- html은 다음과 같이 설정해준다.

- ```html
  <p>{{pick}}</p>   
  ```

