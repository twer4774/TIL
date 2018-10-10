# 상속(Overriding)

한 클래스가 다른 클래스에서 정의된 프로퍼티나 메소드를 물려 받아 사용하는 것

```swift
class A {
    var name = "class A"
    var description : String{
        return "This className is \(slef.name)"
    }
    func foo(){
        print("\(self.name)")
    }
}

let a = A()
a.name //class A
a.description //This class name is Class A
a.foo //class A

//서브 클래싱: 상속 받아 새로운 클래스 정의. swift는 단일 상속

class <클래스 이름> : <부모클래스>{ }

class B : A {
    var prop = "Class B"
    func boo() -> String {
        return "\(self.prop)"
    }
}

let b = B()
b.prop //Class B
b.boo //Class B
b.name //Class A
b.foo //Class A
b.name = "Class C"
b.foo //Class C

//탈것의 예
class vehicle {
    var currentSpeed = 0.0
    var description: String {
        return "시간 당 (self.currentspeed)"
    }
    func makeNoise(){
      
    }
}

class Bicycle: vehicle{
    var hasBasket = false
}

let bicycle = Bicycle()
bicycle.hasBasket = true
```



# 오버라이딩 override

부모클래스로부터 물려받은 내용을 재정의

프로퍼티를 오버라이딩 할때 저장 프로퍼티, 연산 프로퍼티 모두 연산 프로퍼티로 오버라이딩 해야함

### 프로퍼티 오버라이딩 시 허용 되는 것

1. 저장 프로퍼티를 get, set 모두 있는 연산 프로퍼티로 오버라이딩
2. get, set 모두 있는 연산 프로퍼티를 연산 프로퍼티로 오버라이딩
3. get 구문 연산 프로퍼티를 연산 프로퍼티로 오버라이딩
4. get 구문 연산 프로퍼티를 get 구문 연산 프로퍼티로 오버라이딩

```swift
class Car: vehicle{
    var gear = 0
    var engineLevel = 0
    
    override var currentSpeed: Double{
        get{ return Double(self.engineLevel * 50) }
        set{print("New Value is \(newValue)")}
    }
}


let c = Car()
c.engineLevel = 5
c.currentSpeed //250
c.description ="New Class Car"
print(c.description) //NewValue is New Class Car

class AutomaticCar : Car{
    override var currentSpeed: Double{
        didSet { self. gear = Int(currentSpeed/100) + 1 }
    }
}
```

 

## 메소드 오버라이딩

까다로움. 매개변수의 개수, 타입, 반환 타입 변경 불가

```swift
class Bike: Vehicle{
    override func makeNoise() {
        print("빠라빠라 밤")
    }
}

let bk = Bike()
bk.makeNoise() //빠라빠라 밤
```

 

*오버로딩: 매개 변수의 개수, 타입에따라 다른 메소드로 판별

func makeNoise() 와 func makeNoise(param:Int) 는 다른것

 

super 키워드를 통해 부모클래스의 프로퍼티나 메소드 호출 가능

## 오버라이딩 막기 - final 키워드 이용

## 오버라이딩의 안좋은 경우 

- 인증코드 

인증코드의 결과를 True / False 로 반환하지만

내부적으로 알고리즘은 매우 복잡(핵심 키가 없으면 인증 못하게 하는등)

하지만 오버라이딩을 이용하면 보안 성이 떨어짐.

단순히 인증했다고 True 메시지 반환 가능



# 타입 캐스팅

```swift
class Vehicle {
    var currentSpeed = 0.0
    func accelerate() {
        self.currentSpeed += 1
    }
}

class Car: Vehicle{
    var gear: Int {
        return Int(self.currentSpeed/20) + 1
    }

    func wiper(){
     
    }
}

 

//Car의 인스턴스를 할당 받지만, 상위 클래스인 Vehicle타입으로 선언 => Vehicle의 프로퍼티와 메소드를 물려 받음
let trans: Vehicle = Car()
```

 

### 상위 클래스 타입으로 선언하는 이유: 인자값으로 사용할 수 있는 객체 범위가 넓어짐

=> 상위 클래스, 상위클래스를 상속받은 모든 클래스의 인스턴스를 인자값으로 이용가능

 

## 타입 비교 연산 is

- 타입의 일치 여부 확인
- 인스턴스(또는 변수, 상수) is      비교대상타입
- suv() is SUV //true
- suv() is Car() //true
- Car()-부모 is SUV-자식      //false

 

## 타입 캐스팅 연산 as

- 타입 캐스팅은 상속관계 내에서만 허용

- 업 캐스팅

- - 하위 클래스 타입 -> 상위       클래스 타입으로 변환
  - 캐스팅 한  후 타입이 상위 클래스 일때
  - 캐스팅 결과가 전보다 추상화 될때
  - 일반적으로 캐스팅 오류가 없음

- 다운 캐스팅

- - 캐스팅 오류 가능성 존재
  - 오류에 대한 처리 방식에 따라 옵셔널       캐스팅(?)과 강제 캐스팅(!)으로 나누어 짐
  - 구체화 됨

- 다운 캐스팅을 앱 만들때 많이 사용함      : 더욱 구체화된 프로퍼티와 메소드를 사용할 수  있기 때문

 

 

# Any, AnyObject

상속 관계에 있지 않아도 타입 캐스팅할 수  있는 예외 => 범용 타입

Any: 모든 타입. 자료형, 구조체, 열거형, 함수

너무 추상적이여서 프로퍼티나 메소드를 제공하지 않음

실행해 보기전에 타입을 알수 없음 -> 런타임 오류 -> 앱성능 저하

AnyObject: 클래스의 일종. 범용타입의 클래스

 

# 초기화 구문

초기화: 인스턴스를 생성해서 메모리 공간 할당 받는것

## init 초기화 메소드

```swift
init(<매개변수>:<타입>, <매개변수>:<타입>){
//1. 매개변수의 초기화
//2. 인스턴스 생성 시 기타 처리할 내용
}


```

 

### 특성

1. 초기화 메소드의 이름은 Init으로 통일
2. 매개변수의 개수, 이름, 타입은 임의로      정의할 수 있음
3. 매개변수의 이름과 개수, 타입이 서로      다른 여러개의 초기화 메소드정의 가능(오버로딩)
4. 정의된 초기화 메소드는 직접 호출되기도      하지만, 대부분 인스턴스 생성시 간접 호출