# module exports이용 

# (코드 실행 X, 함수 호출에 주목해서 볼것)

- 모듈은 캐쉬된다.

```js
var you = require('./student.js');
you.study(); //1시간째 공부중
you.study(); //2시간째 공부중
var him = require('./student.js');
him.study(); //3시간째 공부중
```



1. require로 파일을 불러오고, 내용을 변수에 저장한 뒤 서버를 실행하면서 이벤트 발생

```js
//Main.js
const user = require('./user.js');
const board = require('./board.js');

const ServerFunciton = () => {
    if(condition == 'user'){
        user.main();
    } else if(condition == 'baord'){
        board.main();
    }
};

ServerFunciton.createserver();

//user.js
exports.main = () => {
    if(condition == 'login'){
        user_login();
    }else if(condition == 'logout'){
        user_logout();
    }else if(condition == 'join'){
        user_join();
    }
};

const user_login = ()=>{};
const user_logout = ()=>{};
const user_join = ()=>{}

//board.js
exports.main = () =>{
    if(condition == 'write'){
        board_write();
    }else if(condition == 'read'){
        board_read();
    }else if(condition == 'modify'){
        board_modify();
    }
};

const board_write = () => {};
const board_read = () => {};
const board_modify = () => {};


//requireGreeting.js
var greeting = require('./greeting.js');
greeting.goodMorning();

//greeting.js
module.exports.goodMorning = function(){
    //모듈 함수 기능 작성
    console.log("hello");
}
exports.goodNight = function(agr, callback){
    //module 생략 가능
}
```

1. exports를 이용해 외부로 내보낼 함수,변수 선언하기

```js
//Main2.js
const data = require('./data2.js');
const ServerFunction = () => {
    data.main();
    console.log(data.list);
};

ServerFunction.createServer();

//data2.js
exports.main = () => {
    somefunction();
};

exports.list = [1,2,3];
```

3.module.exports사용: 해당 파일을 하나의 함수 혹은 하나의 오브젝트로 인지함. 다양한 기능 이용가능. 협업에서 좋음(기능별 분할)

```js
//Main3.js
const item = require('./item.js');
console.log(item());
item.test();

//item3.js
let list = [1,2,3];
module.exports = () => {
    for( let  i = 0; i < list.length; i++){
        list[i] *= 2;
    }
    return list;
};

module.exports.test = () =>{
    console.log("test");
};


//tarnsportExcute.js
var Bus = require('./transport').Bus;
var bus = new Bus();
bus.take();

//transport.js
function BusDef(){
    this.take = function(){}
    console.log('hello Bus');
}
function MetroDef(){
    this.ride = function(){}
}

module.exports.Bus = BusDef;
exports.Metro = MetroDef; //module생략 가능

```



