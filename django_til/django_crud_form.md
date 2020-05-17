# Django CRUD form

##### 막간을 이용한 http 짤막상식

- get : 브라우저에 주소창을 보내는 요청 / url을 활용, 데이터 전송

- post : 서버의 변경사항을 만듬 / http 요청메시지의 body에 데이터 전송

![image](https://user-images.githubusercontent.com/53211781/78618498-b63baf80-78b5-11ea-9911-9cb03af175d6.png)



## form을 활용한 CRUD 모델링

### 1. `forms.py` 생성

- meta 클래스의 클래스 인스턴스로 **상속해 오려는 클래스명**과 유효성 검증을 위한 **필드**를 받는다. 

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm) : 
    class Meta : 
        model = Article   # 메타 데이터를 담기 위해 정의 / 유효성 검증
        fields = ['title','content']
```



### 2. `views.py` 예시

#### Create

- POST 방식으로 요청이 들어오면(사용자가 양식을 전송한다면) 전송한 양식을 제목과 내용으로 분류해 form 객체로 만들어준다. 
- 제목, 내용이 유효하다면(하나라도 비어있지 않다면) 저장 후 DB에 반영한다. 
- GET방식으로 요청이 들어온 경우(새글 작성 창으로 이동한 경우) 사용자에게 form을 보여준다. 
- 만일 유효하지 않은 form인 경우에는 렌더링을 통해 작성창을 계속해서 보여준다.

```python
def new(request) :   
    if request.method = 'POST' : 
        form = ArticleForm(request.POST) : 
        if form.is_valid() : 
            article = form.save()
            return redirect('articles:index')
    
    else : 
    	form = ArticleForm()
        
    context = {
        'form' : form
    }
    return render(request,'article/new.html',context)
```

#### Review

- `Article.object.get(pk=pk)` 대신 Article 객체의 모든 쿼리셋과 pk를 인자로 받는 `get_object_or_404()`를 활용해 작성되지 않은 게시글을 요청 시 404 메시지 출력

```python
from django.shortcuts import get_object_or_404

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)
```

#### Update

- 글을 수정하기 위해서는 항상 인스턴스를 넘겨주어야 한다. 
- POST 요청 시(수정을 마치고 수정 내용을 사용자가 전송 시) 요청한 내용을 form 객체로 만든다.
- 유효성 검증을 마친 후 유효하다면 인덱스 페이지로 돌아간다. 
- 유효하지 않거나 GET 요청 시(수정 페이지로 접속 시) detail/< int:pk >에 해당하는 내용을 form에 담아 사용자에게 보여준다.  

```python
def update(request,pk):
    article = get_object_or_404(Article,pk)
    if request.method == "POST" : 
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid() : 
        	article = form.save()
            return redirect('article:index')
```

#### Delete

- 그 전까지의 삭제 로직(GET 방식)에는 치명적인 문제가 하나 존재했다. 
- `delete/<int:pk>`를 통해 아무 글이나 삭제가 가능했기 때문이다. 
- 하지만 POST방식을 활용하면 위와 같은 접근으로 삭제를 차단할 수 있다. 
- 대신 `@require_POST`를 활용해 상기한 GET 방식의 접근 시에는 함수가 동작하지 않게 한다. 

```python
from django.views.decorators.http import require_POST

@require_POST
def delete(request,pk) : 
    article = get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('article:index')
```



### 3. Templates 예시

#### `create.html`

- 사용자에게는 form 객체를 보여주고 submit 동작 시 POST 방식으로 전송한다.  

- bootstrap 라이브러리 사용 시 부트스트랩 형식으로 form 객체를 정렬해준다. 
- 일반 버전은 form 객체를 <p> <ul> <table> 세 가지 타입으로 정렬 방식을 선택할 수 있다. 
- form 객체가 정렬 및 유효성 검증 기능까지는 제공하나 submit과 csrf 토큰은 제공하지 않는다. 

```html
// bootstrap ver
<form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <!-- input type:submit -->
    <button class="btn btn-primary">제출</button>
</form>

// standard ver
<form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="제출">
</form>
```



#### `detail.html`

- 삭제를 위한 버튼은 POST 방식으로 삭제 요청을 전송할 수 있게 한다. 

```html
{% extends 'base.html' %}

{% block body %}
    <h1>{{ article.pk }}번 글</h1>
    <h2>{{ article.title }}</h2>
    <p>생성 : {{ article.created_at }}</p>
    <p>수정 : {{ article.updated_at }}</p>
    <hr>
    <p>{{ article.content }}</p>
    <form action="{% url 'articles:delete' article.pk %}" method="POST" class="d-inline">
        {% csrf_token %}
        <button class="btn btn-primary">삭제</button>
    </form>
    <a href="{% url 'articles:update' article.pk %}"><button class="btn btn-primary">수정</button></a>
{% endblock %}
```



