# SQL Example IS NULL

> - 이름이 없는 동물의 아이디
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
> 동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.
>
> ##### 예시
>
> 예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME       | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | ---------- | --------------- |
> | A368930   | Dog         | 2014-06-08 13:20:00 | Normal           | NULL       | Spayed Female   |
> | A524634   | Dog         | 2015-01-02 18:54:00 | Normal           | *Belle     | Intact Female   |
> | A465637   | Dog         | 2017-06-04 08:17:00 | Injured          | *Commander | Neutered Male   |
>
> 이름이 없는 채로 들어온 동물의 ID는 A368930입니다. 따라서 SQL을 실행하면 다음과 같이 출력되어야 합니다.
>
> | ANIMAL_ID |
> | --------- |
> | A368930   |
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.
>
> ※ 2019년 9월 4일 13시: 예시가 헷갈린다는 의견이 많아, 본문의 예시를 수정하였습니다.

## 풀이

- IS NULL 이용

```sql
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL;
SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL; //이름이 있는 동물의 ID
```



## 또 다른 문제 (IFNULL 이용)

> - NULL 처리하기
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
> 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 No name으로 표시해 주세요.
>
> ##### 예시
>
> 예를 들어 `ANIMAL_INS` 테이블이 다음과 같다면
>
> | ANIMAL_ID | ANIMAL_TYPE | DATETIME            | INTAKE_CONDITION | NAME  | SEX_UPON_INTAKE |
> | --------- | ----------- | ------------------- | ---------------- | ----- | --------------- |
> | A350276   | Cat         | 2017-08-13 13:50:00 | Normal           | Jewel | Spayed Female   |
> | A350375   | Cat         | 2017-03-06 15:01:00 | Normal           | Meo   | Neutered Male   |
> | A368930   | Dog         | 2014-06-08 13:20:00 | Normal           | NULL  | Spayed Female   |
>
> 마지막 줄의 개는 이름이 없기 때문에, 이 개의 이름은 No name으로 표시합니다. 따라서 SQL문을 실행하면 다음과 같이 나와야 합니다.
>
> | ANIMAL_TYPE | NAME    | SEX_UPON_INTAKE |
> | ----------- | ------- | --------------- |
> | Cat         | Jewel   | Spayed Female   |
> | Cat         | Meo     | Neutered Male   |
> | Dog         | No name | Spayed Female   |
>
> ※ 컬럼 이름은 일치하지 않아도 됩니다.
>
> ------
>
> 본 문제는 [Kaggle의 Austin Animal Center Shelter Intakes and Outcomes](https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes)에서 제공하는 데이터를 사용하였으며 [ODbL](https://opendatacommons.org/licenses/odbl/1.0/)의 적용을 받습니다.

## 풀이

- IF NULL을 이용하여 NULL인 이름에 No name을 대신 넣어 해

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name') as NAME, SEX_UPON_INTAKE FROM ANIMAL_INS;
```

