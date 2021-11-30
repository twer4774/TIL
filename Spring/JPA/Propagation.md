# [Transactional] propagation

## @Transactional 사용시 주의사항

- @Transactional을 클래스 또는 메소드 레벨에 명시하면 해당 메소드 호출 시 지정된 트랜잭션이 작동한다.

### Propagation.REQUIRED

- default
- 부모 태랜잭션 내에서 실행하며, 부모 트랜잭션이 없을 경우 새로운 트랜잭션을 생성한다.
- 해당 메소드를 호출한 곳에서 별도의 트랜잭션이 설정되어 있지 않다면, 새로운 연결로 트랜잭션을 시작한다.
- 이미 트랜잭션이 설정되어 있다면, 기존의 트랜잭션 내에서 로직을 실행한다.
- 예외가 발생하면 롤백되고, 호출한 곳에도 롤백이 전파된다.

### Propagation.REQUIRES_NEW

- 매번 새로운 트랜잭션을 시작한다.
- 호출한 곳에서 이미 트랜잭션이 설정되어 있다면 기존의 트랜잭션은 메소드가 종료할 때까지 잠시 대기 상태로 두고, 자신의 트랜잭션을 실행한다.
- 새로운 트랜잭션 안에서 롤백이 발생하더라도 호출한 곳에 롤백이 전파되지 않는다.
- 2개의 트랜잭션이 완전 독립적으로 동작한다.

### Propagation.NESTED

- 해당 메소드가 부모 트랜잭션에서 진행될 경우 별개로 커미소디거나 롤백될 수 있다.
- 둘러싼 부모 트랜잭션이 없을 경우 Propagation.REQUIRED와 동일하게 작동한다.
- 차이점은 Save point 기능을 지원해야 사용 가능하다.
- 이미 진행중인 트랜잭션이 있다면 중첩 트랜잭션을 시작한다.

### Propagation.MANDATORY

- 부모 트랜잭션 내에서 실행되며, 부모 트랜잭션이 없을 경우 Exception 발생

### Propagation.SUPPORT

- 부모 트랜잭션이 존재하면 부모 트랜잭션으로 동작하고, 없을 경우 non-transactional하게 동작한다.

### Propagation.NOT_SUPPORT

- non-transactional로 실행되며 부모 트랜잭션이 존재하면 일시 정지한다.

### Propagation.NEVER

- non-transactional로 실행되며 부모 트랜잭션이 존재하면 Exception이 발생한다.



### 