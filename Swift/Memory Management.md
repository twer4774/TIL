# 메모리 관리(Memory Management)

## MRC(Menual Reference Counting) = MMR(Manual Retain Release)

- 객체의 소유권을 기반으로 메모리 관리 - 하나 이상의 소유자가 있는 경우 메모리에 유지됨
- 소유자가 하나도 없을 경우 메모리에서 해제 됨
- 객체의 소유권을 관리하기 위해서 참조 카운트를 사용 => 객체를 소유할 때마다 1씩 증가, 소유권 포기시 1씩 감소

```objective-c
@protocol NSObject
	(instancetype) retain Objective-C_ARC_UNAVAILABLE;
	(oneway void)release Objective-C_ARC_UNAVAILABLE;
	(instancetype)autorelease Objective-C_ARC_UNAVAILABL;
	(NSUInteger)retainCount Objective-C_ARC_UNAVAILABL;
@end
    
@interface NSObject <NSObject>
   (void)dealloc;
@end
```

- MRR 메모리 관리 규칙
  1. alloc, new, copy, mutableCopy로 시작하는 이름을 가진 메소드로 생성한 객체는 호출자(리시버)가 소유권을 획득
  2. 객체를 메모리에 유지하려면 retain 메소드를 통해 객체의 소유권을 획득 해야 함
  3. 객체가 더 이상 필요하지 않다면 release, autorelease 메소드를 통해 객체의 소유권을 포기해야 함
  4. 자신이 소유한 객체의 소유권만 포기할 수 있음
- MRR 모델 메모리 관리코드

```objective-c
Person* p = [[Person alloc] init]; //1번에 따라 alloc메소드로 생성된 객체를 소유 함 => 객체의 참조카운트:1
NSString* name = p.name; //name속성 값을 저장할 때는 retain메소드를 사용하지 않음 => name변수는 p.name 속성에 저장되어 있는 문자열 객체를 소유하지 않음
[p release]; //release 메시지 -> 참조카운트 1감소

//리턴되는 메모리가 정상적으로 해제되도록 구현
//returnSomething메소드는 문자열을 리턴함
-(NSString*)returnSomething{
    //메소드에서 생성된 문자열은 str이 소유하고, 참조 카운트가 1이 됨
    NSString* str = [[NSString alloc] initWithString:@"Something"];
    //만약 [str release] 코드가 있어 메모리를 해제하게 되면 런타임에서 오류 발생-메소드 실행이 종료되기 전에 메모리에서 해제되어 버려 return str가 런타임 오류를 발생시킴 ==> 해결방법: autorelease
    return str;
}

//autorelease
-(NSString*)returnSomething{
    NSString* str = [[NSString alloc] initWithString:@"Something"];
    [str autorelease];
    return str;
}

//MRR모델에서 객체가 해제될때, 할당받은 메모리는 직접 해제해야 함.
-(void)delalloc{
    [_name release];
    [super dealloc];
}

```



## AutoRelease Pool

- autorelease 메시지를 받은 객체가 해제되기 전까지 저장되는 공간
- 이 공간에 저장된 객체들은 오토릴리즈 풀이 해제될 때 release 메시지를 받음
- 한의 객체가 여러번 추가 되었다면 추가된 횟수만큼 release 메시지를 받음
- 코코아 환경에 오토릴리즈 풀은 필수 - Xcode로 생성된 모든 프로젝트는 메인스레드에서 동작하는 기본 오토릴리즈 풀을 제공

```objective-c
//MMR - Objective-C
NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
	//...
[pool release];

//ARC - Objective-C
@autoreleasepool{
    //...
}
```

```swift
autorelease{
    //...
}
```

- autorelease pool을 프로그래머가 직접 생성해야 할 경우
  1. 명령줄 도구와 같이 UI프레임워크를 사용하지 않는 프로그램을 개발할 때
  2. 반복문에서 다수의 임시 객체를 생성할 때
  3. 스레드를 직접 생성할 때



## ARC(Automatic Reference Counting)

- ARC 도입 배경
  - 여러 객체가 상호 작용하는 코드에서 소유권을 올바르게 처리하는 코드 작성은 어려움
  - 작성해야 하는 코드의 양이 증가하는 만큼 메모리 오류의 가능성과 디버깅 난이도 증가
  - => 결국 유지보수가 어려워지기 때문에 ARC가 도입됨
