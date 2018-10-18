# 오류처리

protocol Error{ } 

프로토콜 구현자체가 중요한 경우 => 구현한 열거형(인증마크 역할)은 오류타입으로 사용해도 된다.

```swift
enum DateParseseError:Error {
    case oversizeString
    case undersizeString
    case incorrectFormat(part: String)
    case incorrectData(part: String)
}

//오류 던지기
func canThrowError() thorws -> String
func cannotThrowErrors() -> String

//오류잡기
do { try <오류를 던질 수 있는 함수>
   
}catch <오류타입 1> {
    //오류타입1에 대한 내용
}
```

