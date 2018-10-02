# 에러 및 예외 처리

- 예외처리: 다양한 이유로 오류가 발생하는데 대처하는 코드 작성



## 에러처리

- 에러: 프로그램 상에서 코드의 실수로 오류가 난 것
- try catch문을 통해 기본적인 에러 처리 가능

```js
try{
    wrong_function();
}catch(e){
    console.log("에러가 발생하였습니다.");
}

//파일,네트워크 등을 여는 부분
openResource();
try{
    userResource();
}finally{
    closeResourece();
}
//만약 너무 많은 MySQL접속이나, 파일 처리 후 리소스를 반환하지 않으면 에러 발생


//구문 시도에 문제가 없을 시 finally실행, 문제 발생시 catch문 실행 뒤 finally 실행
try{
    wrong_function();
}catch(e){
    console.error(e.message);
}finally{
    console.log('function ended');
}
```



## 예외처리

- 네트워크, 외부 디바이스와 연계되는 작업들은 에러 발생이 많음
- 콜백 형태의 함수를 가지는 함수들은 예외 처리에 관한 기능이 내장 되어 있음

```js
//ExceptionHandler.js
const fs = require('fs');
fs.readFile('temp.txt', (err, data)=>{
    if(err){
        console.log("에러로 인해 파일을 열 수 없습니다.\n에러는 다음과 같습니다.");
        console.error(err);
        return;
    }
    console.log(data);
});
fs.unlink('temp.txt', (err)=>{
    if(err){
        console.error("에러로 인해 파일을 삭제할 수 없습니다.\n에러는 다음과 같습니다.");
        console.error(err);
        return;
    }
    console.log('파일이 성공적으로 삭제되었습니다.');
});
//결과
에러로 인해 파일을 열 수 없습니다.
에러는 다음과 같습니다.
{ [Error: ENOENT: no such file or directory, open 'temp.txt'] errno: -2, code: 'ENOENT', syscall: 'open', path: 'temp.txt' }
에러로 인해 파일을 삭제할 수 없습니다.
에러는 다음과 같습니다.
{ [Error: ENOENT: no such file or directory, unlink 'temp.txt'] errno: -2, code: 'ENOENT', syscall: 'unlink', path: 'temp.txt' }
```



## 에러 저장

- 에러 저장 방법
  - 파일로 저장
  - 데이터베이스에 저장
  - 클라우드 툴 이용
- 에러 발생은 여러 곳에서 일어날 수 있으므로, 이중 삼중으로 로그를 남겨두는것이 좋음
- 추천 방법: 1차적으로 파일에 저장, 2차적으로 슬랙에 자동으로 보내기

```js
//파일로 남기기
//시간대를 서울로 설정. 설정 안하면 UTC로 설정 됨
process.env.TZ = 'Asia/Seoul'; 

//현재 시간 하늘색으로 출력, 실행중인 node.js버전과 파일명 출력
console.log("\033[36m"+new Date()+"\033[0m: Node Version: ["+process.version+"]");
console.log("\033[36m"+new Date()+"\033[0m: ["+__filename+"] Started");

Object.defineProperty(global, '__stack', {
    get:() => {
        let orig = Error.prepareStackTrace;
        Error.prepareStackTrace = (_, stack) => {return stack;};
        let err = new Error;
        Error.captureStackTrace(err, arguments.callee);
        let stack = err.stack;
        Error.prepareStackTrace = orig;
        return stack;
    }
});

Object.defineProperty(global, '__line', {
    get:() => {
        return __stack[1].getLineNumber();
    }
});
const fs = require('fs');

//로깅 모듈
global.Logger = (log) =>{
    //현재 로컬 시간을 문자열 형태로 반화하는 함수
    const getDateStr = ()=>{
        return new Date().getFullYear()+"_"+("0"+(1+new Date().getMonth())).slice(-2)+"_"+("0"+new Date().getDate()).slice(-2);
    };
    let stack = (new Error()).stack.toString().split("\n")[2].split(" ").pop().split(":");

    let str = new Date()+": ["+stack[0].substr(1)+"] Line: "+stack[1];

    if(log){
        str += "" + JSON.stringify(log);
    }

    let k = __filename.split("/");
    k.pop();

    let str_dsp = "\u001b[36m"+new Date()+"\u001b[0m: ["+stack[0].substr(1)+"] Line:"+stack[1];
    if(log){
        str_dsp += " "+JSON.stringify(log, null, "\t");
        str_dsp = str_dsp.replace("\"type\": \"init\"", "\"type\": \u001b[33m\"init\"\u001b[0m");
        sr_dsp = str_dsp.replace("\"type\": \"error\"", "\"type\": \u001b[101m\"error\"\u001b[0m");
    }
    console.log(str_dsp);
    fs.appendFile(k.join("/")+'/'+getDateStr()+".log", str+"\r\n", (err)=>{
        if(err){
            console.log(str);
        }
    });
};

Logger({
    "type":"error",
    "text":"something error",
    "code":"code01"
});
console.log(__line, "Some Code");

//결과
Tue Oct 02 2018 14:08:00 GMT+0900 (GMT+09:00): Node Version: [v10.10.0]
Tue Oct 02 2018 14:08:00 GMT+0900 (GMT+09:00): [/Users/wonik/Desktop/TACADEMY-ONLINE/NodeJs/Node200/nodejsProgramming/ExceptionHandler/StoreError.js] Started
Tue Oct 02 2018 14:08:00 GMT+0900 (GMT+09:00): [/Users/wonik/Desktop/TACADEMY-ONLINE/NodeJs/Node200/nodejsProgramming/ExceptionHandler/StoreError.js] Line:55 {
	"type": "error",
	"text": "something error",
	"code": "code01"
}
```

