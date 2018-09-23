# 가장 기본인 Node.js서버

```js
const http = require('http');
const port = 80;

const server = http.createServer((req, res) =>{
    res.statusCode = 200;
    res.setHeader = ('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, (err) =>{
    if(err){
        console.log(err);
    }
    console.log('Server running');
});

//localhost접속
```



## Forever Node.js

- node로 실행할 때 접속을 끊으면 프로그램이 바로 정지해버림.
- Forever프로그램으로 사용자가 멈추라는 명령을하거나, 프로그램을 잘못 작성해 멈추거나, 컴퓨터가 꺼지기 전까지 종료되지 않음

```
npm install forever - g
forever start FirstServer.js //실행
forever stop FirstServer.js //정지
forever list //실행중인 목록
forever stop 0 //맨위에 있는 모듈 정지
forever stopall //모두 정지

forever start -a -l /desktop/TIL/FirstServer.log FirstServer.js //-a는 로그 파일을 기록하되 뒷부분에 추가. -a없으면 항상 처음부터 다시씀(덮어쓰기), -l은 바로 뒤에 오는 경로에 로그파일 저장
```

