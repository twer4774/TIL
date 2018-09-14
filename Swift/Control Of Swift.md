# 흐름제어 구문

종류: 반복문, 조건문, 제어 전달문

 

# 반복문

### For 반복문

for ~ in 구문

```swift
for <루프상수> in <순회대상>{

<실행구문>

}
```

<순회대상> : 배열, 딕셔너리, 집합, 범위데이터, 문자열

 

- 문자열에서 문자 추출

```swift
var lang = "swift"

for char in lang.characters{

print("\(char)")

}
```

 

- 루프상수를 _ 로 설정

```swift
let size = 5

let padChar = "0"

var keyword = "3"

for _ in 1...size{

keyword = padChar + keyword

}

print("\(keyword)")

// 000003
```

### while 구문 : 조건을 만족하는 동안은 계속 실행

사용하는 경우

- 실행 횟수가 명확하지 않을 때
- 직접 실행해보기 전까진 실행 횟수를 알 수 없을때
- 실행횟수를 기반으로 할 수 없는 조건일때

 

 

# 조건문

if, guard, switch

### if문

```swift
if <조건식> { 실행구문 }
```

 

### guard문

if문과의 차이점

- else 블록이 필수
- 표현식의 결과가 참일때 실행되는 블록이 없음

```swift
guard <조건식 또는 표현식> else {

<false일때 실행코드>

}

/*
주로, 후속 코드들이 실행되기 전에, 특정조건을 만족하는지 확인하는 용도

=> 특정조건을 만족하지 않고 후속코드를 실행하면 심각한 오류가 발생하는 경우, 조기종료의 목적으로 이용

코드 중첩이 필요 없음
*/

func divide(base: Int){

guard != 0 else {

print("연산할 수 없습니다.")

return

}

let result = 100/base

print(result)

}



```

 

### #available구문

기기의 os버전별로 구문 작성.

현업에서 'API 버전을 탄다' 라고 함

```swift
if #available(<플랫폼 이름 버전>, <...> , <*>){

<해당 버전에서 사용할 수 있는 API구문>

} else {

<API를 사용할 수 없는 환경에 대한 처리>

}

if #available(ios 9, osx 10, *){

//ios 9용 API 구문, osx 10용 API 구문

} else {

//API를 사용하지 못했을 때에 대한 처리 실패 구문

}
```

### switch 구문

```swift
switch <비교대상>{

case <패턴1>:

<패턴1 처리구문>

case <패턴2>:

<패턴2 처리구문>

default:

<기본 처리 구문>

}
//비교대상이 case에서 모두 처리 가능하다면, default는 생략 가능하다.

//fall through - 패턴이 일치하는 case블록 실행 대신, 그 다음 case 블록으로 실행흐름 전달

let sapmleChar: Character = "a"

switch sampleChar{

case "a":

fall through

case "A":

print("글자는 A")

default:

print("일치하는 글자가 없음")

}

=> 글자는 A

```



## 제어전달문

break, continue, fall through, return

##### break : 조건의 결과와 상관없이 즉각 종료

##### continue: 다음 반복문의 시작

##### 구문 레이블과 break, continue

```swift
<레이블 이름> : while<조건식>{

실행구문

break <레이블 이름> or continue <레이블 이름>

}

outer: for i in 1...5{

//1 에서 5까지 반복

inner: for j in 1...9{

if (j == 3){

break outer

}

//구구단 출력

print("(i) * (j) = (i*j)")

	}

}

```

 

 

 