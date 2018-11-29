# iOS애니메이션 - 코어 애니메이션(CALayer)

- UIKit 및 AppKit과 그래픽 하드웨어 및 OpenGL사이의 계층에 있는 그래픽 드롱잉 및 애니메이팅 인프라로, 뷰와 기타 시각 요소들에 애니메이션을 적용하는 데 사용

- 뷰에 대한 애니메이션을 앱의 인프라로서 수행하는 역할을 이해할 때 도움이 됨(굳이 뷰의 애니메이션을 코어애니메이션으로 구현할 필요는 없음)

- 애니메이션 품질과 앱의 성능 향상을 위한 돌파구

- 코어 애니메이션의 핵심 클래스: CALayer

  - 모서리, 마스크, 그림자등의 드롱잉 효과 적용 가능
  - 애니메이션 시에는 이 콘텐츠를 비트맵으로 캐싱하여 사용 가능
  - CPU에만 의존하는 Core Graphic과는 달리 GPU에 의한 하드웨어 가속 지원
  - 대상의 특성에 맞게 CAShapeLayer, CATileLayer, CATextLayer등의 세부 서브 클래스들로 정의 됨

- CALayer 클래스의 동작 과정

  1. CALayer 클래스는 특정 키패스의 값이 변경될 때 이를 애니메이팅 할 것인지를 결저앟는 needsDisplay(forKey:)에 의해 결정
  2. CALayer 클래스나 인스턴스는 특정한 키 패스 값이 변경될 때 이를 처리할 액션을 정의(action(forKey:))할 수 있으며, 레이어의 기학적/시각적 속성은 이미 기본적으로 이런 액션들을 정의해 두고 있음
  3. 특정한 키패스의 값이 변경되며, 해당 키패스에 해당하는 액션 객체가 생성되고, 이것이 레이어에 add되면서 실행 됨 (액션은 매 프레임마다 display()를 호출함)
  4. CALayer는 모델, 프레젠테이션 레이어 상태를 유지 함.
     - 모델: 레이어 객체의 실제 속성값을 그대로 나타내는 값
     - 프레젠테이션: 애니메이션이 진행되는 매 프레임마다 표시되는 일종의 캐시 같은 순간 값
  5. 2에서 결정된 액션은 매 프레임마다 display() 메소드를 호출하고, 이 메소드는 프레젠테이션 레이어의 상태를 화면에 렌더링 하는 일을 수행함

  => CALayer를 서브클래싱하면, needsDisplay(forKey:), action(forKey:), display() 값의 변경을 애니메이팅 할 수 있음

- 코어 애니메이션이 지원하는 두가지 방법

  - 암시적 애니메이션
    - CALayer 객체에서 뷰의 위치, 크기, 변형, 배경색, 투명도 등 시각적 특성을 나타내는 프로퍼티들을 변경 -> 각 프로퍼티의 키에 대해서 어떤 액션(주로 애니메이션)이 정의되어 있는데 이 액션들에 의해 애니메이션이 구동 함
  - 명시적 애니메이션
    - 어떤 레이어 객체에서 애니메이트 되어야 하는 프로퍼티의 키패스에 대해 CAAnimation객체를 생성
    - 애니메이션 객체에서 애니메이션에 대한 세부 사항을 기술해준 다음, 애니메이션 객체를 레이어 객체에 '추가'하게 되면 해당 애니메이션이 실행 됨

- 현재는 코어 애니메이션을 기반으로 게임을 만들 정도로 발전해 있음

- 