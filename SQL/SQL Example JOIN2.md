# SQL Example JOIN2

> - 오랜 기간 보호한 동물(1)
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
> `ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.
>
> | NAME             | TYPE       | NULLABLE |
> | ---------------- | ---------- | -------- |
> | ANIMAL_ID        | VARCHAR(N) | FALSE    |
> | ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
> | DATETIME         | DATETIME   | FALSE    |
> | NAME             | VARCHAR(N) | TRUE     |
> | SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |
>
> 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
>
> ##### 예시
>
> 예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면
>
> ```
> ANIMAL_INS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME   | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | ------ | --------------- |
> | A354597   | Cat         | 2014-05-02 12:16:00 | Normal           | Ariel  | Spayed Female   |
> | A373687   | Dog         | 2014-03-20 12:31:00 | Normal           | Rosie  | Spayed Female   |
> | A412697   | Dog         | 2016-01-03 16:25:00 | Normal           | Jackie | Neutered Male   |
> | A413789   | Dog         | 2016-04-19 13:28:00 | Normal           | Benji  | Spayed Female   |
> | A414198   | Dog         | 2015-01-29 15:01:00 | Normal           | Shelly | Spayed Female   |
>
> ```
> ANIMAL_OUTS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | NAME  | SEX_UPON_OUTCOME |
> | --------- | ----------- | ------------------- | ----- | ---------------- |
> | A354597   | Cat         | 2014-05-02 12:16:00 | Ariel | Spayed Female    |
> | A373687   | Dog         | 2014-03-20 12:31:00 | Rosie | Spayed Female    |
>
> SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | NAME   | DATETIME            |
> | ------ | ------------------- |
> | Shelly | 2015-01-29 15:01:00 |
> | Jackie | 2016-01-03 16:25:00 |
> | Benji  | 2016-04-19 13:28:00 |
>
> ※ 입양을 가지 못한 동물이 3마리 이상인 경우만 입력으로 주어집니다.
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.

# 풀이

- 아직 입양을 못 간 동물 중, 
  - ANIMAL_INS와 ANIMAL_OUTS에서 ANIMAL_ID 값은 일치하지만,
  - ANIMAL_OUTS.ANIMAL_ID가 NULL인 경우
- 가장 오래 보호소에 있었던 동물 3마리의 - LIMIT으로 3개만 출력
- 이름과 보호 시작일을 조회하는 SQL문을 작성 
- 이때 결과는 보호 시작일 순으로 조회 - ORDER BY

```sql
SELECT AI.NAME, AI.DATETIME 
FROM ANIMAL_INS AI 
LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID 
WHERE AO.ANIMAL_ID IS NULL
ORDER BY AI.DATETIME 
LIMIT 3;
```





## 또 다른 문제

> - 보호소에서 중성화한 동물
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
> `ANIMAL_OUTS` 테이블은 동물 보호소에서 입양 보낸 동물의 정보를 담은 테이블입니다. `ANIMAL_OUTS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `NAME`, `SEX_UPON_OUTCOME`는 각각 동물의 아이디, 생물 종, 입양일, 이름, 성별 및 중성화 여부를 나타냅니다. `ANIMAL_OUTS` 테이블의 `ANIMAL_ID`는 `ANIMAL_INS`의 `ANIMAL_ID`의 외래 키입니다.
>
> | NAME             | TYPE       | NULLABLE |
> | ---------------- | ---------- | -------- |
> | ANIMAL_ID        | VARCHAR(N) | FALSE    |
> | ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
> | DATETIME         | DATETIME   | FALSE    |
> | NAME             | VARCHAR(N) | TRUE     |
> | SEX_UPON_OUTCOME | VARCHAR(N) | FALSE    |
>
> 보호소에서 중성화 수술을 거친 동물 정보를 알아보려 합니다. 보호소에 들어올 당시에는 중성화[1](https://programmers.co.kr/learn/courses/30/lessons/59045#fn1)되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.
>
> ##### 예시
>
> 예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면
>
> ```
> ANIMAL_INS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME      | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | --------- | --------------- |
> | A367438   | Dog         | 2015-09-10 16:01:00 | Normal           | Cookie    | Spayed Female   |
> | A382192   | Dog         | 2015-03-13 13:14:00 | Normal           | Maxwell 2 | Intact Male     |
> | A405494   | Dog         | 2014-05-16 14:17:00 | Normal           | Kaila     | Spayed Female   |
> | A410330   | Dog         | 2016-09-11 14:09:00 | Sick             | Chewy     | Intact Female   |
>
> ```
> ANIMAL_OUTS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | NAME      | SEX_UPON_OUTCOME |
> | --------- | ----------- | ------------------- | --------- | ---------------- |
> | A367438   | Dog         | 2015-09-12 13:30:00 | Cookie    | Spayed Female    |
> | A382192   | Dog         | 2015-03-16 13:46:00 | Maxwell 2 | Neutered Male    |
> | A405494   | Dog         | 2014-05-20 11:44:00 | Kaila     | Spayed Female    |
> | A410330   | Dog         | 2016-09-13 13:46:00 | Chewy     | Spayed Female    |
>
> - Cookie는 보호소에 들어올 당시에 이미 중성화되어있었습니다.
> - Maxwell 2는 보호소에 들어온 후 중성화되었습니다.
> - Kaila는 보호소에 들어올 당시에 이미 중성화되어있었습니다.
> - Chewy는 보호소에 들어온 후 중성화되었습니다.
>
> 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | ANIMAL_ID | ANIMAL_TYPE | NAME      |
> | --------- | ----------- | --------- |
> | A382192   | Dog         | Maxwell 2 |
> | A410330   | Dog         | Chewy     |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.
>
> ------
>
> 1. 중성화를 거치지 않은 동물은 `성별 및 중성화 여부`에 Intact, 중성화를 거친 동물은 `Spayed` 또는 `Neutered`라고 표시되어있습니다. [↩](https://programmers.co.kr/learn/courses/30/lessons/59045#fnref1)

## 풀이

- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물
  - 중성화 수술을 원래대로 되돌릴 수 없기 때문에 ANIMAL_INS.SEX_UPON_INTAKE와 ANIMAL_OUTS.SEX_UPONN_OUTCOME의 값이 다르면 된다.
- 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회하는 SQL 문을 작성해주세요.

```sql
SELECT AI.ANIMAL_ID, AI.ANIMAL_TYPE, AI.NAME 
FROM ANIMAL_INS AI 
LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID 
WHERE AI.SEX_UPON_INTAKE != AO.SEX_UPON_OUTCOME 
ORDER BY AI.ANIMAL_ID;
```

