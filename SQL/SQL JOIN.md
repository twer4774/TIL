# SQL JOIN - 테이블 결합

- 교차결합 - FROM구에서 ,를 이용하면 곱집합이 이루어진다.

  ```sql
  SELECT * FROM 테이블명1, 테이블명2;
  
  SELECT * FROM sampleTableX;
  SELECT * FROM sampleTableY;
  
  #곱집합 구하기
  SELECT * FROM sampleTableX, sampleTableY;
  ```

### UNION 연겨과 결합 연결의 차이

확대 방향의 차이

- UNION - 세로로 더해짐(행방향확장)
- FROM - 가로로 더해짐(열방향확장)



## INNER JOIN으로 내부결합(최근에 통용적으로 사용)

```sql
#최근방식
SELECT * FROM 테이블명1 INNER JOIN 테이블명2 ON 결합조건;
SELECT 상품.상품명, 재고수.재고수 FROM 상품 INNER JOIN 재고수 ON 상품.상품코드 = 재고수.상품코드 WHERE 상품.상품분류 = '식료품';

#상품코드가 같은 행 검색 - 내부결합(예전방식)
SELECT 상품.상품명, 재고수.재고수 FROM 상품, 재고수 WHERE 상품.상품코드 = 재고수.상품코드 AND 상품.상품분류 = '식료품';
```

- 상품테이블과 메이커 테이블 내부결합

```sql
#메이커 테이블 작성
CREATE TABLE 메이커(
	'메이커코드' CHAR(4) NOT NULL,
  '메이커명' VARCHAR(30),
  PRIMARY KEY(메이커코드)
);

#상품 테이블과 메이커 테이블을 내부결합하기
SELECT S.상품명, M.메이커명 FROM 상품2 S INNER JOIN 메이커 M ON S.메이커코드 = M.메이커코드;
```

- 외부키 : 메이커 테이블의 메이커코드는 기본키. 상품테이블의 메이커코드는 외부키

  - ## 다른 테이블의 기본키를 참조하는 열이 외부키가 됨

## 예전방식의 내부결합(참고)

교차결합보다 내부결합이 자주 사용됨

- 내부결합 : 교차결합으로 계산된 곱집합에서 원하는 조합을 검색하는 것(WHERE 절 이용)

```sql
#상품 테이블 작성하기
CREATE TABLE 상품(
	'상품코드' CHAR(4) NOT NULL,
  '상품명' VARCHAR(30),
  '메이커명' VARCHAR(30),
  '가격' INTEGER,
  '상품분류' VARCHAR(30),
  PRIMARY KEY (상품코드)
);

#재고관리 테이블 작성하기
CREATE TABLE 재고수(
 '상품코드' CHAR(4),
  '입고날짜' DATE,
  '재고수' INTEGER
);

```

- 상품테이블의 기본키는 '상품코드', 이 열의 값을 알면 상품명을 포함한 상품 데이터를 참조할 수 있음
- 참조할 테이블의 기본키와 동일한 이름과 자료형으로 열을 만들어서 행을 연결하는 경우가 많음

- 위의 테이블에서 상품명, 재고수를 결합하여 테이블을 만들고 싶음

```sql
#상품테이블과 재고관리테이블 교차결합
SELECT * fROM 상품, 재고수;

#상품코드가 같은 행 검색 - 내부결합
SELECT * FROM 상품, 재고수 WHERE 상품.상품코드 = 재고수.상품코드;
```



### 외부결합(LEFT JOIN, RIGHT JOIN)

- 어느 한쪽에만 존재하는 데이터행을 어떻게 다룰지를 변경할 수 있는 결합 방법
  - 내부결합인 경우 한쪽에만 존재한다면 검색되지 않음

```sql
#외부 결합 - 기준이되는 상품테이블을 왼쪽에 기술
SELECT 상품3.상품명, 재고수.재고수 FROM 상품3 LEFT JOIN 재고수 ON 상품3.상품코드 = 재고수.상품코드 WHERE 상품3.상품분류 = '식료품';
```

