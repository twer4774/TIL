# 제어문

## 조건문

### if

```
if(조건문) {
    조건이 참인 경우 실행
} else {
    조건이 거짓인 경우 실행
}
```

```js
if (true) {
    console.log('조건이 true일 때 실행');
}

const number = 100;

if (number >= 100){
    console.log('number는 100보다 큽니다.');
}

if (number > 200){
    console.log('number는 200보다 큽니다.');
}
```

### if ... else

```js
if (true){
    console.log('true');
} else {
    console.log('false');
}
//true
```

### if ... else if ... else

```js
const score = 85; //상수로 선언
let degree = ''; //변수로 선언

if(score >= 90){
    degree = 'A';
} else if (score >= 80){
    degree = 'B';
} else if (score >= 60){
    degree = 'C';
} else {
    degree = 'F';
}
console.log('degree : ', degree); //B
```



## Switch

```js
const number = 3;

let msg = '';
switch (number) {
    case 1:
        msg = '값이 아닙니다.';
        break;
    case 2:
        msg = '값이 아닙니다.';
        break;
    case 3:
        msg = '찾는 값입니다.';
        break;
    default:
}
console.log(msg); //찾는 값입니다.
```



## 반복문

## for

```js
const number = 9;
for (let value = 1; value < 10; value += 1){
    console.log(number * value);
}

//구구단 출력
for (let j = 2; j <= 9; j++){
    console.log('%d단', j );
    for (let i = 1; i <= 9; i++){
        console.log('%d * %d = %d', j, i, j*i);
    }
}

//for문 끝내기 break
const studentList = [
    { name: 'wonik', age: 27, score: 85 },
    { name: 'wonik2', age: 21, score: 35 },
    { name: 'wonik3', age: 23, score: 45 },
    { name: 'wonik4', age: 25, score: 75 },

];

let resultStudent = '';
for (let index = 0; index < studentList.length; index += 1){
    if (studentList[index].name === 'wonik4'){
        resultStudent = studentList[index];
        break;
    }
    console.log(studentList[index].name, '은 wonik4이 아닙니다.');
    /*wonik 은 wonik4이 아닙니다.
	wonik2 은 wonik4이 아닙니다.
	wonik3 은 wonik4이 아닙니다*/
}
console.log('resultStudent :', resultStudent);
//resultStudent : { name: 'wonik4', age: 25, score: 75 }


//for of 개수만큼 반복

const userList = [
    { name: 'wonik', age: 27, score: 85 },
    { name: 'wonik2', age: 21, score: 35 },
    { name: 'wonik3', age: 23, score: 45 },
];
for (const user of userList){
    console.log('user:', user);
}
/*
user: { name: 'wonik', age: 27, score: 85 }
user: { name: 'wonik2', age: 21, score: 35 }
user: { name: 'wonik3', age: 23, score: 45 }
*/

//.forEach()
//값을 하나씩 뽑아서 바로 함수에 넣어서 계산할때 편함
//요소들을 user라는 이름으로 뽑아내고, function(uswer)()에 넣어줌
userList.forEach(function(user){
    console.log(user);
});
console.log('-----------------');

//arrow function
userList.forEach(user => console.log(user));

/*
 name: 'wonik', age: 27, score: 85 }
{ name: 'wonik2', age: 21, score: 35 }
{ name: 'wonik3', age: 23, score: 45 }
*/
```

## while

```js
const number = 9;
let value = 1;

while (value < 10){
    console.log(number * value);
    value += 1;
}
```

- for문은 정해진 횟수가 있을때 사용
- while문은 반복 그 자체에 의미를 두는 경우에 사용 - 조건식만 나타냄