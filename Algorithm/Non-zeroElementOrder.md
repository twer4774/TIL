# 매일프로그래밍 실리콘밸리 문제9



## 문제

> 정수 배열(int array)이 주어지면 0이 아닌 정수 순서를 유지하며 모든 0을 배열 오른쪽 끝으로 옮기시오.
>
>  단, 시간복잡도는 O(n), 공간복잡도는 O(1)여야 합니다.
>
> 예)
>
> *Input: [0, 5, 0, 3, -1]*
>
> *Output: [5, 3, -1, 0, 0]*
>
> *Input: [3, 0, 3]*
>
> ﻿*Output: [3, 3, 0]*



## 풀이 - Python

### 내 풀이

##### 내 생각

- 0인 요소들을 배열에서 제거하고, 0을 제거한 만큼 뒤에다가 붙여주면 쉽지 않을까?
- 실행 결과 주어진 배열에 대해서는 성공했지만,  정확히 답이다! 라는 느낌이 없어서 답답하다.

```python
arr = [0, 5, 0, 3, -1]
arr2 = [3, 0, 3]
def test(s):
    answer = []
    for i in s:
        if i == 0:
            s.remove(i)
            s.append(0)
            print(s)
        answer = s
        print(answer)

    return answer
```



### 다른 풀이

##### 해설

0을 오르쪽으로 옮기는 것 보다 0이 아닌 정수를 왼쪽으로 옮긴다고 생각하면 쉽게 풀 수 있다.

```python
def sol(arr):
    # 0이 아닌 정수의 위치를 표현하는 j
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != j:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr
```

