# 네트워크 통신과 API

- 대량의 데이터를 표현할 때 데이터 파일을 따로 구성하여 앱 내부에 넣어두고, 읽어들이는 방식을 이용함
- 데이터를 최신으로 유지하기 위해서 서버를 이용해 데이터 파일만 내려받음

## 네트워크 통신의 종류

- 소켓 방식 연결성 통신
  - TCP/UDP
- 프로토콜을 이용한 비연결성 통신
  - HTTP, HTTPS, SMTP

## 소켓 방식의 연결 지향 통신

- 소켓을 이용한 네트워크 통신 방식은 보통 저수준(Low-level)통신을 통하여 구현

- 한쪽에서 연결을 해제할때까지 연결되는 방식

- 연결 단계, 연결 유지단계, 연결종료 단계 등으로 단계를 나누어서 관리함

- 장점

  - 재연결이 필요없음
  - 빠르게 메시지를 주고 받음

- 단점

  - 연결유지를 위해 네트워크 자원을 많이 소모함
  - 서버 부하

- 사용처

  - 메신저, 화상통화, RPG 게임에서 이용

  #### TCP

- 데이터 유실 방지

- 완전한 전송을 보장

- UDP보다 느림

  #### UDP

- 빠른 연결

- 완전한 전송 비보장



## 비연결 지향 통신

- HTTP/HTTPS, SMTP등 프로토콜 이용
- 요청이 들어오면 응답을 보낸 뒤 바로 종료됨
- 장점
  - 네트워크 대역 소모를 줄임
  - 서버 부하를 낮춤
  - 범용적인 모바일 서비스에서 많이 사용됨
- 단점
  - 데이터 전송속도에 제약이 존재함
- 웹 서비스(Web Service): HTML 웹 페이지가 아닌, 데이터만을 주고 받을 수 있도록 설계된 모듈
  - 아키텍쳐 구조에 따라 SOAP, RESTful 방식으로 나눔
  - 데이터 타입에 따라 XML, JSON방식으로 나눔

#### SOAP(Simple Object Access Procotol)방식

- HTTP, HTTPS, SMTP 등의 프로토콜을 통해 양쪽에서 XML형태의 메시지를 주고 받도록 구현된 프로토콜
- 원격 프로시저호출(REmote Procedure Call: RPC)이라고 불리는 클라이언트-서버 구조의 메시지 패턴을 많이 사용함
- 통신구조 : Envelope/Header/Body영역으로 구분
  - Header: 선택사항. 반복이나 보안 및 트랜젝션 정보를 저장하는 메타정보 처리
  - Body: 전달하고자 하는 핵심 내용

```html
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
	<SOAP-ENV:BODY>
    	<getItemDetails xmlns="https:warehouse.example.com/ws">
            <itemId>5712587</itemId>
            <itemName>Sample Item</itemName>
        </getItemDetails>
    </SOAP-ENV:BODY>
</SOAP-ENV:Envelope>
```

- 장점
  - SOAP을 사용한 HTTP는 프록시나 방화벽에 관계없이 통신 가능
  - 표준 전송 프로토콜을 HTTP지만, 다른 프로토콜이용 가능
  - 플랫폼에 독립적인 통신이므로 이기종 플랫폼 간의 데이터 통신 편리
  - 프로그래밍 언어에 종속되지 않음
  - 매우 간단하고 확장이 용이함
- 단점
  - XML포맷을 사용하므로 다른 기술에 비해 느림(큰 데이터가 아니면 속도문제는 상관없음)

#### RESTful(Representational State Transfer)방식

- WWW 과 같은 분산 하이퍼 미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식

- 네트워크 자원을 정의하고 자원에 대한 주소를 관리하는 방법

- REST: 웹 형식을 빌어 데이터를 전송하되, 별도의 전송 프로토콜(SOAP, 쿠키) 없이 전송하기 위한 인터페이스

  - HTTP프로토콜을 바탕으로 별도의 규약없이 데이터를 주고 받음 - URI(Uniform Resource Identifier)를 이용함

    - URL(Uniform Resource Locator)과 URI(Uniform Resource Identifier)의 차이

      URL은 URI의 한 종류. URI가 인터넷 상의 자원을 구분하는 구분자이면, URL은 인터넷상으로 접근할 수 있는 파일의 위치를 나타냄

      ```
      //URL
      http://endic.naver.com/endic.nhn
      
      //URI
      http://endic.naver.com/endic.nhn?docid=1232950
      ```

- RESTful: REST 원리를 따라 구현된 시스템  

```
//URI
http://127.0.0.1/movie
```



#### RESTful API와 HTTP 전송 방식

- CRUD(Create, Read, Update, Delete)

