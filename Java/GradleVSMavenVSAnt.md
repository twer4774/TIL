# 빌드 도구 Ant, Maven, Gradle

자바 빌드 도구

- 빌드도구 : 라이브러리 추가, 라이브러리 버전 동기화

  - Apache Ant
    -  초기의 JAVA 빌드 도구
    - 각 프로젝트에 대한 XML기반 빌드 스크립트 개발
    - 형식적인 규칙이 없음 : 결과물을 넣을 위치를 정확히 알려줘야 하며, 프로젝트에 특화된 Target과 Dependency를 이용해 모델링
    - 절차적 : 명확한 빌드 절차 정의 필요
    - 생명주기를 갖지 않기 때문에 각각의 target에 대한 의존관계가 일련의 작업을 정의해 주어야 함
    - 프로젝트가 복잡해질경우 build 과정을 이해하기 어려움
    - XML, Remote Repository를 가져 올 수 없음
    - 스크립트의 재사용이 어려움
  - Apache Maven
    - Dependecy를 리스트 형태로 관리
    - XML, remote repository를 가져 올 수 있음. mvnrepository.com에서 디펜던시를 복붙하여 사용하며, jar, classpath를 다운로드 할 필요 없이 선언만으로 사용 가능하다.
    - pom.xml에 디펜던시와 플러그인을 기재한다.
    - 단점
      - 라이브러리가 서로 종속할 경우 XML이 복잡해짐
      - 계층적인 데이터를 표현하기에 좋지만, 플로우나 조건부 상황을 표현하기엔 어려움
      - 편리하나 맞춤화된 로직 실행이 어려움
  - Apache Gradle
    - JVM 기반의 빌드도구로 Ant, Maven을 보완
    - 오픈소스기반의 build 자동화 시스템으로 Groovy 기반 DSL(Domain-Specific Language)로 작성
    - Build-by-convention을 바탕으로 함 : 스크립트 규모가 작고 읽기 쉬움
    - Multi 프로젝트의 빌드를 지원하기 위해 설계됨
    - 설정 주입방식(Configuration Injection)

  #### Gradle이 Maven보다 좋은점

  - Build라는 동적 요소를 XML로 정의하기 어렵다.
  - 가독성이 좋다
  - 의존관계가 복잡하게 얽힌 프로젝트 설정에 적합하다
  - 상속구조를 이용한 멀티 모듈 구현이 가능하다.
  - Groovy를 사용하기 때문에, 동적인 빌드는 Groovy 스크립트로 플러그인을 호출하거나 직접 코드를 짜면 된다.
  - Configuration Injection 방식을 사용해서 공통 모듈을 상속하는 단점을 보완했다. 설정 주입 시 프로젝트의 조건을 체크할 수 있으므로, 프로젝트별로 주입되는 설정을 다르게 할 수 있다.

  