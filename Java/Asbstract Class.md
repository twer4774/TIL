# Asbstract Class(추상 클래스)

- 미완성 설계도역할을 하는 클래스
- abstract 키워드 이용
- 추상클래스로는 인스턴스를 생성할 수 없음
- 새로운 클래스를 작성하는데 조상 클래스로서 중요한 역할을 수행
  - 새로운 클래스를 작성할 때 아무것도 없는 것 보다 가이드라인이 있으면 만들기 편함

### Abstract Class

- 클래스간의 공통점을 찾아내서 공통의 조상을 만드는 작업

### Abstract Method

- 메서드는 선언부와 구현부로 구성
  - 선언부만 작성하고 구현부를 남겨둔것 => Abstract Method

```java
abstract 리턴타입 메서드이름();

abstract class Player {
  abstract void play(int pos); //추상메서드
  abstract void stop(); //추상메서드
}

class AudioPlayer extends Player{
  void play(int pos) { ... }
  void stop() { ... }
}
```

