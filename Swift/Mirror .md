# Mirror

swift2 이후에 거의 사용되지 않는 방법인 것 같음

런타임 도중에 값을 표현하는 Standard Library중 하나

Debugging과 Reflection 방법 중 Reflection하는 방법

> A representation of the substructure and display style of an instance of any type.

모든 타입 인스턴스의 표현 스타일, 하위구조를 표현해주는 구조체

- 저장프로퍼티, 콜렉션, 튜플 등의 인스턴스 파트를 표현해 줌
- display style 프로퍼티는 어떻게 미러가 렌더링 되는지 알려줌
- 예를들어 dump(\_:\_:\_:\_:)함수를 거치는 인스턴스가 있다면, 인스턴스의 런타임 내용을 렌더링하는데 미러가 이용됨

```swift
struct Point {
    let x: Int, y: Int
}

let p = Point(x: 21: y: 30)
print(String(reflecting: p))
// Prints "▿ Point
//           - x: 21
//           - y: 30"
```

- 인스턴스 속성 중 childern은 child 요소들의 콜렉션을 구조체 형태로 반영함