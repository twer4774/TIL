# Message Passing VS Shared Memory

- 메시지 교환 vs 메모리 공유
- IPC
  - Inter Process Communication
  - 협력을 위한 소통방법
  - 프로세스는 독립적인 프로세스와 협력적인 프로세스로 나뉨. IPC는 협력적인 프로세스에서 데이터를 공유하는 방법
  - 네트워킹에서도 사용되는 용어
    - 소켓
    - RPC(Remote Procedure Call) 
    - RMI 
- 협력 프로세스를 이용하는 이유
  - 정보공유
  - 속도개선
  - 모듈화
  - 멀티태스킹

## Messagin Passing(메시지 교환)

- 메모리 보호를 위해 OS가 대리로 전달
- 안전하며 동기화 문제가 없음(OS가 동기화 진행)
- 성능은 Shared Memory보다 안좋음
- 직접 전달과 간접전달방법
  - 직접 전달(direct commuication)
    - OS(커널)에 직접 메시지를 주고 전달
  - 간접 전달(indirect communication)
    - OS에 메시지를 넣어두고, 다른 프로세스가 OS에 접근하여 메시지 확보

## Shared Memory(메모리 공유)

- 두 프로세스 간의 공유된 메모리를 생성 후 이용
- 동기화 문제발생(어플리케이션에서 직접 동기화 필요)
  - 두 프로세스 간의 트랜잭션문제 발생 가능성 있음