- SNS의 RESTful을 이용한 URI 구성 - 액션을 구분지어야 함(권장하지 않음) => HTTP를 이용해 액션 구분 권장

  ```
  http://127.0.0.1/sns/article/create
  http://127.0.0.1/sns/article/read
  http://127.0.0.1/sns/article/update
  http://127.0.0.1/sns/article/delete
  ```

- RESTful API에서 HTTP메소드의 종류

  - 

    | 메소드(전송방식) | 목적                                                |
    | ---------------- | --------------------------------------------------- |
    | GET              | 특정 리소스의 대표적인 정보를 요청할 때             |
    | POST             | ID없이 리소스를 생성하거나 수정할 때                |
    | PUT              | ID기반으로 리소스를 생성하거나 수정할때             |
    | DELETE           | 리소스를 삭제할 때                                  |
    | HEAD             | GET 방식의 요청이지만 내용 없이 메타정보만 요청할때 |
    | OPTIONS          | 특정 URL에 대한 보조 메소드 역할                    |

  - URI 헤더에 구분 액션을 추가하여 처리함

- HTTP메소드

  - GET: 데이터 요청
    - 데이터를 전송할 수 있지만, URL뒤에 데이터를 줄줄이 붙여 전송하기 때문에 URL이 복잡해짐
    - 1024바이트 이상 정보를 전송 못함
  - POST: 데이터 전송


## 응답 데이터 형식에 따른 구분

## XML(Extensible Markup Language)방식

- 데이터를 주고 받을 수 있도록 작성된 Markup 언어 - HTML의 한계 극복
- 자료구조 표현에 장점
- 요청에 대한 응답을 XML포맷으로 제공
- SOAP방식의 요청이나, RESTful API모두 XML방식으로 만들어진 결과를 제공할 수 있음

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SearchViaSTNArrivalTimeByTrainService>
	<list_total_count>55</list_total_count>
    <RESULT>
    	<CODE>INFO-000</CODE>
        <MESSAGE>정상 처리되었습니다.</MESSAGE>
    </RESULT>
    <row>
        <FR_CODE>134</FR_CODE>
        <STATION_CD>1002</STATION_CD>
        <STATION_NM>남영</STATION_NM>
        <SUBWAYENAE>양주</SUBWAYENAE>
        <ARRIVETIME>06:42:00</ARRIVETIME>
        <WEEK_TAG>1</WEEK_TAG>
        <INOUT_TAG>1</INOUT_TAG>
    </row>
    <row>
        <FR_CODE>139</FR_CODE>
        <STATION_CD>1006</STATION_CD>
        <STATION_NM>영등포</STATION_NM>
        <SUBWAYENAME>양주</SUBWAYENAME>
        <ARRIVETIME>06:29:30</ARRIVETIME>
        <WEEK_TAG>1</WEEK_TAG>
        <INOUT_TAG>1</INOUT_TAG>
    </row>
</SearchViaSTNArrivalTimeByTrainService>
```

- XML 형식으로 전달 된 데이터는 데이터 형식에 맞게 분석하는 과정이 필요함 => Parsing
- Parsing을 처리하는 모듈: Parser
- iOS에서는 XMLParser모듈을 이용해 데이터 분석 가능함
- 장점
  - 시스템에 의존적이지 않아데이터 교환의 표준으로 삼을 수 있음
- 단점
  - 데이터의 의미 전달을 위한 마크업 태그 => 데이터 용량이 커짐

## JSON(JavaScript Object Notation)방식

- XML전달 방식의 단점인 용량 문제 해결을 위한 경량의 데이터 교환 형식
- 텍스트 기반 데이터 구조
- 구분
  - JSON객체
    - 집합구조
    - 순서없는 집합
    - {키: 값, 키: 값...}
  - JSON배열
    - 리스트 구조
    - 순서화 된 리스트
    - [객체1, 객체2, 객체3...]

### JSON객체 - 정렬시키는 사이트: jsonlint.com

- {키:데이터} 형태의 사전형식
- 다양한 값 표현 가능. 실수의 경우 큰따옴표를 붙이지 않음

```json
{
	"title":"다크나이트", 
    "description": "배트맨 시리즈", 
    "rating":8.95, 
    "image":"darknight.jpg"
}
```

#### JSON배열

- 배열 내부에 들어가는 항목: 아이템

```json
[
    {
	"title":"다크나이트", 
    "description": "배트맨 시리즈", 
    "rating":8.95, 
    "image":"darknight.jpg"
    },
    {
    "title":"범죄도시", 
    "description": "마동석 사이다", 
    "rating":9.9, 
    "image":"crimecity.jpg"
    }
]
```

