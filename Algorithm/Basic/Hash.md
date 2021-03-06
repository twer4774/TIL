# 해시(Hash)

- 해시란 원래의 모양을 분해해서 잘게 만든 후 다시 하나의 모양으로 만드는 것
- 해시 값(해시): 계산과정을 거치면서 작아진 값
- 해시 함수: 해시를 계산하는 함수
- 해싱: 해시함수를 통해 해시값을 만드는 과정
- 해시검색: 해시를 이용해 검색 => 다른 검색알고리즘 보다 속도가 월등히 빠름
  - 검색키: 내가 검색하고자하는 자료를 가리키는 값 ex)학번으로 학생을 검색 => 학번이 검색키가 됨
  - 해시검색은 검색키에 대한 해시계산을 이용해 검색하는 방법
- 해시 테이블: 해시함수를 계산한 주소에 따라 자료를 저장하는 자료구조 -배열을 선호함(주소를 통해 바로 접근가능)
  - 버킷(Bucket): 해시 테이블에서 자료를 저장하는 단위. 해시 주소 이용
    - 하나의 고유한 해시(주소)에 대응하여 실제 자료가 저장되는 곳
    - 하나의 버킷에는 여러 자료가 저장될 수 있다(슬롯 이용)
  - 슬롯(Slot): 버킷 안에서 자료를 저장하는 단위. 실제로 자료가 저장되는 부분

## 검색 방법

### 계산 검색방법

- 해시검색
  - 해시 함수는 검색키의 입력값으로 단순 계산만하면 되므로 𝜪(1)의 시간 복잡도를 가진다.
  - 장점: 자료의 개수와 상관없이 상수시간 내에 계산 가능하다.

### 비교 검색방법

- 순차 검색, B-트리 검색
  - 비교 검색 방법의 경우 𝜪(nlogn)의 복잡도를 가진다 => 자료의 개수에 따라 검색시간이 느려진다.

=> 비교 검색 방법 보다 계산 검색방법(해시검색)이 더 우수함. 단, 최적의 성능을 위해 해시함수와 해시테이블 설계시 제약사항이 필요



## 해시 검색과정

### 자료 추가

1. 주소계산: 검색 키(입력값) -> 해시함수 -> 버킷의 주소(해시)
2. 해시 테이블 확인: 해시테이블에서 주소 값으로 자료가 저장 가능(이미 자료가 저장되어있지 않는지)한지 확인
3. 자료저장 -> 충돌 발생 시 다른 주소 값에 저장해야함

### 자료 검색

1. 주소 계산: 검색 키(입력값) -> 해시함수 -> 버킷의 주소(해시)
2. 해시 테이블 확인: 계산한 주소에 자료가 저장되어 있으면 검색 성공



## 해시 함수

- 해시 검색의 핵심이며, 해시 검색의 성능을 좌우함
- 좋은 해시함수의 기준
  - 모든 값이 골고루 나오는 것이 좋은 해시 함수
  - 각각의 key는 중복 없이 m개의 slot으로 동일한 확률로 해시되며(simple)
  - 각각의 key는 다른 key값의 해시값과 관계없이 해시된다.(uniformly)
  - M개의 slot이 있으면 중복 없이 확률적으로 m개의 slot에 골고루 나누어지는것이 좋으며 이를 simple uniform hasing이라고 부른다.

|  좋은 해시함수의 기준   | 설명                                                    |
| :---------------------: | :------------------------------------------------------ |
|     낮은 충돌 빈도      | 빈 공간을 찾아 자료를 저장 하는 정도                    |
| 높은 해시 테이블 사용률 | 해시 테이블에 자료가 고르게 분포. 충돌 빈도와 반비례 함 |
|     빠른 계산 시간      | 검색면에서 좋음                                         |

- 충돌이 발생하면 해시함수를 이용해 재계산해야 하므로 느려진다.



## 해시 함수로 사용되는 함수들

### 숫자 분석 기반의 해시 함수

- 검색키를 만드는 방법 => 다른 기법들과 함께 사용
- 검색 키의 특성을 알아내어 값의 분포를 분석함
- 예
  - K = 2011-108206
  - 2011 입학년도, 108 학과, 206 학생번호 => 입력 값으로 충돌 발생가능성이 낮은 값을 이용(학과번호,학생번호)
  - 키 값을 108206로 이용
