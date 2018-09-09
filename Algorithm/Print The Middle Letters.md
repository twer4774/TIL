# 프로그래머스 문제

## 문제

> 단어 s의 가운데 글자를 반환하는 함수
> 단어의 길이가 짝수라면 가운데 두 글자를 반환
>
> 예)
>
> *Input: "abcde"*
>
> *Output: "c"*
>
> *Input: "qwer"*
>
> *Output: "we"*

## 풀이 - Python

### 내 풀이

#### 내 생각

* 문자열의 길이를 구하고(stringLen), 문자열의 길이를 2로 나누었을 때, 나머지가 0인지 아닌지 확인한다.(짝수, 홀수 확인)
* 문자열의 길이를 2로 나누면 문자열의 가운데 값(pickString)이 나오므로, 짝수인지 홀수인지에 따라 가운데 글자(if부분)와 그 다음글자의 출력(else 부분)을 나눈다.

```python
s = input('입력하세요')

def solution(s):
    answer =''
    stringLen = len(s)
    pickString = int(stringLen/2)

    if stringLen%2 != 0:
        answer = s[pickString]
        print(answer)
    else:
        answer = s[pickString-1:pickString+1]
        print(answer)
    return answer

solution(s)
```

![image-20180909122514488](/var/folders/4l/l32v4snd18qfng3lcvwv24bw0000gn/T/abnerworks.Typora/image-20180909122514488.png)

![image-20180909122612187](/var/folders/4l/l32v4snd18qfng3lcvwv24bw0000gn/T/abnerworks.Typora/image-20180909122612187.png)

### 다른사람의 풀이

#### 내 생각

한 줄로 그냥 끝내버렸다... 풀이 방식은 문자열을 2로 나누고, 나눈 문자열 부터 다음 문자열까지 출력시킨다.

이때 //를 이용하는데, //은 파이썬에서 정수부분만 값을 반환시키는 역할을 한다.(일반적인 /연산은 float형식으로 출력된다!)

아래의 풀이는 문자열의 길이에서 1을 빼고 2를 나눈뒤의 문자열인덱스와, 문자열의 길이를 2로 나눈뒤 1을 더한 문자열 인덱스를 이용했는데, 이런 식을 이용 하게 되면 문자열의 길이가 홀수일 때는 문자열의 가운데 1자리만 출력되고 짝수일 때는 가운데 1자리와 그 다음 문자열까지 출력되는 문자열 인덱싱이 실행된다.

```python
def anotherSolution(str):
    print(str[(len(str)-1)//2:len(str)//2+1])
    return str[(len(str) - 1) // 2:len(str) // 2 + 1]

anotherSolution(s)
```

![image-20180909122922964](/var/folders/4l/l32v4snd18qfng3lcvwv24bw0000gn/T/abnerworks.Typora/image-20180909122922964.png)

## 테스트 결과

내 풀이와 다른 사람의 풀의 테스트 실행 시간은 거의 비슷했다( 내 것이 더 빠르게 나와서 기분이 좋다~).

다른 사람의 풀이방식은 코드가 아주 매우 간단해서 보기 좋다. 그렇지만 저 문자열 특성을 이용한 식을 한번더 생각해야 되는 단점이 있는 것 같다. 

내 풀이는 누구나 쉽게 생각할 수 있고, 인간의 언어와 유사하다라는 파이썬의 특성에 더 걸맞지 않을까 생각한다.(의식의 흐름대로 했으므로)

실행결과 둘다 잘 실행되고 속도의 차이도 별로 없는듯 하다. 물론 어느 코드가 더 좋다고 단정지을 수는 없지만, 다른 사람의 풀이방식을 다른 문제를 풀때도 항상 참고해서, 내 스타일 대로 좋은 코드를 만들어 내고 싶다.

