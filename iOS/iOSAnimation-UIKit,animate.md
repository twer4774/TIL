# iOS애니메이션 - UIKit, animate

iOS의 애니메이션 구현은 크게 두가지로 나눌 수 있음

- UIKit의 애니메이션 API를 사용하는 방법 - iOS4 이전에 사용되던 방식
- 코어 애니메이션을 사용하는 방법 - iOS4 이후부터 사용되는 방식

## UIKit의 애니메이션

- UIView.beginAnimations(), UIView.commitAnimations() 두 클래스메소드를 이용함
  1. UIView.begineAnimations()메소드를 호출
  2. 메소드가 호출되면, 화면상의 뷰의 위치나 색상 등 시각적 표현과 관련된 코드는 즉각적으로 뷰에 반영되지는 않는다.
  3. UIView의 클래스 메소드를 호출하여 애니메이션의 지속시간 등의 애니메이션 속성을 지정하거나 애니메이션이 완료되거나 중단되었을 때의 동작을 셀렉터를 통해서 지정할 수 있다.
  4. 애니메이션의 내용과 속성에 대한 지정이 완료되면 UIView.commitAnimations()를 호출
  5. 시스템은 별도의 스레드에서 애니메이션을 계산하고 화면에 표현함

  ```swift
  UIView.beginAnimations()
  self.circleView.frame = CGRect(x: 100, y: 20, width:100, height:100)
  UIView.commitAnimations()
  ```

- 문제점: 이벤트 처리가 셀렉터로만 넘겨져 애니메이션 코드를 작성하기 번거로웠음

## 코드블럭을 사용한 새로운 API

- UIView.animate(withDuration:animations:)를 기본으로 그와 관련된 함수들을 이용하는 방법

```swift
UIView.animate(withDuration: 1.5){
    circleView.center = CGPoint(x:100, y:20)
}
```

- 지속시간, 애니메이션의 옵션(타이밍 함수 등), 완료 핸들러등을 메소드의 각 인자로 분리함
- 애니메이션의 내용은 클로저안에 작성해 가독성이 높음
- 현재 사용되는 방법
- 관련 함수
  - animate(withDuration:animations:) - 기본 타이밍 함수
  - animate(withDuration:animations:completion:) - 완료 핸들러
  - animate(withDuration:delay:options:animations:completion:) - 딜레이 기능과 options으로 기본 외의 애니메이션 지정
  - animate(withDuration:delay: usingSpringWithDamping:initialSpringVelocity: options:animations:completion:) - 일반적인 곡선이 아닌 스프링에 의한 타이밍함수 사용(iOS10이상부터)
  - animateKeyframes(withDuration:delay:options: animations:completion:) - 키 프레임 애니메이션 표시
  - transition(with:duration:options:animations:completion:) - 뷰 트랜지션
  - transition(from:to:duration:options:completion) - 제 3의 뷰를 트랜지션
  - perform(_on:options:animations:completion:)
  - performWithoutAnimation(_:)