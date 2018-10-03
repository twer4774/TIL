# URL Route

## 요청의 형태와 방식

- GET

  - 클라이언트가 데이터 요청 - 서버는 조건에 맞게 찾아서 반환

  - 키=값, 연결은 &

    - 쿼리에서 ?name=myname&key=value

  - ```js
    const url = require('url');
    let url_str = "http://user:pass@host.com:8080/p/a/t/h?query=string#hash";
    console.log(url.parse(url_str));
    
    //결과
    Url {
      protocol: 'http:',
      slashes: true,
      auth: 'user:pass',
      host: 'host.com:8080',
      port: '8080',
      hostname: 'host.com',
      hash: '#hash',
      search: '?query=string',
      query: 'query=string',
      pathname: '/p/a/t/h',
      path: '/p/a/t/h?query=string',
      href: 'http://user:pass@host.com:8080/p/a/t/h?query=string#hash' }
    
    //쿼리문자열 사용
    const url = require('url');
    const querystring = require('querystring');
    let url_str = "http://user:pass@host.com:8080/p/a/t/h?query=string&key=vlaue#hash";
    let Parse_url = url.parse(url_str);
    console.log(Parse_url);
    
    let Query = querystring.parse(Parse_url.query);
    console.log(Query);
    
    //결과
    Url {
      protocol: 'http:',
      slashes: true,
      auth: 'user:pass',
      host: 'host.com:8080',
      port: '8080',
      hostname: 'host.com',
      hash: '#hash',
      search: '?query=string&key=vlaue',
      query: 'query=string&key=vlaue',
      pathname: '/p/a/t/h',
      path: '/p/a/t/h?query=string&key=vlaue',
      href:
       'http://user:pass@host.com:8080/p/a/t/h?query=string&key=vlaue#hash' }
    { query: 'string', key: 'vlaue' }
    ```

- POST

- REST => PUT, DELETE

```html
<!--POST와 GET구분해서 받기-->
<html>
    <body>
        <form method="post" action="http://127.0.0.1:8080/" target="_target">
            <input name="test">
            <button type="submit">POST</button>
        </form>
        <form method="get" action="http://127.0.0.1:8080/" target="_target">
            <input name="test">
            <button type="submit">GET</button>
        </form>
    </body>
</html>
```



```js
//POST와 GET구분해서 받기
const http = require('http');
const server = http.createServer((req, res) => {
    console.log(req.url);
    console.log(req.method);

    res.statusCode = 200;

    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello World');
});

server.listen(8080, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Sever running');
});

//결과
/
POST
/favicon.ico
GET
/?test=afdf
GET
/favicon.ico
GET
```



#### GET, POST를 구분해 데이터를 받는 방법

```js
const http = require('http');
const url = require('url');
const qs = require('querystring');

const server = http.createServer((req, res) => {

    let Url_data = url.parse(req.url);
    let pathname = Url_data.pathname;
    let query = qs.parse(Url_data.query);

    if(req.method == 'GET'){
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end("현재 GET Method 페이지의 pathname은 "+pathname+"이며 query는"+JSON.stringify(query)+"입니다.");
        return;
        //post의 경우 무제한 데이터를 받아 들일 수 있음
    } else if(req.method == 'POST'){
        let post_data = "";
        req.on('data',(chunk)=>{
            post_data += chunk;
        }).on('end',()=>{
            let post_query = qs.parse(post_data);
            res.statusCode=200;
            res.setHeader('Content-Type', ' text/plain');
            res.end("현재 POST Method페이지의 pathname은 " + pathname +"이며 query는 " + JSON.stringifypost_query+"입니다");

        });
    } else {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Unknown Method');
    }
});

server.listen(8080, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Sever running');
});
```

```html
<!--파일 업로드 가능-->
<html>
    <body>
        <form method="post" action="http://127.0.0.1:8080/" target="_target" enctype="multipart/form-data">
            <input type="file" name="fileToUpload" id="fileToUpload"><br/>
            <input name="test">
            <button type="submit">POST</button>
        </form>
        <form method="get" action="http://127.0.0.1:8080/" target="_target">
            <input name="test">
            <button type="submit">GET</button>
        </form>
    </body>
</html>
```

