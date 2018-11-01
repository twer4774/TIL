# 프로그래머스 문제

## 문제

> 문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
> 예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
>
> 제한 사항
> s는 길이 1 이상, 길이 8 이하인 문자열입니다.
>
> 입출력 예
> s      return
> "a234" false
> "1234" true



## 풀이 - Python

### 내 풀이

##### 내 생각

- 제한사항이 1 이상, 길이 8이하인 문자열이므로 문자열 제한을 둔다.
- 문자열 길이 제한을 두면서 길이가 4또는 6인지 확인한다.
- isdigit() 함수로 문자열이 숫자인지 확인한다.

```python
def solution(s):
    answer = True
    if len(s) in range(1,8) and len(s) == (4 or 6):
        if s.isdigit() == True:
            answer = True
        else:
            answer = False
    else: 
        answer = False
    return answer
```

### 다른 사람의 풀이1

- re => 정규표현식을 이용하는 방법.
- ^는 문자열의 처음, $는 문자열의 끝, \d는 숫자 => 숫자가 4번 또는 6번 반복되는지 확인 
- bool값으로 True/False 리턴

```python
def solution(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
```

### 다른 사람의 풀이2

- 문자열 s를 isdigit()함수로 숫자를 찾는다
- 길이가 4인지 6인지 확인한다.

```python
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
```



## 느낀점

나는 문자열 길이 제한사항을 먼저 생각했는데 다시 생각해보니 4 또는 6인 것만 찾으면 어차피 1~8 사이에 들어가게된다.

isdigit()함수로 문자열 찾는것을 성공했지만, len(s)를 할때 or 함수대신 다른 사람의 풀이2에서 처럼 튜플형식으로 값을 찾는것도 굉장히 좋은 방법인것 같다.

정규식을 표현해서 문제를 푸는 경우 멋지고 좋지만, 이 문제처럼 간단하게 같은 결과를 낸다면 가독성면에서 정규표현식을 배제하는 것도 좋을듯 하다.