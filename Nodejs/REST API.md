# Node.js를 활용하여 REST API구현

## Node.js를 활용한 서버구축

- Node.js는 HTML을 직접 다루기 보다는 서버역할을 하면서 데이터를 다루는 것이 이점
- HTML을 다루기 위해서는 express에서 사용되는 jade가 대표적
- Node.js의 활용처
  - REST서버로 활용
  - 웹페이지에서 Ajax요청
  - 모바일 서버통신
- REST: 기계와 기계, 프로그램과 프로그램 사이의 통신 수단

## Express사용

```
npm install express
npm install express-generator -g //express모듈을 더 쉽게 시작하도록 도와주는 모듈=>기본 골격을 빠르게 만들어주는 역할

express MyNodeAPP //MyNodeApp으로 앱이 만들어짐
cd MyNodeApp && npm install //앱 폴더로 이동한 뒤 npm 설치
DEBUG=mynodeapp:* npm start
```

- node app_name VS npm start
  - node app_name: 해당 파일을 직접 실행
  - npm start: 디렉터리 안에 있는 package.json을 읽어서 그 내용을 실행

```js
//애플리케이션을 만들기 위해 파일 수정
//app.js

//수정 전
app.use('/', indexRouter);
app.use('/users', usersRouter);
//수정 후
app.use('*',indexRouter);
//app.use('/users', usersRouter);

//routes/index.js
//수정 전
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
//수정 후
router.get('/', (req, res, next) =>{
  console.log("GET:", req.body);
  res.status(200).send("GET");
});

router.post('/',(req, res, next)=>{
  console.log("POST:", req.body);
  res.status(200).send("POST");
});

router.put('/',(req, res, next)=>{
  console.log("PUT:", req.body);
  res.status(200).send("PUT");
});

router.delete('/',(req, res, next)=>{
  console.log("DELETE:", req.body);
  res.status(200).send("Delete");
});
```



## REST API구현준비

- 레디스와 비슷한 기능을 가진 앱 만들기

- 레디스: 인메모리 방식의 키-값 체인으로 이루어진 서비스. 매우 빠른 속도로 데이터를 주고받음.

- 구현할 기능

  - Key-Stack API: 주어진 정보를 정해진 배열에 쌓고 꺼내는 기능. 
    - 데이터 입력: PUT
    - 데이터 출력: GET, 데이터가 없을때 Null리턴
  - Key-Queue API: 주어진 정보를 처리하는 큐 기능 제공
    - 데이터 입력 API
    - 데이터 출력 API

- 구현 스펙 정리

  - /stack/{array_name}
    - PUT: 데이터 저장, 저장된 데이터는 가장 위에 쌓임
    - GET: 데이터 출력, 데이터를 가져오면 배열에서 제거됨
  - /que/{array_name}
    - PUT: 데이터 저장, 배열의 가장 뒤에 데이터 추가
    - GET: 데이터 출력, 배열 맨 앞의 데이터 가져옴

  ## REST API 실제 구현하기

  ```
  npm install body-parser
  npm install multer
  ```

  ```js
  const express = require('express');
  const app = express();
  const bodyParser = require('body-parser');
  const multer = require('multer');
  const upload = multer();
  
  
  let stack_list = [];
  
  app.route('/stack/:stack_name').get(( req, res) =>{
      let stack_name = req.params.stack_name;
      let result;
      if( stack_list[stack_name]){
          result = stack_list[stack_name].pop();
      } else {
          result = null;
      }
  
      res.json(result);
  }).put((req, res)=>{
      let stack_name = req.params.stack_name
  
      if(stack_list[stack_name]){
          stack_list[stack_name].push(req.body);
      }else{
          stack_list[stack_name] = [req.body];
      }
      res.json({
          result:'ok'
      });
  });
  
  let que_list = [];
  
  app.route('/que/:que_name').put((req, res)=>{
      let que_name = req.params.que_name;
      if(que_list[que_name]){
          que_list[que_name].push(req.body);
      }else{
          que_list[que_name] = [req.body];
      }
      res.json({
          result:'ok'
      });
  }).get((req, res)=>{
      let que_name = req.params.que_name;
  
      let result;
      if(que_list[que_name]){
          result = que_list[que_name].shift();
      }else{
          result = null;
      }
  });
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({extended: true}));
  
  app.listen(8080, ()=>{
      console.log("Start");
  });
  ```
