# 클래스와 구조체

유연성: 코드를 다른 곳으로 옮기거나 새로운 코드를 추가하기 쉬움

| 멤버 | 프로퍼티 | 구조체와 클래스 내부에서 정의하는 상, 변수 |
| ---- | -------- | ------------------------------------------ |
|      | 메소드   | 구조체와 클래스 내부에서 정의하는 함수     |

 

# 구조체 VS 클래스

공통점

- 프로퍼티: 변수나 상수를 사용하여 값을 저장하는 프로퍼티를 정의 할 수 있다.
- 메소드: 함수를 사용하여 기능을 제공하는 메소드를 정의할 수 있다.
- 서브스크립트: 속성 값에 접근할 수 있는 방법을 제공하는 서브스크립트를 정의할 수 있다.
- 초기화 블록: 객체를 원하는 초기 상태로 설정해주는 초기화 블록을 정의 할 수 있다.
- 확장: 객체에 함수적 기능을 추가하는 확장 구문을 사용할 수 있다.
- 프로토콜: 특정 형식의 함수적 표준을 제공하기 위한 프로토콜을 구현할 수 있다.

 

# 클래스가 할 수 있는 것(구조체 보다 클래스 기능이 많음)

- 상속: 클래스의 특성을 다른 클래스에게 물려 줄 수 있다.
- 타입 캐스팅: 실행 시 컴파일러가 클래스 인스턴스의 타입을 미리 파악하고 검사할 수 이싿.
- 소멸화 구문: 인스턴스가 소멸되기 직전에 처리해야 할 구문을 미리 등록 할 수 있다.
- 참조에 의한 전달: 클래스 인스턴스가 전달 될 때는 참조형식으로 제공되며, 이때 참조 가능한 개수는 제약이 없다.

 

 

# 구조체와 클래스의 기본 개념

### 인스턴스

틀: 클래스 또는 구조체

도장: 인스턴스 => 메모리에 공간을 할당 받음

=> 즉, 클래스 또는 구조체 객체로 도장을 만들 틀을 정의하고, 도장 역할을 하는 인스턴스를 만들어 메모리에 공간을 할당한다.( 내가 도장 공장에 가서 도장의 색, 재질, 전각, 글자 모양을 정의(클래스,구조체 정의) 하고 도장을 그 틀 대로 만들어 낸다(인스턴스 생성). 이 도장(인스턴스)는 '조원익'이라는 이름이 새겨져 있다고 가정한다면, 인주를 '조'라는 글자에만 묻히고 찍어내면, 종이에는 '조'라는 글자만 찍어낼 수 있다(프로퍼티의 사용))

 

## 초기화

1. 프로퍼티를 선언하면서 동시에 초기화 값을 지정하는 경우
2. 초기화 메서드 내에서 프로퍼티의 초기값을 지정하는 경우

구조체에서는 멤버와이즈초기화기능을 제공한다.

#### 초기화 구문에서 지켜야 할 원칙

1. 모든 프로퍼티는 정의할 때, 초기값을 주던가 아니면 옵셔널 타입으로 선언한다.
2. 인스턴스를 생성할 때에는 클래스 뒤에 ()를 붙여준다.

 

 

## 구조체의 값 전달 방식: 복사에 의한 전달

구조체 인스턴스를 변수에 대입하면 복사한 새로운 값 대입

 

## 클래스의 값 전달 방식: 참조에 의한 전달

클래스는 메모리 주소참조에 의한 전달 방식을 사용 -> 참조타입

- 참조: 인스턴스가 저장된 메모리 주소 정보를 전달
- 클래스에서는 메모리 참조 문제가 발생됨
- 구조체의 인스턴스는 단일 참조 -> 사용이 끝나면 바로 메모리 해제
- 클래스의 인스턴스는 여러 곳에서 참조 -> 맘대로 메모리 해제 불가. => ARC(Auto Reference Counter)
             ARC : 지금 클래스 인스턴스를 참조하는 곳이 모두 몇 군데인지 자동으로 카운트 해주는 개체
                     참조 카운트가 0이 되면 메모리 해제

 

## 클래스 인스턴스에서 단순한 값 비교는 불가능

- 동일 인스턴스인지 비교할 때 : ===
- 동일 인스턴스가 아닌지 비교할 때 : !==

 

## 다음 조건에 해당하는 경우 구조체 사용

