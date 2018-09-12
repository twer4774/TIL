# 함수

## 함수를 사용하는 이유

- 재사용성
- 가독성 : 프로그램의 흐름을 잘 파악하고, 에러를 쉽게 잡을 수 있다.

## 함수의 구조

def 이용

```python
def sum(a, b):
    return a+b

#입력값이 없는 함수
def say():
    return 'Hi'

#결과값이 없는 함수
def sum(a, b):
    print("%d, %d의 합은 %d" %(a, b, a+b))
    
#입력값, 결과값이 둘다 없는 함수
def say():
    print('Hi')
```

## 가변 인자를 받는 함수

인자에 *를 붙이면 입력 값들을 모두 모아서 튜플 형식으로 만들어 준다.

```python
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i #*args에 입력받은 모든 값을 더한다
    return sum
```

## 함수의 결과값은 언제나 하나이다.

```python
def sum_and_mul(a, b):
    return a + b, a * b

result = sum_and_mul(3,4)
#(7, 12)의 값으로 튜플형식으로 받게 됨

#각각의 결과 값으로 받고 싶다면 아래와 같이 함수를 호출한다.
sum, mul = sum_and_mul(3,4) 
```

## 입력 인수에 초깃값 미리 설정하기

주의 사항: 초기화 시킬 인자값은 항상 가장 뒤쪽에 있어야하며, 가운데 초기화 시킬 인자가 들어갈 경우 오류가 발생한다.

```python
def say_myself(name, old, man=True):
    print("my name is %s", %name)
    print("my age is %d", %old)
    if man:
        print("M")
    else:
        print("W")
```

## 함수 안에서 선언된 변수의 효력 범위

```python
a = 1 #함수 밖의 변수 a
def vartest(a):
    a = a + 1

vartest(a) #2출력
print(a) #1출력

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return이용
def vartest(a):
    a = a+1
    return a
#2. global 명령어 이용
def vartest(a):
    global a
    a = a+1
```

