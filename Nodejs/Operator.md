# 연산자

## Typeof로 변수의 타입 알기

```js
const pi = 3.14;
const name = 'wonik';
console.log('hello : %s', typeof 'hello');
console.log('"20" : %s', typeof '20');;
console.log('pi : %s', typeof pi);
console.log('name : %s', typeof name);
console.log('30 : %s', typeof 30);
console.log('[] : %s', typeof []);
console.log('{} : %s', typeof {});
/*
hello : string
"20" : string
pi : number
name : string
30 : number
[] : object
{} : object
*/
```

## 증감연산자

```js
let number = 1;

console.log('number : ', number);
number += 1;
console.log('after number += 1: ', number); //2
number -= 1;
console.log('after number -=1 :', number); //1
number += 10;
console.log('after number += 10 :', number); //11
number -= 5;
console.log('after number -= 5 :', number); //6
```

## 비교연산자

- == : 단순히 값 비교
- ===: 값과 type을 같이 비교함(숫자 === 문자 => False)

```js
const a = 5;
const b = 6;

if ( a == 5 ) {
    console.log(a == 5); //true
    console.log(a == b); //false
    console.log(a == '5'); //true
}

if ( a === 5 ){
    console.log(a === 5); //true
    console.log(a === b); //ture
    console.log(a === '5'); //eqaul value and equal type //false
}

if (a > b){
    console.log(a > b); //false
}
```

## 논리연산자

```js
const value30 = 30;
const value50 = 50;

const andTrueTrue = value30 >= 30 && value50 >= 30;
const andTrueFalse = value30 >= 30 && value50 >= 100;
const andFalseFalse = value30 >= 40 && value50 >= 100;

const orTrueTrue = value30 >= 30 || value50 >= 30;
const orTrueFalse = value30 >= 30 || value50 >= 100;
const orFalseFalse = value30 >= 40 || value50 >= 100;

console.log('andTrueTrue: ', andTrueTrue);
console.log('andTrueFalse: ', andTrueFalse);
console.log('andFalseFalse: ', andFalseFalse);
console.log('------------------------------')
console.log('orTrueTrue: ', orTrueTrue);
console.log('orTrueFalse: ', orTrueFalse);
console.log('orFalseFalse: ', orFalseFalse);
/*
andTrueTrue:  true
andTrueFalse:  false
andFalseFalse:  false
------------------------------
orTrueTrue:  true
orTrueFalse:  true
orFalseFalse:  false
*/
```

## 삼항연산자

- 결과가 Boolean으로 나오는 식을 한줄로 쓰고 싶을때 이용함 => if .... else 와 같은 기능

```js
const num1 = 1;
const num2 = 2;
const list = [1, 2, 3, 4];
const emptyList = [];

const result = num1 > num2 ? 'nnum1' : 'num2';
console.log(result, '이(가) 더 큽니다.');

list.length > 0 ? console.log(list) : console.log('list가 비었습니다.');
emptyList.length > 0 ? console.log(list) : console.log('list가 비었습니다.');
/*
num2 이(가) 더 큽니다.
[ 1, 2, 3, 4 ]
list가 비었습니다.
*/
```

