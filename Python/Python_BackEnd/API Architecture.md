# API Architecture

## API Architecture

- 생각해야 할 요소
  - extensiblity(확장성)
  - reusability(재사용성)
    - 코드가 아니라 구조적인 재사용성에 초점
  - maintability(유지보수 가능성)
  - readability(가독성)



## Layered Pattern

- Presentaition Layer
  - 사용자 혹은 클라이언트 시스템과 직접 연결되는 부분
  - 웹사이트의 UI, 백엔드의 endpoint에 해당
  - API의 endpoint정의, HTTP Request를 읽어 들이는 로직 구현
- Business Layer
  - Business Logic 구현
    - ex) tweet은 300자를 넘기면 안된다
- Persistence Layer
  - 데이터베이스와 관련된 로직 구현