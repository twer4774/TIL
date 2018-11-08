# 병합 정렬

- 기존 자료를 동일한 원소 개수를 가진 부분집합으로 분할하고, 분할된 각 부분을 병합하면서 정렬 
- 몇개의 부분집합으로 나누느냐에 따라 n-way병합으로 나뉨

### 병합 과정(2원병합)

1) 분할 단계

기존 자료를 원소의 개수가 동일한 부분 집합으로 분할

Step 0:							 80 75 10 60 15 49 12 25

Step 1: 					80 75 10 60					15 49 12 25

Step 2:				80 75		 10 60			15 49		12 25

Step 3:			80		   75	   10	 		60	15		49	12			25



2) 병합 단계

Step 0:			80		75	10	 		60	15		49	12			25

Step 1:			      75 80		 10 60			15 49		12 25

Step 2:					10 60 75	80					12 15 25	49

Step 3: 								10 12 15 25 49 60 75 80

- 병합하는 과정에서 정렬이 이루어짐
- 첫번째 원소부터 마지막 원소까지 순서대로 비교함
  - {15 49} {12 25}를 정렬하는 경우
    - 가장 작은 값인 12가 선택됨
    - 자료가 선택된 집합을 다음 자료를 가리키도록 이동 12 -> 49
    - 위의 두 과정을 반복 수행 => 12 15 25
    - 부분집합이 하나만 남으면 남은 부분집합은 순서대로 정렬된 배열(위의 12 15 25)에 순서대로 추가함
      - 주의사항: 남은 부분집합은 정렬된 상태여야 함



### 구현 - Python

- 배열과 배열의 갯수를 파라미터로 받음
- 병합정렬은 정렬 도중 정렬대상이 되는 배열만큼 추가 메모리가 필요함 => 버퍼 필요

```python
value = [80, 75, 10, 60, 15, 49, 12, 25]

#분할 단계 - 재귀
def merge_sort(value):
    #자료가 하나밖에 없을 때
    if len(value) <= 1:
        return value
    middle = len(value)//2

    #분할과정
    leftList = value[:middle]
    rightList = value[middle:]

    #재귀 함수로 분할 한 부분집합을 다시 분할
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)

    print(leftList, rightList)

    #병합
    return merge(leftList, rightList)

#병합 단계
def merge(left, right):
    buffer = []

    #두 부분집합의 갯수가 1개 이상일때 수행
    while len(left) > 0 or len(right) > 0:
        #두 부분집합이 모두 1개이상의 자료가 있을 때
        if len(left) > 0 and len(right) > 0:
            #left와 rirght의 자료 비교
            #left의 자료가 크면 left의 자료를 버퍼에 저장하고, 인덱스를 1 올린다
            if left[0] <= right[0]:
               buffer.append(left[0])
               left = left[1:]
            #right의 자료가 크면 right의 자료를 버퍼에 저장하고, 인덱스를 1 올린다
            else:
                buffer.append(right[0])
                right = right[1:]
        #두 집합 중 추가되지 않은 자료들을 순서대로 버퍼에 추가한다.
        #주의사항: 추가되는 자료들은 정렬되어있다(여기서는 완전분할되어 병합시 정렬 되므로, 신경쓸 필요없음)
        elif len(left) > 0:
            buffer.append(left[0])
            left = left[1:]
        elif len(left) == 0:
            buffer.append(right[0])
            right = right[1:]

    return buffer

print(merge_sort(value))

#결과
[80] [75]
[10] [60]
[75, 80] [10, 60]
[15] [49]
[12] [25]
[15, 49] [12, 25]
[10, 60, 75, 80] [12, 15, 25, 49]
[10, 12, 15, 25, 49, 60, 75, 80]
```

