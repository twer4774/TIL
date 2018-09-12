# 모듈

- 함수나 변수 또는 클래스 들을 모아 놓은 파일

- 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만들어진 파일

## 모듈 만들기

```python
#mod1.py
def sum(a, b):
	return a + b

def safe_sum(a, b):
    if type(a) != type(b): #객체 a와 b의 자료형이 같지 않다면
        print("더할 수 없습니다.")
        return
  	else:
        result = sum(a,b)
    return result
#import mod1
#print(mod1.safe_sum(3, 4)) #7

```

## 모듈을 불러오는 방법

1. from 모듈이름 import 모듈함수

   from mod1 import sum

2. from 모듈이름 import *

## if \__name__="\__main__": 의 의미

```python
#mod1.py
def sum(a, b):
    return a+b
def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 없습니다.")
        return
    else:
        result = sum(a,b)
    return result
    
print(safe_sum('a', 1)) 
print(safe_sum(1, 4)) 

#도스창에서
python mod1.py
#더할 수 없습니다.
#5

'''
도스 창에서
import mod1
#을 실행하면 그냥 바로 
#더할수 없습니다.
#5
가 실행된다. 이 경우에 
if __name__ == "__main__":
	print(safe_sum('a', 1)) 
	print(safe_sum(1, 4))
를 이용하면 모듈을 불러올때(import mod1)는 if문에 속한 구문들이 실행되지 않는다.
'''
```

## 클래스나 변수등을 포함한 모듈

```python
#mod2.py
PI= 3.141592
class Math:
    def solv(self, r):
        return PI * (r**2)
    def sum(a,b):
        return a+b
if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))
```

### 모듈에 포함된 변수, 클래스 사용하기

```python
print(mod2.PI) #3.141592
a = mod2.Math()
print(a.solv(2)) #12.566368
print(mod2.sum(mod2.PI, 4.4)) #7.541592
```

## 새 파일 안에서 이전에 만든 모듈 불러오기

주의사항: 모듈이 작업하는 파일과 같은 폴더안에 존재해야 한다.

```python
#modtest.py
import mod2
result = mod2.sum(3,4)
print(result)
```

