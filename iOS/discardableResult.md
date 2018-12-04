# @discardableResult

- 리턴 값을 별도로 사용하지 않는 경우 경고 뜨는 것을 없앨 수 있다.

```swift
//함수에 리턴값이 있지만, 사용하지 않는 경우 처리 방법1
func funcDiscardableResult() -> String{
    return "출력"
}
_ = funcDiscardableResult() //출력

//리턴 값을 별도로 사용하지 않는다면 아래와 같이 선언 방법2
@discardableResult
func funcDiscardableResult() -> String{
    return "출력"
}
funcDiscardableResult() //"출력"

//방법2의 다른 예
@discardableResult
func printMessage(message: String) -> String{
    let outputMessage = "Output : \(message)"
    print(outputMessage)
    
    return outputMessage
}
printMessage(messge: "Hello Swift")
```

