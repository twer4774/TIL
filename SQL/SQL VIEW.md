# SQL VIEW

테이블과 같은 부류의 데이터베이스 객체 중 하나

- SELECT 명령을 기록하는 데이터베이스 객체
- 이용하는 목적 : SELECT명령을 간략히 표기하기 위함(서브쿼리에서 이용하면 좋음)

```sql
CREATE VIEW 뷰명 AS SELECT명령
CREATE VIEW sampleView AS SELECT * FROM sampleTable;
SELECT * FROM sampleVIew;
#응용
SELECT * FROM (SELECT * FROM sampleTable) sq; 
#위와 같은 객체를 뷰 객체로 만들면 다음과 같이 사용 가능
SELECT * FROM sampleView;


DROP VIEW 뷰명
DROP VIEW sampleView;
```

### 뷰의 약점

- 뷰는 데이터베이스 객체로서 저장장치에 저장되지만, 테이블과 달리 대용량의 저장공간이 필요없음
- 단, CPU자원을 사용함

- 머티리얼라이즈드뷰(Materialized View) - MySQL에서는 사용불가(Oracle, DB2만 사용가능)
  - 뷰의 근원이 되는 테이블에 보관하는 데이터양이 많은 경우, 집계처리할 때도 뷰를 사용한다면 속도가 떨어짐
  - 위와 같은 현상을 방지하기 위해 머티리얼라이즈드 뷰를 사용함
    - 일반적인 뷰는 데이터를 일시적으로 저장했다가 쿼리가 종료될때 함께 삭제
    - 머티리얼라이즈드뷰는 테이블처럼 저장장치에 저장해두고 사용
- 함수테이블
  - 뷰를 구성하는 SELECT명령은 단독으로 실행할 수 있어야 함
  - 함수테이블을 이용해 SELECT명령을 단독으로 사용가능하게 만듦
  - 함수테이블은 사용자정의 함수로 만들며, 테이블을 결과값으로 반환해줌

