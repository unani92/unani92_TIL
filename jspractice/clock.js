// queryselector : 자식 노드를 탐색
const clockContainer = document.querySelector(".js-clock");
const clockTitle = clockContainer.querySelector('.js-title')

const amFm = function(time){
    if (time < 10) {
        return `0${time}`
    } else {
        return time
    }
}

const getTime = function() {
    const date = new Date();
    const minutes = date.getMinutes();
    const hours = date.getHours();
    const seconds = date.getSeconds()
    clockTitle.innerText = `${amFm(hours)} :  ${amFm(hours)} : ${amFm(seconds)}`
}

function init(){
     getTime();
     setInterval(getTime,1000)
}
init();

// 간단한 조건문 작성 시 사용 가능 팁 : ? -> if / : -> else 
// clockTitle.innerText = `${amFm(hours)} :  ${amFm(hours)} : ${
//     seconds < 10 ? `0${seconds}` 
//     : seconds
// }`