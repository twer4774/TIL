## NoSQL

- 카산드라(Cassandra), 몽고디비(MongoDB), 레디스(Redis), 다이나모(Dynamo, 아마존)
- 현재 NoSQL은 레디스를 많이 사용함
- 일반적인 데이터 처리는 MySQL을 이용, 세션이나 간단한 공용 데이터 형태를 사용하는 경우 레디스를 사용함

## Redis

- 사용하는 이유: 엄청나게 빠른 속도. 인메모리 DB
- Pub/Sub 기능이 핵심
- 하나의 채널을 열어 놓고 여러개의 프로그램이 채널을 구독 한뒤, 한 서버에서 이벤트가 발생하면 해당 내용을 발행 해 모든 구독자가 이벤트를 받을 수 있도록 함
- 공용의 데이터 공간에 이미지 파일을 업로드한 뒤, 개별 서버들에게 Pub/Sub을 이용해 변경 내역만 알려줌

```
apt install redis-server
//mac에서는
brew install redis

//server켜기
redis-server
//서버로 접속
redis-cli
//ping을 입력하면 pong을 리턴함
//단, 현재는 로컬 호스트에서만 접속이 가능함. 설정을 바꿔줘야함
// /etc/redis/redis.conf //우분투
// /usr/local/etc/redis.conf 파일에서 bind 127.0.0.1을 삭제하거나, 다른 IP를 추가함 //mac
//보안 취약 문제로 비밀번호를 입력하는 경우
#bind 127.0.0.1
requirepass somepassword 를 입력하고 저장함(somepassword가 비밀번호임)

//설정 후 재시작
service redis-server restart //우분투
brew services restart redis //mac
//비밀번호로 권한 얻기
127.0.0.1:6379> ping
(error) NOAUTH Authentication required. //권한이 없으면 인증을 요구함
127.0.0.1:6379> auth somepassword //auth 비밀번호로 인증
OK
```

- 레디스는 기본적으로 key-value chain형태 (RDS는 테이블 형태, 레디스는 선형구조이므로 체인으로 연결됨)

```
127.0.0.1:6379> SET mykey "Hello"
OK
127.0.0.1:6379> GET mykey
"Hello"
127.0.0.1:6379>

//session을 저장하는 경우 접두사를 넣어 구분해주면 나중에 데이터를 볼 때 쉬워짐
127.0.0.1:6379> SET session:session_name_1 "mysession_data"
OK
127.0.0.1:6379> SET session:session_name_2 "mysession_data2"
OK
127.0.0.1:6379> GET session:session_name_1
"mysession_data"

//json포맷으로 세션 활용
127.0.0.1:6379> SET session:session_name_3 "{\"userId\":\"id3\",\"auth_level\":2}" EX 10 //EX 10은 만료시간
OK
127.0.0.1:6379> get session:session_name_3
"{\"userId\":\"id3\",\"auth_level\":2}"
```

### Pub/Sub

- 여러 대의 서버를 사용할 때, 각각의 서버에서 공통적으로 파일을 보관해야 하는 경우 유용함

  > 하나의 공통 스토리지가 있고, 10대의 서버가 있고, 각각의 서버는 하나의 레디스 서버에서 구독함.
  >
  > 사용자가 그중 하나의 서버에 접속하여 이미지를 올리면, 해당 서버는 공용 스토리지에 이미지 파일을 업로드 하고, 레디스에 이 사실을 알림(publish). 그러면 구독 중이던 모든 서버로 해당사항은 즉시 알려지고, 모든 서버는 해당 파일을 다운로드하여 저장.

```
//여러개의 콘솔창 필요
redis-cli
127.0.0.1:6379> auth somepassword
OK
127.0.0.1:6379> subscribe pushnoti //pushnoti라는 이름의 새로운 채널을 구독하는 명령 -각 콘솔창마다 실행
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "pushnoti"
3) (integer) 1 

127.0.0.1:6379> publish pushnoti msg 
(integer) 2 //두개의 콘솔창에서 데이터를 받음을 알 수 있음

//다른 콘솔창에서의 화면
127.0.0.1:6379> subscribe pushnoti
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "pushnoti"
3) (integer) 1
1) "message"
2) "pushnoti"
3) "msg" //해당 메시지가 추가됨
```



### Node.js에서 레디스 사용

```
npm install redis
```

```js
const redis = require("redis"), client = redis.createClient(6379, '127.0.0.1');
client.auth("somepassword"); //비밀번호설정
//데이터 저장
client.set("item:abc", "some val", 'ex', 10, (err, result)=>{
    console.log("Result: ");
    console.log(result);
});
//만료시간이 있는 데이터 저장
client.setex("item:abc", 100, "some val", (err, result)=>{
    console.log("Result: ");
    console.log(result);
});

//결과
Result:
OK
Result:
OK

//Pub/Sub
const redis = require("redis"), client = redis.createClient(6379, '127.0.0.1');
client.auth("somepassword");
//subscribe(구독))
client.on("subscribe", (channel, message)=>{
    console.log("client subscribe channel" + channel);
});
client.on("message", (channel, message)=>{
    console.log("client message channel" + channel +":" + message);
});
client.subscribe("pushnoti");

//다른 콘솔창에서 publish pushnoti msg를 실행하면
client message channelpushnoti:msg //다음과 같은 결과가 나옴

//Redis-Pub:Sub2.js
//pusblish
const redis = require("redis"), client= redis.createClient(6379, '127.0.0.1');
client.auth("somepassword");
client.publish("pushnoti", "I am Sending my last message.");

//실행시 
1) "message"
2) "pushnoti"
3) "I am Sending my last message."

//client message channelpushnoti:I am Sending my last message. => Redis-Pub:Sub.js
```

