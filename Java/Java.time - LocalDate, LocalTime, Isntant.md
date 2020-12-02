# Java.time - LocalDate, LocalTime, Isntant

- 날짜 LocalDate
- 시간 LocalTime
- 날짜&시간 LocalDateTime
- 시간대 ZonedDateTime 

### Period와 Duration

- 날짜 - 날짜 = Period
- 시간 - 시간 = Duration

#### 객체 생성

- now() - 현재 날짜와 시간 저장

```java
LocalDate date = LocalDate.now(); //2015-11-23
LocalTime time = LocalTime.now(); //21:44:01.123
LocalDateTime dateTime = LocalDateTime.now(); //2015-11-23T21:43:01.222
ZonedDateTime dateTimeInKr = ZonedDateTime.now(); //2015-11-23T21:43:01.222+09:00[Asia/Seoul]
```

- of() - 필드의 값을 지정하면 자동으로 객체생성

```java
LocalDate date = LocalDate.of(2015, 11, 23); //2015년 11월 23일
LocalTime time = LocalTime.of(23, 59, 59); //23시 59분 59초
LocalDateTime dateTime = LocalDateTime.of(date, time);
ZonedDAteTime zDateTime = ZonedDateTime.of(dateTime, ZoneId.of("Asia/Seoul"));
```

### Temporal과 TemporalAmount

- 날짜와 시간을 표현하는 함수들은 Tempral, TempralAccessor, TemporalAdjuster인터페이스를 구현한 것
- TemporalAmount인지 아닌지만 확인 하면 됨
  - TemproalAmount는 Period와 Duration의 인터페이스

### TemporalUnit과 TemporalField

- TemporalUnit인터페이스
  - 날짜와 시간의 다누이를 정의해 놓은 것
  - ChronoUnit : TemporalUnit인터페이스를 구현 한것
- TemproalField
  - 년, 월, 일 등 날짜와 시간의 필드를 정의 해 놓은 것

```java
LocalTime now = LocalTime.now(); //현재시간
int minute = now.getMinute(); //현재시간에서 분(minute)만 뽑아낸다.
int minute = now.get(ChronoField.MINUTE_OF_HOUR); //위의 문장과 동일

LocalDate today = LocalDate.now(); 오늘
LocalDate tomorrow = today.plus(1, ChronoUnit.DAYS); //오늘에 1을 더함
LocalDate tomorrow = today.plusDays(1); //위 문장과동일
```

## LocalDate와 LocalTime

### 특정 필드에서 값 가져오기 - get(), getXXX()

- calendar와의 차이점 : 월이나 요일을 가져올 때 0부터가 아닌 1부터 시작함
- LocalDate
  - getYear(), getMonthValue(), getMonth(), getDayOfMonth(), getDayOfYear(), getDayOfWeek(), lengthOfMonth(), lengthOfYear(), isLeapYear()
- LocalTime
  - getHour(), getMinute(), getSecond(), getNano()



### 날짜와 시간의 비교 - isAfter(), isBefore(), isEqual()

```java
import java.time.*;
import java.time.temproal.*;

class NewTimeEx{
  public static void main(String[] args){
    LocalDate today = LocalDate.now(); //오늘의 날짜
    LocalTime now = LocalTime.now(); //현재시간
    
    LocalDate birthDate = LocalDate.of(1999, 12, 31); //1999년 12월 31일
    LocalTime birthTime = LocalTime.of(23, 59, 59); //23시 59분 59초
    
    System.out.println("today="+today);
    System.out.println("now="+now);
    System.out.println("birthDate="+birthDate); //1999-12-31
    System.out.println("birthTime="+birthTime); //23:59:59
    
    //with : 값을 변경할때 쓰임
    System.out.println(birthDate.withYear(2000)); //2000-12-31
    System.out.println(birthDate.plusDays(1)); //2000-01-01
    System.out.println(birthDate.plus(1, ChronoUnit.DAYS)); //2000-01-01
    
    //23:59:59 -> 23:00
    System.out.println(birthTime.truncatedTo(ChronoUnit.HOURS));
    
    //특정 ChronoField의 범위를 알아내는 방법
    System.out.println(ChronoField.CLOCK_HOUR_OF_DAY.rang()); //1-24
    System.out.println(ChronoField.HOUR_OF_DAY.range()); //0-23
  }
}
```



## Intant

- 에포크 타임(EPOCH TIME, 1970-01-01 00:00:00 UTC)부터 경과된 시간을 나노초 단위로 표현
  - 한국 시간대가 +09:00이므로 9시간 차이가 남
- 사람에겐 불편하지만 단일진법이기 때문에 계산하기 쉬움

```java
Instant now = Instant.now();
Instant now2 = Instant.ofEpochSecond(now.getEpochSecond());
Instant now3 = Instant.ofEpochSecond(now.getEpochSecond(), now.getNano());
```

### Instant와 Date간의 변환

Instant는 기존 java.util.Date를 대체하기 위한 것

```java
static Date from(Instant instant) //Instatn -> Date
Instatn toInstant() //Date -> Instant
```

