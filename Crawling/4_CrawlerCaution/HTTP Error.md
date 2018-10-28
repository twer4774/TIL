# 상태코드와 오류처리

### HTTP통신 오류

- 네트워크 레벨의 오류
  - DNS 이름 해석 실패 또는 통신 타임아웃 등 서버와 통신을 할 수 없는 경우 발생
- HTTP 레벨의 오류
  - 서버와 정상적으로 통신은 할 수 있지만, HTTP 레벨에서 오류 발생
- 웹 서버는 HTTP 상태코드로 요청의 결과를 반환

| 상태 코드                 | 설명                                                  |
| ------------------------- | ----------------------------------------------------- |
| 100 Continue              | 요청이 연결 됨                                        |
| 200 OK                    | 요청 성공                                             |
| 301 Moved Permanently     | 요청한 리소스가 영구적으로 이동                       |
| 302 Found                 | 요청한 리소스가 일시적으로 이동                       |
| 304 Not Modified          | 요청한 리소스가 변경되지 않음                         |
| 400 Bad Request           | 클라이언트의 요청에 문제가 있으므로 처리 할 수 없음   |
| 401 Unauthorized          | 인증되지 않아 처리할 수 없음                          |
| 403 Forbidden             | 요청이 허가되지 않음                                  |
| 404 Not Found             | 요청한 리소스가 존재하지 않음                         |
| 408 Request Timeout       | 타임아웃                                              |
| 500 Internal Server Error | 서버 내부에 문제 발생                                 |
| 502 Bad Gateway           | 게이트웨이 서버가 백엔드 서버로부터 오류를 받음       |
| 503 Service Unavailabe    | 서버가 일시적으로 요청을 처리 할 수 없음              |
| 504 Gateway Timeout       | 게이트웨이 서버에서 백엔드 서버로의 요청이 타임아웃됨 |

- HTTP 통신 오류 대처 방법
  - 재시도

```python
#error_handling.py
import time

import requests
#일시적인 오류를 나타내는 상태 코드 지정
TEMP_ERROR_CODES = (408, 500, 502, 503, 504)

def main():
    #무작위로 200, 404, 503상태코드 반환
    response = fetch('http://httpbin.org/status/200, 404, 503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error')

def fetch(url):
    #지정한 URL에 요청한 뒤 Response 객체를 반환
    #일시적인 오류가 발생하면 최대 3번 재시도 실행
    
    max_retries = 3 #최대 3번 재실행
    retries = 0 #현재 재시도 횟수
    while True:
        try:
            print('Retrieving {0}...'.format(url))
            response = requests.get(url)
            print('Status: {0}'.format(response.status_code))
            if response.status_code not in TEMP_ERROR_CODES:
                return response #일시적인 오류가 아니라면 response 반환
        except requests.exceptions.RequestException as ex:
            #네트워크 레벨오류의 경우 재시도
            print('Exception occured: {0}'.format(ex))
            retries += 1
            if retries >= max_retries:
                #재시도 횟수 상한을 넘으면 예외 발생
                raise Exception('Too many retries')
            #지수 함수적으로 재시도 간격 증가(**는 제곱)
            wait = 2**(retries -1)
            print('Waiting {0} seconds...'.foramt(wait))
            time.sleep(wait) #대기

if __name__ == '__main__':
    main()
    
#결과 - 랜덤하게 상태코드 출력
Retrieving http://httpbin.org/status/200, 404, 503...
Status: 200
Success!

Retrieving http://httpbin.org/status/200, 404, 503...
Status: 404
Error
```

- 재시도는 @retry데코레이터를 추가해서 간단하게 처리할 수 있음
- retrying 라이브러리 사용

```python
#error_handling_with_retrying.py
import requests
from retrying import retry #pip install retrying 설치 필요

#일시적인 오류를 나타내는 상태 코드 지정

TEMP_ERROR_CODES = (408, 500, 502, 503, 504)

#stop_max_attempt_number로 최대 재시도 횟수 지정
#wait_exponential_multiplier로 특정한 시간 만큼 대기하고 재시도하게 함. 단위: 밀리초
@retry(stop_max_attempt_number=3, wait_exponential_multiplier=1000)

def main():
    #무작위로 200, 404, 503상태코드 반환
    response = fetch('http://httpbin.org/status/200, 404, 503')
    if 200 <= response.status_code < 300:
        print('Success!')
    else:
        print('Error')

def fetch(url):
    #지정한 URL에 요청한 뒤 Response 객체를 반환
    #일시적인 오류가 발생하면 최대 3번 재시도 실행
    print('Retrieving {0}...'.format(url))
    response = requests.get(url)
    print('Status: {0}'.format(response.status_code))
    if response.status_code not in TEMP_ERROR_CODES:
        #오류가 없다면 response 반환
        return response
    #오류가 있다면 예외 발생
    raise Exception('Temporary Error:{0}.froamt(response.status_code')


if __name__ == '__main__':
    main()

#결과
Retrieving http://httpbin.org/status/200, 404, 503...
Status: 503
Retrieving http://httpbin.org/status/200, 404, 503...
Status: 200
Success!
```





