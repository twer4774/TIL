# Desing Pattern

## MVC: Model - View - Controller

- 하나의 객체가 다른 객체와 독립성을 유지하면서 메시지를 통해 필요한 데이터와 이벤트를 전달
- 독립성으로 인해 다른 객체에 영향을 주지 않고 구현을 변경하거나 새로운 기능을 추가할 수 있다는 장점
- Model
  - 앱의 데이터를 추상화 함
  - 클래스, 구조체를 통해 정의되며 데이터를 저장하고 조작하는 속성과 메소드를 가지고 있음
  - 저장된 데이터는 주로 View 객체가 화면에 표시할 내용을 구성할 때 사용
  - View객에와 직접적으로 연결되지 않으며, Controller 객체 또는 노티피케이션을 통해 필요한 데이터를 주고 받음
- View
  - Model객체에 저장된 데이터를 시각적으로 출력
  - View 객체는 구현된 로직에 따라 비트맵 데이터를 생성 => View객체의 로직을 변경해도 다른 객체에 영향을 주지 않음
  - UIView 클래스 또는 이 클래스를 상속한 클래스를 통해 구현됨
- Controller
  - View객체와 Model객체의 연결을 담당
  - View 이벤트 발생 -> 데이터가 업데이트 되도록 Model로 이벤트 전달
  - Model업데이트 -> View로 이벤트 전달

## Delegation: 대리자 패턴

- 대리자 객체는 다른 객체가 스스로 처리할 수 없는 작업을 대신 처리함
- 테이블 뷰에서 UITableViewControllerDelegate를 이용해 테이블 뷰에 표시할 목록의 수(numberOfSection)와 표시해야 할 데이터 정보(cellForRowAt)를 출력함
- 대리자 객체 = DataSource. 다른 객체가 사용할 데이터를 제공하는데 중점을 둠. 그외 나머지는 Delegate가 처리 함
- 셀에서 이벤트가 발생하면 Delegate로 전달 되고, Delegate객체가 연락처와 연관되어 있다면 연락처 목록으로 이동 함



## Singleton

- 프로그램 내에서 중복되지 않는 하나의 객체를 생성하기 위해서 사용되는 패턴

- 최초에 생성된 인스턴스 하나를 갖고 이 객체를 계속 이용함

- 보통 환경설정이나 디바이스 하드웨어와 가은 공유 자원을 사용하는 객체를 싱글톤으로 구현

- UIApplication, UIDevice, NSUserDefaults 등의 싱글톤 객체를 제공 함

- ```swift
  class NetworkManager{
      static let sharedManager = NetworkManager()
  }
  ```



## Target-Action

- 이벤트가 발생할 때 다른 객체로 전달할 메시지를 저장하는 패턴
- 전달대상(Target)과 호출할 메소드의 셀렉터(Action)로 구성

```swift
@IBAction func fun_name(_ sender: AnyObject){
    
}
```

- sender 파라미터는 id, AnyObject로 주로 쓰이지만 UIButton, UISwitch 등 특정 객체의 자료형으로 쓰이기도 함