# 외장 함수

파이썬 라이브러리는 전세계 파이썬 유저들이 만든 프로그램으로 파이썬을 설치하면 자동으로 설치된다.

## sys

파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈

- 명령 행에서 인수 전달하기 - sy.argv

- ```python
  #dos : python test.py abc pey guido
  
  #argv_test.py
  import sys
  print(sys.argv)
  
  #dos : python argv_test.py you need python
  #['argv_test.py', 'you', 'need', 'python']
  ```

- 강제로 스크립트 종료하기 - sys.exit

- 자신이 만든 모듈 불러와 사용하기 - sys.path
  파이썬 모듈들이 저장되어 있는 위치를 나타낸다. 경로에 상관없이 불러올 수 있다

  ```python
  import sys
  sys.path
  
  #paht_append.py
  import sys
  sys.path.append("C:/Python/Mymodules") #이 명령어를 실행하면 파이썬 모듈을 불러와 사용할 수 있음
  ```



## 그 외 외부함수들

```python
#pickle: 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게하는 모듈
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

#pickle.load를 이용해서 원래 있던 딕셔너리 객체 상태 그대로 불러오는 예
data = picle.load(f)
print(data)


#os모듈: 환경변수나 디렉터리, 파일등의 OS자원을 제어할 수 있게하는 모듈
#내 시스템의 환경변수 값을 알고 싶을 때 - os.environ
#디렉터리 위치 변경하기 - os.chdir
#디렉터리 위치 리턴받기 - os.getcwd
#시스템 명령어 호출하기 - os.system
#실행한 시스템 명령어의 결과값 리턴받기 - os.popen

#shutil: 파일을 복사해주는 파이썬 모듈
#shutil.copy("src.txt", "dst.txt") 동일한 파일 존재할 경우 덮어씀

#glob: 특정 디렉터리에 있는 파일 이름을 모두 알아야 할때
#디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

#tempfile: 파일을 임시로 만들어서 사용할 때, 파일이름은 무작위로 리턴함
#f.close() 호출 시 파일이 삭제됨
import tempfile
filename = tempfile.mktemp()
filename #'C:\~-2852932-1'

#time
#time.time: 현재시간을 실수 형태로 리턴하는 함수
#time.localtime: 연, 월, 일, 시 ,분, 초 형태로 바꿈
time.localtime(time.time())
#time.asctime: 위의 locatime에서 반환된 값을 인수로 받아서 날짜와 시간을 리턴
time.asctime(time.localtime(time.time()))
#time.ctime: 현재시간 리턴
time.ctime()
#time.strftime
time.strftime('추력할 형식 포맷 코드', time.localtime(time.time()))
import time
time.strftime('%x', time.localtime(time.time()))
'05/01/01'
#time.sleep: 일정한 시간 간격을 두고 실행
#sleep1.py
import time
for i in rnage(10):
    print(i)
    time.sleep(1)
    
    
#calendar
import calendar
print(calendar.calendar(2015)) #전체 달력을 볼수 있음
#calendar.calendar(연도, (월))로 위와 같은 결과 값을 볼 수 있음
#calendar.weekday: 월요일은 0 ~ 일요일은 6으로 리턴
calendar.weekday(2015, 12, 31) #3 목요일
#calendar.monthrange(연도, 월): 1일이 무슨 요일인지와 그 달이 며칠까지 있는지 리턴
calendar.monthrange(2015, 12) #(1, 31)

#random: 난수 발생
import random
random.random() #0.0~1.0사이의 실수 중 난수 값 리턴
random.randint(1, 10) #1~10사이의 정수 중 난수 값 리턴

#webbrower: 자신의 시스템에서 사용되는 기본 웹 브라우저가 실행되게 하는 모듈
import webbrower
webbrower.open("http://google.com")
webbrower.opne_new("http://google.com") #이미 웹브라우저 실행된 상태이더라도 새로운 창으로 열림
```