```js
//업로드한 파일을 서버에서 받는 내용

const url = require('url');
const http = require('http');
const qs = require('querystring');

const server = http.createServer((req, res)=>{
    let Url_data = url.parse(req.url);
    let pathname = Url_data.pathname;
    let query = qs.parse(Url_data.query);
    if(req.method == 'GET'){
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/palin');
        res.end("현재 GET Method페이지의 pathnamedms "+pathname+" 이며 query는" +JSON.stringify(query)+"입니다");
    }else if (req.method == 'POST'){
        let raw_post_data = "";

        req.on('data', (chunk) =>{
            if(raw_post_data.length > 1000 * 1000 * 200){
                req.connection.destroy();
                return;
            }
            raw_post_data += chunk;
        }).on('end', ()=>{
            if (req.headers['content-type'] && req.headers['content-type'].split(";")[0]=='multipart/form-data'){
                let boundary = req.headers['content-type'].split(";")[ 1 ].split("=")[ 1 ];

                let data_parts = raw_post_data.split( "--"+boundary );
                data_parts.shift();
                data_parts.pop();

                let post_data = {};
                let file_data = {};

                for(let i = 0; i < data_parts.length; i++){
                    let data_parts_str = data_parts[i];
                    let item_value = {};

                    const GetLine = () => {
                        let str_pos = data_parts_str.indexOf("\r\n");
                        let temp_str = data_parts_str.slice(0, str_pos);
                        data_parts_str = data_parts_str.slice(str_pos+"\r\n".length);
                        return temp_str;
                    };

                    GetLine();

                    let content_disposition = GetLine();
                    content_disposition = content_disposition.split(";").map((item)=>{
                        let temp = item.trim().split("=");
                        if(temp.length == 2){
                            item_value[temp[0]] = temp[1].slice(1, -1);
                        }
                    });

                    if( item_value.filename ){
						item_value['Content-Type'] = GetLine().split(": ")[ 1 ];
						GetLine();
						item_value['data'] = data_parts_str.slice( 0 , -2 );

						file_data[ item_value['name'] ] = item_value;
						delete file_data[ item_value['name'] ].name;
					}else{
						GetLine();
						post_data[ item_value['name'] ] = GetLine();
					}
				}

                console.log("post_data: ", post_data);
                console.log("file_data: ", file_data);

                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/plain');
                res.end("현재 POST Method페이지 pathname은 " +pathname+" 이며 query는 " + JSON.stringify(post_data)+"입니다.");
            }else{
                let post_query = qs.parse(raw_post_data);
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/plain');
                res.end("현재 POST Method페이지의 pathname은 " +pathname+"이며 query는 " + JSON.stringify(post_query)+"입니다.");
            }
        });
    } else {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Unknown Method');
    }
});
server.listen(8080, (err)=>{
    if(err){
        console.log(err);
    }
    console.log('Server Running');
});
```



## 요청에 따른 분류 방법

- 주소에 입력한 값에 따라 서버가 사용자에게 결과물을 어떻게 보여주는가(POST, GET처럼 분류됨)

```js
const url = require('url');
const http = require('http');

const server = http.createServer((req, res)=>{
    let Ulr_data = url.parse(req.url);
    let pathname = Ulr_data.pathname;

    let url_pathname = url.parse(req.url).pathname;
    let url_route = url_pathname.split("/");
    if(url_route.length < 2 || url_pathname == '/'){
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('index');
        return;
    }

    let statusCode = 200;
    let Header = {
        'Content-Type': 'text/plain; charset=utf-8'
    };

    let output = "";

    switch(url_route[1]){
        case 'board':
        let userId = url_route[2];
        let boardName = url_route[3];
        output = "사용자명은 "+userId+"이며, 게시판명은 " +boardName+"입니다.";
        break;
        default:
            statusCode = 404;
            output = "404 File Not Found";
    }

    //위의 스위치코드는 함수로 만들 수 있음 => 가독성이 좋아짐
    // const Case1_route = (req, res) =>{
    //     res.statusCode = 200;
    //     res.setHeader('Content-Type', 'text/plain');
    //     res.end('Case1_route');
    // };
    // const Case2_route = (req, res) =>{
    //     res.statusCode = 200;
    //     res.setHeader('Content-Type', 'text/plain');
    //     res.end('Case2_route');
    // };
    // const Case3_route = (req, res) =>{
    //     res.statusCode = 200;
    //     res.setHeader('Content-Type', 'text/plain');
    //     res.end('Case3_route');
    // };

    res.writeHead(statusCode, Header);
    res.end(output);
});

server.listen(8080, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Sever Running');
});
```

