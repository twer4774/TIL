# Java.time - parsing, format

- Parsing : 날짜와 시간을  원하는 형식으로 출력하고 해석
- 형식화(formatting)와 관련된 클래스들은 java.time.format패키지에 정의되어 있음
  - DateTimeFormatter가 핵심

```java
LocalDate date = LocalDate.of(2016, 1, 2);
String yyymmdd = DateTimeFormatter.ISO_LOCAL_DATE.format(date); //2016-01-02
String yyyymmdd = date.foramt(DateTimeForamtter.ISO_LOCAL_DATE); //2016-01-02
```

- ISO_DATE_TIME / ISO_LOCAL_DATE / ISO_LOCAL_TIME / ISO_LOCAL_DATE_TIME / ISO_OFFSET_DATE / ISO_OFFSET_DATE / ISO_OFFSET_TIME  등 다양한 종류의 DateTimeFormatter 정의되어 있음

### 로컬에 종속된 형식화

- DateTimeFormatter의 static메서드 ofLocalizedDate(), ofLocalizedTime(), ofLocalized DateTime()은 로케일에 종속적인 포맷터 생성

```java
DateTimeFormatter formatter = DateTimeFormatter.ofLocalizedDate(FormatStyle.SHORT);
String shortFormat = formatter.foramt(LocalDate.now());
```

### 출력형식 정의

```java
DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy/MM/dd");
```

| 기호          | 의미                                                         | 보기         |
| ------------- | ------------------------------------------------------------ | ------------ |
| G             | 연대(BC, AD)                                                 | 서기 또는 AD |
| y 또는 u      | 년도                                                         | 2020         |
| M 또는 L      | 월(1~12 / 1월~12월)                                          | 12           |
| Q 또는 q      | 분기(quarter)                                                | 4 (분기)     |
| w / W         | 년의 몇 번째 주(1~53) / 월의 몇 번째 주(1~5)                 | 48 / 4       |
| d / D         | 월의 몇 번째 일(1~31) / 년의 몇 번째 일(1~366)               | 3 / 338      |
| F             | 월의 몇 번째 요일(1~5)                                       | 4            |
| E 또는 e      | 요일                                                         | 토 또는 7    |
| a             | 오전/오후(AM, PM)                                            | 오후         |
| H / k / K / h | 시간(0~23) / 시간(1~24) / 시간(0~11) / 시간(1~12)            |              |
| m             | 분(0~59)                                                     |              |
| s / S / A     | 초(0~59) / 천분의 일초(0~999) /천분의 일초 (그 날의 0:0:0부터의 시간) |              |
| n / N         | 나노초                                                       |              |
| V             | 시간대 Id                                                    | Asia/Seoul   |
| z             | 시간대 이름                                                  | KST          |
| O             | 지역화된 zone-offset                                         | GMT+9        |
| Z             | zone-offset                                                  | +0900        |

### 문자열을 날짜와 시간으로 파싱하기

```java
import java.time.*;
import java.time.format.*;

class DateFormatterEx{
  public static void main(String[] args){
    LocalDate newYear = LocalDate.parse("2016-01-01", DateTimeFormaater.ISO_LOCAL_DATE);
    
    LocalDate date = LocalDate.parse("2001-01-01");
    LocalTime time = LocalTime.parse("23:59:59");
    LocalDateTime dateTime = LocalDateTime.parse("2001-01-01T23:59:59");
    
    DateTimeFormatter pattern = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
    LocalDateTime endOfYear = LocalDAteTime.parse("2015-12-31 23:59:59", pattern);
    
    Syste.out.println(newYear); //2016-01-01
    Syste.out.println(date); //2001-01-01
    Syste.out.println(time); //23:59:59
    Syste.out.println(dateTime); //2001-01-01T23:59:59
    Syste.out.println(endOfYear); //2015-12-31T23:59:59
  }
}
```

