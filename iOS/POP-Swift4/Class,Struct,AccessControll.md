# 클래스, 구조체, 접근제어

## 클래스 (Class)

- 청사진: 애플리케이션에 객체의 속성과 행위를 알리는 역할
- 객체지향 프로그래밍의 청사진- 클래스
- 객체의 프로퍼티와 메소드 , 생성자를 단일 타입으로 캡슐화하는 구성체

```swift
class MyClass{
    var oneProperty: String
    
    init(oneProperty: String){
        self.oneProperty = oneProperty
    }
    
    func oneFunction(){
     
    }
}
```



## 구조체 (Struct)

- 인스턴스의 프로퍼티와 메소드, 생성자를 단일 타입으로 캡슐화하는 하나의 구성체 -클래스와 유사
- 기본으로 생성자를 제공함

```swift
struct MyStruct{
    var oneProperty: String
    
    func oneFunction(){
        
    }
}
```



# 접근제어 (assess control)

- 외부 코드에 대한 접근성과 가시성을 제한
- 상세 구현을 숨기고 외부 코드가 접근했으면 하는 인터페이스만 노출
- 클래스와 구조체 모두 구체적이 접근단계를 부여할 수 있음
- 6가지 접근 단계
  - Open: 가장 눈에 띄눈 접근 단계. 어느곳에서든지 접근을 허용. 주로 프레임워크에서 프레임워크의 공개 API를 노출시키기 위해 사용
  - Public: 어느곳에서든지 접근 허용. 프레임워크에서 프레임워크의 공개 API를 노출하기 위해 사용
  - Internal: 프레임워크 내부에서는 접근 허용. 프레임워크 외부 코드에서는 접근 불가
  - Fileprivate: 동일한 소스파일에서만 접근 허용
  - Private: 가장 가까운 접근단계. 소스파일내에서 접근 가능
- 주로 public, internal, private를 사용함

