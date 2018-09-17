# 변수와 상수

- 선언 한 후 값을 바꿀 수 있는 것이 변수
- es5일 때 작성된 코드는 변수 앞에 let 대신 var를 사용한 예제가 있음 => babel로 호환성문제 해결
- var는 같은 이름의 변수를 선언할 수 있지만, let은 다른 이름으로만 변수 선언 가능 => 버그를 줄 일 수 있음

```js
//변수(variable)의 이용
let fruit = 'apple';
console.log('fruit: ', fruit)
fruit = 'grape'
console.log('fruit:', fruit)
//fruit: apple
//fruit: grape
```

- 상수는 constant를 붙여 사용
- const를 기본으로 사용해 개발하고, 바뀌는 값이면 let으로 바꾸어 주는것이 좋음

```js
let fruit1 = 'apple';
fruit1 = 'banana';
const pi = 3.14;

console.log('fruit1: ', fruit1);
console.log('pi : ', pi)
```

