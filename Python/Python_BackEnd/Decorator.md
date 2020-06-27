# Decorator

- 여러 함수에서 공통적인 기능을 필요로 하는 경우에 자주 사용되는 구현 방법
- 어떠한 함수를 다른 함수가 실행되기 전에 자동으로 먼저 실행될 수 있도록 해주는 문법
- @를 붙여서 적용하고자 하는 함수의 정의 부분 위에 지정해준다.

```python
@run_this_first
def and_then_run_this():
  print("Running the second method")
```

### Decorator 함수

- 함수를 리턴하는 함수
- functools 모듈의 wraps decorator 함수 이용

```python
from functools import wraps

def test_decorator(f):
  #필수는 아니지만 공홈에서 권장함 - 여러 이슈해결을 해준다.
  @wraps(f)
  #decorator함수를 리턴해줘야하므로 nested함수로 지정.*args, **kwargs를 이용해 모든형태의 인자를 받음
  def decorated_function(*args, **kwargs):
    print("Decorated Function")
    return f(*args, **kwargs) #f함수를 실행시켜 리턴 -> 해당 decorator함수가 실행되고 난 후 decorator가 적용된 함수를 호출해주는것
  
  return decorated_function

@test_decorator
def func():
  print("Calling func function")
```

```
#결과
>>> func()
Decorated Function
Calling func function
```