1. 서로 연관된 몇 개의 기본 데이터 타입들을 캡슐화 하여 묶는 것이 목적일 때
2. 캡슐화된 데이터에 상속이 필요하지 않을때
3. 캡슐화된 데이터를 전달하거나 할당하는 과정에서 참조 방식보다는 값이 복사되는 것이 합리적일때
4. 캡슐화된 원본 데이터를 보존해야 할 때

 

## 클래스를 이용하면 좋은 경우

- 상수나 변수에 할당할 때도 복사가 발생하지 않기 때문에, 여러 곳에 할당하더라도 메모리 낭비가 없으며, 인스턴스가 늘어나지 않으므로 코딩상에서 혼란이 적어짐

 

# 프로퍼티

값을 제공하는 것  *값을 저장하는 것과는 다름

프로퍼티를 사용하려면 인스턴스가 필요함. 인스턴스에 속한 프로퍼티를 '인스턴스 프로퍼티'라고 함

*메소드 안에 있는 변수, 상수는 프로퍼티가 아니라, 메소드의 지역 상수, 변수

 

## 저장 프로퍼티

- 클래스 내에서 선언 된 변수나 상수를 부르는 이름
- 프로퍼티 선언 시 초기화를 하지 않을 경우, 선언 시 옵셔널 타입을 선언
- 입력된 값을 저장하거나 저장된 값을 제공하는 역할
- 상수 및 변수를 사용해서 정의 가능
- 클래스와 구조체에서는 사용이 가능하지만, 열거형에서는 사용할 수 없음

### 저장프로퍼티에서 오류 안생기는 법

초기화 구문에서 프로퍼티 값 초기화도 가능 
 => 프로퍼티의 초기 값은 인스턴스를 생성하기 전까지만 할당하면 됨

1. ```swift
   //1. 초기화 구문(init) 이용
                 init(){ self.name="" }
   //2. 변수 선언 시 ?, ! 이용
                 var name : String? or !
   //3. 변수 선언 시 초기화하기
                 var name: String = ""
   ```


###  

### 구조체 인스턴스와 저장 프로퍼티에서 변수 및 상수에 따른 변경 가능 여부

|      | 저장 프로퍼티 | 구조체 인스턴스 |
| ---- | ------------- | --------------- |
|      | 변수          | 상수            |
| 변수 | 값 변경 가능  | 값 변경 불가    |
| 상수 | 값 변경 불가  | 값 변경 불가    |

*클래스에서는 상수로 인스턴스를 할당하더라도 클래스 내에서 변수로 선언한 저장 프로퍼티는 얼마든지 수정가능(참조에 의한 전달방식)

 

### 지연 저장 프로퍼티 lazy

저장프로퍼티의 초기화를 지연시킴

클래스 인스턴스가 생성되어 모든 프로퍼티가 만들어지더라도 lazy키워드가 붙은 프로퍼티는 선언만 될 뿐, 초기화 되지 않고 계쏙 대기하고 있다가 프로퍼티가 호출 되는 순간에 초기화

```swift
class OnCreate{
    init(){
        print("On Create!")
    }
}

 
class LazyTest{
    var base = 0
    lazy var late = OnCreate()
    init() {
        print("Lazy Test")
    }
}

 

let lz = LazyTest() //"Lazy Test"
lz.late //"On Create!"
//=> lazy 프로퍼티에 접근해야 초기화가 이루어짐
```

 

### 클로저를 이용한 저장프로퍼티 초기화

저장프로퍼티 중에 연산이나 로직 처리를 통해 얻어진 값을 이용하여 초기화를 해야하는 경우
 '클로저'를 이용해 필요한 로직을 수행한 후 반환 값을 저장 프로퍼티에 초기화 함

*연산 프로퍼티와의 차이점

연산프로퍼티는 참조 할 때마다 매번 값이 재평가됨
 클로저 이용 : 최초 한번만 값이 평가됨

```swift
//클로저를 이용한 저장 프로퍼티 초기화

let/var 프로퍼티명: 타입 ={
    정의내용
    return 반환값
}()

 
class PropertyInit{
    //저장프로퍼티 - 인스턴스 생성시 최초 한번만 실행
    var value01: String!={
    print("Value01 Execute")
    return "value01"
    }()

    let value02: String!={
        print("Value02 Execute")
        return "value02"
    }()
}


let s = PropertyInit()

//Value01 Execut
//Value02 Execute
s.value01 //실행결과 없음
s.value02 //실행결과 없음
```

 

### lazy를 이용한 방법

