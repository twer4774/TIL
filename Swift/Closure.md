# 클로저

일회용 함수를 작성할 수 있는 구문 => 익명함수, 람다함수

1. 전역 함수 : 이름이 있으며, 주변환경에서 캡처할 어떤 값도 없는 클로저
2. 중첩 함수 : 이름이 있으며, 자신을 둘러싼 함수로부터 값을 캡처할 수 있는 클로저
3. 클로저 표현식 : 이름이 없으며, 주변환경으로부터 값을 캡처할 수 있는 경량 문법으로 작성된 클로저

 

## 클로저 표현식

```swift
{ (매개변수) -> 반환 타입 in 실행할 구문 }

let c = { (s1: Int, s2: String) -> Void in
    print("s1: \(s1), s2: \(s2)")
}
c(1, "closure")


```

 

## 클로저 표현식과 경량 문법

```swift
var value = [1, 9, 5, 7, 3, 2]
 

//1.
value.sort(by: { (s1: Int, s2: Int) -> Bool in
    if s1 > s2 {
        return true
    } else {
        return false
    }
}) 
//[9, 7, 5, 3, 2, 1]

 
//2.
value.sort(by:{ (s1: Int, s2: Int) -> Bool in
    return s1 > s2
})

//3.
value.sort(by: {(s1, s2) in return s1 > s2})

//4.
value.sort(by: { $0 > $1})
```

 

 

## 트레일링 클로저

함수의 마지막 인자 값이 클로저일 때, 인자 값 형식으로 작성하는 대신, 함수의 뒤에 꼬리처럼 붙일 수 있는 문법

```swift
value.sort() { (s1, s2) in return s1 > s2 }
```

 



## @escaping

인자 값으로 전달된 클로저를 저장해 두었다가, 나중에 다른 곳에서도 실행 할 수 있도록 허용해주는 속성

```swift
func callback(fn: @escaping () -> Void){
    let f = fn //클로저를 상수 f에 대입
    f() //대입된 클로저 실행
}
callback {
    print("closure가 실행 되었습니다.")
}
```

 원래 클로저의 기본속성은 탈출 불가하게 관리 -> 컴파일러의 코드 최적화의 이유 때문

 

## @autoclosure

인자 값으로 전달된 일반 구문이나 함수 등을 클로저로 래핑하는 역할

=> 일반 구문을 인자 값으로 넣더라도 컴파일러가 알아서 클로저로 사용

'()' 형태로 사용 가능 -> 인자 값을 직접 클로저 형식으로 넣어줄 필요 없음

```swift
func condition(stmt: @autoclosure () -> Bool){
    if stmt() == true{
        print("결과 참")
    } else {
        print("결과 거짓")
    }
}

//실행
condition(stmt: (4 > 2))
```

 