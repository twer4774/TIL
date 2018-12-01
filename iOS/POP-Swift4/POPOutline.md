# POP

## 프로토콜 요구 사항

- get, set 키워드로 프로퍼티가 읽기전용인지 쓰기전용인지 명시
- 타입추론을 사용할 수 없으므로 타입을 명시해야 함

## 메소드 요구 사항

- 값 타입(구조체)인 경우 메소드가 내용을 변경하는 경우 mutating키워드 입력

## 프로토콜 컴포지션

- 프로토콜을 연달아 준수하는경우(상속을 여러개 한다고 생각하면 됨)



## 프로토콜을 타입으로 사용

```swift
//Protcol 정의
//4개의 프로퍼티와 1개의 생성자 정의
protocol Person{
    var firstName: String { get set }
    var lastName: String { get set }
    var birthDate: Date { get set }
    var profession: String { get }
    init(firstName: String, lastName: String, birthDate: Date)
}

//프로토콜을 함수나 메소드 또는 생성자의 매개변수와 반환타입으로 사용
func updatePerson(person: Person) -> Person{
    var new Person: Person
    //person을 갱신하는 코드를 정의
    retrun newPerson
}

//콜렉션을 저장하기 위한 타입
var personArray = [Person]()
var personDict = [String: Person]()

//프로토콜 타입을 요구하는 곳 어디에서나 인스턴스를 사용할 수 있음
var myPerson: Person
myPerson = SwiftProgrammer(firstname: "Jo", lastName: "Wonik", birthDate: birthDateProgrammer)
myPerson = FootballPlayer(firstName: "Son", lastName: "Hengmin", birthDate: birthDatePlayer)

//프로토콜의 다형성
var programmer = SwiftProgrammer(firstName: "Jo", lastName: "Hoffma", birthDate: bDateProgrammer)
var player = FootballPlayer(firstName: "Son", lastName: "Hengmin", birthDate: bDatePlayer)
var people: [Person] = [] 
people.append(programmer) 
people.append(player)
```

## 프로토콜 다형성

- 여러 타입을 위한 단일 인터페이스
- 하나의 일관된 인터페이스를 통해 여러 타입과 상호작요알 수 있게 해줌

```swift
//PersonProtocol 프로토콜을 따르는 타입의 인스턴스면 변수에 대입
//프로토콜 타입을 요구하는 곳 어디에서나 인스턴스를 사용할 수 있음
var myPerson: Person
myPerson = SwiftProgrammer(firstname: "Jo", lastName: "Wonik", birthDate: birthDateProgrammer)
myPerson = FootballPlayer(firstName: "Son", lastName: "Hengmin", birthDate: birthDatePlayer)

//PersonProtocol을 따르는 타입의 인스턴스를 배열에 추가
var programmer = SwiftProgrammer(firstName: "Jo", lastName: "Hoffma", birthDate: bDateProgrammer)
var player = FootballPlayer(firstName: "Son", lastName: "Hengmin", birthDate: bDatePlayer)
var people: [Person] = [] 
people.append(programmer) 
people.append(player)
```

## 프로토콜과 형 변환

- 인스턴스의 타입을 확인하거나 인스턴스를 명시된 타입으로 다루기 위한 방법
- 특정 타입의 인스턴스인지 확인: is 키워드
- 특정 타입의 인스턴스로 변환: as 키워드

```swift
//person 인스턴스가 SwiftProgrammer타입일 경우 true 반환
if person is SwiftProgrammer{
    print("\()person.firstName) is a Swift Programmmer")
}
//특정 인스턴스만 반환하게 배열을 필터링하기 위해 where문을 is 키워드와 함께 조합
for person in people where person is SwiftProgrammer{
    print("\(person.firstName) is a Swift Programmer")
}

//형변환 as? 키워드는 옵셔널을 반환하므로 옵셔널 바인딩 이용
if let _ = person as? SwiftProgrammer{
    print("\(person.firstName) is a Swift Programmer")
}
```

## 연관 타입과 프로토콜

- 하나 이상의 연관 타입 associated type 정의
- 프로토콜 내에서 타입을 대신해 사용할 수 있는 플레이스 홀더명 제공
- 연관 타입에서 사용하는 실제 타입은 프로토콜이 채택되기 전까지는 정의되지 않음
- 연관타입은 "우리는 사용할 타입을 정확히 몰라. 이 프로토콜을 채태갛는 타입이 정확한 타입을 정할거야"라고 암시해 줌

