# Server분석

```js
const http = require('http');
const port = 80;
const hostname = '127.0.0.1';

const server = http.createServer((req, res) => {
   res.statusCode = 200;
   res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World\n');
});

server.listen(port, (err) => {
    if( err ){
        console.log(err);
    }
    console.log('Server Running');
});
```

- http모듈: 웹 서버와 클라이언트에서 데이터를 주고 받을 때 사용하는 모듈, http.request와 http.response를 이용해 통신한다. https를 사용할 수 있지만, SSL인증서가 필요하다.
- hostname: 특정 IP주소에서만 서버를 동작시킬 때 이용하는 경우에만 해당 주소를 입력하고, 그렇지 않을 때는 비워둠
  클라우드 서비스를 이용할때에는 내부IP주소와 외부IP주소가 다르기때문에 비워두어야 이용이 가능하다.
- IP별로 다른 동작을 구현할 경우, 서버를 선언하는 부분이 아니라 동작하는 부분에서 구분해 줌
- port: 일반적으로 http서비스를 이용하는 경우 80, https서비스의 경우 443으로 설정 => 검색엔진에서도 검색되도록
  다른 포트번호로 이용할 경우 웹서버와 통신이 어려움. 개발 테스트의 경우, 8000 or 8080번 이용
- 응답헤더: 페이지에 대한 다양한 정보, Desktop or Mobile 구분. 

```js
const http = require('http');

const server = http.createServer((req, res) => {
    //클라이언트측 IP를 받아들이는 부분, Proxy시스템을 통과할 경우 x-forwarded-for라는 헤더 값을 사용해 실제IP를 헤더에 포함시킴 => 서버에서는 현재 자신이 접속하고 있는 상대방 IP는 알 수 있는데, 중간에 프록시나 로드밸런스가 있으면 중간의 IP는 알 수 있지만, 실 사용자의 IP주소는 모르기 대문에 헤더값을 통해서 정보 전달
   var ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
    console.log("ip: ", ip);
    console.log("url: ", req.url);
    console.log("headers: ", req.headers);
    
    res.statusCode = 200;
    //실제 넣고 싶은 헤더 값들을 넣는 곳, 현재 페이지를 어떤 형식으로 출력할 지 결정
    //text일 때, 본문 그대로 표시. html일 때 마크업에 따라 화면에 출력
    res.setHeader('Content-Type', 'text/plain'); 
    //서버가 클라이언트에 실제로 보내고자 하는 데이터를 보냄. write(계속 보낼 수 있음) or end(전송후 종료)
    res.end('Hello World\n' + JSON.stringify(req.headers, null, 4));
});

server.listen(80, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Server Running');
});
```



## HTTP응답코드

| 응답코드 |         의미          |                          설명                          |
| :------: | :-------------------: | :----------------------------------------------------: |
|   200    |          OK           |           정상적인 요청에 정상적으로 응답함            |
|   206    |    Partial Content    |            서버가 일부 콘텐츠를 전송하였음             |
|   301    |   Moved Permanently   | 현재 요청한 페이지는 영구적으로 다른 주소로 이동되었음 |
|   302    |   Moved Temporarily   |   현재 요청된 페이지는 임시로 다른 주소로 이동되었음   |
|   304    |     Not Modified      |       마지막 접속 요청 후 페이지가 변경되지 않음       |
|   403    |       Forbidden       |             요청된 주소는 접근이 막혀 있음             |
|   404    |       Not Found       |               요청된 페이지를 찾을 수 없               |
|   500    | Internal Server Error |     서버에 오류가 생겨 해당 요청을 처리할 수 없음      |

