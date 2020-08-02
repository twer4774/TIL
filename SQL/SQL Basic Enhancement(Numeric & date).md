# SQL Basic Enhancement(Numeric & date)

- 반올림 출력, 버림
  - mysql - TRUNCATE()
  - oracle - TRUNC()

```sql
 SELECT '876.567' as 숫자, ROUND(876.567, 1) FROM dual;
 SELECT '876.567' as 숫자, TRUNCATE(876.567, 1) FROM dual;
```

- 몫, 나머지 출력

```sql
SELECT FLOOR(10/3) FROM DUAL;
SELECT empno, MOD(empno, 2) FROM emp;
```

- 날짜 간 개월 수 출력

```sql
//MySQL
SELECT ename, TIMESTAMPDIFF(MONTH, hiredate, NOW()) fROM emp;
//Oracle
SELECT ename, MONTHS_bETWEEN(sysdate, hiredate) FROM emp;
```

- 개월 수 더한 날짜 출력
  - 지정한 날짜에 100달 뒤의 날짜 구하기

```sql
//MySQL
SELECT DATE_ADD('2020-08-01', INTERVAL 100 MONTH) FROM DUAL;
//Oracle
SELECT ADD_MONTHS(TO_DATE('2020-08-01', 'RRRR-MM-DD'), 100) FROM DUAL;
SELECT TO_DATE('2020-08-01', 'RRRR-MM-DD') + 100 FROM DUAL; => 100일 후 날짜 출력
```

- 시간 빼기

```sql
SELECT DATE_SUB(NOW(), INTERVAL 1 SECOND); == SELECT DATE_ADD(NOW(), INTERVAL -1 SECOND); 
```