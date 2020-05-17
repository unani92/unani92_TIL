const todoForm = document.querySelector('.js-todoForm'); 
const todoInput = todoForm.querySelector('input');
const todoList = document.querySelector(".js-todoList")

const TODOS_LOCALSTORAGES = 'toDos'
const toDos = [];

const paintTodoIterate = toDo => {
    paintTodo(toDo.text);
}

function loadTodos() {
    const loadTodos = localStorage.getItem(TODOS_LOCALSTORAGES)
    if (loadTodos !== null ) {
        const parseTodos = JSON.parse(loadTodos);
        parseTodos.forEach(paintTodoIterate);   
    }
}
function paintTodo(text) {
    const li = document.createElement("li");
    const delBtn = document.createElement("button");
    const span = document.createElement("span");
    const newId = toDos.length + 1;
    delBtn.innerHTML = "\u{274C}";
    span.innerText = text;
    li.appendChild(span);
    li.appendChild(delBtn);
    li.id = newId;
    todoList.appendChild(li);

    const toDoObj = {
        text: text,
        id : newId,
    }

    toDos.push(toDoObj)
    localStorage.setItem(TODOS_LOCALSTORAGES,JSON.stringify(toDos));

}
function handleSubmit(event) {
    event.preventDefault();
    const currentValue = todoInput.value;
    paintTodo(currentValue);
    todoInput.value = ""
}
function init() {
    loadTodos();
    todoForm.addEventListener('submit', handleSubmit)
}
init();