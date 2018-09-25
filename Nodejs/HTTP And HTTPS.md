# 서버만들기(1) - http

- Node.js에서 가장 비중 있게 사용하는 모듈
- Node.js를 사용하는 이유: 서버의 역할, 웹 서버로 사용
- 네트워크를 사용하는 모든 모듈은 실시간 응답이 불가능한 비동기 함수 => 콜백을 통해 응답하는 함수
- Node.js는 싱글스레드 기반이므로 비동기에 적합함
- 콜백 지옥에서 벗어나는 방법 => Async, Babel모듈이용, Promise형태 이용

```js
//HTTPServer.js
const http = require('http');

http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type':'text/plain'});
    res.end('Hello World\n');
}).listen(8800, ()=>{
    console.log("Server listen started", new Date());
});

console.log("Server Running", new Date());
```

## write와 end의 차이

```js
//Code A
let send_str = "hello world!\n";
send_str += "hello world2";
res.end(send_str);

//Code B
res.write("Hello world\n");
res.write("Hello world2\n");
res.end();
```

- write는 데이터를 바로 전송하지 않고, 네트워크 버퍼에 일정량이 차면 전송함.
  - 데이터를 나눠서보내는 Code B
  - 작은 데이터의 경우 마지막 end를 보낼때 한번에 보냄
  - 데이터를 여러개의 묶음(chunk)으로 전송 => 묶음의 단위: 패킷
- end는 즉시 전송한뒤 소켓을 종료함



## 서버만들기(2) - https(http over SSL)

- 보안이슈와 같은 이유로 https서버를 만듦
- 구글은 http보다 https를 검색결과를 먼저 보여줌
- webhook은 https만 지원하므로 https서버를 만들어야 함
- 엔진엑스나 아파치 같은 프록시 서버를 중간에 두거나, 다양한 클라우드 시스템의 로드밸런서를 이용하면 직접 https를 구현하지 않아도 무방함
- https는 서버와 클라이언트가 암호화된 방법(SSL)으로 통신 => 공개키와 개인키가 필요함
- https로 접속한 주소 앞에는 자물쇠 모양이 생김
- http: 클라이언트가 요청하면 서버가 그냥 전달.   https: SSL에 암호화된 통신채널을 요청하고, 안정성 확인후에 데이터 요청 및 전송 => 해킹하기 어려움

```js
const https = require('https');
const fs = require('fs');

const options = {
    key: fs.readFileSync('agent-key.pem'),
    cert: fs.readFileSync('agent-cert.pem')
};

https.createServer( option, (req, res) => {
    res.writeHead(200);
    res.end('hello wrold\n');
}).listen(8000);
```



## 서버만들기(3) -http, https

- API사용, 외부에 접속해 데이터를 가져와야 하는 경우 => http/s를 통해 외부에서 파일을 가져와야 함

- GET방식으로 데이터를 불러오는 경우

  ```js
  //on을 통해서 데이터의 양이 많거나, 네트워크 상태가 좋지 않을때 나눠서 받음
  //API는 일반적으로 josn으로 리턴해주므로 end이벤트 처리때 JSON.parse()로 받으면 됨
  const http = require('http');
  
  http.get('httt://google.co.kr/',(res) => {
      let body = '';
      res.on('data', (d) => { 
          body += d;
      });
      res.on('end', () => {
          console.log("DATA: ", body);
      });
  }).on('error', (e) => {
      console.log("Error: ",e);
  });
  ```

- POST메서드 처리

  - GET은 주소줄을 이용하여 데이터를 전달
  - POST는 헤더를 이용하여 데이터 전달

- ```js
  const qs = require('querystring');
  const http = require('http');
  
  const post_data = qs.stringify({
      'key1': 'val1',
      'key2': 'val2'
  });
  
  const post_options = {
      host: 'posttestserver.com',
      port: '80',
      path: '/post.php',
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www.form-urlencoded',
          'Content-Length': post_data.length
      }
  };
  
  const post_req = http.request(post_options, (res) =>{
      res.setEncoding('utf8');
      res.on('data', (chunk)=>{
          console.log('Response: ' + chunk);
      });
  });
  
  post_req.write(post_data);
  post_req.end();
  ```


