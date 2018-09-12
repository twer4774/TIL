# 클래스

## 클래스의 사용

- 재사용성이 용이함 : 같은 일을 하는 함수들을 클래스 단위로 묶어 인스턴스를 생성하고, 각 인스턴스 마다 다른 값을 받는 같은 일을 할 수 있다.

- 객체와 인스턴스의 차이: 인스턴스는 클래스의 객체이다. a = classA() => a는 classA()의 인스턴스이다. 즉, 클래스와의 관계를 표현하기 위해 용어의 차이를 둔다.

- 클래스 안에서 함수를 사용할 경우, 첫번째 인자값은 self로 넣어준다.

  ```python
  class A:
      def outHi(self, name):
          a = "하이"
          result = a + name
          print("%s" %result)
          
  instanceA = A()
  instanceA.outHi('원익') #하이원익
  
  class MyClass:
      var = '안녕하세요'
      def sayHello(self): #클래스 메소드는 첫 번째 인자가 반드시 self로 시작해야 함
          print(self.var)
  
  obj = MyClass()
  print(obj.var)
  obj.sayHello()
  
  ```

## self 이용하기

```python
class Service:
    def setname(self, name):
        self.name = name  #self.name을 통해 앞으로 self.name에는 인자로 들어온 name의 값이 저장됨
    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))
        
pey = Service()
pey.setname("홍길동")
pey.sum(1, 1) #홍길동님 1 + 1 = 2입니다.

#class 멤버와 instance 멤버
class MyClass2:
    var = '안녕하세요'
    def dayHello(self):
        param1= '안녕'
        self.param2 = '하이' #인스턴스 멤버
        print(param1)
        print(self.var)

obj2 = MyClass2()
print(obj2.var)
obj2.dayHello()
# print(obj2.param1)  #에러발생
print(obj2.param2)  #성공 인스턴스 멤버라서 가능함

#클래스 메소드 이해하기
class MyClass3():
    def sayHello3(self):
        print("안녕하세요")

    def sayBye(self, name):
        print('%s! 다음에 보자' %name)

obj3 = MyClass3()
obj3.sayHello3()
obj3.sayBye('철수')

```



## \__init__

인스턴스를  만들때 항상 실행되는 함수

```python
class Service:
    def __init__(self, name):
        self.name = name
	def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))
        
pey = Service("홍길동")
pey.sum(1, 1) #홍길동님 1 + 1 = 2입니다.

#클래스 생성자, 소멸자 이해하기
class MyClass4():
    def __init__(self):
        self.var = '안녕하세요'
        print('MyClass4 인스턴스 생성')

    def __del__(self):
        print('MyClass4 인스턴스가 메모리에서 제거됨')

obj4 = MyClass4()
print(obj.var)
del obj4

```



## 클래스의 상속

```python
#클래스 상속 이해하기
class Add:
    def add(self, n1, n2):
        return n1 + n2

class Multiply:
    def multiply(self, n1, n2):
        return n1 * n2

class Calculator(Add, Multiply): #다중 상속이 됨
     def sub(self, n1, n2):
        return n1-n2

obj5 = Calculator()
print(obj5.add(1,2))
print(obj5.sub(1,2))
print(obj5.multiply(3,2))
```

## 메서드 오버라이딩(overriding) - 재정의

메서드와 이름은 같지만 행동이 달라야 할 때, 자식 클래스에서 부모 클래스의 메서드를 재정의 함

```python
class Add:
    def add(self, n1, n2):
        return n1 + n2
class Calculator(Add, Multiply): #다중 상속이 됨
     def add(self, n1, n2):
        return n1 + n2 + 1 #n1 + n2 + 1한 값이 출력됨
     def sub(self, n1, n2):
        return n1-n2
```

## 오버로딩

사칙연산등을 포함해, 정의된 함수의 인자값이 다르면 다른 함수로 인식하는 기법으로, \__init__(self) 과 \__init(self, name)__은 다른 것으로 인식한다.

