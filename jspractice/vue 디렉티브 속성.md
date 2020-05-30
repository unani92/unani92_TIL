# Vue event handling

## intro

`v-on` : Vanilla JS의 `addEventListener`와 같다. shortcut으로 `@`로 대신할 수도 있다.

`v-bind` : HTML의 속성의 값에 대해 interpolate을 할 때 사용한다. shortcut으로 `:`로 대신할 수 있다. 
```html
<a :href="googleUrl">Google</a>
<a v-bind:href="naverUrl">Naver</a>

<script >
  new Vue({
      ...
      ...
    data: {
            googleUrl: "https://google.com",
            naverUrl: "https://naver.com",
            randomImageUrl: "https://picsum.photos/200",
            altText:"random-image",
          }
})
</script>
```

`v-model` : 폼 input과 textarea 엘리먼트에 양방향 데이터 바인딩을 생성해 준다.(공식문서)
> 뷰 인스턴스에 정의한 데이터와 양방향으로 연결이 된다고 생각하면 이해가 쉽다. 
> 공식문서에 있는 예시를 보면 vue 인스턴스에 사전 정의된 데이터의 message에 
> `v-model`을 통해 바인딩을 걸어주면 vue 인스턴스의 message가 실시간으로 변경된다. 

```html
<input v-model="message" placeholder="여기를 수정해보세요">
<p>메시지: {{ message }}</p>
```
![image](https://user-images.githubusercontent.com/53211781/83280269-59070f00-a211-11ea-84e2-78915f34cff9.png)

## toDo 앱 구현하기

### 기본 컨셉
![image](https://user-images.githubusercontent.com/53211781/83281964-dcc1fb00-a213-11ea-9e86-0ca4b2a534a4.png)

할 일을 적고 추가를 하면 `ul>li` 에 추가가 된다.
체크박스를 클릭하면(일을 마치면) 취소선이 그어지고
완료 버튼을 클릭하면 마친 일들이 데이터에서 삭제된다.

### `addTodo()`

#### `v-model`
뷰 인스턴스의 data에 `newInput` 값을 빈 값으로 설정하고 `<input>` 태그와 바인딩을 해준다.
바인딩되어 반영된 `newInput`을 바탕으로 `content`와 `completed(완료여부)`를 object에 넣어 
`todo` 배열에 넣어준다. 이러한 방식을 통해 todo 목록들이 쌓이게 된다. 

#### `v-on`
`<input>` 태그에 엔터키가 입력되는 이벤트 혹은 + 버튼이 눌리는 이벤트가 발생하면
`addTodo` 매서드가 동작한다. 

```html
<input v-model="newInput" @keydown.enter="addTodo" type="text" class="form-control"placeholder="할 일을 적어주세요">
<button @click="addTodo" class="btn btn-light">+</button>
<script>
  const app = new Vue({
        el: '#app',
        data: {
            status: "all",
            newInput: "",
            todos: []
        },
        methods: {
            addTodo() {
                this.todos.push(
                    {content: this.newInput, completed: false}
                )
                this.newInput = ''
            },
        }
    })
</script>
``` 

### `filterTodo()`

1. v-for은 함수의 return 값을 인자로 받을 수도 있다.todo를 All, Active, Completed로 나누어 해당하는 todo를 보여주기 위해 `fitlerTodo`를 정의하였다. 
2. `is_completed` 클래스를 가지면 취소선이 그어지도록 하기 위해 todo의 completed가 `true`이면 클래스가 표시되도록 `v-bind`를 걸어주었다. 
3. `<input type="checkbox">`와 모델 바인딩을 통해 체크박스의 true/false여부가 todo의 completed와 연결되게 함으로써 진행중인 일과 완료된 일을 구분하는 것을 구현하였다. 

```html
<select v-model="status" class="form-control">
  <option value="all">All</option>
  <option value="active">Active</option>
  <option value="completed">Completed</option>
</select>
<ul>
  <li v-for="todo in filterTodo()" :class="{is_completed:todo.completed}">
    <input v-model="todo.completed" type="checkbox">
    {{todo.content}}
  </li>
</ul>  
```

#### filter 함수 사용하기
여러 데이터 뭉치들로부터 조건에 만족하는 데이터만을 모아 todos를 재구성해 보여줄 것이기 때문에 `filter` 함수를 사용한다. 
함수 안에 인자는 콜백 함수가 들어간다. 따라서 콜백 함수의 조건에 맞는 todo만이 todos에서 필터링 되어 재구성된다. 
```javascript
data: {
    status: "all",
    newInput: "",
    todos: [
        // 예시를 위한 더미데이터
        {content: 'eat kimchi', completed:false}
    ]
},
methods: {
  filterTodo() {
      if (this.status === "active") {
          return this.todos.filter(todo => !todo.completed)
      } else if (this.status === "completed") {
          return this.todos.filter(todo => todo.completed)
      }
      return this.todos
  }
}
```

### `removeComplete()`

완료된 일(`todo.completed === true`)은 아예 data의 **todos 배열에서 삭제** 해버리는 기능을 구현하고자 한다. 
completed가 false인것(`todo.completed === false`)을 필터링해 todos에 담는 매서드를 구현해 클릭하고자 하는 버튼에 이벤트를 걸어주면 된다.

```html
<button @click="removeCompleted" style="width: 70px" class="btn btn-light">완료</button>
```

```javascript
methods: {
  removeCompleted() {
      this.todos = this.todos.filter(todo => {
      // 
          return !todo.completed
      })
  }
}
```