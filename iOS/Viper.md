# VIPER

- MVC패턴을 대체하기 위해 만들어진 패턴

- View, Interactor, Presenter, Entity, Router로 구성

- Entity = Model Object. 단순하게 모델의 속성들만 정의되어 있음

- Interactor : Entity를 조작. 어떠한 동작에 따라 모델 객체를 조작하는 로직을 가지고 있음. Interactor에서 조작이 이루어지더라도 View에는 아무런 영향을 주지 않는다.

- Presenter : Interactor에서 데이터를 가져오고 View에 뿌려주는 역할. View, Interactor, Router와 상호작용한다.

- Router(Wireframe) : 화면전환 담당. Presenter가 '언제'화면을 전환하는지 로직을 가지고 있다면, Router는 '어떻게' 화면을 전환하는지 알고 있음. 화면전환 애니메이션을 구현하고, ViewController를 생성하여 Presenter와 연결함

  