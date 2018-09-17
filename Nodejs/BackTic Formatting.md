# \`${변수}` 백틱을 이용한 포맷팅

- %s, %d 템플릿보다 백틱 템플릿을 권장함

```js
const greeting1 = 'hello';
const greeting2 = 'bye';
const name1 = 'gildong';
const name2 = 'dooly';

const statement = `${greeting1}! my name is ${name2}`;
const statement2 = `${greeting2}! my name is ${name2}`;

console.log(`${greeting1}! my name is ${name1}`); //hello! my name is gildong
console.log(`${greeting2}! my name is ${name1}`); //bye! my name is gildong
console.log('statement:', statement); //statement: hello! my name is dooly
console.log('statement2:', statement2); //statement2: bye! my name is dooly
```



