# Callback함수

- Node.js는 이벤트 드리븐 방식
- 이벤트 호출 방식
  - on메서드로 이벤트호출
  - 함수 내에서 자체적으로 이벤트 생성

```js
const function_name = new Func();
function_name.on('evnet1', ()=>{
    callback_process1();
}).on('event2', ()=>{
    callback_process2();
});

function_name.startServer();

function_name(some_input, (err, result) => {
    process_function();
});
```

#### Callback 함수의 문제점과 해결책

- 콜백함수

  - 이벤트를 수신하는 형태의 콜백함수
  - 작업을 처리하고 해당 작업이 끝난 뒤 돌려받는 콜백함수

- 콜백 지옥

  - 파일을 열고, 네트워크를열고, DB접속 과정에서 구문이 중첩되어 정신없는 코드가 되어버림

    ```js
    handleOpen((hd)=>{
        hd.handleProcess((err,reuslt)=>{
            if(err){
                console.error(err);
                handleClose(hd);
                return;
            }
            someProcess(result);
            handleClose(hd);
        });
    });
    ```

  - 해결책

    - promise
    - await
    - async모듈로 함수화

    ```js
    /특별한 처리를 하지 않은 코드
    const func = ()=>{
        console.log("process1");
        setTimeout(()=>{
            console.log("process2");
            setTimeout(()=>{
                console.log("process ended");
            },1000);
        },1000);
    };
    func();
    
    //함수화하여 콜백지옥 탈출
    //코드가 길어지긴했지만 가독성이 좋아짐
    const func =()=>{
        console.log("process1");
        func2();
    };
    
    const func2 =()=>{
        setTimeout(()=>{
            console.log("process2");
            func3();
        },1000);
    };
    
    const func3 = () =>{
        setTimeout(()=>{
            console.log("process ended");
        },1000);
    };
    func();
    ```

    ```js
    //병렬화에도 장점
    //func2를 10번 실행. 비동기함수들은 일반적으로 for문을 사용하기 어려움
    //순차적으로 동작시키면 for문 없이 for문 효과를 냄
    const func = ()=>{
        console.log("process 1");
    };
    
    let func2_count = 0;
    const func2 = ()=>{
        if(func2_count == 10){
            func3();
            return;
        }
        func2_count++;
        setTimeout(()=>{
            console.log('process %d', func2_count);
            func2();
        },1000);
    };
    
    const func3 = ()=>{
        setTimeout(()=>{
            console.log("process ended");
        },1000);
    };
    
    
    //다중 실행
    //for문을 비동기 함수에서 이용하는 경우
    //크롤링 시 웹페이지를 여러개 동시에 가져 올 경우
    const main = ()=>{
        for(let i = 0; i<10; i++){
            Crawling();
        }
    };
    
    const Crawling = () =>{
        setTime(()=>{
            console.log("Get page");
            GetPage();
        },1000);
    };
    
    let page = 0;
    const GetPage = () => {
        console.log("Page Process: %d", page);
        page++;
        if(page == 10){
            console.log("Process Ended");
        }
    };
    
    main();
    ```


