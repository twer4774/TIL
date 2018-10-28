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