```swift
 lazy var value03: String!={
        print("Value03 Execute")
        return "value03"
    }()

 
s.value03 //Value03 Execute
s.value03 //실행결과 없음
```

 

## 연산 프로퍼티

- 다른 프로퍼티의 값을 연산처리하여 간접적으로 값 제공
- get: 프로퍼티의 값을 참조. 반환 값(return)으로 프로퍼티 값 제공
- set: 선택적으로 연산프로퍼티에 값을 할당하거나 변경하고자 할때 실행
- 특정 연산을 통해 값을 만들어서 제공하는 역할
- 변수만 사용해서 정의 가능
- 클래스, 구조체, 열거형 모두에서 사용가능

```swift
class/struct/enum 객체명 {

    var 프로퍼티명: 타입{
        get{
            필요한 연산과정
            return 반환값
        }
        set(매개변수명){
            필요한 연산 구문
        }
    }
}
```



- 연산 프로퍼티는 다른 프로퍼티에 의존적이거나 특정 연산을 통해 얻을 수 있는 값을 정의할 때 사용

ex) 나이 -> 나이는 출생연도에 의존적이며, 현재 연도를 기준으로 계산

- 예제 1 나이계산 현재 연도 - 출생 연도

```swift
import Foundation //DateFormatter이용을 위해 추가
struct userInfo{
    //저장프로퍼티: 태어난 연도
    var birth: Int!
    //연산 프로퍼티: 올해가 몇년도인지 계산
    var thisYear: Int!{
        get{
            let df = DateFormatter()
            df.dateFormat = "yyyy"
            return Int(df.string(from: Date()))
        }
    }

    //연산 프로퍼티: 올해 - 태어난 연도 + 1
    var age: Int{
        get{
            return (self.thisYear - self.birth) + 1
        }
    }
}

let info =userInfo(birth: 1980)
print(info.age)
```



- 예제 2 사각형의 중심좌표 계산

```swift
struct Rect{
    //사각형이 위치한 기준 좌표(좌측 상단 기준)
    var originX: Double = 0.0, originY: Double = 0.0
    //가로 세로 길이
    var sizeWidth: Double = 0.0, sizeHeight: Double = 0.0

    //사각형의 x좌표 중심
    var centerX: Double{
        get{
            return self.originX + (sizeWidth/2)
        }
        set(newCenterX){
            originX = newCenterX - (sizeWidth/2)
        }
    }

 

    //사각형의 y좌표 중심
    var centerY: Double{
        get{
            return self.originY + (sizeHeight/2)
        }

        set(newCenterY){
            self.originY = newCenterY - (sizeHeight/2)
        }
    }
}

 

var square = Rect(originX: 0.0, originY: 0.0, sizeWidth: 10.0, sizeHeight: 10.0)
print("square.centerX= \(square.centerX), square.centerY = \(square.centerY)")
```

 

- 연산 프로퍼티의 장점(내 의견)

위의 예제들과 같이 사각형의 중심좌표, 나이 계산 등 저장 프로퍼티와 다른 환경(조건)의 변화에 따른 값들의 저장이 필요할 경우, 반복적으로 코드를 작성하는 일이 줄어들 된다

 

- 연관선을 기준으로 사각형 구조체 나누기

```swift
struct Position{
    var x: Double = 0.0, y: Double = 0.0
}

struct Size{
    var width: Double = 0.0, height: Double = 0.0
}

 

struct Rect{
    //사각형이 위치한 기준 좌표(좌측 상단 기준)
    var origin = Position()
    //가로 세로 길이
    var size = Size()
    //사각형의 X좌표 중심
    var cneter: Position{
        get {
            let centerX = self.origin.x + (self.size.width/2)
            let centerY = self.origin.y + (self.size.height/2)
            return Position(x: centerX, y: centerY)
        }

        set(newCenter){
            self.origin.x = newCenter.x - (size.width/2)
            self.origin.y = newCenter.y - (size.height/2)
        }
    }
}

 

let p = Position(x: 0.0, y: 0.0)
let s = Size(width: 10.0, height: 10.0)
var square = Rect(origin: p, size: s)
print("sqaure.centerX = \(square.center.x), square.centerY = \(square.cneter.y)")
```

 

## 프로퍼티 옵저버

- 프로퍼티 값을 모니터링

- 사용자가 정의한 특정액션과 반응하도록 처리

- 우리가 직접 정의한 저장 프로퍼티에 추가

- 슈퍼 클래스로부터 상속 받은 서브 클래스에서도 추가 가능

