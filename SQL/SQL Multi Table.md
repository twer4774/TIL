# SQL Multi Table 복수의 테이블 다루기

## 집합연산

### UNION

- 합집합
  - 열의 이름은 달라도, 열의 개수와 자료형이 서로 같아야 함(전체데이터(*)를 가져오는 경우)
  - *를 쓰지않고 열을 따로 지정하여 사용하는 경우, UNION 사용가능

```sql
SELECT * FROM sample1 UNION SELECT * FROM sample2; 
```

### UNION을 사용할 때의 ORDER BY

- 가장 마지막 SELECT 명령에만 지정하며, 데이터 컬럼명이 같아야 함(다르다면 아래와 같이 AS를 이용해 통일 시켜줌)

```sql
SELECT a AS c FROM sample1 UNION SELECT b AS c FROM sample2 ORDER BY c; 
```

### UNION ALL

- 기본적으로 UNION은 합집합이므로, 중복되는 요소는 자동으로 제거됨
- UNION ALL은 중복을 생략하지 않고 합침

```sql
SELECT * FROM sample1
UNION ALL
SELECT * FROM sample2;
```

### 교집합과 차집합

- MySQL에서는 지원하지 않음