```swift
protocol Queue{
    associatedtype QueueType
    mutating func addItem(item: QueueType) //매개변수 타입으로 사용
    mutating func getItem() -> QueueType? //반환타입으로 사용
    func count() -> Int
}

//비제네릭 클래스에서 Queue 구현
struct IntQueue: Queue{
    var items = [Int]()
    
    mutating func addItem(item: Int){
        items.append(item)
    }
    
    mutating func getItem() -> Int?{
        if items.count > 0{
            return items.remove(at: 0)
        } else {
            return nil
        }
    }
    
    func count() -> Int {
        return items.count
    }
}
```



## 델리게이션

- 한 타입의 인스턴스가 다른 인스턴스를 대신해서 동작하는 상황에 적합
- 동작을 위임하는 인스턴스(델리게이팅)는 델리게이트 인스턴스의 참조를 저장하고 있다가 어떠한 액션이 발생하면 델리게이팅 인스턴스는 계획된 함수를 수행하기 위해 델리게이트를 호출함

```swift
import UIKit

protocol DisplayNameDelegate{
    func displayName(name: String)
}

struct Person{
    //델리게이트 타입의 인스턴스를 가짐 -> firstName과 lastName이 변경될 때 이름을 보여주어야 하는 책임을 갖게 됨
    var displayNameDelegate: DisplayNameDelegate
    
    var firstName = ""{
        //프로퍼티 옵저버
        didSet{
            displayNameDelegate.displayName(name: getFullName())
        }
    }
    
    var lastName = ""{
        didSet{
            displayNameDelegate.displayName(name: getFullName())
        }
    }
    
    init(DisplayNameDelegate: DisplayNameDelegate){
        self.displayNameDelegate = displayNameDelegate
    }
    
    func getFullName() -> String{
        return "\(firstName) \(lastName)"
    }
}

//타입 생성
struct MyDisplayNameDelegate: DisplaynameDelegate{
    func displayName(name: String) {
        print("Name: \(name)")
    }
}
//사용
var displayDelegate = MyDisplayNameDelegate() //인스턴스 생성
var person = Person(displayNameDele: displayDelegate)
person.firstname = "Jo"
person.lastName = "Wonik"
```

## 프로토콜을 사용해 설계

- 객체지향 프로그래밍에서는 서브클래스를 위한 모든 기본적인 요구사항을 포함하는 슈퍼 클래스를 갖음
- 프로토콜지향 프로그래밍에서는 슈퍼클래스 대신 프로토콜을 사용하며, 요구사항을 더 큰 덩어리의 프로토콜이 아닌 작고 매우 구체적인 프로토콜로 나눔

```swift
//2차원(앞,뒤,좌,우)로 동작
protocol RobotMovemnet{
    func forward(speedPercent: Double)
    func reverse(speedPercent: Double)
    func left(speedPercent: Double)
    func right(speedPercent: Double)
    func stop()
}

//3차원으로 동작(위(하늘), 아래(땅))
protocol RobotMovemnetThreeDimensions: RobotMovemnet{
    func up(speedPercent: Double)
    func down(speedPercent: Double)
}

//센서 추가
protocol Sensor{
    var sensorType: String{ get } //타입 정의
    var sensorName: String{ get set } //이름 정의
    
    init(sensorName: String) //초기화
    func pollSensor() //센서를 폴링하는데 사용
}

//환경 센서 만들기
protocol EnvironmentSensor: Sensor{
    func currentTemperature() -> Double
    func currentHumidity() -> Double
}

//센서 추가
protocol RangeSensor: Sensor{
    //특정 거리내에 물체가 이씅면 클로저 호출
    func setRangenotification(rangeCentimeter: Double, rangeNotification: () -> Void)
    func currentRange() -> Double
}

protocol DisplaySensor: Sensor{
    fnc displayMessage(message: String)
}

protocol WirelessSensor: Sensor{
    //메시지가 들어오면 클로저 호출
    func setMessageReceivedNotification(messageNotification: (String) -> Void)
    func messageSend(message: String)
}

//로봇 타입을 위한 요구사항 정의
protocol Robot{
    var name: String{get set}
    var robotMovement: RobotMovement{get set}
    var sensors: [Sensor] {get}
    
    init(name: String, robotMovement: RobotMovement)
    func addSensor(sensor: Sensor)
    func pollSensor()
}

```

