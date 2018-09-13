# 패키지

- 도트(.)를 이용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할수 있게 해준다.
- 패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있다.

## 패키지 만들기

패키지 안에는 \__init__.py파일이 각 디렉터리 마다 들어가야 한다.

#### 예)

```
mkdir mypackage
cd mypackage
nano __init__.py #mypackage의 init파일
mkdir sound
cd sound
nano __init__.py #sound의 init파일
nano echo.py
cd ..
mkdir graphic
cd graphic
nano __init__.py #grahpic의 init파일
nano render.py
```

```python
#echo.py
def echo_test():
    print("echo")
    
#render.py
def render_test():
    print("render")
```

```
#위의 패키지를 참조하기 위해서는 도스창에서 set명령을 이용하여 PYTHONPATH환경변수에 위의 패키지가 저장된 디렉터리(예: C:/Python)를 추가한다.
set PYTHONPATH=C:/Python
```

### 패키지 안의 함수 실행하기

주의사항: 세가지 방법은 시작할때 마다 새로운 인터프리터로 작업해야 전에 import했던것들이 메모리에서 해제된다

1. echo모듈을 import하여 실행

   ```p
   import mypackage.sound.echo
   mypackage.sound.echo.echo_test()
   #echo
   ```

2. echo모듈이 있는 디렉터리까지를 from .. import 실행

   ```
   from mypackage.sound import echo
   echo.echo_test()
   #echo
   ```

3. echo모듈의 echo_test함수를 직접 import

   ```
   from mypackage.sound.echo import echo_test
   echo_test()
   #echo
   ```



## \__init__.py의 용도

- 해당 디렉터리가 패키지의 일부임을 알려주는 역할
- 만약 디렉터리에 \__init__.py가 없으면 임포트에서 오류가 발생한다.

```
#__all__의 사용
from mypackage.sound import *
echo.echo_test() #오류발생
''' import *를 했으므로 정상작동 할 것으로 예상되는데 오류 발생. ''''

#sound.__init__.py
__all__=['echo']

'''위의 명령어 __all__을 해줘야 import*를 할때 불러올 수 있음.'''
```

### relative패키지

```python
'''graphic 디렉터리의 render.py모듈이 sound디렉터리의 echo.py모듈 사용하고 싶을때'''
#render.py
from mypackage.sound.echo import echo_test
def render_test():
    print("render")
    echo_test()

#인터프리터에서 
from mypackage.grahpic.render import render_test
render_test()
#rendder
#echo
#작동 됨

#relative접근자 - 인터프리터에서는 사용불가. 모듈 안에서만 이용가능
# .. : 부모 디렉터리
# . : 현재 디렉터리
#render.py
from ..mypackage.echo import echo_test

def render_test():
    print("render")
    echo_test()
```

