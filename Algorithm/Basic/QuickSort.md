# 퀵 정렬

- 중심값(Pivot)을 기준으로 두 자료의 키값을 비교하여 위치를 교환하는 방법. 분할정복 알고리즘의 하나
- Pivot을 잘 정해야 알고리즘의 효율이 좋아짐(최악의 경우를 방지하기 위해 보통 자료의 중간값을 이용함)

### 퀵정렬방법(오름차순 기준, Pivot: 가장 오른쪽값)

1. 가장 왼쪽에서 오른쪽으로 이동하면서 Pivot보다 큰 값을 찾는다(left or start)
   가장 오른쪽에서 왼쪽으로 이동하면서 Pivot보다 작은 값을 찾는다(right or end)
   단, left는 right보다 오른쪽으로 가지 못하고, right는 left보다 왼쪽으로 가지 못한다.
2. 이동 중 Pivot보다 작은 수와 큰 수를 발견하면, 두 자료(left, right)의 위치를 교환한다.
3. 1~2를 계속 반복하다가 left와 right가 만나면, 그 자료의 위치와 Pivot의 위치를 교환한다.(정렬 1번 완료)
4. 3번을 완료하면 Pivot값을 기준으로 왼쪽에는 작은 값, 오른쪽에는 큰 값이 저장됨
5. 나누어진 부분집합(작은값들, 큰값들)에서 다시 퀵 정렬을 수행한다. 단, 자료가 2개 이상인 집합에서만 수행



### 퀵정렬 과정 {80, 75, 10, 60, 15, 49, 12, 25}

- 정렬 과정
  - 가장 오른쪽의 값을 초기 피봇으로 설정
  - left는 pivot보다 큰 값, right는 피봇보다 작은 값을 만나면 위치 교환
  - left, right가 같은 자료를 가리키면, pivot과 위치 교환

| 1st Quick |    80(left)     |       75        |  10  |           60            |        15        |  49  |        12        | 25 (right, pivot) |
| :-------: | :-------------: | :-------------: | :--: | :---------------------: | :--------------: | :--: | :--------------: | :---------------: |
|  Step 1   | <u>80(left)</u> |       75        |  10  |           60            |        15        |  49  | <u>12(right</u>) |     25(pivot)     |
|  Step 2   | <u>12(left)</u> |       75        |  10  |           60            |        15        |  49  | <u>80(right)</u> |     25(pivot)     |
|  Step 3   |       12        | <u>75(left)</u> |  10  |           60            | <u>15(right)</u> |  49  |        80        |     25(pivot)     |
|  Step 4   |       12        | <u>15(left)</u> |  10  |           60            | <u>75(right)</u> |  49  |        80        |     25(pivot)     |
|  Step 5   |       12        |       15        |  10  | <u>60(left, right)</u>  |        75        |  49  |        80        | <u>25(pivot)</u>  |
|  Step 6   |       12        |       15        |  10  | <u>25</u><u>(pivot)</u> |        75        |  49  |        80        |     <u>60</u>     |

- 첫번째 정렬
  - 첫번째 정렬이 끝나면 pivot을 기준으로 왼쪽에는 pivot보다 작은 값, 오른쪽에는 pivot보다 큰 값들이 저장 됨
  - 왼쪽 값(부분집합1), 오른쪽 값(부분집합2)에 대한 퀵 정렬 수행
  - Pivot값을 정렬하는 가장 오른쪽 값으로 지정

| 2nd Quick |       12(left)        |  15  | 10(right,pivot)  |
| :-------: | :-------------------: | :--: | :--------------: |
|  Step 1   |       12(left)        |  15  | 10(right,Pivot)  |
|  Step 2   | <u>12(left,right)</u> |  15  | <u>10(pivot)</u> |
|  Step 3   |   <u>10(pivot)</u>    |  15  |        12        |

