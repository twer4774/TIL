# 열거형과 익스텐션

# 열거형

- 직접 입력해야 할 정보들을 '선택' 할 수 있게 해 오류를 줄임

- 하나의 주제로 연관된 데이터들이 멤버로 구성되어 있는 자료형 객체

- 데이터들은 열거형 객체를 정의하는 시점에서 함께 정의됨
   => 데이터를 함부로 삭제/변경할 수 없음. 삭제시 정의하는 구문 수정

- 변수에 입력될 값들을 몇가지로 특정 할 수 있다면 열거형 이용

- 열거형을 사용하면 좋은 경우

- - 원치않는 값이 입력되는 것을 막고 싶을때
  - 입력 받을 값을 미리 특정할 수 있을 때
  - 제한된 값 중에서만 선택하도록 강제하고 싶을 때

## 열거형의 정의 enum

```swift
enum 열거형 이름{
//열거형의 멤버 정의
case 멤버 값1
case 멤버 값2, 멤버값3
}

enum Direction{
    case noth
    case south, east, west
}
let N = Direction.noth
```

 

## switch 구문과 열거형

```swift
var directionToHead = Direction.west

switch directionToHead {
case Direction.noth:
    print("북")
case Direction.south:
    print("남")
case Direction.west:
    print("서")
case Direction.east:
    print("동")
}
```

 

## 멤버와 값의 분리

데이터만으로 의미 전달이 어려운 경우 열거형 멤버에 이름 할당

ex) HTTP 응답 코드

200 정상응답

304 캐싱된 데이터 전송

404 존재하지 않음. 페이지 없음

500 서버 에러

 

*멤버에 이름을 붙여줄 때에는 반드시 열거형의 타입을 선언해 주어야 함

```swift
enum HTTPCode:Int{
    case OK = 200
    case NOT_MODIFY = 304
    case INCORRECT_PAGE = 404
    case SERVER_ERROR = 500

    var value: String{
        return "HTTPCode Number is \(self.rawValue)"
    }

    func getDescription() -> String{
        switch self {
        case .OK:
            return "응답 성공(self.rawValue)"
        case .NOT_MODIFY:
            return "변경내역 없음
        case .INCORRECT_PAGE:
            return "페이지 없음"
        case .SERVER_ERROR:
            return "서버 에러"
        }
        
        static func getName() -> String{
            return "This Enumration is HttpCode"
        }
    }
}

var response = HTTPCode.OK
response = .NOT_MODIFY
respnse.value //HTTPCode number is 304
response.getDescription() //변경된 내역 djqtdma. HTTPCode 304
HTTPCode.getName() //This Enumration is HttpCode
```

 

## 멤버에 보조 값 설정 => 연관값

```swift
enum ImageFormat{
    case JPEG, PNG(Bool)
    case GIF(Int, Bool)
}


var newImage = ImageFormat.PNG(true)
newImage = .GIF(256, false)
```

 

## 열거형의 활용

메소드 호출 옵션이나 스타일을 설정할 때

ex) 예제 1 앨범이미지나 카메라를 다룰 때 이미지 피커 컨트롤러

```swift
enum UIIMagePickerControllerSourceTpye:Int{
case photoLibrary
case camera
case savePhotosAlbum
}
```

 

예제 2 알람창 Alert

컴파일러 자동 완성기능을 도움 .actionSheet 할때

 

# 익스텐션

- 기능추가

- 익스텐션을 통해 구현 할 수 있는 것

- - 새로운 연산프로퍼티 추가
  - 기존개체를 수정하지 않고 프로토콜       구현
  - 새로운 메소드 정의
  - 새로운 초기화 구문 추가

- extension <확장 할 기존      객체명> { }

 

## 익스텐션과 연산 프로퍼티

저장프로퍼티는 익스텐션으로  추가 하지 못한다.

```swift
extension Doulbe{
    var km: Double { return self * 1000.0 }
    var m: Double { return self}
    var description: String{
        return "\(self)km는 ..."
    }
}

let distance = 42.0.km + 195.m
print("총 거리는 \(distance)")
```

 

## 익스텐션과 메소드

오버로딩의 특성을 이용해 새로운 메소드 추가 가능

단, 같은 메소드 재정의는 안됨( 클래스의 상속 영역 )

```swift
extension Int{
    mutating func square(){
        self = self * self
    }
}

var value = 3
value.square() //a
```

 

##  익스텐션을 활용한 코드 정리

custom class 작성 후 extension을 통해 기능 확장

=> 별도의 그룹으로 묶여 코드가 정리되는 효과가 있음

| 점프바에서 구분됨 |                |                   |
| ----------------- | -------------- | ----------------- |
| 공식적인 메소드   | viewController |                   |
|                   |                | viewDidlLoad()    |
|                   |                | didMemoryWaring() |
| 비공식적인 메소드 | viewController |                   |
|                   |                | save              |
|                   |                | load              |

 

## 익스텐션과 델리게이트 패턴

extension으로 기능별(델리게이트)로 나누면 가독성이 쉬움

*MARK주석 -> 점프바나 심벌 탐색기에 표시되는 특수한 용도의 주석

//MARK: 테이블 뷰를 위한 프로토콜 델리게이트 구현

//MARK: - 테이블 뷰를 위한 프로토콜 델리게이트 구현 (-점프바에서 구분이 용이하도록 수평선이 그려짐)

 

 