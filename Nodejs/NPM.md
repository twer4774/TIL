# NPM(Node Package Manager)

- nodejs가 모듈을 관리하는 패키지
- 전역 설치보다는 개별 설치를 권장함 => 특정 버전 모듈에 의존적인 상황이면 문제 발생
- npm준비

```
npm init //package.json이 생성됨
```

- 설치

```
npm install mysql //npm으로 설치
npm install --save mysql //package.json에 의존성이 추가됨 => 협업에 유용(npm install 이용)
```

- npm업데이트

```
npm install npm@latest -g //npm업데이트
npm install mysql@latest //mysql업데이트
npm update [모듈명]
```

- -g 옵션을 넣으면 해당폴더에 node_modules디렉터리 설치 => forever같은 어느 경로에서나 사용할 경우 이용=> sudo이용해야 함
- 삭제

```
npm uninstall mysql
```

- 현재 디렉터리에 package.json이 있을 경우 의존성에 따라 자동으로 설치

```
npm install
```

## NPM사용하기

```js
//qs는 JSON형태의 데이터를 url에서 다룰 수 있는 형태의 문자열로 서로 변환할 때 주로 사용
const qs = require('qs');

//stringify는 데이터를 url에서 사용가능한 query문자열 형태로 변환 => 문자열형태가 아닌 데이터 형태로 넣어야함
//문자열로 넣고 싶다면 JSON.parse를 사용해 변환한 뒤 넣어야 함
let obj = qs.parse('a=1&b=2');
console.log(JSON.stringify(obj));

let str = qs.stringify(obj);
console.log(str);

let str = qs.stringify(JSON.parse('{"a":"1","b":"2"'));
console.log(str);
```