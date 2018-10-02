# 실시간 데이터 통신

## http통신

- 본래 정적 웹페이지를 목표로 개발 됨
- Ajax 기술이 도입되면서 동적 웹 구현 가능
- HTTP 프로토콜을 사용해 서버와 웹 브라우저 통신
- 클라이언트가 서버에 요청하면 서버는 응답을 한 뒤, 데이터 전송이 끝나면 연결을 종료하는 기술
- 실시간 데이터 전송이 많아지면서 기술이 발달 => Comet(페이스북에서 이용), WebSocket
- Node.js에서는 Socket.io 모듈이 있음
  - 만약 WebSocket을 지원하는 브라우저라면 WebSocket으로 연결하고, 
  - 아니라면, Comet 또는 Adobe Flash Player로 연결

## Comet - LongPolling

- Http프로토콜의 단점: 지속 연결이 어려움
- Comet의 구현방법
  - long polling
    - 폴링: 주기적인 접속. 5초에 한 번씩 서버에 접속을 요청해 그 동안 변경된 데이터를 가져오는 방식
    - 롱 폴링: 한 번의 요청으로 충분히 긴 시간(30초가량)동안 접속을 유지하고 있으면서, 중간에 서버에서 클라이언트에 보내야 하는 정보가 발생하면 그 시점에 해당 연결에 데이터를 실어 보낸 뒤 접속을 종료. 클라이언트 측에서 이벤트 처리 후 즉시 재요청을 함
  - streaming: 하나의 접속을 계속 유지하면서 지속적으로 정보를 보내는 것. 대용량 데이터 전송에 적합

```js
//LongPoliing.js
const http = require('http');
const fs = require('fs');
const server = http.createServer((req, res) =>{
    //Router구현, /일 경우 index.html파일을 읽어 사용자에게 전달, 없을 경우 File Not Found 전달
    if (req.url == '/'){
        fs.readFile('index.html', 'utf8', (err, data)=>{
            if(err){
                res.statusCode = 404;
                res.setHeader('Content-Type', 'text/plain');
                res.end('File Not found\n');
            } else {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/html');
                res.end(data);
            }
        });
        //longpolling일 경우 long polling접속으로 간주하여 HttpConnection배열에 저장
        //실제 서비스 구현 시 쿠키, 레디스 세션키 값등을 이용 해야함
    }else if(req.url == '/longpolling'){
        HttpConnection.push([req, res]);
        //예상 외의 경우 Hello World cnffur
    }else{
        console.log(req.url);
        setTimeout(()=>{
            res.statusCode=200;
            res.setHeader('Content-Type', 'text/plain');
            res.end('Hello World\n');
        },1000);
    }
});

server.listen('127.0.0.1', 80, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Server Running');
});

let HttpConnection = [];

setInterval(() => {
    console.log(HttpConnection.length);
    if(HttpConnection.length > 0){
        const Connection = HttpConnection.pop();
        const res = Connection[1];
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('End/\n');
    }
}, 30*1000);
```

```html
<!--index.html-->
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <script src = "https://ajax.googleapis.com/ajsx/libs/jquery/3.1.1/jquery.min/js"></script>
    </head>
    <body>
        <script type="text/plain">
        var CallLongPoll = () => {
            $.ajax({
                type:'post',
                url:'/longpolling',
                success:(data)=>{
                    console.log("END");
                    CallLongPoll();
                }
            });
        };

        CallLongPoll()
        </script>
    </body>
</html>
```



## WebSocket과 Socket.io

- WebSocket
  - 접속 후 지속연결(persistence connection) 형태로 프로토콜이 이루어짐
  - comet과 달리 최신 브라우저를 사용해야 함 => 현재 대부분이 WebSocket 지원
  - 일반인이 많이 쓰는 사이트는 Comet, 개발자가 좀 더 많이 접근하는 사이트는 WebSocket으로 단일화 하는 추세
  - HTTP프로토콜의 변형 -> Node.js 사용 제약 -> NPM이용 => Socket.io

```
npm install socket.io
```

