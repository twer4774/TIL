# 내장 함수

파이썬에서 제공하는 내장함수

## abs

절대값을 리턴해주는 함수

```python
abs(3)
#3
abs(-3)
#3
abs(-1.2)
#1.2
```

## all

반복가능한(iterable) 자료형 x를 입력 인수로 받으며, x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴

```python
all([1, 2, 3])
#True 리스트 자료형 [1, 2, 3]은 모든 요소가 참이므로 True 반환

all([1, 2, 3, 0])
#False 0은 거짓이므로 False 반환
```

## any

x중 하나라도 참이 있을 경우 True, 모두 거짓일 경우 False리턴 all과 반대

```python
any([1, 2, 3, 0])
#True
any([0, ""])
#False 모두 거짓
```

## chr <-> ord

아스키 코드값을 입력받아 그 코드에 해당하는 문자열 출력

```python
chr(97)
'a'
chr(48)
'0'
ord('a')
97
ord('0')
48
```



## 다음 여러 내장함수들

```python
#dir: 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
dir([1, 2, 3])
['append', 'count', 'extend', 'index', 'insert', 'pop', ...]
dir({'1': 'a'})
['clear', 'copy', 'get', 'has_key', 'items', 'keys', ...]

#divmod: divmod(a, b)는 2개의 숫자를 입력 받아 a를 b로 나눈 몫고 ㅏ나머지를 튜플 형식으로 리턴
divmod(7, 3)
(2, 1)

'''
#enumerate: 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
0 body
1 foo
2 bar
#리스트 모든 요소를 인덱스와 쌍으로 추출하기 enumerate
ret3 = list(enumerate(solarsys))
print(ret3)

for i, body in enumerate(solarsys):
    print('%d: %s' %(i,body))
'''

#eval: 실행 가능한 문자열을 입력으로 받아 실행한 결과값을 리턴
eval('1+2')
3
eval("'hi' + 'a'")
'hia'

#filter: filter(함수이름, 반복가능한 자료형)
#positive.py
def positive(numberList):
    result = [] #리턴 값이 참인 것만 걸러내서 저장할 변수
   	for num in numberList:
        if num > 0:
            result.append(num)
    return result
print(positive([1, -3, 2, 0, -5, 6])) #[1, 2, 6]

#filter1.py
def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) #[1, 2, 6]
#lambda함수 이용
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

#hex: 정수값을 입력받아 16진수로 변환
hex(234)
'Oxea'

#oct: 정수값을 입력받아 8진수로 변환
oct(34)
'0o42'

#id: 객체를 입력받아 고유 주소값(레퍼런스)을 리턴하는 함수
a = 3
id(3)
135072304
b = a
id(b)
135072304

#input: 사용자의 입력을 받는 함수
a = input()
hi
a #'hi'
b = input("Enter: ")
Enter: hi  #b #'hi'
    
#int: 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴하는 함수로 정수를 입력 받으면 그대로 리턴
int('3') #3
int(3.4) #3
int('11', 2) #3 => 2진수로 표현된 11의 10진수 값 구하기
int('1A', 16) #26 => 16진수로 표현된 10진수 값 구하기

#isinstance: isinstance(object, class) 인스턴스가 그 클래스의 인스턴스인지 판단하여 T/F 리턴
class Person: pass #아무 기능이 없는 클래스
a = Person() #Person 클래스의 인스턴스 a생성
isinstance(a, Person) #a가 Person클래스의 인스턴스인지 확인
True

#lambda: 보통 함수를 한줄로 간결하게 만들 때 사용한다. def를 사용할 정도로 복잡하지 않거나, def를 사용할 수 없는 경우에 이용
#lambda 인수1, 인수2, ...: 인수를 이용한 표현식
sum = lambda a, b: a+b
sum(3,4) #7
#def를 사용할수 없는 경우: 리스트 내에 lambda 이용
myList = [lambda a,b:a+b, lambda a,b:a*b]
myList[0](3,4) #7 리스트의 첫번째 요소에 a+b를 리턴해주는 람다함수 정의되어 있음

#len: 입력값의 길이 리턴
len("python") #6

#list: 반복 가능한 자료형 s를 입력 받아 리스트로 만들어 리턴
list("python")
['p', 'y', 't', 'h', 'o', 'n']
list((1,2,3))
[1, 2, 3]

#map: map(f, iterable) 함수(f)와 반복가능한(iterable) 자료형을 입력으로 받는다. 입력 받은 자료형의 각 요소가 함수 f에 의해 수행된 겨로가를 묶어서 리턴하는 함수
#two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result) #[2, 4, 6, 8]

#map이용
def two_times(x): return x*2
list(map(two_times,[1, 2, 3, 4])) #[2 ,4, 6 ,8]
#map+lambda
list(map(lambda x: x*2, [1, 2, 3, 4]))

#max: 최대값 리턴
max([1, 2, 3])
3
max("python")
'y'

#min: 최소값 리턴
min([1, 2, 3])
1
min("python")
'h'

#pow: x의 y제곱한 결과 리턴
pow(2, 4)
16

#range: for문과 함께 사용되는 함수
#인수가 하나일 경우 0부터 시작
list(range(5)) #[0, 1, 2, 3, 4]
#인수가 2개일 경우 시작~(끝숫자-1)
list(range(5,10)) #[5, 6, 7, 8, 9]
#인수가 3개일 경우 세번째 인자는 숫자 사이의 거리
list(range(1, 10, 2)) #[1, 3, 5, 7, 9]

#리스트 요소 정렬 sort(원본 변경), sorted(원본 유지) -> namelist.sort(), ret1 = sorted(namelist):오름차순 ret2 = sorted(namelist, reverse=True): 내림차순
#리스트 무작위섞기
from random import shuffle
for i in range(3):
    shuffle(listData)
    print(listData)
    


```

```python
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:4]
gas_planets = solarsys[4:]
print('태양계의 암석형 행성 ', end='')
print(rock_planets)
print('태양계의 가스형 행성 ', end='')
print(gas_planets)

#짝수번째 요소만 추출
listData = list(range(1,21))
evenlist = listData[1::2]
print(evenlist)

#리스트 요소 역순만들기
#reverse() 메소드는 리스트의 모든 요소 순서를 거꾸로 만듦. 원본 리스트 자체가 변경됨 주의
listData2 = list(range(5))
listData2.reverse()
print(listData2)

#reversed() 내장함수 이용 원본 데이터를 변경하지 않음
listData3 = list(range(5))
ret1 = reversed(listData3)
print('원본리스트', end=''); print(listData3)
print('역순리스트', end=''); print(list(ret1))
print('test', end=''); print(reversed(listData3)) #reversed(listData3)가 객체이므로 바로 출력 시키면 오브젝트 값이 출력됨
ret2 = listData3[::-1]
print('슬라이싱 이용한 역순', end=''); print(ret2)

#리스트 요소 추가하기
listData4 = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력[%d/3]: ' %(i+1))
    listData4.append(txt)
    print(listData4)

#리스트 특정 위치에 요소 삽입 insert
pos = solarsys.index('목성') #목성의 인덱스를 구해서 pos에 저장
solarsys.insert(pos, '소행성') #목성의 인덱스 pos인 부분에 소행성 추가
print(solarsys)

#요소 제거 del
del solarsys[pos]
print(solarsys)
#구간제거 del solarsys[1:3]
#리스트 제거 del solarsys

#특정요소 제거 remove
solarsys.remove('태양')
print(solarsys)

#리스트 요소 개수 구하기 len
listsize = len(listData4)
print(listsize)

#특정 요소의 개수 구하기
c1 = solarsys.count('목성')
print(c1)

```

