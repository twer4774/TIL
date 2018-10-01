# 데이터베이스

#### RDBMS(Relational Database Management System): 관계형 데이터베이스 시스템

MySQL, MariaDB, Oracle

- 정형화된 대량의 데이터를 분석하여 결과를 도출하는데 유리

#### NoSQL

- 비정형화된 데이터를 대량으로 다루거나 매우 빠른 데이터 처리에 유리

레디스(Redis)

- 메모리에 저장

- 빠른 입출력 속도
- 안정적인 성능
- 단점: 문제가 생길 경우 한번에 데이터 손실 가능성 있음



## MySQL

```
npm install mysql
```

```js
const mysql = require('mysql');
//port를 넣지 않을 경우 기본값이 3306이 됨
const connection = mysql.createConnection({
    host : 'localhost',
    user : 'userid',
    password : 'dbpassword',
    database : 'dbname'
});
connection.connect((err) => {
    if (err) {
        console.error('error connecting: ' + err.stack);
        return;
    }
    console.log('connected as id' + connection.threadId);
});

connection.query('SELECT 1 + 1 AS solution', (err, rows, fields)=>{
    if(err) throw err;
    console.log('The solution is: ', rows[0].solution);
});
connection.end();
```



### 풀링

- 여러개의 테이블을 다룰 때 동시에 만은 접속을 해야 함
- 여러개의 연결을 미리 대기 시켜놓고, 새로운 연결을 통해 다른 쿼리 작업 진행
- 풀링이 가득차면 새로운 작업을 할 수 없으므로, 작업이 끝나면 해당 연결을 반환해주는 작업이 필요

```js
const mysql = require('mysql');
const pool = mysql.createPool({
    host :'localhost',
    user: 'userid',
    password: 'dbpassword',
    database: 'dbname',
    connectionLimit: 5
});
for ( let i = 0; i < 6; i++){
    pool.getConnection((err, connection)=>{
        if(err){
            console.log("ERROR:", err);
            return;
        }
        pool.query('SELECT something FROM sometable', (err, rows)=>{
            //데이터를 사용한 작업
            console.log(new Date());
            
            setTiemout(()=> {
                connection.release();
            },3000);


            //현재 작업에서는 DB연결이 끊겨 작업 불가능
        });
    });
}
```



### 쿼리

```js
connection.query('SELECT col1, col2, col3, FROM mytable', (err, rows, fields)=>{
    connection.release();
    if(err){
        //에러가 발생할 경우 에러를 표시하고 종료한다.
        console.error(err);
        return;
    }

    //받은 결과값의 필드 리스트를 보여준다
    console.log(fields);

    //결과물을 출력
    for(let i = 0; i < rows.length; i++){
        console.log("row: ", rows[i]);
    }
});

connection.query('SELECT col1, col2, col3 FROM mytable where col1 =?', ['val'], (err, rows, fields)=>{
    connection.release();
    if(err){
        //에러 발생할 경우 종료
        console.log(err);
        return;
    }

    console.log(fields);
    for(let i = 0; i< rows.length; i++){
        console.log("Row:" , rows[i]);
    }
});

//두 쿼리는 같은 쿼리문
let val_name1 = 'val1';
let val_name2 = 'val1';
connection.query('SELECT col1, col2, col3 FROM mytable where col1 = ? and col2 =?', [val_name1, val_name2]);
connection.query('SELECT co1, col2, col3 FROM mytable where col1 \''+val_name1+'\' and col2 = \''+val_name2+'\'');


//UPDATE, INSERT, DELETE
connection.query('DELETE FROM posts WHERE title = "wrong"', (err, result) => {
    if (err) {
        console.log(err);
        return;
    };
    console.log('result: ', result);
})


connection.query('UPDATE test set col1 = "teable2" WHERE col1 = "table"', (err, result)=>{
    connection.release();

    if(err){
        console.log(err);
        return;
    };
    console.log('result: ', result);
});
```

