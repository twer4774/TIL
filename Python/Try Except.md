# 예외 처리

오류는 프로그램이 잘못 동작되는 것을 막기 위한것.

오류를 무시하고 싶은 경우 try, execpt를 이용해 예외적으로 오류를 처리함

## 오류가 발생하는 경우

- 디렉터리안에 없는 파일을 열려고 시도했을 경우

  ```python
  f = open("없는파일",'r')
  #에러발생
  #FileNotFoundError: No such file or director: '없는파일'
  ```

- 0으로 다른 숫자를 나누는 경우

  ```python
  4/0
  #ZeroDivisionError: division by zero
  ```

- 리스트 안에 요소가 없을때 - indexError

  ```python
  a = [1, 2, 3]
  a[4]
  #IndexError: list index out of range
  ```

## 오류 예외 처리 기법

### try, except문

try 구문에서 오류가 발생하면 except 블록이 실행된다.

```python
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
    
#except사용법 3가지
'''
1. try, except만 쓰는 방법
try:
	...
except:
	...
오류 종류에 상관없이 오류가 발생하기만 하면 except 블록 수행

2. 발생 오류만 포함한 except문
try:
	...
except 발생 오류:
	...
미리 정의해 놓은 오류 이름과 일치할 때만 except블록 수행

3. 발생 오류와 오류 메시지 변수까지 포함한 except문
try:
	...
except 발생 오류 as 오류 메시지 변수:
	...
2번의 경우에서 오류 메시지의 내용까지 알고 싶을때 이용하는방법
try:
	4/0
except ZeroDivisionError as e:
	print(e)
#division by zero
'''
```



### try .. else

else절은 예외가 발생하지 않은 경우 실행되며 반드시 except절 바로 다음에 위치해야 한다.

```python
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as a:
    print(str(e))
else:
    data = f.read()
    f.close()
#foo.txt라는 파일이 없다면 except문 수행, foo.txt이 있다면 else문 수행 됨
```



### try .. finally

finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행 된다.

보통 finally절은 사용한 리소스를 close할때 많이 사용된다.

```python
f = open('foo.txt', 'w')
try:
    #무언가를 수행한다
finally:
    f.close()
```



## 오류 회피하기

특정 오류가 발생할 경우 그냥 통과시켜야 할 때 이용

```python
try:
    f = open("없는 파일", 'r')
except FileNotFoundError:
    pass
```



### 오류 일부러 발생시키기

raise명령어를 이용함

```python
#Bird라는 클래스를 상속받는 자식 클래스는 반드시 fly라는 함수를 구현하도록 만들고 싶을 때
class Bird:
    def flay(self):
        raise NotImplementedError
        
class Eagle(Bird):
    def fly(self):
        print("very fast")

#eagle = Eagle()
#eagle.fly() #very fast
```