```js
//socketio.js
const SocketServer = require('socket.io');
const io = new SocketServer();

const chat = io
.of('/chat')
//connectin이벤트로 socket을 인자로 받음. 이후 socket으로 데이터 주고 받음
.on('connection', (socket)=>{
    console.log("connection");
    socket.on('msg',(data)=>{
        console.log("RECV MSG", data);

        setTimeout(()=>{
            //emit은 데이터를 메시지 형태로 보내는 것
            //socket.emit은 socket자신에게 메시지를 보내는 것
            socket.emit("msg","Send from Server1"+new Date());
            //chat.emit은 현재 접속하고 있는 모든 소켓에 메시지 보내는 것(전체공지)
            chat.emit("msg","Send from Server2"+new Date());
        },1000);
    }).on('distconnect',()=>{
        console.log("disconnect");
    });
});

io.listen(3000);
```

```html
<!--socketio.html-->
<html>
    <body>
        <script src="https://cdn.socket.io/socket.io-1.4.5.js"></script>
        <script>
        var socket = io.connect('http//localhost:3000/chat');
        socket.on('connect', ()=>{
            console.log("connect");
            socket.emit('msg','first connect');
        }).on('msg',(data)=>{
            console.log(data);
            setTiemout(()=>{
                console.log('Send to Server'+new Date());
                socket.emti('msg', 'Send to Server'+new Date());
            },1000);
        }).on('disconnect',()=>{console.log(1);});
        </script>
    </body>
</html>
```

## 랜덤채팅 만들기 - 코드 참고용

```html
<!--RandomChat.html-->
<html>
    <body>
        <script src="https://cdn.socket.io/socket.io-1.4.5.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
        <textarea style="background-color: #ccc;height: 400px;width: 400px;overflow: hidden;"readonly="true"></textarea>
        <br/>
        <from>
            <input style="width: 400px;" type="" id="inputbox">
        </from>
        <script>
            var socket = io.connect('http://localhost:3000/chat');
            socket.on('connect',()=>{
                console.log("connect");
            }).on('disconnect',()=>{
                console.log('disconnect');
            }).on('msg',(data)=>{
                $("textarea").val($("textarea").val()+"\n"+data)
                .scrollTop($("textarea")[0].scrollHeight);
            });

            $("from").submit(()=>{
                socket.emit('msg', $("form input").val());
                $("form input").val("");
                return false;
            });
        </script>
    </body>
</html>
```

```js
//RandomChatServer.js
const SocketServer = require('socket.io');
const io = new SocketServer()

//사용자들으 소켓을 관리하기 위한 변수
let SockList = {};
const chat = io.of('/chat').on('connection', (socket) =>{
    SockList[socket.id] = null;
    socket.emit("msg", "서버에 접속되었습니다ㅏ."+new Date());

    //빈 원소가 있다면 그 원소에 해당 소켓을 연결하고 대화방을 연결 시킴
    //빈 대화방이 없다면 연결되지 않음
    for(let sock_id in Socklist){
        if(sock_id != socket.id && SockList[sock_id] == null){
            SockList[sock_id] = socket.id;
            SockList[socket.id] = sock_id;
            break;
        }
    }

    let opt_socket = SockList[socket.id];
    if(opt_socket){
        chat.sockets[opt_socket].emit("msg","[상대방]이 서버에 접속하였습니다.");
        chat.sockets[socket.id].emit("msg","[상대방과 연결되었습니다.]");
    }
    socket.on('msg',(dta)=>{
        const opt_socket = SockList[socket.id];
        if(opt_socket){
            chat.sockkets[opt_socket].emit("msg","[상대방]"+data);
            chat.sockets[socket.id].emit("msg","[나]"+data);
        }
    }).on('disconnect', ()=>{
        let opt_socket = SockList[socket.id];
        if(opt_socket){
            chat.sockets[opt_socket].emit("msg","상대방이 접속을 종료합니다.");
            SockList[opt_socket] = null;
        }
        delete SockList[socket.id];
    });
});

io.listen(3000);

setInterval(() => {
    let count = 0;
    for(let sock_id in SockList){
        count++;
    }
    chat.emit("msg","[전체공지]현재 접속 인원은 총 "+count+"명입니다.");
},1000*10);
```

