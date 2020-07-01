# Remove Num(숫자 제외시키기)

> 문제 설명
>
> 숫자와 문자가 섞인 문자열 입력에서 숫자를 제외하고 문자만 남게하여 반환
>
> input
>
> ```
> input_str_1 = "H123e4l516o7, P8y9t1h2o3n.4"
> input_str_2 = "6L11if1e 4is 5to1o1 s1hort."
> input_str_3 = "7Yo3u nee12d p1y2t5h1o1n."
> ```
>
> output
>
> Hello python., Life is too short., You need python.

#### 풀이

```python
def solution(input_str):
    answer = ""

    number_list = list(map(str, range(10)))

    for i in input_str:
        if i in number_list:
            pass
        else:
            answer += i

    return answer
```

#### 내 풀이

- isdigit() 함수 이용
  - isalpha()를 이용할 수 있지만, 띄어쓰기 공백또한 인식하기 위해서 if not 구문 이용

```python
def solution(input_str):
    answer = ""

    for i in input_str:
        if not i.isdigit():
           answer += i

    return answer
```

- 정규식 이용

```python
def solution(input_str):
    import re
    a = re.compile("[^0-9]")
    print("".join(a.findall(input_str)))
    answer = ""

    return answer
```

