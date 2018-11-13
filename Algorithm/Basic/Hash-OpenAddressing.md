# 충돌해결방법: 개방주소법

## 개방주소법(조사법)

- 해시 테이블에 계산한 주소가 비어있지 않으면, 다음 주소가 비었는지 조사
- 만약 주소가 비었다면 바로 저장하고, 비어있지 않다면 다음주소로 이동해 다시 빈 주소인지 확인을 반복 수행
- 다음 주소를 어떻게 정하는에 따라 선형 조사법, 제곱 조사법, 이중해싱 방법으로 나뉨

### 선형조사(Linear probing)

- 일정 상수만큼 증가시켜 다시 조사하는 방법

```
h(k) = (k + try_count) mod M
k -> (충돌) -> (k+1) -> (충돌) -> (k+2) - > (충돌) -> (k+3)...
```

- 장점: 비교적 간단한 계산으로 빈 주소를 찾음
- 단점: 일단 충돌이 발생하면 충돌이 시작된 주소 주위로 군집화 현상이 나타남

```
M: 5, 해시함수: mod 5, 저장되는 검색키: {1, 3, 8, 13}
1. 1 -> 1 mod 5 = 1
2. 3 -> 3 mod 5 = 3
3. 8 -> 8 mod 5 = 3(충돌) => 재계산 => (8+1) mod 5 = 4 => 4에 저장
4. 13 -> 13 mod 5 = 3(충돌) => 재계산 => (13+1) mod 5 = 4 => 충돌 =>(13+2) mod 5 = 0 => 0에 저장
```

### 제곱조사(Quadric probing)

- 충돌 발생시, 주소를 조사 횟수의 제곱 만큼 증가시켜 다시 조사
- 1차충돌 => 1², 2차충돌 => 2², 3차충돌 => 3² … => n차충돌 => n²

```
h(k) = (k + try_count * try_count) mod M
k -> (충돌) -> (k+1) -> (충돌) -> (k+4) -> (충돌) -> (k+9) ... ...
```

- 단점: 선형조사에 비해 군집화 현상이 적지만 여전히 존재함. 해시 테이블의 크기가 반드시 소수여야 함

```
M:5, 해시함수: mod 5, 저장되는 검색키: {1, 3, 8, 13}
1. 1 -> 1 mod 5 = 1
2. 3 -> 3 mod 5 = 3
3. 8 -> 8 mod 5 = 3(충돌) => 재계산 => (8+1) mod 5 = 4 => 4에 저장
4. 13 -> 13 mod 5 = 3(충돌) => 재계산 => (13+1) mod 5 = 4 => 충돌 =>(13+4) mod 5 = 2 => 2에 저장
```

### 이중해시(Double hashing)

- 충돌 발생시, 원래의 해시함수와 추가적인 해시함수를 이용해 주소 증가
- 장점: 군집화를 줄일 수 있음
- 대표적인 방법: 같은 조사간격을 이용하는 방법
  - (조사 간격) = M - (k mod M)

```
M:5, 해시함수: mod 5, 저장되는 검색키: {1, 3, 8, 13}
1. 1 -> 1 mod 5 = 1
2. 3 -> 3 mod 5 = 3
3. 8 -> 8 mod 5 = 3(충돌) => (조사간격) = M-(k mod M) => 5 - (8 mod 5) = 2(조사간격) ==> 이전 충돌 발생주소: 3, 조사간격: 2 => h(k) = (3+2) mod 5 = 0 =>> 0에 값 저장
4. 13 -> 13 mod 5 = 3(충돌) => (조사간격) = M - (k mod M) => 5 - (13 mod 5) = 2(조사간격) ==> 이전 충돌 발생주소: 3, 조사간격: 2 => h(k) = (3+2) mod 5 =0 => (충돌발생) -> 충돌발생주소:0, 조사간격:2 => h(k) = (0+2) mod 5 = 2 ==> 2에 값 저장
```

### 구현

- 파이썬에서 해시를 굳이 구현할 필요는 없다. 딕셔너리 타입을 사용하면 된다.
- 딕셔너리 타입은 해시로 구현되어있다.

#### 딕셔너리로 구현

```python
local_code = dict()
#None으로 채워진 해시테이블 선언
hash_table = list([None for i in range(10)])

#해시함수
def hash_func(data):
    return data % 5

#데이터 저장
def storage_data(hash_address, data):
    hash_table[hash_address] = data
   
#데이터 가져오기
def get_data(k):
   return hash_table[hash_func(k)]

#데이터 저장, 읽기
address = hash_func(1)
storage_data(address, "제주")
print(get_data(1))

#결과
제주
```



#### 파이썬으로 구현

```python
data_list = ["서울", "제주", "부산", "대전"]
#해시 테이블 만들기
hash_table = list([None for i in range(10)])

#해시함수 - 나머지함수이용
def hash_func(data):
    hash_value = data % 5
    return hash_value

#해시 테이블에 저장
#충돌회피 - 선형조사방법 이용
def storage_data(key_value, data):
    inc = 1
    hash_address = hash_func(key_value)

    if hash_table[hash_address] == None:
        hash_table[hash_address] = data
    else: #선형 조사방법으로 재귀를 이용함
        storage_data(key_value + inc, data)
        inc = inc + 1
def run(storeKey):
    j = 0
    for i in storeKey:
        storage_data(i, data_list[j])
        print(hash_table)
        j = j+1

run(storeKey)

#결과
[None, '서울', None, None, None, None, None, None, None, None]
[None, '서울', None, '제주', None, None, None, None, None, None]
[None, '서울', None, '제주', '부산', None, None, None, None, None]
['대전', '서울', None, '제주', '부산', None, None, None, None, None]
```

```python
#해시 검색 => 저장된 인덱스를 출력
#키를 가지고 검색을 시도함. 저장된 데이터가 키와 같은지 비교후 다르면 선형조사법으로 검색 재시도
def search_data(key, data):
    # print(id(hash_table[hash_func(key)]))
    inc = 1
    #해시함수로 해시테이블에 데이터가 저장되어있는지 확인, 있으면 주소 리턴
    if hash_table[hash_func(key)] == data:
        print(hash_func(key))
    #데이터가 다르다면 선형조사법을 이용해 해시함수 재계산 후 재실행
    else:
        search_data(key + inc, data)
    return hash_table[hash_func(key)]

search_data(1, "서울")
search_data(3, "제주")
search_data(8, "부산")
search_data(13, "대전")

#결과
1
3
4
0
```

