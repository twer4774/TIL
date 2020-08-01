# SQL Baic Enhancement(String)

- 대소문자 변환 함수
  - 저장되어 있는 컬럼명이 대문자인지 소문자인지 헷갈릴때 이용하면 좋음
  - oracle에서는 INITCAP()함수가 있음
    - 첫 글자만 대문자로 바꿈

```sql
SELECT UPPER(ename), LOWER(ename) FROM emp;
SELECT ENAME, SAL FROM emp WHERE LOWER(ename)="scott"; => 대문자인지 소문자인지 헷갈릴때이용
```

- 문자에서 특정 철자 추출 및 길이

```sql
SELECT SUBSTR("SMITH",1,3) FROM DUAL; => SMI 나옴
SELECT ename, LENGTH(ename) FROM emp;
```

- 문자에서 특정 철자의 위치 출력

```sql
SELECT INSTR("SMITH", "M") FROM DUAL;
 SELECT SUBSTR("abcdefgh@naver.com", INSTR("abcdefgh@naver.com", "@")+1) FROM DUAL; => naver.com
 SELECT SUBSTR("abcdefgh@naver.com", 1, INSTR("abcdefgh@naver.com", "@")-1) FROM DUAL; => abcdefg
```

- 특정 철자를 다른 철자로 변경

```sql
SELECT ename, REPLACE(sal, 0, '*') FROM emp; => 월급을 출력할 때 0을 *로 대체
SELECT ename, REGEXP_REPLACE(sal, '[0-3]', '*') as SALARY FROM emp; => 월급의 숫자 0~3까지를 *로 출력(정규식 이용)
```

- 추가 테이블 생성

```sql
CREATE TABLE TEST_ENAME(ENAME VARCHAR(10));

INSERT INTO TEST_ENAME VALUES('김인호');
INSERT INTO TEST_ENAME VALUES('안상수');
INSERT INTO TEST_ENAME VALUES('최영희');

SELECT REPLACE(ENAME, SUBSTR(ENAME,2,1), '*') as "전광판_이름" FROM test_ename;
=> 김*호 안*수 최*희
```

- 특정 철자를 N개만큼 채우기
  - 데이터를 시각화하기 유용

```sql
SELECT ename, LPAD(sal, 10, '*') as salary1, RPAD(sal, 10, '*') as salary2 FROM emp; => 월급 컬럼의 자릿수를 10자리로 하고 월급을 출력하고 남는 자리에 *로 채워 출력
SELECT ename, sal, LPAD('*', round(sal/100), '*') as bar_chart FROM emp; => 데이터 시각화
```

- 특정 철자 잘라내기
  이용하는 방법이 다름
  - mysql - 공백제거가 주 목적이며, 오라클의 LTRIM과 RTRIM을 이용하기 위해서는 TRIM의 옵션을 이용한다.
    - TRIM
      - 좌우 공백 제거 - SELECT TRIM(' aabbccbbaa ');
      - 좌우 문자 제거 - SELECT TRIM(BOTH 'a' FROM 'aabbccbbaa'); = > bbccbb
      - 좌측 공백 제거 - SELECT TRIM(LEADING FROM '  aabbccbbaa  ');
      - 좌측 문자 제거 - SELECT TRIM(LEADING 'a' FROM 'aabbccbbaa');
      - 우측 공백 제거 - SELECT TRIM(TRAILING FROM ' aabbccbbaa ');
      - 우측 문자 제거 - SELECT TRIM(TRAILING 'a' FROM 'aabbccbbaa');
    - RTRIM - 오른쪽 공백제거
    - LTRIM - 왼쪽 공백제거
  - oracle
    - SELECT 'smith', LTRIM('smith', 's'), RTRIM('smith', 'h'), TRIM('s' from 'smiths') FROM dual;

