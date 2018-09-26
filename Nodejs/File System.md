# 파일 사용 - file system

```js
const fs = require('fs');

//콜백형태로 성공/실패 리턴 => 콜백으로 리턴하는 이유: 디스크 자원을 참조해 느리기 때문
fs.unlink('/hello', (err) => {
    if( err ) throw err;
    console.log("successfully deleted /hello");
});

//파일에 기록하는 방법1 - writeFile 사용: 단순하게 기존 파일이 있으면 대체, 없으면 새로 생성
const fs2 = require('fs');
fs2.writeFile('test.txt', 'hello world2', (err) => {
    if(err) throw err;
    console.log('File wirte compledted');
});

//파일에 기록하는 방법2 - open과 write사용
const fs3 = require('fs');
//test.txt파일을 쓸 수 있게 핸들을 엶
fs.open('test.txt', 'w', (err, fd)=>{
    //실패 시 err리턴, 성공시 fd라는 핸들 리턴
    if(err) throw err;
    //파일에 쓰기를 수행합니다.
    fs3.write(fd, "hello world", (err, written) => {
        //실패시에는 err를 리턴하며, 성공 시에는 기록된 바이트 수를 리턴합니다.
        if (err) throw err;
        console.log( written + "bytes Written");
        
        fs3.close(fd,()=>{
            console.log('Done');
        });
    });
});

//파일에 기록하는 방법3 - update로 문자 바꾸기
//주의사항: open시에 'w'가 아닌 'a'로 열어야 초기화되지 않음
//position 4(o)위치에 Update가 찍힘
const fs4 = require('fs');

//test.txt파일을 쓸 수 있게 핸들을 엶
fs.open('test.txt', 'a', (err, fd) => {
    //실패 시에는 err를 리턴하며 성공 시에는 fd라는 핸들을 리턴
    if (err) throw err;

    //파일에 쓰기를 수행함
    fs.write(fd, "Update" , 4, (err, written) => {
        //실패 시에는 err리턴, 성공시에는 기록된 바이트 수 리턴
        if (err) throw err;

        console.log(written + "bytes Written");

        fs4.close(fd, ()=>{
            console.log('Done');
        });
    });
});
```

## Stream

- 콜백 처리 중에 해당파일에 대한 액세스 혹은 쓰기 명령을 추가하면 충돌 발생
- DB, 네트워크에서 여러 프로세스가 동시에 액세스하고 수정하는 과정에서의 문제점 해결을 위한 방법

```js
//파일모듈 선언
const fs5 = requrie('fs');
//data.txt라는 파일을 쓰기 위한 핸들을 엶
const fd = fs.createWriteStream('data.txt', {flag: 'w'});

//파일 핸들이 생성되면 콜백을 반환
fd.on('open', ()=>{
    //파일을 열고 Data라고 기록
    fd.write("Data");

    //파일을 닫음
    fd.end(() => {
        //파일을 닫은 뒤 END출력
        consoel.log("END");
    });
});
```

- 기존의 방법과의 차이: 기존-콜백함수로 부터 파일이 열렸음을 통지받음. stream-이벤트로부터 파일이 열렸음을 통지받음
- 주의사항: Node.js는 싱글스레드에 의해 이벤트루프가 돌아감 => 대용량 파일을 입출력할때 다른 이벤트는 대기하게 됨 => 멀티 쓰레드 이용해야함!!

## 그 외의 파일 사용법

```js
//파일 삭제 unlink
const fs = rquire('fs');
fs.unlink('results.txt', ()=>{
    console.log('file unlinked'):
});

//파일 이동/이름변경(rename)
fs.rename('oldname.png', 'newname.png', function(){
    consoel.log('file renaemd');
});

//파일의 정보읽기(stat) 파일이 존재하지 않을경우 err
fs.stat('tempnewname.png', (err, stats)=> {
    if(err){
        console.log(err);
        return;
    }
    console.log(stats);
});

//파일 검사하기(watch) 파일의 변경이벤트 감지해서 특정작업을 함

//디렉터리 관리하기
//mkdir
fs.mkdir('tempdir', (e) =>{
    if(e){
        throw e;
    }
    console.log('Created!', e);
});
//디렉터리 내의 목록 읽기 readdir
fs.readdir('tempdir', (err, files)=>{
    if(err){
        throw err;
    }
    console.log(files);
});
//파일 삭제 rmdir
//주의사항: 비어있는 디렉터리가 아닐 경우 파일을 먼저 삭제한 후 실행해야 에러가 안남
fs.rmdir('tempdir',(err, files) => {
    if(err){
        throw err;
    }
    console.log(err);
});

```

