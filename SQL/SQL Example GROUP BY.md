# SQL Example GROUP BY

> - 동명 동물 수 찾기
>
> - darklight
>
>   sublimevimemacs
>
>   MySQL 
>
> ###### 문제 설명
>
> `ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.
>
> | NAME             | TYPE       | NULLABLE |
> | ---------------- | ---------- | -------- |
> | ANIMAL_ID        | VARCHAR(N) | FALSE    |
> | ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
> | DATETIME         | DATETIME   | FALSE    |
> | INTAKE_CONDITION | VARCHAR(N) | FALSE    |
> | NAME             | VARCHAR(N) | TRUE     |
> | SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |
>
> 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.
>
> ##### 예시
>
> 예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | ------ | --------------- |
> | A396810   | Dog         | 2016-08-22 16:13:00 | Injured          | Raven  | Spayed Female   |
> | A377750   | Dog         | 2017-10-25 17:17:00 | Normal           | Lucy   | Spayed Female   |
> | A355688   | Dog         | 2014-01-26 13:48:00 | Normal           | Shadow | Neutered Male   |
> | A399421   | Dog         | 2015-08-25 14:08:00 | Normal           | Lucy   | Spayed Female   |
> | A400680   | Dog         | 2017-06-17 13:29:00 | Normal           | Lucy   | Spayed Female   |
> | A410668   | Cat         | 2015-11-19 13:41:00 | Normal           | Raven  | Spayed Female   |
>
> - Raven 이름은 2번 쓰였습니다.
> - Lucy 이름은 3번 쓰였습니다
> - Shadow 이름은 1번 쓰였습니다.
>
> 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | NAME  | COUNT |
> | ----- | ----- |
> | Lucy  | 3     |
> | Raven | 2     |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.



## 풀이

- MySQL
  - 같은 이름이 두번 이상 쓰인 경우만 조회 - NAME을 기준으로 그룹화한 후 이름이 두번 이상 쓰이는 조건(HAVING)필요
  - 이름이 없는 동물은 집계에서 제외 - IS NOT NULL 조건 필요
  - 결과는 이름 순으로 조회 - 오름차순(ASC)로 정렬

```SQL
SELECT NAME, COUNT(NAME) as "NAMECOUNT" FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING NAMECOUNT > 1 ORDER BY NAME ASC;
```



## 또다른 문제

> - 입양 시각 구하기(1)
>
> - darklight
>
>   sublimevimemacs
>
>   MySQL 
>
> ###### 문제 설명
>
> `ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.
>
> | NAME             | TYPE       | NULLABLE |
> | ---------------- | ---------- | -------- |
> | ANIMAL_ID        | VARCHAR(N) | FALSE    |
> | ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
> | DATETIME         | DATETIME   | FALSE    |
> | NAME             | VARCHAR(N) | TRUE     |
> | SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |
>
> 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
>
> ##### 예시
>
> SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | HOUR | COUNT |
> | ---- | ----- |
> | 9    | 1     |
> | 10   | 2     |
> | 11   | 13    |
> | 12   | 10    |
> | 13   | 14    |
> | 14   | 9     |
> | 15   | 7     |
> | 16   | 10    |
> | 17   | 12    |
> | 18   | 16    |
> | 19   | 2     |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.



## 풀이

- MySQL

```sQL
SELECT HOUR(DATETIME) as "HOUR", COUNT(HOUR(DATETIME)) as "COUNT" FROM ANIMAL_OUTS WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) <= 19 GROUP BY HOUR ORDER BY HOUR;
```

## 또 다른 문제2

> - 입양 시각 구하기(2)
>
> - darklight
>
>   sublimevimemacs
>
>   MySQL 
>
> ###### 문제 설명
>
> `ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다.
>
> | NAME             | TYPE       | NULLABLE |
> | ---------------- | ---------- | -------- |
> | ANIMAL_ID        | VARCHAR(N) | FALSE    |
> | ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
> | DATETIME         | DATETIME   | FALSE    |
> | NAME             | VARCHAR(N) | TRUE     |
> | SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |
>
> 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
>
> ##### 예시
>
> SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | HOUR | COUNT |
> | ---- | ----- |
> | 0    | 0     |
> | 1    | 0     |
> | 2    | 0     |
> | 3    | 0     |
> | 4    | 0     |
> | 5    | 0     |
> | 6    | 0     |
> | 7    | 3     |
> | 8    | 1     |
> | 9    | 1     |
> | 10   | 2     |
> | 11   | 13    |
> | 12   | 10    |
> | 13   | 14    |
> | 14   | 9     |
> | 15   | 7     |
> | 16   | 10    |
> | 17   | 12    |
> | 18   | 16    |
> | 19   | 2     |
> | 20   | 0     |
> | 21   | 0     |
> | 22   | 0     |
> | 23   | 0     |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.

### 풀이

- 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요
  - SUB QUERY를 이용하여 입양 건수 파악

- 이때 결과는 시간대 순으로 정렬해야 합니다.
  - 0~23의 HOUR을 순차적으로 나와야 함
  - SET을 이용하여 변수를 만들고 SELECT구문에 이용한다.

```sql
set @hour := -1;
SELECT (@hour := @hour + 1) as 'HOUR',
       (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE @hour < 23;
```

