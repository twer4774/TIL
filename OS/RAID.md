# RAID

- Redundant Array of Inexpensive Disk (값싼 디스크의 중복 배열법)
- 회사에서 서비스를 위해 많이 사용되는 기술
  - 데이터 공유 목적
- 파일시스템이 아닌 저장 시스템
- 싼 디스크를 여러개 갖다 붙여 하나의 디스크처럼 보이게 하며, 신뢰도와 성능을 모두 잡음

### RAID의 구성

- Raid Software
  - 디스크를 이어 붙일 때, 버스에 직접 붙이고 OS나 Raid SW를 이용해 Raid 적용
  - Raid HW보다 성능 및 신뢰도가 떨어짐
  - 저렴한 비용
- Raid Hardware
  - Raid Controller 밑에 디스크를 이어 붙여 Raid 적용
  - 보통 제조될때 하드웨어적으로 Raid 시스템을 수용하도록 구현하여 Raid HW라 부름
  - 비용이 높음
  - 성능 좋음

### 신뢰도

- 데이터가 휘발되지 않도록 저장
- 여러 디스크들을 이어붙이고, 여러 디스크에 동일한 내용을 저장한다면 신뢰도 증가함 - 싼 디스크를 이용하므로 여러개 사용 가능
- 신뢰도를 높이는 방법(중복 저장)
  - 미러링(Mirroring)
    - 여러 대비 백업용을 똑같이 만듦
    - 데이터는 그대로 보존되기 때문에 결함허용(Fault-Tolerance)라고 부름
    - 백업용 디스크를 많이 만들어야 하므로 디스크 용량이 최소 2배는 필요 
  - 패리티 디스크(Parity Disk)
    - 4개의 디스크가 있다면, 3개는 데이터를 저장하는데 쓰이고 하나는 패리티 디스크로 사용
    - 3개의 디스크 중 하나가 오류가 나면 패리티 디스크를 이용해 오류를 복구함
    - 문제점 - 디스크 두개가 나가면 복구를 할 수 없음 => 미러링보다 가격은 낮췄지만 신뢰도를 낮춘 방식
  - 에러 코렉팅 코드(ECC, Error Correcting Code)
    - 패리티 디스크보다 디스크를 추가로 더 둬서 해밍 코드 방식으로 동작하게 함
    - 데이터를 읽을때 마다 데이터의 오류 확인
    - 구현이 어려움
    - 비쌈
    - 더 좋은 방법들이 많아 현재는 사용하지 않음

### 성능

- 하나의 디스크에서 데이터를 읽는 것 VS 여러 디스크에서 동시에 읽는 것 => 여러 디스크에서 동시에 읽는 것이 빠름
- 성능을 높이는 두 가지 방법 - Striping(스트라이핑)
  - 비트 스트라이핑
    - Raid를 4개의 디스크로 구성한다면, 하나에 저장할 디스크 블럭을 4개로 쪼개어 저장
    - Read시에 4개의 데이터를 동시에 읽어 합쳐서 출력
    - 하나의 디스크에서 읽는 것보다 여러 디스크에서 읽는 것이 속도가 빠름
  - 블럭 스트라이핑
    - Raid를 4개의 디스크로 구성한다면, 디스크 블럭을 0부터 3까지 하나씩 순서대로 저장
      - 만약 5개의 디스크 블럭이 있으면 0: b1, b5 / 1: b2 / 2: b3 / 3: b4 저장
  - 두가지 방식중에 비트 스트라이핑은 잘 쓰이지 않음 => 블럭 스트라이핑을 많이 사용
    - 비트 레벨은 디스크를 조금씩 나눠서 쓰이므로 성능 향상의 폭이 크지 않음