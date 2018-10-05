# 함수

독립적으로 처리할 수 있는 부분을 분리하여 구조화한 객체

swift는 함수형 프로그래밍 패러디임을 채택

 

## 함수의 기본 개념

입력 값(인자 값, 파라미터)을 받아 처리과정을 거쳐, 결과 값(반환 값, 리턴 값)을 내어 놓는 형태

- 함수의 이점

- - 재사용성
  - 기능 단위로 함수화하여 가독성과 유지보수 용이

 

## 사용자 정의 함수

```swift
func 함수이름 (매개변수1: 타입, ...) -> 반환타입{
    실행내용
    return 반환값
}
```

 

### 함수의 4가지 형태

```swift
//매개변수와 반환값이 모두 없는 함수

func printHello() {
    print("안녕하세요")
}

 

//매개변수가 없지만 반환값은 있는 함수

func sayHello() -> String{
    let returnValue = "안녕하세요"
    return returnValue
}

 

//매개변수는 있으나 반환값이 없는 함수

func printHelloWithName(name: String){
    print("\(name)님, 안녕하세요")
}

 

//매개변수와 반환값이 모두 있는 함수

func sayHelloWithName(name: String) -> String{
    let returnValue = "\(name)님, 안녕하세요 "
    return returnValue

}
```

 

## 함수의 반환 값과 튜플

여러개의 반환 값 => 집단 자료형(딕셔너리, 배열, 튜플), 구조체, 클래스

```swift
func getIndvInfo()->(Int, String){
    let height = 100
    let name = "원익"
    return (height, name)

}
```

 

실행 결과로 반환되는 튜플의 각 아이템을 변수에 미리 할당 가능

=> 함수를 실행 할 때 결과값을 바인딩 하지 않아도 특정변수명으로 바인딩 된 튜플인자로 사용할 수 있음

```swift
func getUserInfo() -> (h: Int, g: Character, n: String){
    let gender: Character = "M"
    let height = 100
    let name = "원익"
    return (height, gender, name)
}

var result = getUserInfo()
result.h //100
result.g //M
result.n //원익

```

 

## 타입 알리어스

- 새로운 축약형 타입 정의
- 이름이 길거나 사용하기 복잡한 타입표현을 새로운 타입명으로 정의
- typealias 키워드 이용
             typealias <새로운 타입 이름> = <타입 표현>
- 타입 표현을 짧게 줄여 전체적으로 코드가 간결해 짐

```swift
typealias infoResult = (Int, Character, String)
func getUserInfo() -> infoResult{
    let gender: Character = "M"
    let height = 100
    let name = "원익"
    return (height, gender, name)
}
```

 

# 매개변수

## 내부 매개변수명(인자값 참조), 외부 매개변수명(인자값 구분)

func (외부 내부: 타입)

- 외부에서 바라보는 내부의 의미가 다를때 이용
- 내부 매개 변수명이 너무 길때 이용
- Objective-C와의 호환성

 

## 가변 인자

func (매개변수명: 매개변수타입...)

입력된 인자값을 배열로 처리

for ~ in 구문으로 모든 인자값을 순서대로 읽음

```swift
func avg(score: Int...) -> Double{
    var total = 0 //점수 합계
    for r in score { //배열로 입력된 값들을 순회하면서 점수 합산
        total += r
    }
    return (Double(total) / Double(score.count)) //평균값 반환
}

print(avg(score: 10, 20, 30, 40)) //25.0
```

 

## 기본값을 갖는 매개변수 

func 함수이름(매개변수: 매개변수타입 = 기본값) { 실행내용 }

## 매개변수의 수정

함수 내에서 인자 값을 수정 불가능 => 매개상수 ==> 파라미터로 표현하는게 맞음

```swift
func incrementBy(base: Int) -> Int{
    var base = base //변수안에 인자값 넣기
    base += 1
    return base
}
```

1. 함수 내에서 인자 값을 그대로 가져와서 수정하려면 불가능함
2. 변수를 하나 만들어서(var base)      변수에 인자 값을 연산한 값을 할당 시킴
3. 이 방법은 인자 값 자체를 변경한게 아니라 인자 값을 복사하여 원하는 연산을 실행한 것

 

## InOut 매개변수

- 함수 내에서 변경된 인자 값은 외부에 영향을 줄 수 없다
- inout 키워드를 통해 함수 내부에서 수정된 인자 값을 외부까지 전달 가능
             *리터럴, 상수는 inout을 사용할 수 없음(원본객체값을 수정할 수 있어야 해서)
- inout 키워드가 붙으면 인자값이 전달될 때 인자 값 복사 대신, 인자 값 자체를 함수 내부로 전달
             저장된 메모리 주소 전달 -> 포인터와 유사 => 참조에 의한 전달

```swift
func foo(paramCount: inout Int) -> Int{
    paramCount += 1
    return paramCount
}
var count = 30
print(foo(paramCount: &count)) //함수내부에의 paramcount: 31
print(count) //외부에서 정의된 count: 31
```



#### 값에 의한 전달과 참조에 의한 전달

값에 의한 전달 : 인자 값의 경우 복사본을 통해 함수 내부에서 이용. 원본은 그대로 둠

참조에 의한 전달: 

- 함수에서 inout 키워드 이용시 적용. class는 항상 참조에 의한 전달

-> class는 함수의 인자 값으로 전달한 클래스 인스턴스는 함수내부에서 값이 수정되면 원본객체도 수정됨

- 상위 범위에서 정의된 변수는 하위 범위에서도 사용 가능
             함수외부에서 정의된 변수를 함수 내부에서 가져다 사용하면, inout과 같은 효과가 나타남

 

