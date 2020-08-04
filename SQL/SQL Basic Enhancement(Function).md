# SQL Basic Enhancement(Function)

- RANK - 데이터의 순위 출력
  - over 다음에 나오는 괄호 안에 출력하고 싶은 데이터를 정렬하는 SQL문장을 넣음

```SQL
#직업이 ANALYST, MANAGER인 사원들의 이름, 직업, 월급, 월급의 순위 출력
SELECT ename, job, sal, RANK() over (ORDER BY sal DESC) 순위 FROM emp WHERE job IN ('ANALYST', 'MANAGER');

#직업별로 묶어서 순위를 부여하기 위해 ORDER BY 앞에 PARTITION BY job을 사용
SELECT ename, sal, job, RANK() over (PARTITION BY job ORDER BY sal DESC) as 순위 FROM emp;
```

- DENSE_RANK
  - 데이터의 순위를 상세히 출력
  - RANK와 차이 
    - RANK - 동일한 순위가 있으면 다음 순위는 다다음순위가 됨(1위가 2명이면, 2등은 없고 3등이 됨)
    - DENSE_RANK - 동일한 순위가 있어도 다음 순위는 다음 순위(1위가 2명이여도, 2등은 2등)
  - 주의점. AS DENSE_RANK등수 (DENSE_RANK만 쓰면 SQL문으로 인식하여 별칭을 다른 것으로 바꿔야 함)

```SQL
SELECT ename, job, sal, DENSE_RANK() over (ORDER BY sal DESC) AS DENSE_RANK등수 FROM emp WHERE job IN ('ANALYST', 'MANAGER');
```

- NTILE
  - 등급 출력 - NTILE(등급화 묶음)

```SQL
#이름, 월급, 직업, 월급의 등급 출력 - 월급은 4등급으로 나눠 출력(1:0~25% / 2:25~50% ...)
SELECT ename, job, sal, NTILE(4) over (order by sal desc) 등급 FROM emp WHERE job in ('ANALYST', 'MANAGER', 'CLERK');
```

- CUME_DIST
  - 특정 데이터 순위의 비율 출력
    - 결과는 1등부터 14등까지 있음
      - 1등 -> 1/14 => 0.07
      - 2등 -> 2/14 => 2등이 두명이여서 3/14로 계산 => 0.214285714

```SQL
SELECT ename, sal, RANK() over (order by sal desc) as "순위", DENSE_RANK() over (order by sal desc) as "세밀한 순위", CUME_DIST() over (order by sal desc) as "순위의 비율" FROM emp;
```

- 데이터를 가로로 출력
  - MySQL - GROUP_CONCAT()
  - Oracle - LISTAGG()
    - within group(order by)가 항상 따라와야 사용가능함 - '~이내의'라는 뜻으로 gorup 다음에 나오는 괄호에 속한 그룹의 데이터를 출력하겠다는 의미

```SQL
#MySQL
SELECT deptno, GROUP_CONCAT(ename ORDER BY ename SEPARATOR ',') as "EMPLOYEE" FROM emp GROUP BY deptno;

#Oracle
SELECT deptno, LISTAGG(ename, ',') within group (order by ename) as EMPLOYEE FROM emp GROUP BY deptno;

#직업과 그 직업에 속한 사원들의 이름을 가로로 출력
#MySQL
SELECT job, GROUP_CONCAT(ename ORDER BY ename ASC SEPARATOR ',') as EMPLOYEE FROM emp GROUP BY job;

#Oracle
SELECT job, LISTAGG(ename, ',') within group (ORDER BY ename asc) as EMPLOYEE FROM emp GROUP BY job;
```

- 컬럼을 ROW로 출력
  - SUM+IF or DECODE

```SQL
#MySQL
SELECT SUM(IF(deptno = 10, sal, 0)) as "10", SUM(IF(deptno = 20, sal, 0)) as "20", SUM(IF(deptno = 30, sal, 0)) as "30" FROM emp;

#Oracle
SELECT SUM(DECODE(deptno, 10, sal)) as "10", SUM(DECODE(deptno, 20, sal)) as "20", SUM(DECODE(deptno, 30, sal)) as "30" FROM emp;			
#Oracle - pivot이용
SELECT * FROM (select deptno, sal from emp) PIVOT (sum(sal) for deptno in (10, 20, 30));
#Oracle - unpivot(row -> column)
SELECT * FROM order2 UNPIVOT (건수 for 아이템 in (BICYCLE, CAMERA, NOTEBOOK));
```

- 누적 데이터 출력
  - SUM OVER
    - OVER 다음의 괄호 안에는 값을 누적할 윈도우를 지정
      - UNBOUNDED PRECEDING - 맨 첫 번째 행을 가리킴
      - UNBOUNDED FOLLOWING - 맨 마지막 행을 가리킴
      - CURRENT ROW - 현재 행을 가리킴

```SQL
#ANALYST, MANAGER인 사원들의 사원 번호, 이름, 월급, 월급의 누적치 출력(제일 첫 번째 행부터 현재 행의 위치까지의 누적치가 나옴)
SELECT empno, ename, sal, SUM(SAL) OVER (ORDER BY empno ROWS BETWEEN UNBOUnDED PRECEDING AND CURRENT ROW) 누적치 FROM emp WHERE job in ('ANALYST', 'MANAGER');
```

- 집계 결과 출력
  - MySQL - WITH ROLLUP
  - Oracle - ROLLUP

```SQL
#MySQL
SELECT job, sum(sal) FROM emp GROUP BY job WITH ROLLUP;

#Oracle
SELECT job, sum(sal) FROM emp GROUP BY ROLLUP(job);
```

- 넘버링

```SQL
SELECT empno, ename, sal, ROW_NUMBER() OVER (ORDER BY sal DESC) 번호 FROM emp WHERE deptno = 20;
```

