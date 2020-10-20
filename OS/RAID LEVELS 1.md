# RAID LEVELS 1

- Raid를 구성하는 방법으로 9단계로 나뉘어 짐

### Raid 0 - Block Striping

- 신뢰도를 고려하지 않고 Striping 함 - 성능 향상
  - striping : 디스크 블럭을 쪼개 나누어 저장
- 신뢰도 보다 성능이 우선시 되는 동영상 재생 등에서 이용 => 버퍼링을 줄이고 속도를 높임

### Raid 1 - Mirroring

- 성능보다 신뢰도 우선 - Raid 0와 반대
- 기준 디스크와 동일한 디스크를 복제하여 운영
- striping 기술을 사용하지 않음
- 중복 저장으로 디스크 낭비가 50%에 가까움

### Raid 2 - Bit Striping, ECC

- 성능과 신뢰도를 포함
- ECC(Error Correcting Code = 해밍코드)를 저장하는 디스크를 두어 디스크들의 에러 관리
- ECC의 계산 복잡도 때문에 잘 사용되지 않음

