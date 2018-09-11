# 매일프로그래밍 실리콘밸리 문제10

## 문제

> String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.
> Given a string, find the longest substring that does not have duplicate characters.
>
> 예제)
>
> Input: “aabcbcbc”
>
> Output: 3 // “abc”
>
> Input: “aaaaaaaa”
>
> Output: 1 // “a”
>
> Input: “abbbcedd”
>
> ﻿Output: 4 // “bced”



## 풀이 - Python

### 내 풀이

- 일단, 서브스트링은 문자열을 자르는 역할을 한다. 예를 들면, a[0:3]처럼 이용해  a에 저장된 문자열을 0부터 2번째 요소까지 가져온다.

- 문자열 리터럴을 for in 구문으로 돌려서 풀어볼려고 생각했다.

- 중복된 char(문자)가 없으니까 Set의 특성을 이용해서 중복된 char를 없애려고 했다.
  aa가 나오면 set을 이용하면 a만 유지될 수 있기 때문에 가능할 것 같다.

  예)에서는 abc, bced 처럼 순서가 있지만, 어차피 중복된 값이 없는 것이기 때문에 순서는 상관 없지 않을까?

- 가장 긴 서브스트링을 찾는 것이므로, 아무리 없어도 최소 1개의 문자는 존재하니까 서브스트링의 최소값을 1로 둔다.

```python
arr1 = "aabcbcbc"
arr2 = "aaaaaaaa"
arr3 = "abbbcedd"
arr4 = "fbcdeabc" #내가 만든 입력 예
def solution(s):
    maxRepeat = 1
    stringLen = len(s)
    ls = list(s)
    temp = ls[0]
    for i in range(0, stringLen - 1):
        if ls[i] != ls[i + 1]:
            temp += (ls[i + 1])
            # print(temp)
            maxRepeat = len(set(temp))
        elif ls[i] == ls[i + 1]:
            temp = ls[i]
            # print(temp)
    print(maxRepeat)
    
solution(arr1)
solution(arr2)
solution(arr3)
solution(arr4)
```

![image-20180911194456103]

예상했던 결과대로 잘 나온다. 다른 특이한 테스트 케이스가 더 주어졌으면 좋았을 것 같다.



### 다른 풀이

#### 해설

- 풀이에서는 자바의 해쉬맵을 사용했다. string의 각 char를 확인하여 해쉬맵에 있다면 substring의 시작 index를 그 다음 char의 인덱스로 두면 된다고 한다

```python
def sol(string):
    ret = start = 0 #ret과 start를 0으로 둔다.
    s_dict = dict() #사전 객체를 생성한다.
    for i in range(len(string)):
        if string[i] in s_dict: #사전 객체 안에 문자가 존재한다면, 
            start = max(s_dict[string[i]], start) #start에 사전형식으로 문자를 Key값으로, start를 Value값으로 저장한다.
        ret = max(ret, i - start + 1)
        s_dict[string[i]] = i + 1
    print(ret)
    return ret

```

만약 리스트를 바로 { list[i] : i }와 같은 딕셔너리로 바꾸고 싶다면 아래와 같이 이용한다.

```python
s_dict = { string[i] : i for i in range(len(string)) }
```

## 테스트 결과

실행 결과 내가 푼 방식으로 해도 결과에는 이상이 없는 듯 하다.

다른 사람의 풀이에는 내가 생각하지 못한 방법들을 이용해 푸는 경우가 많은데, 꼭 그 사람들의 풀이를 따라해야 하는가에 대해서 요새 고민이다.

내가 느끼기에는 내 풀이 방식은 의식의 흐름에 따라 흘러가는대로 코드를 작성하기 때문에 읽기 더 수월하지 않을까??

다른 사람의 코드를 더 참고해서 심플하지만 잘 작동하는 코드도 만들어보도록 노력해야겠다.
