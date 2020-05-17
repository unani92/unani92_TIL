const clicked = "clicked"
const title = document.querySelector('#title')



function init() {
    title.addEventListener('click', handleClick)
}

init();

// toggle ver : 있으면 add 없으면 remove
function handleClick() {
    title.classList.toggle(clicked)
}

// const handleClick = function() {
//     const hasClass = title.classList.contains(clicked)

//     if (hasClass) {
//         title.classList.remove(clicked);
//         // title.classList.remove("btn")

//     } else {
//         title.classList.add(clicked);
//         // title.classList.add('btn')
//     }
// }