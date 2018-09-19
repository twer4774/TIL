# 최빈값과 Swap

```python
'''
이 문제에는 표준 입력으로 문자열, mystr이 주어집니다. mystr에서 가장 많이 등장하는 알파벳만을 사전 순으로 출력하는 코드를 작성해주세요.
input		output
'aab'		'a'
'dfdefdgf'	'df'
'''
import collections
my_str = input().strip()
def solution(l):
    c = collections.Counter(l)
    order = c.most_common()
    maximum = max(c.values())
    # print(maximum)
    modes = ''
    for num in sorted(order): #중요! sorted가 없으면 order에 저장한 요소가 튜플인 리스트의 순서가 바뀜
        if num[1] == maximum:
            modes += num[0]
    print(modes)
    return modes
solution(my_str)

#일반적인 방법
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = {}
for number in my_list:
    try:
        answer[number] += 1
    except KeyError:
        answer[number] = 1

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100])  # =  raise KeyError

#collections이용
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
```

```python
#일반적인 방법
a = 3
b = 'abc'

temp = a
a = b
b = temp

#파이썬에서 이용하는 방법
a = 3
b = 'abc'

a, b = b, a 
```

