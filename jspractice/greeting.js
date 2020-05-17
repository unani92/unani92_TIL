// querySelector
const form =  document.querySelector(".js-form")
const input = form.querySelector("input")
const greeting = document.querySelector('.js-greetings')
// localStorage
const USER_LOCALSTORAGE = 'username'
// classname
const SHOWING = 'showing'
// function

function saveName(text) {

}


function paintGreeting(text) {
    form.classList.remove(SHOWING);
    greeting.classList.add(SHOWING);
    greeting.innerText = `hello ${text}`; 
}

function handleSubmit(event) {
    // form 태그는 submit 동작 발생 시 새로고침이 발생하기 때문에 저장된 값이 어디론가 날아가버린다. 
    // 따라서 이를 방지하기 위해서 default 동작을 막아주고 input을 받아와야 한다. 
    event.preventDefault();
    const currentValue = input.value;
    paintGreeting(currentValue);
    localStorage.setItem(USER_LOCALSTORAGE, currentValue);
}

function askUserName() {
    form.classList.add(SHOWING)
    form.addEventListener('submit',handleSubmit)
}

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

function init() {
    loadName()
}
init();