# 없는 숫자 찾기(Find_num)

#### 문제설명 :

숫자로 구성된 입력 문자열을 받아 해당 문자열에 없는 숫자를 찾아서 반환 (0~9 중 없는 숫자 반환)

> #### 제한사항
>
> - 하나의 숫자만 없음
>
> ##### input #####
>
>  input_str_1 = "012345678"
>  input_str_2 = "483750219"
>  input_str_3 = "2428104857060109726496" 
>
> ##### output #####
> # 9, 6, 3

### 풀이 - Python

내 풀이 

- 문자열의 길이를 구한다.
- 문자열 길이에 맞게(len + 1) 반복문을 돌리면서 없는 숫자를 찾아낸다

```python
def solution(input_str):

    answer = ""
    input_len = len(input_str)
    print(input_len)

    for i in range(input_len + 1):
        if str(i) in input_str:
            pass
        else:
            answer = str(i)
            break

    return answer


input_str_1 = "012345678"
input_str_2 = "483750219"
input_str_3 = "2428104857060109726496"

print(solution(input_str_1) + ", " + solution(input_str_2) + ", " + solution(input_str_3))
```

