# JSON

- JavaScript Object Notation(자바스크립트 오브젝트 노테이션)의 약자
- 자바스크립트에서 오브젝트를 표현하는 방법
- 데이터를 처리하는데 효율적

```js
const user = {};
user.name = 'wonik';
user.age = 28;

console.log(user); //{ name: 'wonik', age: 28 }

const user2 = { name: 'wonik', age: 28 };
console.log(user2); //{ name: 'wonik', age: 28 }


//JSON에서 값 뽑기, 필드 추가하기
const user3 = { name: 'wonik', age: 28 };
console.log('user:', user3); //user: { name: 'wonik', age: 28 }
console.log('user.name:', user3.name); //user.name: wonik
console.log('user.age:', user3.age); //user.age: 28

user3.job = 'developer'; 
user3.nation = 'korea';
console.log(user3); //{ name: 'wonik', age: 28, job: 'developer', nation: 'korea' }

const memberName = 'age';
console.log(user[memberName]); //28
```

