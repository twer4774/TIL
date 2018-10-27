# 크롤러를 사용할 때 기억해야 할 것

## 크롤러 분류하기

### 세 가지 기준에 분류

- 상태를 가지고 있는지
  - 상태를 가지는 스테이트풀(Statefull) 크롤러
  - 상태를 가지지 않는 스테이트리스(Stateless) 크롤러
    - HTTP: 모든 요청이 독립적인 특징. 인터넷 거래시, 로그인시에 식별자가 필요하면 쿠키를 이용함
    - 쿠키: HTTP요청과 응답 때 작은 데이터를 추가해서 송수신하는 구조 => Session객체로 쿠키관련 처리가능
    - Referer(리퍼러): 바로 이전에 살펴본 페이지의 URL을 서버에 전송하는 HTTP헤더 => 이미지 원본보기기능있는 사이트 크롤링
- 자바스크립트를 실행할 수 있는지
  - 대부분의 웹사이트에서 잡스크립트 사용
  - Selenium사용으로 크롤러만듦
    - 프로그램에서  브라우저를자동으로 조작할 수 있게 해주는 도구
    - 헤드리스  브라우저도 조작가능 => PhantomJS 가 유명함
- 불특정 다수의 사이트를 대상으로 하는지
  - 특정 웹사이트만을 대상으로하는 크롤러
    - 데이터를 수집하는 경우에 사용
  - 불특정 다수의 웹사이트를 대상으로 하는 크롤러
    - 구글봇 또는 사용자가 입력한 임의의 URL 크롤링
    - 특정 페이지에 모두 대응해야하므로 난이도가 높은 작업



## 크롤러를 만들 때 주의해야 하는 것

- 저작권 침해
- 크롤링 대상 웹사이트에 대한 피해등을 고려

### 피해를 줄이는 방법

#### robots.txt로 크롤러에게 지시하기

특정페이지를 크롤링하지 않을때 robots.txt와 robots meta 태그를 사용

- robots.txt

  - 웹사이트 최상위 디렉터리에 배치되어있는 텍스트파일

  - Robots Exclusion Protocol이라고 표준화 되어 있음

  - 검색 엔진은 이러한 표준을 지켜 만듦

  - | 디렉티브    | 설명                                        |
    | ----------- | ------------------------------------------- |
    | Disallow    | 크롤링을 거부할 경로를 나타냄               |
    | Allow       | 크롤링을 허가할 경로를 나타냄               |
    | Sitemap     | XML 사이트 맵의 URL을 나타냄                |
    | Crawl-delay | 크롤러의 간격을 나타냄                      |
    | User-agent  | 디렉티브 정보의 대상이 되는 크롤러를 나타냄 |

    ```
    #모든 크롤러에 대해 모든 페이지 크롤링을 허가하지 않는 robots.txt
    User-agent: * #모든 크롤러
    Disallow: /   #/로 시작하는 모든 경로
    
    #주의
    Disallow:   #값이 비었다면, 모든 크롤링이 허용된다는 것
    
    ```

    ```
    #annoying-bot이라는 문자열을 포함한 크롤러는 모두 허가하지 않음
    #나머지 크롤러는 /old/, /tmp/ 아래를 허가하지 않음
    User-agent: *
    Disallow: /old/
    Disallow: /tmp/
    
    
    User-agent: annoying-bot
    Disallow: /
    ```

    ```
    #/article/ 아래의 경로는 허가하지만 다른 경로는 허가하지 않음
    USer-agent: *
    Allow: /aritcles/
    Disallow: /
    ```

    ```python
    >>> import urllib.robotparser
    >>> rp = urllib.robotparser.RobotFileParser()
    #set_url()로 robots.txt의 URL을 설정함
    >>> rp.set_url('http://wikibook.co.kr/robots.txt')
    #read()로 robots.txt를 읽음
    >>> rp.read()
    #첫번째 매개변수에는 User-Agent 문자열, 두번째 매개변수에는 URL을 넣어 크롤링을 해도 괜찮은지 확인
    >>> rp.can_fetch('mybot', 'http://wikibook.co.kr/')
    True
    ```



#### robots meta태그

- robots.txt와 같은 목적으로 사용되는 태그
- HTML 태그로 크롤링 관련 내용 전달

```
<meta name="robots" content="noindex">
```

- 쉼표로 구분해서 여러 개의 값을 지정할 수 있음
  - nofollow: 해당 페이지 내부의 링크를 타고 도는 것을 허가하지 않음
  - noarchive: 해당 페이지를 아카이브로 저장하는 것을 허가하지 않음
  - noindex: 해당 페이지를 검색 엔진에 인덱스하는 것을 허가하지 않음



## XML 사이트맵

- 크롤러에게 크롤링해도 괜찮은 URL 목록을 제공하기 위한 XML 파일
- XML파일을 참고해서 크롤링하면 순회하는 링크의 수가 줄어들어 효율적임

```xml
<!--XML사이트맵의 예--->
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
	<url>
        <loc>http://www.example.com</loc>
        <lastmod>2005-01-01</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>
```

- 하나의 사이트맵은 10MB이내, 포함된 URL이 5000개 이내라는 제한이 있음
- 파일이 커서 분할될 경우 인덱스를 명시함

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
	<sitemap>
    	<loc>http://www.example.com/sitemap1.xml.gz</loc>
        <lastmod>2005-01-01</lastmod>
    </sitemap>
    <sitemap>
    	<loc>http://www.example.com/sitemap2.xml.gz</loc>
        <lastmod>2005-01-01</lastmod>
    </sitemap>
</sitemapindex>
```

#### 

