# String & Number

## String

```js
//문자열 개수 세기 .length
const string = 'hello';

console.log('string:', string.lenght);
console.log('string[0]', string[0]); //주의 배열은 0부터시작한다.

//해당 문자열 찾기 indexOf() 값이 없으면 -1 리턴함
const string = 'hello';
const string2 = 'helelelelelelllo';

console.log('hel:', string.indexOf('hel')); //hel: 0
console.log('el:', string.indexOf('el')); //el: 1
console.log('elelelel:', string2.indexOf('el')); //elelelel: 1 //첫번째 위치 리턴
```

## Number

```js
//문자와 숫자
const string10 = '10';
const string20 = '20';
const number10 = 10;
const number20 = 20;

console.log('string:%s', string10 + string20);
console.log('number:%d', number10 + number20);
console.log('string + number:%s', string10 + string20 );

//숫자인지 판단하기 .isNaN()
const isNaN123 = isNaN(123);
const isNaNMinus123 = isNaN(-123);
const isNaN234 = isNaN('234');
const isNaNHello = isNaN('hello');

console.log('isNaN123:', isNaN123);
console.log('isNaNMinus123:', isNaNMinus123);
console.log('isNaN234:', isNaN234);
console.log('isNaHello:', isNaNHello);
```