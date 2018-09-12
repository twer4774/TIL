# 프로그래머스 문제

## 문제

> 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 배열 arr에서 제거 되고 남은 수들을 return 하는 solution 함수를 완성해 주세요. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
> 예를들면
>
> arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
> arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

## 풀이 - Python

### 내 풀이

##### 내 생각

- 입력된 arr의 길이를 이용 하되, 첫번째 인자는 answer에 들어가도록 한다.
- arr의 두번째 인자부터 arr를 순회한다.
- arr의 i-1번째와 i, 그리고 answer에 저장된 값이 다르면 arr[i]를 저장하고 answer의 인덱스 값을 하나 올려준다.

```python
def solution(arr):
    answer = []
    arrC = len(arr)
    ansC = 0
    answer.append(arr[0])
    
    for i in range(1, arrC):
        if arr[i-1] != arr[i] != answer[ansC]:
            answer.append(arr[i])
            ansC += 1
    return answer
```

### 다른 사람의 풀이

```python
def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    print(a)
    return a
```

1. a = [1]
2. a의 1과 s의 1 비교 => 같으므로 continue
3. a의 1과 s의 3 비교 => 다르므로 append(i)     a=[1,3]
4. 위의 과정 반복

## 테스트 결과

문자열 인덱싱을 할때 빈 배열임에도 불구하고, a[-1:0]을 하면 오류가 안뜨는게 신기했다. 

혹시나해서 a[-1]값을 넣어봤는데 오류가 발생했다. 왜 문자열 인덱싱을 하면 오류가 안뜨는 걸까??

실행결과는 내 코드와 정확성이나 효율성면에서 차이는 없었다.

