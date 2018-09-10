# 문자열 자료형

## 문자열을 만드는 방법 4가지

1. 큰 따옴표(")로 감싸기

```python
"Hello World"
```

2. 보통 문자열에 작은 따옴표가 있을 때, 이를 인지시키기 위해 필요

```python
a = "Hello i'm Wonik"
```

- \(백슬러시)를 이용하면 문자열에 큰 따옴표로 인식시킬 수 있음

```python
	a = " \"Hello\" "
```

3. 작은 따옴표(')로 감싸기

```python
'Hello World'
```

- 문자열에 큰 따옴표가 있을 때, 인지시키기 위해 필요

  ```python
  	a = ' "Hello" '
  ```

- \(백슬러시)를 이용하면 문자열에 작은 따옴표로 인식시킬 수 있음

  ```
  a = Hello i\'m Wonik
  ```

4. 큰 따옴표 3개로 감싸기

```python
"""Hello World"""
```

5. 작은 따옴표 3개로 감싸기

```python
'''Hello World'''
```

**4, 5번은 여러 줄의 문자를 입력할 때 이용**

```python
a = '''

Hello

my name is wonik

'''

b = """

Hello

myname is wonik

"""
```

## 문자열 연산하기

파이썬에서는 문자열을 더하거나 곱할 수 있다.

1. 문자열 더해서 연결하기

```python
a = "Hello"

b = "wonik"

a + b 
#'Hello wonik'
```

2. 문자열 곱하기

```python
a = "Hello"

a * 2

#'HelloHello'
```

3. 문자열 곱하기 응용

```python
# multistring.py #프로그램 제목

print("=" * 50)

print("My Program")

print("=" * 50)
```

 
## 문자열 인덱싱과 슬라이싱

- 문자열 인덱싱

  ```python
  a = "Life is too short, You need Python"
  a[3] #'e'
  a[-1] #'n' 오른쪽 문자부터 -1로 인덱싱 됨
  ```

- 문자열 슬라이싱

  ```python
  a = "Life is too short, You need Python"
  b = a[0] + a[1] + a[2] + a[3]
  b #'Life'
  c = a[0:4]
  c #'Life'
  
  #끝 번호를 생략하면 시작번호부터 문자열 끝까지 출력
  a[19:] # 'You need Python'
  
  #시작 번호를 생략하면 처음부터 끝 번호까지 출력
  a[:17] # 'Life is too short'
  
  #시작 번호와 끝 번호를 생략하면 모두 출력
  a[:] # 'Life is too short, You need Python'
  ```

- 슬라이싱으로 문자열 나누기

  ```python
  a ="20180908Sunny"
  date = a[:8]
  weather = a[8:]
  date # '20180909'
  weather # 'Sunny'
  ```

- 문자열 요소 바꾸기

  ```python
  a = "Piython"
  a[1] ='y' # 에러 남. 문자열의 요소 값은 바꿀 수 있는 값이 아님
  a[:1] # 'P'
  a[2:] # 'thon'
  a[:1] + 'y' + a[2:]  #Python
  ```


## 문자열 포맷팅

문자열 내에 어떤 값을 삽입하는 방법

1. 숫자 바로 대입

```python
"I eat %d apples." %3  #'I eat 3 apples'
"I eat {0} apples.".format(3) #'I eat 3 apples'
```

2. 문자열 바로 대입

```python
"I eat %s apples." %"five"  #'I eat five apples.'
"I eat {0} apples.".format("five")  #'I eat five apples.'
```

3. 변수로 대입

```python
number = 3
"I eat %d apples." %number  #'I eat 3 apples'
"I eat {0} apples.".format(number)  #'I eat 3 apples'
```

4. 2개 이상의 값 넣기

```python
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
```

5. 이름으로 넣기

```python
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
```

6. 정렬 

```python
#왼쪽 정렬
"{0:<10}".format("hi")  #'hi        '

#오른쪽 정렬
"{0:>10}".format("hi")  #'        hi'

#가운데 정렬
"{0:^10}".format("hi")  #'    hi    '

#공백채우기
"{0:=^10}".format("hi")  #'====hi===='
```

 

문자열 포맷 코드

| %s   | 문자열                   |
| ---- | ------------------------ |
| %c   | 문자 1개                 |
| %d   | 정수                     |
| %f   | 부동 소수                |
| %o   | 8진수                    |
| %x   | 16진수                   |
| %%   | Literal %(문자 '%' 자체) |

 

## 포맷 코드와 숫자 함께 사용하기

1. 정렬과 공백

```python
"%10s" % "hi"   #'        hi' <-hi가 오른쪽 정렬됨

%10s : 전체 길이가 10개인 문자열 공간에서 hi를 오른쪽으로 정렬하고 나머지는 공백 %-10s는 왼쪽 정렬됨
```

2. 소수점 표현하기

```python
"%0.4f" %3.42134234    #'3.4213'   4자리까지만 표시
```

  

## 문자열 관련 함수들

- 문자열 개수 세기(count)

- ```python
  a = "hobby"
  a.count('b')   #2
  ```

- 위치 알려주기1(find)

- ```python
  a = "Python is best choice"
  a.find('b')  #10
  a.find('k')  #-1  찾는 문자가 존재하지 않으면 -1을 반환함
  ```

- 위치 알려주기2(index)

- ```python
  a = "Life is       too short"
  a.index('t')  #8
  a.index('k')       #오류처리됨
  ```

- 문자열 삽입(join)

- ```python
  a = ","
  a.join('abcd')  #'a,b,c,d'
  ```

- 소문자를 대문자로 바꾸기(upper)

- ```python
  a = "hi"
  a.upper()  #'HI'
  ```

- 대문자를 소문자로 바꾸기(lower)

- ```python
  a = "HI"
  a.lower()  #'hi'
  ```

- 왼쪽 공백 지우기(lstrip)

- ```python
  a = "hi"
  a.lstrip()  #'hi
  ```

- 오른쪽 공백 지우기(rstrip)

  ```python
  a = "hi"
  a.rstrip()  #'hi'
  ```

- 양쪽 공백 지우기(strip)

- ```python
  a = "hi"
  
  a.strip()  #'hi'
  ```

- 문자열 바꾸기(replace)

- ```python
  a = "Life is too short"
  
  a.replace("Life", "Your leg")  #'Your leg is too short'
  ```

- 문자열 나누기(split)

  ```python
  a = "Life is too short"
  a.split() #공백을 기준으로 문자열 나눔
  ['Life', 'is', 'too', 'short']
  a ="a:b:c:d"
  a.split(':')
  ['a', 'b', 'c', 'd']
<<<<<<< HEAD
  ```
<<<<<<< HEAD
<<<<<<< HEAD
=======
  ```
>>>>>>> 82360a11e97e8b94ed919dc83c307c143f28c56e
=======
>>>>>>> b2196188b8862544b2d223e761d2dfd8ce5bfc23
=======
>>>>>>> b2196188b8862544b2d223e761d2dfd8ce5bfc23
