# 스레드(Thread)

- iOS프로세스는 하나의 메인 스레드를 가짐

- 백그라운드 스레드를 Worker, Secondary Thread라고 부름

- 메인 스레드에서 모든 작업을 처리하면 구현하기 편하지만, UI응답이 느려짐

- iOS에서 스레드 작업 처리

  - Operation
  - GCD

- Task: 스레드의 작업 단위 -> Selector or Closure로 구현

  - 실행방식
    - Serial방식: Task를 지정된 순서대로 실행 => 동기방식
    - Concurrent방식: 다수의 Task를 동시에 실행 => 비동기방식

- Operation: 백그라운드 스레드에서 실행할 Task를 캡슐화한 객체

  - Operation Queue로 Operation의 실행 관리.
  - Operation Queue는 기본적으로 백그라운드 스레드에서 Operation을 실행
  - autorelease pool 수동 생성

- ```swift
  OperationQueue.main
  ```


## Main Thread

- 사용자 이벤트와 UI 업데이트를 처리하는 특별한 스레드
- UIKit은 앱 시작 시점에 메인 스레드를 자동으로 생성
- 긴 시간이 소요되는 작업은 메인스레드에서 실행하는 것을 지양 함
  - 파일을 읽거나 네트워크 응답을 기다리는 경우 백그라운드 스레드에서 실행해야 함
- 메인 스레드가 생성될때 기본 Autorelease Pool이 함께 생성됨

### 동기화

- 여러 스레드가 동시에 동일한 리소스에 접근하는 경우 경합 상황 발생
- 리소스 경합을 해결하는 방법
  - 디자인 패턴을 활용해 동시에 접근되는 리소스 제거(추천 방법)
  - 위의 방법으로 해결하지 못할 시 동기화 구현
- 동기화 방법
  - 동시에 접근할 수 없는 영영을 Critical Section으로 지정하고 스레드가 접근하는 순서를 조절하는 작업
  - 대표 기술: Mutex, Semaphore
- 뮤텍스(Mutual Exclusion Lock)
  - Lock: 열쇠, Critical Section: 금고 => Lock을 획득한 후 Critical Section에 접근해야 함
- 세마포어
  - 동시에 접근할 수 있는 스레드의 수를 제한
  - 뮤텍스는 접근할 수 있는 스레드가 1로 고정된 세마포어
  - 세마포어는 제한할 양의 스레드 수를 저장함 -> 스레드가 Critical Section에 접근하기 위해 Lock을 획득할 때마다 저장된 스레드의 갯수를 줄여 스레드 수를 제한 함



## GCD(Grand Central Dispatch)

- iOS에서 스레드를 직접 다루지 않고 동시성 문제를 처리하는 핵심 기술
- 장점
  - 스레드 생성과 관리를 안정적으로 처리
  - 스레드 풀을 통해 스레드 재사용
  - 직관적이고 단순한 API제공
  - 어셈블리 최적화를 통해 빠른 성능 제공
  - 메모리를 효율적으로 사용
  - 동기화 문제를 유연하게 처리
- Task는 블록을 통해 캡슐화 됨. Dispatch Queue에 블록을 추가하면 나머지 작업은 GCD가 자동으로 처리함
- GCD는 사용가능한 시스템 자원을 기반으로 동시에 처리할 수 있는 작업의 수를 관리

### Dispatch Queue

- 작업을 관리하고 싫행 순서를 제어. FIFO 방식
- 스레드에 안전하므로 다수으 스레드에서 동시에 접근 가능함
- Autorlease Pool을 자동으로 생성해 줌

```swift
let serialQueue = DispatchQueue(label: "queue_name")

//main dispatch queue
let mainQueue = DispatchQueue.main

//Concurrent Dispatch Queue(Global Queue)
//작업을 동시에 실행함. High, Default, Low, Background로 구분
let golbalQueue = DispatchQueue.global(priority: DispatchQueue, GlobalQueuePriority.high)
//DispatchQueue 클래스의 생성자에 .concurrent 옵션 -> Concurrent Dispatch Queue 생성 가능
let concurrentQueue = DispatchQueue(label: "queuename", attributes: .concurrent)
```



## 앱을 구현할 때 염두에 두어야 할 사항

- 뷰를 조작하는 작업, 애니메이션 작업 등 UI와 연관된 작업은 메인 스레드에서 실행
- 파일 읽기, 네트워크 응답 대기 등 오랜 시간이 걸리는 작업은 백그라운드 스레드에서 실행
- 앱 시작 시점에는 UI를 최대한 빨리 구성해야 하므로 UI구성에 반드시 필요한 작업을 제외하고 백그라운드 스레드에서 실행

- 백그라운드에서 autorelease pool을 이용할 경우 백그라운드에 구현해 주어야 함(main스레드에서는 자동생성, 백그라운드에서는 직접 구현)