- willSet: 프로퍼티의 값이 변경되기 직전에 호출되는 옵저버
             프로퍼티에 대입되는 값이 매개 상수로 전달됨

  ```swift
  var <프로퍼티명>: <타입>[=<초기값>]{
  
  willSet[(<인자명>)]{
       <프로퍼티 값이 변경되기 전에 실행 할 내용>
   }
  
  }
  ```


- didSet: 프로퍼티의 값이 변경된 직후에 호출되는 옵저버.
             기존의 값이 매개 상수로 전달됨

|         | 예전 값       | 새로운 값     |
| ------- | ------------- | ------------- |
| willSet | 프로퍼티 참조 | newValue 참조 |
| didSet  | oldValue참조  | 프로퍼티 참조 |

 

- 저장프로퍼티에 willSet과 didSet을 구현한 예

```swift
struct Job{
    var income: Int = 0{
        willSet(newIncome){
            print("이번달 월급은 \(newIncome)원")
        }
        didSet{
            if income > oldValue{
                print("월급이 \(income - oldValue)"원 증가")
            } else {
                print("월급 삭감")
            }
        }
    }
}

 
var job = Job(income:  1000000)
job.income = 2000000
//이번달 월급은 2000000원
//월급이 1000000원 증가
job.income = 1500000
//이번달 월급은 1500000원
//월급 삭감
```

 

 

## 타입 프로퍼티

static, class(하위 클래스에서 재정의 가능)

클래스, 구조체, 열거형 같은 객체 자체에 관련된 값을 다룰때 인스턴스를 생성하지 않고, 객체 자체에 값을 저장

저장된 값은 모든 인스턴스가 공통으로 사용 가능

클래스 내에서

```swift
static let/var 프로퍼티명 = 초기값
class let/var 프로퍼티명: 타입{
get{return}
 set{ }
}

 
struct Foo{
    //타입 저장 프로퍼티
    static var sFoo = "구조체 타입 저장 프로퍼티 값"
    //타입 연산 프로퍼티
    static var cFoo: Int{
        return 1
    }
}

 

class Boo{
    //타입 저장 프로퍼티
    static var sBoo = "클래스 타입 저장 프로퍼티 값"
    //타입 연산 프로퍼티
    static var cBoo: Int{
        return 10
    }
    //재정의가 가능한 타입 연산 프로퍼티
    class var oFoo: Int{
        return 100
    }
}
```

 

# 메소드

객체 내에서 구현 목적으로 만들어진 다른 메소드들과 협력하여 함수적인 기능 수행

## 인스턴스 메소드

인스턴스 메소드와 일반 함수의 차이

1. 구조체와 클래스의 인스턴스에 소속됨
2. 메소드 내에서 정의된 변수와 상수 뿐만 아니라 클래스 범위에서 정의된 프로퍼티도 모두 참조할 수 있다는 점
3. self키워드 사용가능 (인스턴스메소드 내에서 프로퍼티를 읽어 올 경우)

```swift
struct Resolution{
    var width = 0
    var height = 0

    //구조체의 설명 리턴 인스턴스 메소드
    func desc() -> String{
        let desc = "\(self.width) * \(self.height)"
        return desc
    }
}

class VideoMode{
    var resolution = Resolution()
    var interlaced = false
    var frameRate = 0.0
    var name: Stirng?

    //클래스의 설명 리턴 인스턴스 메소드
    func desc() -> String{
        if self.name != nil{
            let desc = "\(self.name!) 비디오 모드는 \(self.frameRate)"
            return desc
        } else {
            let desc = "\(self.frameRate)"
            return dese
        }
    }
}
```



#### mutating

구조체나 열거형의 인스턴스 메소드 내부에서 프로퍼티 값을 수정할 때 mutating 키워드 추가
 mutating 키워드로 내부 프로퍼티 값을 수정하는 메소드 임을 컴파일러에게 알림

```swift
//mutating

struct Point{
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double){
        self.x += deltaX
        self.y += deltaY
    }
}

var point = Point(x: 10.5, y: 12.0)
point.moveBy(x: 3.0, y: 4.5)
print("\(point.x) \(point.y)")
```

 

 

## 타입 메소드

인스턴스를 생성하지 않고 클래스 또는 구조체에서 호출하는 메소드

```swift
//타입 메소드
class Foo{
    class func fooTypeMethod(){
        //타입 메소드의 구현 내용
    }
}

let f = Foo()
f.fooTypeMethod() //오류
Foo.fooTypeMethod //성공
```

 

 