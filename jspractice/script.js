const title = document.querySelector("#title")
const BASE_COLOR = 'black'

function handleClick() {
   if (title.style.color === BASE_COLOR) {
       title.style.color = "red";
   } else {
       title.style.color = "black";
   }
}

const init = function(){
    title.style.color = BASE_COLOR;
    title.addEventListener('mouseenter', handleClick);
}
init()

// click 되었을 때 handleClick 함수를 호출하시오
// title.addEventListener('click', handleClick);

// const age = prompt("how old R U?")
// if (age >= 20) {
//     console.log('U can Drink')
// } else {
//     console.log('Sorry U cannot Drink!!')
// }