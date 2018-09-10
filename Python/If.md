# If문

### 조건문

참과 거짓을 판단하는 문장

|  자료형  |      참       | 거짓 |
| :------: | :-----------: | :--: |
|   숫자   | 0이 아닌 숫자 |  0   |
|  문자열  |     "abc"     |  ""  |
|  리스트  |   [1, 2, 3]   |  []  |
|   튜플   |   (1, 2, 3)   |  ()  |
| 딕셔너리 |  {"a" : "b"}  |  {}  |



### 비교연산자

<, >, ==, !=, >=, <=

```python
x = 3
y = 2
x > y #True
x < y #False
x == y #False
x != y # True

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어서 가라")
#걸어서 가라
```

### 논리연산자

and, or, not

```python
money = 2000
card = 1
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어서 가라")
#택시를 타고 가라
```



### x in s, x not in s

|     in      |     not in      |
| :---------: | :-------------: |
| x in 리스트 | x not in 리스트 |
|  x in 튜플  |  x not in 튜플  |
| x in 문자열 | x not in 문자열 |

```python
1 in [1, 2, 3] #True
1 not in [1, 2, 3] #False

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else: 
    pass #아무것도 하지 않음
#택시를 타고 가라
```



### elif

다양한 조건을 판단

```python
pocket = ['paper', 'cellphone']
card = 1
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")
#택시를 타고 가라
```