- ARC 특징
  - MRR과 동일한 참조 카운트 모델을 사용하지만 향상된 컴파일러가 메모리 관리 코드를 자동으로 추가
  - 프로그래머가 더 이상 메모리 관리 코드를 작성할 필요가 없어 프로그램의 기능에 더욱 집중할 수 있게 됨
  - Objective-C는 MRR,ARC 중 선택 가능하고, Swift는 ARC를 기본 메모리 관리 모델로 사용
  - Garbage Collection과 유사
    - 차이점: 
      Gabage Collection은 런타임에서 주기적으로 메모리를 정리함
      ARC는 컴파일 시점에 코드가 자동으로 추가되는 방식이므로 런타임에 메모리 관리를 위한 오버헤드가 발생하지 않음.
  - ARC는 객체를 생성할 때마다 객체에 대한 정보를 저장하는 별도의 메모리 공간을 생성함 - 이 공간에는 객체에 대한 형식 정보와 속성 값이 저장 됨 => ARC는 이 정보를 기반으로 메모리를 관리 함
- 소유 정책
  - 참조 카운트를 관리하는 규칙을 소유 정책이라고 정의함
    - 모든 객체는 생성될 때 참조 카운트가 1이 됨
    - 객체에 retain 메시지를 보내면 참조 카운트가 1 증가함. 이 메시지를 보낸 호출자는 객체를 소유하게 됨
    - 객체에 release 메시지를 보내면 참조 카운트가 1 감소함. 이 메시지를 보낸 호출자는 객체의 소유권을 포기함
    - autorelease 메시지를 보내면 현재 사용 중인 오토릴리즈 풀 블록의 실행이 종료되는 시점에 참조 카운트가 1 감소함. 이 메시지를 보낸 호출자는 객체의 소유권을 포기함
    - 참조 카운트가 0이 되면 객체의 메모리가 해제 됨

### 강한참조(Strong Reference)

- 해제된 객체에 접근하는 코드는 런타임 오류의 원인이 됨
- ARC는 이러한 문제를 방지하기 위해 객체를 참조하고 있는 속성, 상수, 변수를 추적 함
- 활성화된 참조가 하나라도 존재하면 객체는 해제되지 않음

```swift
class Person{
    var name = "wonik"
    deinit{
        print("\(name) is deinit")
    }
}

var person1: Person?
var person2: Person?
var person3: Person?

person1 = Person() //person1은 Person객체와 강한 참조 유지
//person2,3에 person1을 할당하면 두 변수도 Person객체와 강한 참조를 유지
person2 = person1
person3 = person1
//Person 객체의 참조카운트는 3

//참조 카운트를 줄이고 싶다면? => nil 할당
person1 = nil
```

### 참조 사이클

```swift
class Person{
    var name = "wonik"
    var car: Car?
    
    deinit{
        print("\(name) is deinit")
    }
}

class Car{
    var model: String
    var lessee: Person?
    
    init(model: String){
        self.model = model
    }
    
    deinit{
        print("\(model) is deinit")
    }
}

var person: Person? = Person() //Person객체와 강한 참조 유지. 참조카운트 1
var rentedCar: Car? = Car(model: "Porshe 911") //Car객체와 강한 참조 유지

person!.car = rentedCar //car속성에 rentedCar변수를 할당하면 car속성과 rentedCar변수가 소유하고 있는 객체 사이에 강한 참조 발생. 이때 Car객체와 유지되고 있는 강한 참조는 두개, 참조 카운트는 2
//마찬가지로, lessee속성에 person변수를 할당해 소유하고 있는 객체 사이에는 강한 참조가 유지되고, 참조카운트는 2가 됨
rentedCar!.lessee = person

//메모리를 해제하려고 해도 서로간의 강한 참조를 유지하고 있기 때문에 해제 할 수 없음 => 강한 참조 사이클현상 발생
person = nil
rented = nil
```

### 약한 참조(Weak Reference)

- 참조 사이클 문제를 해결하기 위해 가장 처음 도입된 참조 방법 => weak 키워드 이용
- 자신이 참조하고 있는 객체가 해제 될 때 자신의 값을 nil로 초기화
- 옵셔널로 선언해야 약한 참조를 선언할 수 있음

```swift
class Car{
    var model: String
    weak var lessee: Person?
    //...
}

var person: Person? = Person()
var rentedCar: Car? = Car(model: "porshe 911")

person!.car = rentedCar
//lessee가 약한 참조로 선언되어 person과 강한참조를 유지하지 않음 => Person 객체의 참조 카운트가 증가하지 않음
rentedCar!.lessee = person
```

