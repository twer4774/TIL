# 크롤링 서버 만들기

- 단순하게 웹 사이트, API를 읽어오는 데몬을 만듦
- 파일 형태로 간단하게 데이터 저장시킴
- Nodejs.org 크롤링
- nodes.org - 문서 - 아무버전이나 들어감 - 상단메뉴에 View as JSON링크로 들어감

```js
const https = require('https');

//가져온 데이터를 담는 변수를 선언
let CrawlData = [];

//해당 URL에서 데이터를 가져옴
https.get('https://nodejs.org/dist/latest-v8.x/docs/api/index.json',(res) =>{
    let body = '';
    res.on('data', (d) => {
        body += d;
    });
    res.on('end', () =>{
        //가져온 데이터를 JSON Object 형태로 변환하여 저장
        let index_data = JSON.parse(body).desc;
        //루프를 돌면서 페이지 데이터를 가져옴
        for(let i = 0; i<index_data.length;i++){
            //해당 데이터의 type이 text일 경우에만 데이터 분석
            if(index_data[i].type == 'text'){
                let str = index_data[i].text;
                str = str.substr(str.indexOf("[")+1);
                let temp_idx = str.indexOf("]");
                let title = str.substr( 0, temp_idx);
                
                str = str.substr(temp_idx + 1);
                let link = str.slice(1, -1);

                CrawlData.push({
                    'title': title,
                    'link': link
                });
            }
        }
        //얻은 데이터를 화면에 출력
        console.log(CrawlData);
    });
}).on('error', (e) => {
    console.log("Error:", e);
});
```



## 개별 링크를 통해 데이터를 가져오기

```js
const https = require('https');

//가져온 데이터를 담는변수 선언
let CrawlData = [ { title: 'File System', link: 'fs.json', methods: [] } ];

const url = 'https://nodejs.org/dist/latest-v8.x/docs/api/';
//해당 URL에서 데이터를 가져옴
https.get( url + CrawlData[0].link, (res) => {
    let body = '';
    res.on('data', (d) => {
        body += d;
    });
    res.on('end', () => {
        //가져온 데이터를 JSON Object 형태로 변환하여 저장
        let index_data = JSON.parse(body).modules[0].methods;

        //루프를 돌면서 메서드를 하나씩 확인
        for( let i = 0; i < index_data.length; i++){
            //개별 메서드에 대해서 필요한 만큼의 데이터를 읽어서 저장
            CrawlData[0].methods.push({
                textRaw: index_data[i].textRaw,
                desc: index_data[i].desc,
                signature: index_data[i].signature
            });
        }

        //화면에 출력
        console.log(CrawlData);
    });
}).on('error', (e) => {
    console.log("Error:", e);
});
```



## 전체 통합코드

```js
const https = require('https');

//가져온 데이터를 담는 변수를 선언
let CrawlData = [];

const url = 'https://nodejs.org/dist/latest-v8.x/docs/api/';

//해당 URL에서 데이터를 가져옴
https.get(url + 'index.json', (res) => {
    let body = '';
    res.on('data',(d)=>{
        body += d;
    });
    res.on('end', () => {
        //가져온 데이터를 JSON Object로 변환하여 저장
        let index_data = JSON.parse( body ).desc;

        //루프를 돌면서 페이지 데이터를 가져옴
        for(let i = 0; i < index_data.length; i++){
            //해당 데이터의 type이 text일 경우에만 데이터를 분석
            if(index_data[i].type == 'text'){
                let str = index_data[i].text;
                str = str.substr(str.indexOf("[") + 1);
                let temp_idx = str.indexOf("]");
                let title = str.substr(0, temp_idx);

                str = str.substr(temp_idx + 1);
                let link = str.slice(1, -1).replace(".html", ".json");

                CrawlData.push({
                    'title': title,
                    'link': link,
                    'methods': []
                });
            }
        }

        //얻은 데이터를 화면에 출력
        setTimeout(() => {
            GetMethod();
        }, 1000);
    });
}).on('error', (e) =>{
    console.log("Error:",e);
});
//해당 URL에서 데이터를 가져옴
let page_idx = 0;
const GetMethod =() => {
    console.log("Get methods");
    https.get(url + CrawlData[page_idx].link, (res) => {
        let body = '';
        res.on('data', (d) => {
            body += d;
        });
        res.on('end', () => {
            //가져온 데이터를 JSON Object형태로 저장
            const temp = JSON.parse(body);

            //메서드를 사용하기 힘든 데이터는 저장히지 않음
            if(!temp || !temp.modules || temp.modules.length == 0 || !temp.modules[0].methods){
                page_idx++;
                setTimeout(() => {
                    GetMethod();
                }, 1000);
                return;
            }
            let index_data = temp.modules[0].methods;

            //루프를 돌면서 메서드를 하나씩 확인
            for(let i = 0; i < index_data.length; i++){
                //개별 메서드에 대해서 필요한 만큼의 데이터를 읽어서 저장

                CrawlData[page_idx].methods.push({
                    textRaw: index_data[i].textRaw,
                    desc: index_data[i].desc,
                    signature: index_data[i].signature
                });
            }

            //데이터를 불러오고 나면 다시 한 번 호출
            if(page_idx < CrawlData.length -1 ){
                page_idx++;
                setTimeout(function(){
                    GetMethod();
                },1000);
            } else {
                //화면으로 출력
                console.log(CrawlData);
            }
        });
    }).on('error', (e)=>{
        console.log("Error",e);
    });
};
```

- 개별 페이지에서 데이터를 가져오는 부분을 함수화하여 루프를 돌면서 가져옴
- 가져올 필요가 없거나 혹은 데이터가 없는 부분들에 대해서는 데이터를 저장하지 않고 실제로 저장한 부분만 따로 저장
- 서버에 마구잡이로 요청하면 안되므로(해킹공격), 일정시간을 두고 다음 페이지 요청 -> setTimeout이용