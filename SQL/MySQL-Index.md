# MySQL - Index

- ### 기억보단 기록을 참고 - https://jojoldu.tistory.com/243

- 지정한 컬럼들을 기준으로 메모리 영역에 일종의 목차를 생성하는 것
- select의 성능을 향상 시키는 것이 목적
  - 주의 : update, delete 행위가 느린것이지 update, delete하기 위한 select는 빠름
- 메모리에 접근하여 읽음으로써 디스크에 덜 접근하도록 함
- 인덱스의 갯수는 3~4개 정도가 적당

### 인덱스 키 값의 크기

- 페이지 : 인덱스의 단위(MySQL). size는 16KB로 고정

> 만약 본인이 설정한 인덱스 키의 크기가 16 Byte 라고 하고, 자식노드(Branch, Leaf)의 주소(위 인덱스 구조 그림 참고)가 담긴 크기가 12 Byte 정도로 잡으면, `16*1024 / (16+12) = 585`로 인해 하나의 페이지에는 585개가 저장될 수 있습니다.
> 여기서 인덱스 키가 32 Byte로 커지면 어떻게 될까요?
> `16*1024 / (32+12) = 372`로 되어 372개만 한 페이지에 저장할 수 있게 됩니다.
>
> 조회 결과로 500개의 row를 읽을때 16byte일때는 1개의 페이지에서 다 조회가 되지만, 32byte일때는 2개의 페이지를 읽어야 하므로 이는 성능 저하가 발행하게 됩니다.

### 인덱스 컬럼 기준

- 1 개의 컬럼만 인덱스를 걸어야 한다면, 해당 컬럼은 카디널리티가 가장 높은 것을 잡아야함
  - 카디널리디(Cardinality) : 해당 컬럼의 중복된 수치
    - ex) 성별, 학년등은 카덜리니티가 낮음 /  주민등록번호, 계좌번호는 카디널리티가 높음
- 인덱스를 최대한 효율적으로 뽑아 내려면 해당 인덱스로 많은 부분을 걸러내야 함
- 카디널리티가 높은 순에서 낮은 순으로 쿼리를 작성해야 효율이 빠름

```sql
#카디널리티가 낮은 순 -> 높은 순
CREATE INDEX IDX_SALARIES_INCREASE ON salaries (is_bonus, from_date, group_no);

#카디널리티가 높은 순 -> 낮은 순
CREATE INDEX IDX_SALARIES_DECREASE ON salaries (group_no, from_date, is_bonus);

#쿼리
select SQL_NO_CACHE * 
from salaries 
use index (IDX_SALARIES_INCREASE)
where from_date = '1998-03-30' 
and group_no in ('abcdefghijklmn10494','abcdefghijklmn3968', 'abcdefghijklmn11322', 'abcdefghijklmn13902', 'abcdefghijklmn100', 'abcdefghijklmn10406') 
and is_bonus = true;

select SQL_NO_CACHE * 
from salaries 
use index (IDX_SALARIES_DECREASE)
where from_date = '1998-03-30' 
and group_no in ('abcdefghijklmn10494','abcdefghijklmn3968', 'abcdefghijklmn11322', 'abcdefghijklmn13902', 'abcdefghijklmn100', 'abcdefghijklmn10406') 
and is_bonus = true;
 
```

### 페이징 성능 개선

- 인덱스를 이용하면 페이징 성능을 개선할 수 있음 - 기억보단 기록을 블로그 참조