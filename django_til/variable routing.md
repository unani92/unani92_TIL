## variable routing

### 1. `urls.py`

```python
urlpatterns = [
    path('myname/<str:name>', views.myname),
	path('add/<int:a>/<int:b>', views.add),    
]

```





### 2. `views.py`

```python
# variable routing
def myname(request,name) :
    return render(request,'myname.html',{'name':name})

def add(request,a,b) :
    result = int(a) + int(b)
    context = {
        'add':result
    }
    return render(request,'add.html',context)
```



### 3. `templates`

```python
더하기를 하자
{{add}}
```





## DTL (Django Template Language)

> 템플릿 파일(html) 은 장고 템플릿 랭기지를 통해 구성할 수 있다. 

1.  출력

   ```
   {{menu}}
   {{menu.0}}  # 메뉴의 0번째 원소
   ```

2. 반복

   ```
   {% for menu in menupan %}
   
   {% endfor %}
   ```

   