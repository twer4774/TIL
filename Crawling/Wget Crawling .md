# 크롤링과 스크레이핑

크롤링(Crawling): 웹 페이지의 하이퍼링크를 순회하면서 웹 페이지를 다운로드하는 작업

스크레이핑(Scraping): 다운로드한 웹 페이지에서 필요한 정보를 추출하는 작업



## 파이썬

서드파티 라이브러리

- NumPy: 숫자계산
- SciPy: 과학 기술 계산
- scikit-learn: 머신러닝
- pandas: 데이터 분석
- Django: 웹 애플리케이션 프레임워크
- Flask: 웹 애플리케이션 프레임워크

#### 크롤링 & 스크레이핑 라이브러리

- lxml
- Beautiful Soup
- Scrapy



## Wget으로 크롤링하기

### Wget

- 유닉스의 대표 다운로더, cURL과 함께 대표적임

- HTTP, FTP를 사용해 서버에서 파일 또는 컨텐츠를 다운로드하는 소프트웨어(다운로더)

- GNU프로젝트의 일부로 무료 배포됨

- 여러 파일을 한번에 다운로드하거나 웹 페이지의 링크를 순회하며 여러 콘텐츠를 자동으로 다운로드 함

- cURL 다운로더 -  HTTP응답이 콘솔에 출력되며, 옵션을 사용해 다양한 형태로 HTTP요청을 보냄. 웹 API 호출시 자주 사용


#### Wget 설치하기

- Hombrew패키지 매니저 이용(mac os)

  - 설치: 터미널에 입력

  - ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    
    //우분투에서는
    sudo apt-get update
    sudo apt-get install -y wget
    ```

- Wget 설치

- ```
  brew update
  brew install wget
  
  wget --version
  ```

- wget 사용법

  - 매개변수에 URL을 지정하면 해당 URL의 콘텐츠를 내려받아 파일로 저장함

  - ```
    //위키북스 로고 다운받기
    wget http://wikibook.co.kr/wikibook.png
    
    //위키북스 index.html파일 다운
    wget http://wikibook.co.kr/
    
    //-O 옵션 이용: 다른 이름으로 파일 저장
    wget http://wikibook.co.kr/ -O wikibook_top.html
    
    //-를 이용하면 파일로 저장하지 않고, 콘솔에 표준출력함(파이프로 다른 명령으로 출력 넘길때 이용)
    //진행 상황 출력을 막는 q옵션과 함께 이용됨
    wget http://wikibook.co.kr/ -q -O 
    
    //결과
    !DOCTYPE html>
    <!--[if IE 7]>
    <html class="ie ie7" lang="ko-KR">
    <![endif]-->
    <!--[if IE 8]>
    <html class="ie ie8" lang="ko-KR">
    <![endif]-->
    <!--[if !(IE 7) | !(IE 8)  ]><!-->
    <html lang="ko-KR">
    <!--<![endif]-->
    <head>
    <title>위키북스 | 안녕하세요! IT 전문서를 펴내는 위키북스입니다.</title>
    <meta charset="UTF-8" /> ... ...
    ```

자주사용되는 옵션

| 옵션                                | 설명                                                         |
| ----------------------------------- | ------------------------------------------------------------ |
| -V, --version                       | wget 버전 출력                                               |
| -h, --help                          | 도움말 출력                                                  |
| -q, --quiet                         | 진행 상황 등을 출력하지 않음                                 |
| -O <file>, --output-document=<file> | file에 저장                                                  |
| -c, --continue                      | 이전 상태에서 계속 이어서 파일을 다운로드 함                 |
| -r, --recursive                     | 링크를 돌며 재귀적으로 다운로드 함                           |
| -l depth, --level=<depth>           | 재귀적으로 다운로드할 때 링크 순회 깊이를 제한               |
| -w <seconds>, --wati=<seconds>      | 재귀적으로 다운로드할 때 간격을 seconds초로 지정             |
| -np, --no-parent                    | 재귀적으로 다운로드할 때 부모 디렉터리는 크롤링하지 않음     |
| -l <list>, --include <list>         | 재귀적으로 다운로드할 때 list에 포함된 디렉터리만 순회       |
| -N, --timestamping                  | 파일이 변경됐을 때만 다운로드                                |
| -m, --mirror                        | 미러링 전용 옵션 활성화<br />-r -N -l inf -no-remove-listing에 해당<br />—no-remove-listing은 FTP통신에서 사용되는 .listing파일을 지우지 않게 하는 설정 |



## 사이트 크롤링하기

- -r: 재귀적 다운로드
- --no-parent: 부모 디렉터리는 크롤링하지 않음
- -w 1: 1초마다 반복(서버 부하를 줄이기 위함)
- -l: 링크를 한번만 더 타고 들어감
- —restrictionists-file-names=nocontrol: URL에 한국어 등이 포함돼 있을 경우 한국어 파일명으로 저장

```
wget -r --no-parent -w 1 -l 1 --restrict-file-names=nocontrol http://www.hanbit.co.kr/

//tree구조로 디렉터리 보기 tree설치 필요함 brew install tree or sudo apt-get install -y tree
tree www.hanbit.co.kr/
```

