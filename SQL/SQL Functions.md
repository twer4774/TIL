# SQL FUNCTIONS

- 행 넘버 출력하기

```sql
#MySQL
SET @rownum:=0; SELECT @rownum:=@rownum+1, empno, ename, job, sal FROM emp WHERE (@rownum:=0)=0;
```

- 출력되는 행 제한하기
  - MySQL - LIMIT
  - Oracle - ROWNUM

```sql
#5개의 행만 출력
#MySQL - LIMIT만 쓰면 되지만, 행의 갯수를 알기 위해 위의 행 넘버 출력을 이용함
SET @rownum:=0; SELECT @rownum:=@rownum+1 as 'rownum', empno, ename, job, sal FROM emp WHERE (@rownum:=0)=0 LIMIT 5;

#Oracle
SELECT ROWNUM, empno, ename, job, sal FROM emp WHERE ROWNUM <= 5;
```

- 여러 테이블의 데이터를 조인하여 출력

```sql
#emp, dept의 사원번호가 일치할때 ename, loc을 출력
#EQUAL JOIN(EQUI JOIN) 이용 - 예전방식이며, 요즘 일반적으로 INNER JOIN 이용
SELECT ename, loc FROM emp, dept WHERE emp.deptno = dept.deptno;
SELECT ename, loc FROM emp INNER JOIN dept ON emp.deptno = dept.deptno;

#사원(EMP) 테이블과 급여 등급(SALGRADE) 테이블을 조인하여 이름, 월급 ,급여 등급 출력
#NON EQUI JOIN 이용
#salgrade - 급여 등급 테이블 / grade - 등급 / losal - 등급을 나누는 월급범위의 하단 / hisal - 월급범위의 상단(5등급이 제일 높음)
SELECT e.ename, e.sal, s.grade FROM emp e, salgrade s WHERE e.sal between s.losal and s.hisal;
```

- OUTER JOIN - EQUI JOIN으로 볼 수 없는 결과 데이터를 출력하기 위해 사용
  - MySQL - LEFT JOIN

```sql
#사원 테이블과 부서 테이블을 조인하여 이름과 부서 위치 출력. 단, BOSTON도 같이 출력하도록 함
#Oralcle
SELECT e.ename, d.loc FROM emp e, dept d WHERE e.deptno (+) = d.deptno;
```

- UNION
  - 여러개의 쿼리 결과 데이터를 위아래 하나의 결과로 출력하면서 중복된 데이터를 제거하는 명령어

```sql
#부서번호와 부서 번호별 토탈 월급을 출력하는데, 맨 아래 행에 토탈 월급을 출력
SELECT deptno, sum(sal)
FROM emp
GROUP BY deptno
UNION
SELECT null as deptno, sum(sal)
FROM emp;
```

