# 멀티 스레드

## 싱글 스레드와 멀티 스레드

- 멀티 스레드: CPU가 메인 스레드를 동작시킬 때 독립적으로 돌아가는 스레드를 여러개 동작 시키는 방법
- Node.js에서는 클러스터(Cluster)라는 기술로 자식 프로세스를 동작시킴



### 자식 프로세스

- 메인 프로세스가 동작하고, 독립된 동작을 수행하는 프로세스 생성 방법
- 메인 프로세스와 동작을 공유하지 않지만 작업하고 있는 리턴 값 정도는 받을 수 있음
- Node.js는 대용량 바이너리 처리가 힘듦 => 자식프로세스로 C/C++로 개발된 프로그램 동작시켜서 해결함

### 클러스터(cluster)

- 같은 작업을 여러개 동시 작업이 필요한 경우 유용함 => 같은 작업의 병렬처리

- 웹 서버를 동작시키는경우 여러개의 CPU를 사용하여 최대한의 효율을 이끌어내는 데 사용하는 방법
- 하나의 포트에 들어오는 웹 접속 요청을 여러 개의 CPU가 나눠받아 작업을 처리할 때 매우 효율적

```js
const cluster = require('cluster');
const http = require('http');

//Master부분
if(cluster.isMaster){
    let numReqs = 0;
    setInterval(() => {
        console.log('numReq = ', numReqs);
    }, 1000);

    //메시지가 올 경우 이벤트 발생
    const messageHandler = (msg) => {
        if(msg.cmd && msg.cmd == 'notifyRequest'){
            console.log("Noti!");
            numReqs += 1; //이벤트 발생시 1씩 증가, 위의 명령어에서 1초마다 numReqs출력
        }
    }

    //CPU의 개수를 알아내어 서브 클러스터를 그 CPU개수만큼 동작시키는 부분
    const numCPUs = require('os').cpus().length;
    for(let i = 0; i < numCPUs; i++){
        cluster.fork(); //fork()는 클러스터를 실행시키는 명령어
        console.log("New Fork!");
    }

    Object.keys(cluster.workers).forEach((id) => {
        cluster.workers[id].on('message', messageHandler);
    });
} else {
    //클러스터부분
    //웹서버로 요청이 들어오면 hello world출력
    http.Server( (req, res) => {
        res.writeHead(200);
        res.end('hello world\n');

        //master로 notifyRequest메시지 보내줌
        process.send({ cmd: 'notifyRequest' });
    }).listen(8000);
}

//결과
New Fork!
New Fork!
New Fork!
New Fork!
numReq =  0 //1초씩 반복
numReq =  0
Noti! //localhost:8000으로 접속시 이벤트 발생
numReq =  1
Noti!
numReq =  2
```



```js
//Master와 cluster가 메시지를 주고 받는 방법
//cluster -> master : process.send -> worker.on
//master -> cluster : worker.send -> process.on

const cluster = require('cluster');

if(cluster.isMaster){
    const worker = cluster.fork(); //클러스터 실행
    let timeout;

    console.log(1);

    //이벤트 발생시 worker클러스터로 recvmsg메시지를 보냄
    worker.on('listening', (address) => {
        console.log(3);
        worker.send('recvmsg');
    });
}else if (cluster.isWorker){
    //worker cluster에서는 서버 실행
    const net = require('net');
    const server = net.createServer((socket) => {});

    server.listen(8000);//대기상태
    console.log(2);
    //클러스터는 마스터에게 proccess.on이벤트 핸들러 처리기를 통해 메시지 수신
    process.on('message', (msg) => {
        console.log(4);
        if(msg === 'recvmsg'){ //recvmsg메시지를 받으면 TEST를 출력
            console.log("TEST");
        }
    });
}

//결과
1
2
3
4
TEST
```



## 파일 분리로 클러스터 동작시키기

- 대형 프로젝트에서 안정적으로 프로그램이 돌아가야 할 때 이용
- 어떤 에러가 나더라도 시스템이 멈추면 안되는 경우에 아래와 같은 방법을 이용하면 유용함

```js
//DividMaster.js
const cluster = require('cluster');
cluster.setupMaster({
    exec: 'worker.js',
});

const worker = cluster.fork();
worker.on('message', (msg) =>{
    console.log(msg);
});

//Worker.js
setInterval(() => {
    process.send('worker');
},1000);

//결과
worker
worker
```

- 마스터에서는 클러스터 형태로 나뉘어있는 프로그래머들을 동작만 시키고
- 실제 동작은 클러스터에서 동작하도록 설계

```js
//Master2.js
const cluster = require('cluster');
cluster.setupMaster({
    exec: 'Worker2.js',
});

const worker = cluster.fork();
worker.on('message', (msg) => {
    console.log(msg);
})
.on('error', ()=>{
    console.log("Error");
})
.on('exit', (code, signal)=>{
    if(signal){
        console.log('worker was killed by signal: ${signal}');
    } else if (code !== 0){
        console.log('worekr exited with error code: ${code}');
    } else {
        console.log('worekr success!');
    }
});

//Worker2.js
setInterval(() => {
    process.send('worker');
},1000);

//5초뒤 에러로 종료되도록 설정
setTimeout(()=>{
    error_function();
},5000);

//결과
worker
worker
worker
worker
worker
error발생
```

