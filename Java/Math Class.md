# Math Class

- 수학적인 계산을 위한 클래스이며 static 메서드로만 구성되어 있어 인스턴스를 생성할 수 없음
- 올림, 반올림, 버림 함수들

```java
Math.ceil(); //올림
Math.floor(); //버림
Math.round(); //반올림
MAth.rint(); //반올림, 단 반환값이 double
```

### 예외를 발생시키는 메서드

- 메서드 이름에 'Exact'가 포함된 메서드들은 오버플로우를 감지하기 위해 존재
- 아래와 같이 'Exact'가 붙은 메서드들은 오버플로우가 발생하면 예외를 발생 시킴

```java
int addExact();
int subtractExact();
...
```

### 그 밖의 함수들

- 삼각함수와 지수, 로그
  - sqrt() 제곱근, pow() n제곱근
  - sin(), cos(), atan()
  - log10()

