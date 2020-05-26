# axios 라이브러리를 통한 비동기처리 방식

## Index : 비동기 처리란 무엇인가?
> 정의 : 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 자바스크립트의 처리

#### 이것은 왜 필요한가?
이렇듯 특정 로직의 실행이 끝날 때까지 기다려주지 않고 나머지 코드를 먼저 실행하는 일은 브라우저에서 효율적인 작업을 위해 필요하다. 이해를 위해 일상적인 사례를 비유로 들어보자

##### 오늘 저녁에 할 일 
1. 거래처에 이메일 보내기
  - 이메일 답장 확인하기
  - 회신 보내기
2. 저녁식사하기
3. 부모님께 전화걸기
  - 전화를 받지 않을 경우 문자로 안부 물어보기
4. 잠자기

오늘 할 일이 4가지 있다고 가정해보자. 동기처리만 존재하고 비동기처리가 없는 세상이라면 일처리는 1번부터 4번까지 순차적으로만 이뤄질 것이다. 문제는 여기서 발생한다.

이메일을 보내는 일이 1번이지만 이메일은 보내면 바로 답장이 오지 않는다. 그렇다면 답장 확인이 불가하고 회신을 보낼 수도 없다. 그러면 저녁은 언제 먹지??? 하는 문제가 발생하고 **오늘 안에 답장을 보내지 못하면 잠도 못자는 상황이 발생**할 것이다. 답장이 빨리 와서 회신을 하고 저녁을 먹었다. 그런데 **부모님이 전화를 받지 않으신다.** 그렇다면 오늘 잠은 다 잤다고 봐야된다. 

비동기처리는 이러한 문제를 해결하기 위한 처리방식이다. 현실세계에서는 이메일을 보내놓고 다른 일을 처리한다. 비동기세계에서도 마찬가지이다. **이메일을 보내놓고 저녁식사를 한다.** 저녁식사를 하던 중 **답장이 오면 이를 확인하고 회신**까지 보낼 수 있다. 이후 일처리도 마찬가지이다. 이러한 비동기처리 방식이 적용되면 우리는 이메일이 오지 않고 부모님이 전화를 받지 않더라도 잠자기까지 무리없이 진행할 수 있다. 이것이 비동기처리의 장점이다. 

## promise 객체란 무엇인가?
> 정의 : 비동기 작업이 맞이할 미래의 완료 또는 실패와 그 결과 값을 나타내기 위한 객체(출처 : MDN)

비동기처리 방식은 **DB에서 데이터를 불러오거나 API에서 데이터를 불러오는 일**과 같이 시간이 걸리지만 다 끝날 때 까지 마냥 기다리고 있기에는 비효율적인 상황을 효율적으로 해결하는 데 유용한 방식이라고 설명하였다. 따라서 이러한 상황의 성공 혹은 실패 시에 어떠한 행동을 이어 할지에 대해 정의해 주어야 한다. 이를 위해 promise 객체가 존재한다. 따라서 promise 객체는 다음과 같이 구성된다. 
  - 대기 : `get / post` 요청을 보내 놓고 이행하거나 거부되지 않은 초기 상태.
  - 이행(`.then()`) : 연산이 성공적으로 완료되었을 때
  - 거부 (`.catch()`): 연산이 실패한 상태

**axios 라이브러리**는 이러한 promise 객체를 쉽고 편하게 만들기 위해 존재한다. 

## axios 라이브러리 사용하기

### 라이브러리 로드하기
axios 라이브러리는 cdn 로딩을 통해 쉽게 사용할 수 있다. 구글에 `axios cdn` 을 검색한다. 깃허브 리드미 공식문서를 확인하면 cdn이 있는데 jsdelivr, unpkg 중 하나 아무거나 가져다 써도 상관 없다. 
```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
```

### get 요청 보내보기
자바스크립트에서의 비동기처리는 주로 **API 통신, DB와의 통신을 위한 GET/POST 요청**에 활용된다. 이번 예시에서는 강아지 사진 API(https://dog.ceo/api/breeds/image/random)를 활용한 이미지 요청을 구현할 것이다. 

```html
<button id="dog">강아지</button>
<div class="dogs"></div>
```
버튼을 누르면 API 요청을 보내 이미지를 가져와 dogs 클래스를 가진 div 박스 안에 랜덤 강아지 사진을 추가해 주는 프로그램을 구현할 것이다. 로직을 정리하면 다음과 걑다.

### 버튼을 눌렀을 때
  1. axios 사용해 서버에서 데이터 요청
  2. 받은 데이터를 담을 img 노드 하나 생성(createElement)
  3. setAttribute(src, url 삽입)

### 구현하기
버튼과 API url을 다음과 같이 변수 할당을 해 주었다. 
```javascript
const button = document.querySelector("#dog")
const url = 'https://dog.ceo/api/breeds/image/random'
```

#### axios GET
```javascript
const getDogImages = function() {
  axios.get(url)
}
```
우선 url에 `get` 요청을 보내 axios 함수를 통해 `promise` 객체를 만들어준다. 객체가 어떻게 생겼는지 알아보자
```javascript
const getDogImages = function() {
  axios.get(url).then(
    (response) => {
      console.log(response)
  })
}
button.addEventListener("click", getDogImages)
```

#### promise 객체 구성요소 알아보기
버튼 클릭 시 다음과 같은 json이 출력된다. 
<img src="스크린샷 2020-05-24 오전 1.06.48.png"/>
이미지 출력을 위해서는 `data.message`에 담겨 있는 url이 필요하다는 것을 알 수 있다. 

#### 비동기처리 함수 구현하기
그렇다면 다음과 같은 코드를 완성할 수 있다. 
```javascript
const getDogImages = function() {
  axios.get(url).then(
    (response) => {
      const imgURL = response.data.message;
      const dogImage = document.createElement("img")
      dogImage.src = imgURL;
      dogImage.style.height ="300px";
      document.querySelector(".dogs").appendChild(dogImage);
  })
}
button.addEventListener("click", getDogImages)
```

#### 프로세스 요약하기
1. url을 통해 get 요청을 보내 promise 객체를 만든다.
2. url 요청이 성공적으로 이뤄진다면 then() 내부의 콜백을 실행한다.
  - promise 객체 내부에서 img url을 추출한다. 
  - `createElement('img')`를 통해 img 태그를 생성산다. 
  - 태그에 src 속성과 style 속성을 정의해준다. 
  - 사전에 만들어 두었던 div 박스 노드를 불러와 img태그를 자식으로 넣어준다.(`appendChild()`)
3. 버튼을 눌러 비동기 요청이 제대로 이뤄지는지 확인한다.
<img src="스크린샷 2020-05-24 오전 1.18.30.png"/>