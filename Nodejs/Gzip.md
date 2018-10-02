# Gzip

- 데이터 압축
- 트래픽을 줄이는 가장 손쉬운 방법 - 압축
- 보통 Node.js에서 압축을 하지 않음. 프록시(엔진엑스)나 로드밸런스, CDN을 거치면서 압축됨
- 업로드한 텍스트 데이터의 양이 방대할 경우, 사용하지 않는 파일을 압축해 필요시 해제하여 사용하면 효율이 좋아짐

## zlib활용

- http://nodejs.org/dist/latest-v6.x/docs/api/all.html 에 접속한뒤 다른이름으로 저장으로 파일을 다운로드함

```js
//zlib.js
const http = require('http');
const zlib = require('zlib');
const fs = require('fs');

const server = http.createServer((req, res) =>{
    //동기 방식으로 파일을 불러옴 - 파일이름이 정확해야함!
    const output = fs.readFileSync('About this Documentation _ Node.js v6.14.4 Documentation.htm', 'utf8');
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    //압축 방식 목록을 헤더에 추가하여 보냄. gzip, deflate, 크롬은 sdch가 추가됨
    let acceptEncoding = req.headers["accept-encoding"];
    if(!acceptEncoding){
        acceptEncoding = '';
    }

    //작은 파일일 경우 deflate가 유리함
    if(acceptEncoding.indexOf("deflate") > -1){
        //문자열을 입력받아 deflate함수를 하용해 압축한 뒤 콜백으로 넘김
        zlib.deflate(output, (err, buffer) => {
            if(err){
                res.end(output);
                return;
            }
            res.setHeader('Content-Encoidng', 'deflate');
            res.end(buffer);
        });
    }else if(acceptEncoding.indexOf("gzip") > -1){
        zlib.gzip(output, (err, buffer) =>{
            if(err){
                res.end(output);
                return;
            }
            res.setHeader('Content-Encoding', 'gzip');
            res.end(buffer);
        });
    }else{
        res.end(output);
    }
});

server.listen(8080, (err) => {
    if(err){
        console.log(err);
    }
    console.log('Server Running');
});

//zlib.js를 실행시킨 뒤 localhost:8080으로 접속하면 해당 페이지를 다운받을 수 있음
```