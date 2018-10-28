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