- 검색키가 문자열인 경우
  - 1) 첫번째 문자 이용
    - ABC => A의 아스키코드(65) 이용
    - 단점: 충돌 빈도가 높음
  - 2) 문자열의 모든 코드 더하기
    - ABC => A(65) + B(66) + C(67) = 198
    - 단점: ABC, ACB, BAC 등 모든 값이 같음
  - 3)문자의 위치를 고려한 코드 더하기
    - 호너의방법(Horner's method)이용
      - 각 문자 코드 값을 자신의 위치에 해당하는 값과 곱하고 더하는 방법
      - f(x) = x³+x²+x+1 = ((1x+1)x+1)x+1
    - 문자열의 위치를 반영하기 위해 자릿수 31을 사용
      - ABC => ((65\*31)+66)\*31+67 = 65\*31\*31 + 66\*31 + 67 = 64578
      - CBA => ((67\*31)+66)\*31+65 = 67\*31\*31 + 66\*31 + 65 = 66498

### 나머지(제산: Division)함수

- 가장 쉽게 사용할 수 있는 함수
- 검색키(K) mod 해시 테이블 크기(M)
- ex) 검색키: 125, 테이블 크기: 100 => 125 mod(%) 100
  - 해시 = 25
- 장점: 방법이 쉬움. 어느 크기의 해시테이블에서도 사용가능
- 특징
  - 테이블의 크기가 소수(Prime number)일수록 충돌빈도수가 낮아짐 => 해시 테이블의 사용률이 높아짐
    - 해시 테이블의 크기가 10인 해시테이블에서 10보다 큰 소수인 11을 이용함
  - 해시테이블의 크기를 2의 지수승을 피하는 것이 좋다.
  - 해시테이블의 크기를 2의 지수승 -1을 피하는것이 좋다 => 2의 지수승과 별로 차이가 없기 때문
  - 해시테이블의 크기를 2의 지수승과 가깝지 않는 소수를 선택한다.

### 접기(접지: Folding) 함수

- 검색키를 분해하고 다시 조합해 새리를 만드는 함수 방법

- 검색 키의 크기가 해시 테이블의 크기보다 큰 경우 사용(K > M)

- 대표적으로 이동 접기 함수와 경계 접기 함수가 있음

- 접기함수의 과정

  - 1. 검색키 값 K를 해시테이블의 크기 M의 자릿수와 같은 크기로 분해
    2. 분해된 키 값들을 이용해 하나의 해시로 조합

- #### 이동 접기 함수(Shift folding function)

  - 분해된 부분들을 이동시킨 후 각 부분을 조합하는 접기 방법

  - 1. 보통 오른쪽 맞춤으로 정렬하여 끝자리를 기준으로 일렬이되도록 만듦
    2. 일치시킨 부분들을 더하기 연산을 이용해 조합

    ex) K = 1234512345(10자리), M=999(3자리)

  - #### 분해하기

    - 123	451	234	5 => M의 자릿수인 3으로 나눠 4묶음으로 나뉨

  - #### 이동 및 더하기

    - 오른쪽을 맞추어 일렬로 만든 후 더하기
      - 123
        451
        234
            5
        \-------
        813
      - 해시 값은 813이 됨
      - 오버플로우 발생 시에 초과한 자릿수를 버림 ex) 1234 => 234가 해시값이 됨

- #### 경계 접기 함수(Boundary folding function)

  - #### 분해하기 - 이동 접기함수와 같음

    - K = 1234512345(10자리), M=999(3자리)
    - 123 451 234 5

  - #### 이동 및 더하기

    - 경계 부분을 선택해 경계부분의 숫자를 뒤집음
    - 1. 마지막 5를 기준으로 잡았을 때, 5의 전 묶음인 234가 경계부분이 된다. 단, 경계부분과 인접해 있는 묶음 경계부분으로 삼을 수 없다. 즉 234의 전인 451묶음은 경계부분으로 만들 수 없다. => 하나 건너 뛰어서 123이 경계부분이 됨.
      2. 123이 경계부분이 되고 123이 마지막 값이므로 경계부분 찾는 것을 종료한다.
      3. 경계부분의 숫자들을 뒤집는다 234 -> 432, 123 -> 321 => 기존의 숫자의 자릿수를 변경해 충돌을 낮추는 방법
      4. 321
         451
         432
             5
         \------
         1209
      5. 해시 값은 오버플로우된 값이 됨 => 초과된 자릿수를 버려 209가 해시값이 됨

- ### 중간 제곱 함수(mid-square function)

  - 검색키의 일부에서 해시를 채취하는 방법
  - 먼저 키의 제곱값을 구한 후 제곱된 값 중에서 중간 부분을 해시 테이블의 주소로 사용
  - K=9541 => 9541\*9541 = 89<u>3214</u>01  해시값: 3214를 이용함