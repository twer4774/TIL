# 프로토콜

iOS는 특정 컨틀롤러에서 발생하는 각종 이벤트를 효율적으로 관리하기 위해 대리자(Delegate)를 지정하여 이벤트 처리를 위임하고, 실제로 이벤트가 발생하면 위임된 대리자가 콜백 메소드를 호출해주는 '델리게이트패턴'을 많이 사용함. 프로토콜은 델리게이트 패턴 구현에 이용됨

 프로토콜에서 선언됨 프로퍼티, 메소드를 '명세'라고 하며, 명세에 맞게 내용을 작성하는 것을 '구현' 이라고 한다.

- 프로토콜을 이용하면 수평적 확장이 가능함
- 상속은 클래스만 가능하며, 레퍼런스 타입으로 멀티 쓰레드 환경에서 값이 꼬이는 현상 발생(OOP)
- 프로토콜을 이용해 값 타입의 구현체를 생성할 수 있어 apple에서 권장하고 있음(POP)

## 프로토콜의 정의

```swift
protocol <프로토콜 명> { <명세1> <명세2>...}
```

프로토콜을  구현할 수 있는 구현체

1. 구조체
2. 클래스
3. 열거형
4. 익스텐션

 

## 프로토콜 프로퍼티

- 초기값 할당 불가
- 연산, 저장 프로퍼티 구분 없음. 단, 저장프로퍼티로 이용할 경우 get, set 모두 필요

```swift
protocol SomePropertyProtocol{
    var name: String { get set }
    var description: String { get }
}

 

struct RubyMember: SomePropertyProtocol {
    var name = "홍길동"
    var description: String {
        return "Name: \(self.name)"
    }
}
```



##  프로토콜 메소드

```swift
protocol SomeMethodProtocol{
    func execute(cmd: String)
    func showPort(p: Int) -> String
}

struct RubyService: SomeMethodProtocol{
    func execute(cmd: String){
        if cmd = "start" {
            print("실행")
        }
    }

    func showPort(p: Int) -> String{
        return "Port: \(p)"
    }
}
```

 

## 프로토콜에서의 mutating, static 사용

- 구조체내의 메소드가 프로퍼티를 변경하는 경우
   메소드 앞에 반드시 mutating선언하여 프로퍼티 값을 수정하는 메소드임을 표시

- mutating 키워드가 안 붙는 경우

- - 구조체, 열거형 등 값 타입의 객체서 내부 프로퍼티의 값을 변경하기 원치 않을 때
  - 주로 클래스를 대상으로 간주하고 작성된 프로토콜일 때

 

## 프로토콜과 초기화 메소드

```swift
protocol SomeIntProtocol{
    init()
    init(cmd: String)
}

 

//init()메소드를 가지는 프로토콜
protocol Init(){
    init()
}

 

//init()메소드를 가지는 부모 클래스
class Parent{ init(){ } }


//부모클래스의 init() + 프로토콜의 init()

class Child: parent, Init{
    override required init() {
    }
}

*클래스에서 초기화 메소드를 구현할 때 required 키워드로 프로토콜에서 온 초기화 구문임을 표시함
```

 

 

## 타입으로서의 프로토콜 

- 상수나 변수 그리고 프로퍼티의 타입으로      사용할 수 있음
- 함수, 메소드 또는 초기화 구문에서      매개변수 타입이나 반환 타입으로 프로토콜을 사용할 수 있음
- 배열이나 사전, 혹은 컨테이너 타입으로      이용 가능

 

## 델리게이션

델리게이트 패턴: 특정기능을 다른 객체에 위임, 그에 따라 필요한 시점에서 메소드의 호출만 받는 패턴

델리게이트 참조를 통해, 메소드를 호출 할 인스턴스 객체를 전달 받고, 이 인스턴스가 구현하고 있는 프로토콜에 선언된 메소드를 호출하는 것

```swift
protocol FuelPumpDelegate{
    func lackFuel()
    func fullFuel()
}

class FuelPump{
    var maxGage: Double = 100.0
    var delegate: FuelPumpDelegate? = nil 

    var fuelGage: Doulbe {
        didSet{
            if oldValue < 10 {
                //연료가 부족해지면 델리게이트의 lackFuel 메소드 호출
                self.delegate?.lackFuel()
            } else if oldValue == self.maxGage{
                self.delegate?.fullFuel()
            }
        }
    }

    init(fuelGage: Double = 0){
        self.fuelGage=fuelGage
    }

    //연료 펌프 가동
    func startPump(){
        while(true){
            if (self.fuelGage > 0){
                self.jetFuel()
            } else {
                break
            }
        }
    }

    

    //연료분사 할때마다 게이지의 눈금이 내려감
    func jetFuel(){
        self.fuelGage = fuelGage - 1
    }
}
 
class Car: FuelPumpDelegate{
    var fuelPump = FuelPump(fuelGage: 100)
    init() {
        self.fuelPump.delegate = self
    }
    func lackFuel(){
    }

    func fullFuel(){
    }

    func start(){
        fuelPump.startPump()
    }
}

```

 

## 클래스 전용 프로토콜

protocol SomeClassOnlyProtocol: class{ }

####  

## 옵셔널

클래스에서만 이용 가능

```swift
import Foundation
//@ojbc 필수
protocol msgDelegate{
@objc optional func onReceive(new:Int)
}
```

