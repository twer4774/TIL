# SQL Basic

- 별칭 사용

```SQL
SELECT empno as "사원 번호", ename as "사원 이름", sal as "Salary" FROM emp;
```

- 연결연산자
  - 오라클의 경우 ||로 간단히 해결
  - MySQL은 CONCAT, CONCAT_WS 함수 이용
    - SELECT CONCAT(str1, str2 …);
    - SELECT CONCAT_WS(separator, str1, str2 …); 
      - SELECT CONCAT_WS(',','First name', 'Second name');
        -> First name, Last name

```sql
SELECT CONCAT(ename, sal) FROM emp;
SELECT CONCAT(ename, sal) as "ENAME||SAL" FROM emp;
SELECT CONCAT_WS('-', ename, sal) as "ENAME||SAL" FROM emp;
```

- 중복 제거

```sql
SELECT DISTINCT job FROM emp;
```

- 데이터 정렬
  - asc : 오름차순
  - desc : 내림차순

```sql
SELECT eanme, sal FROM emp ORDER BY sal asc;
select ename, sal as "월급" from emp order by sal asc; - sal을 월급으로 표시
```

- 데이터 검색

```sql
SELECT ename, sal, job FROM emp WHERE sal = 3000;
```

- 산술연산자

```sql
SELECT ename, sal*12 as "연봉" FROM emp WHERE sal*12 >= 36000;
SELECT ename, sal FROM emp WHERE sal BETWEEN 1000 AND 3000;
SELECT ename, sal FROM emp WHERE sal NOT BETWEEN 1000 AND 3000;
```

- Null처리
  - 표준 - COALESCE(필드, null일때 처리할 값) => 사용권장
  - mysql - ifnull(필드, null일때 처리할 값)
  - oracl - NVL(필드, null일때 처리할 값)

```sql
SELECT sal + COALESCE(comm, 0) FROM emp WHERE ename="KING";
SELECT sal + ifnull(comm,0) FROM emp WHERE ename="KING";
```

- 비교 연산자
  - % : 와일드 카드 아무 철자, 많은 철자가 와도 됨
  - _ : 철자의 숫자만큼 필요

```sql
SELECT ename, sal FROM emp WHERE ename LIKE "S%"; -s로 시작하는 사원들의 이름과 월급 출력
```

- 여러 개의 리스트 값 검색

```sql
SELECT ename, sal, job FROM emp WHERE job in ("SALESMAN", "ANALYST", "MANAGER");
SELECT ename, sal, job FROM emp WHERE (job = "SALESMAN" or job="ANALYST" or job="MANAGER");
=> 결과는 동일
```

- 논리 연산자

```sql
SELECT ename, sal, job FROM emp WHERE job="SALESMAN" AND sal >= 1200;
```

