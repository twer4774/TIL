# #ECMAScript6(ES6)

- ECMA라는 국제 기구에서 만든 표준문서의 6번째 개정판
- ES5와 많이 바뀌고, 내용이 2배이상 많아졌음

```javascript
//es5 스타일
function printhelloEs5() {
	console.log('hello es5')
}

//es6 스타일
const printHelloEs6 = () => {
    console.log('hello es6')
}

printHelloEs5(); //hello es5
printHelloEs6(); //hello es6
```

## console

console 이용방법: 디버깅하거나 로그를 남길때 이용함

```javascript
console.log('hello')
console.log('hello','bye') //여러개의 값 출력가능
console.warn(`this line ${'can make error'}`) //`(백틱, Tab위에 문자)으로 감싸면 템플릿처럼 사용할수 있음
```

