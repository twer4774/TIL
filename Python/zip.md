# zip함수

- zip(*iterables)
- 튜플형식으로 리턴함

```python
mylist = [ 1,2,3 ]
new_list = [ 40, 50, 60 ]
for i in zip(mylist, new_list):
    print (i)

(1, 40)
(2, 50)
(3, 60)
```

##### 사용 예 #1 - 여러 개의 Iterable 동시에 순회할 때 사용

```python
list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for i, j, k in zip(list1, list2, list3):
   print( i + j + k )
```

##### 사용 예 #2 - Key 리스트와 Value 리스트로 딕셔너리 생성하기

```python
#파이썬의 zip 함수와 dict 생성자를 이용하면 리스트 두개를 하나의 딕셔너리로 생성 가능
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds)) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
```

```python
#python문서에서 발췌
def zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> list(zipped)
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zip(x, y))
>>> x == list(x2) and y == list(y2)
True
```

이차원배열을 행과 열을 바꾸는 문제

```python
#보통 생각하는 해결방법
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = [[],[],[]]
for i in range(3):
    for j in range(3):
        new_list[i].append( mylist[j][i] )
        
# zip함수를 이용하면 한줄로 코드를 뒤집을 수 있음
mylist = [ [1,2,3], [4,5,6], [7,8,9] ]
new_list = list(map(list, zip(*mylist)))
#map(f, iterable)을 이용한다.
#zip(*mylist)는 행과 열을 바꿔주는 역할. map()을 이용해 리스트의 요소들을 순회한다.
#최종적으로 zip으로 행과 열을 바꿔주면서, map으로 리스트를 순회한다. 마지막으로 리스트형식으로 다시 만들어준다.

```

