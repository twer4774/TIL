# SOLID

## S - SRP 

- 단일 책임의 원칙 (Single Responsibility Principle)

- 모든 클래스는 단 하나의 책임을 가진다. => 클래스를 수정해야하는 이유는 한가지이다.
- 책임 영역이 명확해야 한다.

## O - OCP

- 개방-폐쇄의 원칙 (Open Closed Principle)
- 확장에 대해서는 개방, 수정에 대해서는 폐쇄
- 구현에 의존하기보다는 정의한 인터페이스에 의존해야 한다.

## L - LSP

- 리스코프 치환법칙 (Liskov Substitusion Principle)

- 자식클래스는 언제나 부모클래스를 대체할 수 있다.

  => 부모클래스가 들어갈 자리에 자식클래스를 대신 넣어도 정상도작한다.

## I - ISP

- 인터페이스 분리 법칙 (Interface Segregation Principle)
- 클라이언트가 자신이 이용하지 않는 메서드에 의존하지 않아야 한다
- 하나의 일반적인 인터페이스보다는 구체적인 여러개의 인터페이스가 낫다

## D - DIP

- 의존성 역전 법칙(Dependency Inversion Principle)
- 상위 클래스는 하위 클래스에 의존되어서는 안된다는 법칙