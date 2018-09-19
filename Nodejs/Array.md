# 배열

- 배열의 시작은 0임을 주의해야한다.
- 배열에 값이 없을 때 출력을하면 Undefiened 오류를 출력한다.
- new Array() 초기화 보다 [ ]로 배열을 선언하는 것을 선호한다.
- 배열의 값을 넣을 때 push()를 이용한다.

```js
const numbers = [1, 2, 3];
const strings = ['hello', 'bye', 'welcome'];

//new Array()를 이용하는 방법은 []를 이용하는 방법과 동일. []를 이용하는 방법을 선호함
const numbers2 = new Array(1, 2, 3);
const strings2 = new Array('hello', 'bye', 'welcome');

console.log('numbers : ', numbers); //[1, 2, 3]
console.log('numbers2 : ', numbers2); //[1, 2, 3]
console.log('strings :', strings); //['hello', 'bye', 'welcome']
console.log('string2 : ', strings2); //['hello', 'bye', 'welcome']

//배열에 값 넣기 push()
const arNumbers = [];
arNumbers.push(1);
arNumbers.push(2);

const arTexts = [];
arTexts.push('hello', 'welcome', 'bye'); //여러개의 값 한번에 넣기

console.log(arNumbers); //[1, 2,]
console.log(arTexts); //['hello', 'bye', 'welcome']


//배열 출력하기
const arCoffee = [];
console.log(arCoffee[0]); //배열에 아무것도 없으므로, undefined가 출력됨
console.log(arCoffee.length); //.length를 이용해 개수를 셈 //0

arCoffee.push('아메리카노', '라떼', '카푸치노');
console.log(arCoffee.length);   //3
console.log(arCoffee[0]); //배열의 시작은 0부터 //아메리카노

```

