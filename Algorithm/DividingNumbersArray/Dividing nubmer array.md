# 프로그래머스문제

## 문제

> array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요. divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
>
> ##### 제한사항
>
> - arr은 자연수를 담은 배열입니다.
> - 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
> - divisor는 자연수입니다.
> - array는 길이 1 이상인 배열입니다.
>
> ##### 입출력 예
>
> | arr           | divisor | return        |
> | ------------- | ------- | ------------- |
> | [5, 9, 7, 10] | 5       | [5, 10]       |
> | [2, 36, 1, 3] | 1       | [1, 2, 3, 36] |
> | [3,2,6]       | 10      | [-1]          |

## 풀이 - Python

### 내 풀이

내 생각

- 일단 나누어지지 않는 값들이 있는 배열은 -1을 리턴하므로 람다를 이용해 표시한다.

- arr를 순회하면서 나머지가 0인 요소들을 answer에 추가한다.(리턴되는 값)
- 마지막으로 정렬된 배열을 리턴해야하므로 sorted함수로 정렬시킨다.

```python
def solution(arr, divisor):
    answer = []
    temp = list(map(lambda x: x%divisor, arr))
    if temp.count(0) == 0:
        answer.append(-1)
    for i in arr:
        if i%divisor == 0:
            answer.append(i)
    return sorted(answer)
```

![result](https://user-images.githubusercontent.com/13410123/45917608-98fee600-beb5-11e8-8100-bfa03567bdc2.png)

### 다른 사람의 풀이

```python
def solution(arr, divisor):
    arr = [x for x in arr if x % divisor == 0];
    arr.sort();
    return arr if len(arr) != 0 else [-1];
```

- arr에 0으로 나누었을때 나머지가 0인 요소들을 저장한다.
- arr를 정렬한다.
- 리턴 값을 줄때 배열의 길이가 0이 아니라면 arr를, 아니면(0이면) [-1]을 대입한다.

## 테스트 결과

코드는 내 것이 복잡해 보인다. 다른 사람의 코드는 깔끔했다. 하지만, 실행결과 각기 다른 테스트 케이스에서 속도의 차이가 있었다. 어떤 케이스에 대해서는 내 알고리즘이 빨랐고, 어떤 케이스에서는 다른 사람의 풀이가 빠르게 동작했다. 속도의 차이는 심하지 않았으므로 내가 생각한 알고리즘도 괜찮은것 같다. 효율성을 테스트하는 결과가 없어서 조금 아쉬웠다.