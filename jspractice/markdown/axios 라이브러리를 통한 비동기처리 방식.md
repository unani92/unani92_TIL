# axios 라이브러리를 통한 비동기처리 방식

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>exercise</title>
</head>
<body>
  <h1>Dog Image(s)</h1>
  <hr>

  <h2>강아지</h2>
  <button id="dog">강아지</button>
  <div class="dogs"></div>
  

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 여기에 코드를 작성하시오.
    const button = document.querySelector("#dog")
    const url = 'https://dog.ceo/api/breeds/image/random'

    // 비동기 처리의 동기화 .then : axios 응답이 완료된 이후 실행될 콜백함수
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
    // 버튼을 눌렀을 때
    // 1. axios 사용해 서버에서 데이터 요청
    // 2. 받은 데이터를 담을 img dom 노드 하나 생성(createElement)
    // 3. setAttribute(src, url 삽입)
  </script>
</body>
</html>
```

