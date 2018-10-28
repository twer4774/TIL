# 크롤러의 설계

- 크롤러를 설계할 때 한번만 사용하더라도 여러번 사용할 것 처럼 설계하는 것이 좋음
- 이유
  - 이후에 변경된 데이터를 추가로 추출할 수 있게 하기 위해
  - 오류 등으로 중간에 중지됐을 때, 중간부터 다시 재개하기 위해
- 예를 들어 블로그를 크롤링할때, 변경된 포스트만 크롤링 한다면 상대 서버에도 부하를 줄일 수 있음
- 방법
  - URL에서 추출한 키를 바탕으로 해당 키가 존재하지 않을 때만 크롤링하면 됨

### 변경된 데이터만 추출하기

- 크롤링할 때 날짜를 함께 저장하고 1일 또는 일주일을 주기로 다시 크롤링
- 불특정 다수의 웹사이트를 크롤링하는 경우 웹사이트에 따라 변경 빈도가 다를 수 있으므로 HTTP캐시 정책을 기반으로 다시 크롤링하게 만드는 것이 좋음

| HTTP 헤더     | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| Last-Modified | 콘텐츠의 최종 변경일을 나타냄                                |
| ETag          | 콘텐츠의 식별자를 나타냄. 콘텐츠가 변경되면 ETag의 값도 함께 바뀌됨 |
| Cache-Control | 콘텐츠를 캐시해도 괜찮은지 등의 캐시 방침                    |
| Pragma        | Cache-Control과 비슷한 것이었지만, 현재는 하위 호환성 때문에 남아있음 |
| Expires       | 콘테츠의 유효 기간을 나타냄                                  |

- 헤더 처리를 위한 라이브러리 이용 CacheControl

```python
#request_with_cache.py
import requests
#pip3 install CacheControl
from cachecontrol import CacheControl

session = requests.session()
#session을 래핑한 cached_session 만들기
cached_session = CacheControl(session)

#첫 번째는 캐시돼 있지 않으므로 서버에서 추출한 이후 캐시함
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache) #False

#두번재는 ETag와 Last-Modified 값을 사용해 업데이트 됐는지 확인
#변경사항이 없는 경우, 콘텐츠를 캐시에서 추출해서 사용 => 빠른 처리 가능
response = cached_session.get('https://docs.python.org/3/')
print(response.from_cache) #True

#결과
False
True
```



## 크롤링 대상의 변화에 대응하기

- 크롤러를 운용할 때는 변화에 대응해야 할 수 밖에 없음
- 대상 웹사이트가 리뉴얼 등으로 구조를 변경한다면 데이터를 추출할 수 없게 되어 버림
- 전자상거래 사이트의 경우 세일기간동안 가격에 강조 표시를 하는 등의 변화가 있을 수 있음

### 변화 감지하기

- 추출한 웹페이지에서 CSS 선택자 또는 XPath로 요소를 추출했을 때 요소가 존재하지 않으면 변화가 일어났다고 판단할 수 있음.
- 이메일 등으로 통지하고, 크롤러를 종료한 뒤 사람이 직접 페이지 변화를 확인하게 해야 함
- 정규표현식을 이용해 추출한 값이 특정 조건을 만족하는지 확인하는것이 좋음

```python
#validate_with_re.py
import re
value = '3,000'

#숫자와 쉼표만을 포함한 정규 표현식에 매치하는지 확인
if not re.search(r'^[0-9,]+$', value):
    #값이 제대로 돼 있지 않다면 예외를 발생시킵니다.
    raise ValueError('Invalid price')
```

- Voluptuous라이브러리로 스키마를 정의해 유효성 검사 가능

```python
#validate_with_voluptuous.py
#pip3 install voluptuous
from voluptuous import Schema, Match

# 다음의 큐칙들을 가진 스키마 정의
schema = Schema({   #규칙1: 객체는 dict 자료형
    'name': str,    #규칙2: name은 str자료형
    'price': Match(r'^[0-9,]+$'), #규치3: price가 정규 표현식에 맞는지 확인
}, required=True)   #rbclr4: dict의 키는 필수

#Schema 객체는 함수처럼 호출해서 사용
#매개변수에 대상을 넣으면 유효성 검사를 수행
# schema({
#     'name': '포도',
#     'price': '3,000',
# }) #유효성 검사를 통과하므로 아무 문제 없음

schema({
    'name': None,
    'price': '3,000',
}) #유효성 검사를 통과하지 못하므로, MultipleInvalid 예외 발생

#결과
voluptuous.error.MultipleInvalid: expected str for dictionary value @ data['name']
```



### 변화 통지하기

- 변화가 감지되면 메일로 통지함

- 파이썬으로 메일 전송하기
  - email모듈과 smtplib 모듈 사용
  - MIME 메시지 생성, SMTP 서버에 전송

```python
#send_email.py
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#MIMEText 객체로 메일을 생성함
msg = MIMEText('메일 본문')


#제목에 한글이 포함될 경우 Header객체 사용
msg['Subject'] = Header('메일 제목', 'utf-8')
msg['From'] = 'twer4774@gmail.com'
msg['To'] = 'twer4774@gmail.com'

#Gmail말고 다른 메일일때 사용
#SMTP() 첫번재 매개변수에 SMTP 서버의 호스트 이름을 지정
with smtplib.SMTP('localhost') as smtp:
    #메일 전송
    smtp.send_message(msg)
```

- Gmail일경우 추가적인 설정 필요
  - 보안탭에서 '앱 비밀번호'를 설정해서 받아야함

```python
#Gmail일 경우 사용
#TLS/SLL클래스 이용
with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
    #구글 계정의 사용자 이름과 비밀번호르 지정해서 로그인
    #2단계 인증을 설정한 경우 앱 비밀번호 사용
    smtp.login('메일주소', '앱 비밀번호')

    #send_message()메서드로 메일 전송
    smtp.send_message(msg)
```

