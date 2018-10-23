# 프로그래머스문제

## 문제:

> 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
>
> 예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.
>
> ##### 제한사항
>
> - 문자열 s의 길이 : 50 이하의 자연수
> - 문자열 s는 알파벳으로만 이루어져 있습니다.
>
> |   입력    | 출력  |
> | :-------: | :---: |
> | "pPoooyY" | True  |
> |   "Pyy"   | False |
>
>



## 풀이 - Python

### 내 풀이

내 생각

-  "단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다." => 대, 소문자로 통일해 문자열을 변환시킨다.
- count로 문자의 갯수를 셀 수 있으므로 count로 문자를 세고, p, y의 갯수가 같은지 확인한다.

```python
def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    upperStr = s.upper()
    p = upperStr.count("P")
    y = upperStr.count("Y")
    if p == y | ( p == 0 & y == 0):
        answer = True
    else:
        answer = False

    return answer
```



### 결과

<img width="383" alt="result" src="https://user-images.githubusercontent.com/13410123/47367134-0a7ebe00-d71a-11e8-9258-ba549bea006a.png">

### 다른사람의 풀이

```python
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
```

- 풀이과정은 같으나 코드가 매우 짧아질 수 있음