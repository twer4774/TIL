# SQL Basic Enhancement(Condition)

- IF문으로 SQL 구현
  - MySQL - IF(조건, 참, 거짓)
  - Oralce - DECODE(컬럼, 값, 참, 거짓)

```sql
#부서의 번호(deptno)에 따라 10이면 300, 20이면 400의 보너스를 출력
SELECT ename, deptno, IF(deptno = 10, 300, IF(deptno = 20, 400, 0)) as 보너스 FROM emp; => MySQL
SELECT ename, deptno, DECODE(deptno, 10, 300, 20, 400, 0) as 보너스 FROM emp; => Oracle

#사원번호가 짝수인지 홀 수 인지 출력
SELECT empno, mod(empno,2), IF(mod(empno,2) = 0, '짝수', '홀수') as 보너스 FROM emp; => MySQL
SELECT empno, mod(empno,2), DECODE(mod(empno,2), 0,'짝수', 1, '홀수') as 보너스 FROM emp; => Oracle
```

- CASE

  - CASE 

    ​	WHEN 조건

    ​	THEN '반환 값'

    ​	ELSE 'WHEN 조건에 해당 안되는 경우 반환 값'

```sql
#이름, 직업, 월급, 보너스를 출력 - 보너스는 월급이 3000이상이면 500을 출력, 월급이 2000-3000이면 300 출력, 1000-2000이면 200 출력, 나머지는 0 출력
SELECT ename, job, sal, CASE WHEN sal >= 3000 THEN 500 WHEN sal >= 2000 THEN 300 WHEN sal >= 1000 THEN 200 ELSE 0 END as 보너스 FROM emp WHERE job In('SALESMAN', 'ANALYST');
```

- GROUP BY - 그룹화
  - SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼 HAVING 조건식;
  - 유형별로 데이터를 가져오고 싶을 때 사용
  - GROUP BY - 특정 컬럼을 그룹화
  - HAVING - 특정 컬럼을 그룹화한 결과에 조건을 걺(WHERE는 그룹화하기 전, HAVING은 그룹화 후의 조건)

```sql
SELECT job, MAX(sal) FROM emp GROUP BY job; => 직업별로 최대 급여 금액
```

- MAX

```SQL
SELECT MAX(sal) FROM emp;

SELECT job, MAX(sal) FROM emp WHERE job='SALESMAN'; =>(Oracle) Error or Null : Max(sal)은 단일값이 나오는데 job은 리스트를 다 출력하려고 하니까 에러 / (MySQL) : 값이 잘 나옴
===>
#Oracle / MySQL
SELECT job, MAX(sal) FROM emp WHERE job='SALESMAN' GROUP BY job;
```

- MIN

```SQL
SELECT MIN(sal) FROM emp WHERE job='SALESMAN';
```

- AVG
  - 평균값 출력
  - 아래의 두 값의 결과는 다르게 나옴
  - 평균값을 작성할 때는 Null을 가진 개체수를 생각해야 한다.

```SQL
SELECT AVG(comm) FROM emp; => 550. null을 무시하고 평균(2200/4)
#NULL대신 0을 넣고 커미션을 다 더한 값에서 14로 나눔
SELECT ROUND(AVG(IFNULL(comm,0))) FROM emp; => 157. null을 0으로 바꾼뒤 평균
```

- SUM

```SQL
SELECT deptno, SUM(sal) FROM emp GROUP by deptno;
SELECT job, SUM(sal) FROM emp GROUP BY job ORDER BY sum(sal) DESC; => 직업과 직업별로 토탈 ㅜ얼급을 출력하는데 직업별 토탈 월급이 높은 것 부터 출력
SELECT job, SUM(sal) FROM emp GROUP BY job HAVING sum(sal) >= 4000;
```

- COUNT

```SQL
SELECT COUNT(empno) FROM emp;
```