## 변수의 생존 범위와 생존 주기

전역 변수: 프로그램 어디에서나 참조 가능

지역 변수: 생명 주기가 끝난 뒤 소멸

 

## 일급 객체로서의 함수 (First-Class object)

swift는 객체지향 언어이자 동시에 함수형 언어

 

### 일급 함수의 특성

#### 일급 객체의 특성

1.  객체가 런타임에도 생성이 가능해야 한다.
2. 인자 값으로 객체를 전달 할 수 있어야 한다.
3. 반환 값으로 객체를 사용할 수 있어야 한다.
4. 변수나 데이터 구조 안에 저장할 수 있어야 한다.
5. 할당에 사용된 이름과 관계없이 고유한 구별이 가능해야 한다.

 

#### 일급 함수의 특성

```swift
//1. 변수나 상수에 함수를 대입할 수 있음

//정수를 입력 받는 함수
func foo(base: Int) -> String{
    print("foo 실행")
    return "결과값은 \(base + 1)"
}

let fn1 = foo(base: 5) // foo 실행. 결과값은 6 -> 단순히 결과값 대입
let fn2 = foo //foo 실행X. fn2상수에 foo함수 할당
fn2(5)        //foo 실행. 결과값은 6

 

//함수타입: 변,상수에 함수를 대입

//(인자 타입1, 인자 타입2) -> 반환 타입

func boo(age: Int) -> String{ return "\(age)"}

//=> 함수 타입 형태로 표현 (Int) -> String

let fn: (Int) -> String = boo //할당
```

 

 

```swift
//2. 함수의 반환 타입으로 사용할 수 있음
func desc() -> String{
    return "this is desc()"
}
func pass() -> () -> String{
    return desc
}
let p = pass()
p() //"this is desc()"


//사칙연산의 예
func plus(a: Int, b: Int) -> Int{
    return a + b
}
func minus(a: Int, b: Int) -> Int{
    return a - b
}
func times(a: Int, b: Int) -> Int{
    return a * b
}
func divide(a: Int, b: Int) -> Int{
    guard b != 0 else{
        return 0
    }
    return a / b
}

func cals(_ operand: String) -> (Int, Int) -> Int{
    switch operand{
    case "+":
        return plus
    case "-":
        return minus
    case "*":
        return times
    case "/":
        return divide
    default:
        return plus
    }
}

let c = cals("+")
c(3,4) //plus(3,4) = 7
```

```swift
//3. 함수의 인자 값으로 함수를 사용할 수 있음
/*
콜백 함수: 특정 구문의 실행이 끝나면 시스템이 호출 되도록 처리된 함수

콜백 함수 등록: 실행하고자 하는 구문을 담은 함수를 인자 값으로 넣는 것을 의미

함수를 인자 값으로 전달할 때, 함수는 함수타입으로 처리
*/
func incr(param: Int) -> Int{
    return param + 1
}

func broker (base: Int, function fn: (Int) -> Int) -> Int{
    return fn(base)
}
broker(base: 3, function: incr) //4

 

//*단점: 함수를 인자로 사용하면 실행 전까지 어떤 구문이 실행 될지 컴파일러가 미리 알 수 없으므로 컴파일 시점에서 디버깅 할 수 없다


//콜백 함수의 예

func successThrough(){ print("연산처리 성공") }
func failThrough() { print("연산처리 실패") }
func divide(base: Int, success sCallBack: () -> Void, fail fCallBack: () -> Void) -> Int{
    guard base != 0 else {
        fCallBack()
        return 0
    }
    defer {
        sCallBack()
    }
    return 100 / base
}

divide(base: 30, success: successThrough, fail: failThrough)

 
/*
*defer

메소드에서 코드의 흐름과 상관없이 가장 마지막에 실행되는 블록

종료 시점에 처리하는 구문을 사용할때 유용

defer 함수의 특성

1. 작성된 위치에 상관 없이 함수가 종료되기 직전에 실행
2. defer 블록을 읽기 전에 함수의 실행이 종료 될 경우, defer 블록은 실행되지 않는다.
3. 하나의 함수나 메서드내에 여러 defer 선언 가능. 마지막 부터 역순으로 실행됨
4. 중첩 사용 가능 바깥쪽 -> 안쪽 순으로 실행

주로 함수가 연산을 처리하는 과정에 영향을 끼치지 않으면서,

실행해야 할 다른 내용이 있을 때, 함수를 종료하기 직전에 정리해야 하는 변수나 상수 값들을 처리하는 용도로 사용함
*/
 

/*
함수를 인자로 넘기는 방법의 장점

1. 함수 내부코드를 외부에서 간섭 할 수 있음
2. 직접 함수나 메소드의 객체를 전달 할 수 있음
*/
```

 

# 함수의 중첩(Nested Function)

함수의 은닉성을 가짐

```swift
//외부함수
func outer(base: Int) -> String{
    //내부함수
    func inner(inc: Int) -> String {
        return "\(inc) 반환"
    }
    let result = inner(inc: base + 1)
    return result
}

outer(base: 3)
```

outer를 불러오지만, 실제로 inner를 실행하는 코드

외부함수에서 내부함수를 반환하게 되면, 외부함수가 종료되더라도 내부 함수의 생명이 유지됨

=> 외부함수가 내부함수를 반환하면, 외부함수가 종료되더라도 내부함수가 유지됨

```swift
//외부함수
func outer(param: Int)-> (Int) -> String{
    //내부함수
    func inner(inc: Int) -> String {
       return "\(inc) 반환"
    }
       return inner
}
let fn1 = outer(param:3) //outer 실행. 결과로 inner대입
let fn2 = fn1(30)
```

  