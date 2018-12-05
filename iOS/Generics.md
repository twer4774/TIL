# 제너릭(Generics)

http://minsone.github.io/mac/ios/swift-generics-summary

- 코드를 유연하게 작성할 수 있고, 재사용가능한 함수와 타입이 어떤 타입과 작업할 수 있도록 요구사항을 정의
- 중복을 피하고 의도를 명확하게 표현하고, 추상적인 방법으로 코드를 작성할 수 있음

```swift
/* 제너릭을 사용하지 않을 때 */
//숫자 Swap
func swapTwoInts(inout a: Int, inout b: Int){
    let temporaryA = a
    a = b
    b = temporaryA
}
var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)
print(" \(someInt), \(anotherInt)") // 107, 3

//문자열 Swap
func swapTwoStrings(inout a: String, inout: b: String){
    let temporaryA = a
    a = b
    b = temporaryA
}

func swapTwoDoubles(inout a: Double, inout b: Double){
    let temporaryA = a
    a = b
    b = temporaryA
}

/* 제너릭 함수를 사용한 경우*/
func swapTwoValues<T>(inout a: T, inout b: T){
    let temporaryA = a
    a = b
    b = temporaryA
}
```

- 제너릭 함수는 타입을 <>로 감싼다

```swift
func swapTwoInts(inout a: Int, inout b: Int)
func swapTwoValues<T>(inout a: T, inout b: T)
```



```swift
var someInt = 3
var anotherInt = 107
swapTwoValues(&someInt, &anotherInt) //107, 3

var someString = "hello"
var anotherString = "world"
swapTwoValues(&someString, &anotherStirng) //world, hello
```

