# greeting,js 만들기

## 로직 

### intro : 초기 변수 설정하기
```javascript
// querySelector
const form =  document.querySelector(".js-form")
const input = form.querySelector("input")
const greeting = document.querySelector('.js-greetings')
// localStorage
const USER_LOCALSTORAGE = 'username'
// classname
const SHOWING = 'showing'
```
> form 태그, 실제 사용자의 입력값을 받을 input 태그, 입력값을 받은 이후 사용자에게 보여줄 문구를 `querySelector` 매서드를 통해 변수화한다. 
> 그리고 로직의 핵심인 localstorage 내에 username이 저장되었는지를 구별하기 위해 변수를 하나 더 저장한다. 
> 마지막으로 classList에 추가 및 삭제를 통해 사용자의 뷰를 분기하기 위해 .css에 `display: block;`로 저장된 showing 클래스를 변수화한다.
### 1. 유저의 이름이 입력되지 않았을 때
유저의 이름을 받는 폼을 보여준다. 

### 2. 유저의 이름이 입력되었을 때
폼을 사용자의 뷰에서 제거하고 'hello username'을 출력한다. 
```javascript
function loadName() {
    const currnetUser = localStorage.getItem(USER_LOCALSTORAGE);
    if (currnetUser === null) {
        askUserName();
    } else {
        form.classList.remove(SHOWING);
        greeting.classList.add(SHOWING);
        paintGreeting(currnetUser);
    }
}
```

#### `localStorage.getItem`
> 로컬 스토리지에 저장된 변수 중에서 인자와 일치하는 값의 결과를 출력한다. 따라서 유저의 이름이 입력되지 않은 경우에는 username을 물어보지만 입력된 경우에는 form을 뷰에서 제거하고 'hello username'을 출력하는 로직을 만들 수 있다. 

#### `askUserName`
```javascript
function askUserName() {
    form.classList.add(SHOWING)
    form.addEventListener('submit',handleSubmit)
}
```
> 사전에 .css 파일에서 `display: none;` 으로 사용자 뷰에서 지운 상태에서 이름을 입력받아야 하기 때문에 `display: block;`로 정의해 놓은 클래스를 classList에 추가해준다. 이후 사용자의 입력값을 submit 한 이후 `handleSubmit` 함수를 실행시킨다.

#### `handleSubmit`
```javascript
function handleSubmit(event) {
    event.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue);
    localStorage.setItem(USER_LOCALSTORAGE, currentValue);
}
```
> 결국 해야 할 일은 사용자로부터 입력받은 값을 받아 'hello username'을 출력하는 것이다. 이를 위해 사용자가 form에 입력한 값인 value를 변수에 저장한 이후 `paintGreeting` 함수를 실행하고 저장된 `currentValue`를 localStorage에 'username'으로 저장해준다.

#### `paintGreeting`
```javascript
function paintGreeting(text) {
    form.classList.remove(SHOWING);
    greeting.classList.add(SHOWING);
    greeting.innerText = `hello ${text}`; 
}
```
> 이제 다 왔다. 사용자로부터 입력값을 받았으니 더이상 필요가 없는 form 태그를 지워준다. 이후 숨겨져 있던 greeting을 보여주고 내부 텍스트에 입력받은 값을 interpolate 해주면 모든 로직이 완성된다. 
