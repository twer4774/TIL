# 값 타입과 참조 타입

- 값 타입 - 구조체, 열거형, 튜플
  - 인스턴스를 전달할때 복사본을 전달
- 참조 타입 - 클래스
  - 인스턴스를 전달할때 원본 인스턴스를 전달

```swift
struct MyValueType{
    var name: String
    var assignment: String
    var grade: Int
}

class MyReferenceType{
    var name: String
    var assignment: String
    var grade: Int
    
    init(name: String, assignment: String, grade: Int){
        self.name = name
        self.assignment = assignment
        self.grade = grade
    }
}

var ref1 = MyReferenceType(name: "Jo", assignment: "Math 1", grade: 90)
var val1 = MyValueType(name: "Jo", assignment: "Math 1", grade: 90)

//학점을 변경하는 함수 만들기
func extraCreditReferenceType(ref: MyReferenceType, extraCredit: Int){
    ref.grade += extraCredit
}

func extraCreditValueType(val: MyValueType, extraCredit: Int){
    var val = val
    val.grade += extraCredit

}

//참조타입
var ref2 = MyReferenceType(name: "Jo", assignment: "Math 1", grade: 90)
extraCreditReferenceType(ref: ref2, extraCredit: 5)
print("Reference: \(ref2.name) - \(ref2.grade)") //Reference: Jo - 95

//값타입
var val2 = MyValueType(name: "Jo", assignment: "Math 1", grade: 90)
extraCreditValueType(val: val2, extraCredit: 5)
print("Value: \(val2.name) - \(val2.grade)") //Value: Jo - 90
```

- 단일 레퍼런스 인스턴스를 참조하는 경우 문제점

```swift
func getGradeForAssignment(assignment: MyReferenceType){
    let num = Int(arc4random_uniform(20) + 80)
    assignment.grade = num
    print("Grade for \(assignment.name) is \(num)")
}

var mathGrades = [MyReferenceType]()
var students = ["Jon", "Kim", "Kailey", "Kara"]
var mathAssignment = MyReferenceType(name: "", assignment: "MathAssignment", grade: 0)

for student in students{
    mathAssignment.name = student
    getGradeForAssignment(assignment: mathAssignment)
    mathGrades.append(mathAssignment)
}
/*
Grade for Jon is 97
Grade for Kim is 85
Grade for Kailey is 86
Grade for Kara is 93
*/

for assignment in mathGrades{
    print("\(assignment.name): grade \(assignment.grade)")
}
/*
Kara: grade 93
Kara: grade 93
Kara: grade 93
Kara: grade 93
*/

//해결방법 - inout을 사용한 값 타입
func getGradeForAssignment2(assignment: inout MyValueType){
    let num = Int(arc4random_uniform(2) + 80)
    assignment.grade = num
    print("Grade for \(assignment.name) is \(num)")
}

var mathGrades2 = [MyValueType]()
var students2 = ["Jon", "Kim", "Kailey", "Kara"]
var mathAssignment2 = MyValueType(name: "", assignment: "MathAssignment", grade: 0)

for student in students2{
    mathAssignment2.name = student
    //inout을 이용하려면 &키워드 추가 필요
    getGradeForAssignment2(assignment: &mathAssignment2)
    mathGrades2.append(mathAssignment2)
}
/*
Grade for Jon is 81
Grade for Kim is 81
Grade for Kailey is 80
Grade for Kara is 81
*/

for assignment in mathGrades2{
    print("\(assignment.name): grade \(assignment.grade)")
}
/*
Jon: grade 81
Kim: grade 81
Kailey: grade 80
Kara: grade 81
*/
```



### 참조타입(클래스)로만 가능한 작업

#### 재귀적 데이터 타입

- 같은 타입의 다른 값을 프로퍼티로 갖는 타입
- 런타임에서 요구 사항에 따라 크기가 늘어나거나 줄어들 수 있음
- 연결리스튼 재귀적 데이터 타입을 이용해 구현하는 동적 자료구조의 좋은 예

```swift
class LinkedListReferenceType{
    var value: String
    var next: LinkedListReferenceType?
    init(value: String){
        self.value = value
    }
}

//값 타입의 경우실패함
//struct LinkedListValueType{
//    var value: String
//    var next: LinkedListValueType?
//}
```

#### 상속

- 슈퍼 클래스로부터 메소드, 프로퍼티 등 상속
- 문제점: 상속 - 상속 - 상속의 경우 로직을 이해하기 힘들어짐 => POP가 답

```swift
class Animal{
    var numberOfLeges = 0
    func sleeps(){
        print("zzzzz")
    }
    
    func walking(){
        print("Walking on \(numberOfLegs) legs")
    }
    
    func speaking(){
        print("No sound")
    }
}

class Biped: Animal{
    override init(){
        super.init()
        numberOfLegs = 2
    }
}

class Quadruped: Animal{
    override init(){
        super.init()
        numberOfLegs = 4
    }
}

class Dog: Quadruped{
    override func speaking(){
        print("Barking")
```

## 다이내믹 디스패치(dynamic dispatch)

- 런타임 오버헤드의 일정 부분은 참조타입만을 위한 상속에서 문제 발생
- final키워드 이용 => 상속 방지
  - 클래스나 메소드 또는 함수에 제약을 설정해 오버라이드를 방지함

```swift
final func myFunc(){}
final var myProperty = 0
final class MyClass {}

class Animal{
    final var numberOfLegs = 0
    func sleeps() {
        print("zzzzzz")
    }
    final func walking(){
        print("Wlaking on \(numberOfLegs) legs")
    }
    func speaking(){
        print("No sound")
    }
}
```

