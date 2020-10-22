# RAID LEVELS 3

### RAID 6

- 디스크 2개의 실패까지 보호 가능
- 기본 4개의 디스크를 사용
- Raid5 보다 parity가 더 많이 존재하여 속도가 더 느림(Dual Parity)
- 실패율 테스트에서 효율이 가장 좋음
  - Raid 60을 제외(실패율 0.01)하고 가장 좋음 => 가성비 문제
    - Raid 6 + Raid 0 = Raid 60
    - Raid 6로 이중 패리티화하여 데이터 보호 / Raid 0으로 속도 증가

### RAID 10

- Raid6 보다 더 안전하고 빠르지만, 가용성이 Raid6가 나음