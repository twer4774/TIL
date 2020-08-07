# SQL CONSTRAINT(제약)

- 테이블에 제약을 설정하여 저장될 데이터를 제한할 수 있음
- 제약의 종류
  - NOT NULL
  - Primary Key(기본키) 제약
  - 외부참조 제약 등

### 테이블 작성시 제약 정의

- CREATE TABLE로 테이블을 작성할 때 제약을 같이 정의
  - ALTER TABLE로 제약을 지정하거나 변경 가능
- 열 제약 - 열에 대해 정의하는 제약

```sql
CREATE TABLE sampleTable(
	a INTEGER NOT NULL,
	b INTEGER NOT NULL UNIQUE,
	c VARCHAR(30)
);

```

- 테이블제약 - '복수열에 의한 기본키 제약'처럼 한 개의 제약으로 복수의 열에 제약을 설명하는 경우(기본키 제약)

```sql
CREATE TABLE sampleTable(
	no INTEGER NOT NULL,
  sub_no INTEGER NOT NULL,
  name VARCHAR(30),
  PRIMARY KEY (no, sub_no)
);
```

- 제약에 이름 붙이기 - CONSTRAINT 키워드 사용
  - 관리하기 쉬워지므로 가능한 한 이름을 붙이는게 좋음

```sql
CREATE TABLE sampleTable(
	no INTEGER NOT NULL<
  sub_no INTEGER NOT NULL,
  name VARCHAR(30),
  CONSTRAINT pkey_sample PRIMARY KEY(no, sub_no)
);
```

### 제약 추가

- 기존 테이블에 제약 추가
- 열 제약 추가
  - 주의 사항 - 제약을 변경하기 전에 변경할 제약사항을 위반하는 데이터가 있는지 먼저 검사할것
    - ex) c를 NOT NULL로 변경할 경우, c의 데이터 중 NULL인 데이터가 없는지 검사 필요

```sql
ALTER TABLE sampleTable MODIFY c VARCHAR(30) NOT NULL;
```

- 테이블 제약 추가
  - ALTER TABLE의 ADD 하부명령으로 추가
  - 이미 기본키가 설정되어 있는 테이블에 추가로 기본키를 작성할 수는 없음
  - 기존의 데이터가 변경할 제약사항을 위반하지 않는지 검사 필요

```sql
ALTER TALBE sampleTable ADD CONSTRAINT pkey_sample PRIMARY KEY(a);
```

### 제약 삭제

- 열 제약 삭제 - ALTER TABLE MODIFY 이용

```sql
ALTER TABLE sampleTable MODIFY c VARCHAR(30);
```

- 테이블 제약 삭제 - ALTER TABLE DROP 이용

```sql
ALTER TABLE sampleTable DROP CONSTRAINT pkey_sample;

#기본키는 데이블당 하나만 설정가능하기 때문에 제약명을 지정하지 않아도 됨(MySQL)
ALTER TABLE smpleTable DROP PRIMARY KEY;
```

### 기본키

```sql
CREATE TABLE sampleTable(
	p INTEGER NOT NULL,
  a VARCHAR(30),
  CONSTRAINT pkey_sample PRIMARY KEY(p)
);
```

- p 가 기본키 - 기본키는 NOT NULL 제약이 걸려있어야 함
- 기본키는 데이블의 행 한개를 특정할 수 있는 검색 키 - 기본키로 설정된 열이 중복하는 데이터 값을 가지면 제약에 위반

- 기본키 제약 = 유일성 제약
  - 중복되는 데이터를 사용할 수 없으므로, INSERT와 UPDATE시에 추가, 변경하고자하는 데이터를 확인해야 함