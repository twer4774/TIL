# SQL Example JOIN

> - 없어진 기록 찾기
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
> 천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
>
> ##### 예시
>
> 예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면
>
> ```
> ANIMAL_INS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | ---- | --------------- |
> | A352713   | Cat         | 2017-04-13 16:29:00 | Normal           | Gia  | Spayed Female   |
> | A350375   | Cat         | 2017-03-06 15:01:00 | Normal           | Meo  | Neutered Male   |
>
> ```
> ANIMAL_OUTS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | NAME  | SEX_UPON_OUTCOME |
> | --------- | ----------- | ------------------- | ----- | ---------------- |
> | A349733   | Dog         | 2017-09-27 19:09:00 | Allie | Spayed Female    |
> | A352713   | Cat         | 2017-04-25 12:25:00 | Gia   | Spayed Female    |
> | A349990   | Cat         | 2018-02-02 14:18:00 | Spice | Spayed Female    |
>
> `ANIMAL_OUTS` 테이블에서
>
> - Allie의 ID는 `ANIMAL_INS`에 없으므로, Allie의 데이터는 유실되었습니다.
> - Gia의 ID는 `ANIMAL_INS`에 있으므로, Gia의 데이터는 유실되지 않았습니다.
> - Spice의 ID는 `ANIMAL_INS`에 없으므로, Spice의 데이터는 유실되었습니다.
>
> 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | ANIMAL_ID | NAME  |
> | --------- | ----- |
> | A349733   | Allie |
> | A349990   | Spice |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.



## 풀이

- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회 
  - 한쪽에는 데이터가 있고, 한쪽에는 없다 => 외부결합 LEFT JOIN or RIGHT JOIN
- 두 테이블을 외부조인 시킨 후 - RIGHT JOIN이용
- ANIMAL_INS와 ANIMAL_OUTS의 ANIMAL_ID가 같고 => ON에 정의
- ANIMAL_INS에서 ANIMAL_ID가 없는 경우를 찾는다 => IS NULL 이용

```sql
SELECT AO.ANIMAL_ID, AO.NAME
FROM ANIMAL_INS AI
RIGHT JOIN ANIMAL_OUTS AO
ON AO.ANIMAL_ID = AI.ANIMAL_ID
WHERE AI.ANIMAL_ID IS NULL;
```



## 또 다른 문제

> - 있었는데요 없었습니다
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
> 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.
>
> ##### 예시
>
> 예를 들어, `ANIMAL_INS` 테이블과 `ANIMAL_OUTS` 테이블이 다음과 같다면
>
> ```
> ANIMAL_INS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME     | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | -------- | --------------- |
> | A350276   | Cat         | 2017-08-13 13:50:00 | Normal           | Jewel    | Spayed Female   |
> | A381217   | Dog         | 2017-07-08 09:41:00 | Sick             | Cherokee | Neutered Male   |
>
> ```
> ANIMAL_OUTS
> ```
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | NAME     | SEX_UPON_OUTCOME |
> | --------- | ----------- | ------------------- | -------- | ---------------- |
> | A350276   | Cat         | 2018-01-28 17:51:00 | Jewel    | Spayed Female    |
> | A381217   | Dog         | 2017-06-09 18:51:00 | Cherokee | Neutered Male    |
>
> SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | ANIMAL_ID | NAME     |
> | --------- | -------- |
> | A381217   | Cherokee |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.

## 풀이

-  보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성 - 조인을 이용(내부, 외부 모두 가능)
- 결과는 보호 시작일이 빠른 순으로 조회해야합니다. - ORDER BY ANIMAL_INS.DATETIME

```sql
#외부 조인 이용
SELECT AI.ANIMAL_ID, AI.NAME FROM ANIMAL_INS AI LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID WHERE AI.DATETIME > AO.DATETIME ORDER BY AI.DATETIME;

#내부 조인 이용
SELECT AI.ANIMAL_ID, AI.NAME FROM ANIMAL_INS AI INNER JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID WHERE AI.DATETIME > AO.DATETIME ORDER BY AI.DATETIME;
```

