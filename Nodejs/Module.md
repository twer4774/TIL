# Node.js 모듈이용

- 모듈을 사용하기 위해서는 선언이 필요: require('모듈명');

## 상태파악하기 - console

- 디버깅의 가장 기초는 화면에 프로그램의 상태를 출력 하는 것

- log, error, info 등 여러 메서드 존재
- 기본적인 기능은 log이며, info는 log의 aliasing임

```js
let item = 5;
console.log('count: ', item);
console.log('count: %d', item);
console.log(`count: %{item}`); //백쿼터 이용한 포맷팅
```



- console.log에 여러개의 변수를 넣으면 줄바꿈 없이 출력되며, 각 변수가 object라면 json형태로 출력됨

```js
const object_item = {a:1, b:'c'};
console.log(1, object_item);
//1{a: 1, b:'c'}

//5초마다 문자열로 화면 표시
setInterval(() => {
    console.log("Now Time is ", new Date() );
}, 5 * 1000);
```



## 모듈 사용하기 - require

```js
const filesystem_var = require('fs');

//tmp/hello파일 삭제, 성공할 경우 콘솔창에 성공 출력, 실패시 에러를 던짐
filesystem_var.unlink('/tmp/hello', (err) => { //unlink는 파일 삭제하는 메서드
    if (err){
        thorw err;
        return;
    }
    console.log('delete success');
});
```

```js
//Start.js
const temp = require("./subfile.js");
console.log("Start.js File");

//subfile
console.log("subfile.js File");

//subfile.js File
//Start.js File

//Start2.js
//globbal선언으로 외부호출
global.temp = "a";
console.log(1, temp);
const tempFile = require("./subfile2.js");
console.log(2, temp);

//subfile2.js
console.log(3, temp);
temp = "b";
consol.log(4, temp);

//Result
1 a
3 a //만약 global이 아니라면 undefined출력
4 b
2 b //만약 global이 아니라면 a 출력

```

