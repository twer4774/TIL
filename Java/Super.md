# Super

- 자손 클래스에서 조상 클래스로부터 상속 받은 멤버를 참조하는데 사용되는 참조 변수
- 조상의 멤버와 자신을 구별한다는 점을 제외하고는 this와 동일
  - super는 조상클래스의 멤버변수 참조
  - this는 현재 클래스의 멤버변수 참조

### super() - 조상클래스의 생성자

- this()와 마찬가지로 super() 또한 생성자
- super()는 조상클래스의 생성자를 호출할 때 이용
  - 만약 부모클래스에 없는 생성자를 자식 클래스에서 호출하면 컴파일 에러 발생
    - 자식 클래스에서 super() 를 넣지 않으면 컴파일러가 자동으로 super()를 넣는데, 이때 부모 클래스에서 매개변수가 없는 생성자가 없을 경우 에러 발생