- 두번째 정렬
  - Pivot값 10보다 작은 값을 right에서 찾을 수 없으므로 12에서 left와 right가 만난다. => left,right 자료와 pivot위치 교환
  - pivot값의 왼쪽에는 부분집합이 없고, 오른쪽에는 부분집합의 원소가 2개이상이므로 퀵정렬 수행

| 3rd Quick |        15(left)        | 12(right, pivot) |
| :-------: | :--------------------: | :--------------: |
|  Step 1   | <u>15(left, right)</u> | <u>12(pivot)</u> |
|  Step 2   |    <u>12(pivot)</u>    |    <u>15</u>     |

- 세번째 정렬
  - right는 pivot보다 작은 값인데 작은 값이 없으므로, 15에서 left와 right가 동시에 가리키므로 pivo과 교환

| 4th Quick |    75(left)     |           49           |  80  | 60(right, pivot) |
| :-------: | :-------------: | :--------------------: | :--: | :--------------: |
|  Step 1   | <u>75(left)</u> |    <u>49(right)</u>    |  80  |    60(pivot)     |
|  Step 2   | <u>49(left)</u> |    <u>75(right)</u>    |  80  |    60(pivot)     |
|  Step 3   |       49        | <u>75(left, right)</u> |  80  | <u>60(pivot)</u> |
|  Step 4   |       49        |    <u>60(pivot)</u>    |  80  |    <u>75</u>     |

- 네번째 정렬
  - 49와 75를 교환
  - left 이동(코드 구현 상 left를 먼저 실행)
  - pivot과 75를 교환함

| 5th Quick |        80(left)        | 75(right, pivot) |
| :-------: | :--------------------: | :--------------: |
|  Step 1   | <u>80(left, right)</u> | <u>75(pivot)</u> |
|  Step 2   |    <u>75(pivot)</u>    |    <u>80</u>     |

- 다섯번째 정렬
  - left의 초기값은 80이므로 pivot값 보다 이미 큼(left로 지정)
  - pivot보다 작은 값을 찾기 위해 right 이동
  - 80에서 left, right가 만남 => pivot값과 교환
- 더 이상의 부분집합이 없으므로, 정렬을 종료함
- 결과

| Quick  |      |      |      |      |      |      |      |      |
| :----: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Result |  10  |  12  |  15  |  25  |  49  |  60  |  75  |  80  |



## 구현 - Python

- 정수 배열과 배열의 개수를 파라미터로 받는다.
- start(left), end(right) 또한 부분집합에서 값을 바꾸어야 하므로 입력 파라미터로 값을 전달 받는다.
- 주의사항: 책에 있는 그대로 C언어를 가져와서 만들어 봤지만, 파이썬에서는 후위증감 연산자를 지원하지 않아 구현방법이 조금 다르다

