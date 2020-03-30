## Django Template Language

※ 언어는 어디서?? **공식문서**에서

### 반복문

```django
{% for reply in replies %}
<li>{{reply}}</li>
{% endfor %}
```

- `{{forloop.counter}}`
- `{{forloop.counter0}}`
- `{{% empty %}}` : 이터러블 객체가 비었는지 안비었는지에 대한 불리언을 출력해줌

### 조건문

```django
{%for article in articles%}
{%if forloop.counter==1%}
{% else %}
{% endfor %}
```



### 빌트인 태그, 필터

```django
{{content|length}}
{{content|truncatechars:10}}
```





### form을 통한 요청처리

#### 개요

1. 사용자로부터 값을 받아서
2. 이를 단순 출력하는 페이지 구성

#### 사용자에게 폼 양식 제공

```python
path('new/',views.new)
```

#### view 함수 생성

```python
def new(request) : 
    return render(request,'boards/new.html')
```

#### template

```html
<form action="/boards/complete">
	제목 : <input type="text" name="title">
</form>
```

- form 태그에는 action 속성을 정의한다. 
  - 사용자로부터 내용을 받아서 처리하는 url
- input 태그에는 name  속성을 통해 사용자가 입력한 내용을 담을 변수 이름을 지정
- 예시 : boards/complete/?title=text

#### 사용자 요청 처리

1. url.py 정의

```python
path('/boards/complete/',views.complete)
```

2. views.py

```python
def complete(request) :
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    return render(request,'boards/complete.html',context)
```