```python
value = [80, 75, 10, 60, 15, 49, 12, 25]
count = len(value)

def quick_sort(value, start, end):
    pivot = 0
    if start < end:
        pivot = partion_quick_sort(value, start, end)
        #두개의 부분집합에 대한 퀵정렬 수행
        quick_sort(value, start, pivot-1)
        quick_sort(value, pivot+1, end)
    print(value, start, end)

def partion_quick_sort(value, start, end):
    # 1. 가장 오른쪽에 있는 값을 pivot으로 정한다
    pivot = end
    left = start
    right = end

    while left < right:
        #2. value[left]는 pivot보다 큰 값, value[right]는 pivot보다 작은 값을 찾는다. => 나중에 교환해서 작은값이 왼쪽이 됨

       #left는 pivot보다 큰 값을 찾아야 하므로 while조건이 참이 되려면 left < pivot. 작은값일때 +1씩해서 큰값을 찾아내야함
        while value[left] < value[pivot] and left < right:
            left += 1

        #end 이동 pivot보다 작은 값을 찾아 반복 수행. right는 작은 값을 찾아야 하므로 while조건이 참이 되려면 right >= pivot. 큰 값일때 -1씩해서 작은 값을 찾아내야함
        while value[right] >= value[pivot] and left < right:
            right -= 1

        if left < right:
            print("교환 전 [pivot: {pivot}, left: {left}, right: {right}]".format(pivot=value[pivot], left=value[left], right=value[right]))
            print_array(value, start, end)

            #교환
            value[left], value[right] = value[right], value[left]

            print("교환 후[pivot: {pivot}, left: {left}, right: {right}]".format(pivot=value[pivot], left=value[left], right=value[right]))
            print_array(value, start, end)
            print("--------------------------------------")

        if left == right:
            print("교환 전 [pivot: {pivot}, left: {left}, right: {right}]".format(pivot=value[pivot], left=value[left], right=value[pivot]))
            print_array(value, start, end)

            value[right], value[pivot] = value[pivot], value[right]

            print("교환 후[pivot: {pivot}, left: {left}, right: {right}]".format(pivot=value[right], left=value[left], right=value[pivot]))
            print_array(value, start, end)

            print("\n")
    print("=====================================")
    print_array(value, start, end)
    print("=====================================\n")

    return right

def print_array(value, start, end):
    answer = []
    for i in range(start, end+1):
        answer.append(value[i])
    print(answer)

quick_sort(value, 0, count-1)

#결과
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7 /Users/wonik/Desktop/Algoritm/Sort/QuickSort.py
교환 전 [pivot: 25, left: 80, right: 12]
[80, 75, 10, 60, 15, 49, 12, 25]
교환 후[pivot: 25, left: 12, right: 80]
[12, 75, 10, 60, 15, 49, 80, 25]
--------------------------------------
교환 전 [pivot: 25, left: 75, right: 15]
[12, 75, 10, 60, 15, 49, 80, 25]
교환 후[pivot: 25, left: 15, right: 75]
[12, 15, 10, 60, 75, 49, 80, 25]
--------------------------------------
교환 전 [pivot: 25, left: 60, right: 25]
[12, 15, 10, 60, 75, 49, 80, 25]
교환 후[pivot: 25, left: 25, right: 60]
[12, 15, 10, 25, 75, 49, 80, 60]


=====================================
[12, 15, 10, 25, 75, 49, 80, 60]
=====================================

교환 전 [pivot: 10, left: 12, right: 10]
[12, 15, 10]
교환 후[pivot: 10, left: 10, right: 12]
[10, 15, 12]


=====================================
[10, 15, 12]
=====================================

[10, 15, 12, 25, 75, 49, 80, 60] 0 -1
교환 전 [pivot: 12, left: 15, right: 12]
[15, 12]
교환 후[pivot: 12, left: 12, right: 15]
[12, 15]


=====================================
[12, 15]
=====================================

[10, 12, 15, 25, 75, 49, 80, 60] 1 0
[10, 12, 15, 25, 75, 49, 80, 60] 2 2
[10, 12, 15, 25, 75, 49, 80, 60] 1 2
[10, 12, 15, 25, 75, 49, 80, 60] 0 2
교환 전 [pivot: 60, left: 75, right: 49]
[75, 49, 80, 60]
교환 후[pivot: 60, left: 49, right: 75]
[49, 75, 80, 60]
--------------------------------------
교환 전 [pivot: 60, left: 75, right: 60]
[49, 75, 80, 60]
교환 후[pivot: 60, left: 60, right: 75]
[49, 60, 80, 75]


=====================================
[49, 60, 80, 75]
=====================================

[10, 12, 15, 25, 49, 60, 80, 75] 4 4
교환 전 [pivot: 75, left: 80, right: 75]
[80, 75]
교환 후[pivot: 75, left: 75, right: 80]
[75, 80]


=====================================
[75, 80]
=====================================

[10, 12, 15, 25, 49, 60, 75, 80] 6 5
[10, 12, 15, 25, 49, 60, 75, 80] 7 7
[10, 12, 15, 25, 49, 60, 75, 80] 6 7
[10, 12, 15, 25, 49, 60, 75, 80] 4 7
[10, 12, 15, 25, 49, 60, 75, 80] 0 7

Process finished with exit code 0

```

