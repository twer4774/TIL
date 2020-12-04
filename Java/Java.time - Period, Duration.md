# Java.time - Period, Duration

- 날짜 - 날짜 = Period
- 시간 - 시간 = Duration

### between()

- 두 날짜, 시간의 차이를 구할 때 쓰임

```java
/* Period */
LocalDate date1 = LocalDate.of(2014, 1, 1);
LocalDate date2 = LocalDate.of(2015, 12, 31);

Period pe = Period.between(date1, date2);

long year = pe.get(ChronoUnit.YEARS); 
long month = pe.get(ChrnoUnit.MONTHS);
long day = pe.get(ChronoUnit.DAYS);


/* Duration */
LocalDateTime time1 = LocalTime.of(00, 00, 00);
LocalDateTime time2 = LocalTime.of(12, 34, 56); //12시 34분 56초

Duration du = Duration.between(time1, time2);

long sec = du.get(ChronoUnit.SECONDS);
int nano = du.get(ChronoUnit.NANOS);
```

- ChronoUnit으로 사용하기엔 불편함이 많으므로  Duration을 LocalTime으로 변환한 뒤 get메서드를 이용하여 계산

```java
LocalTime tmpTime = LocalTime.of(0,0).plusSeconds(du.getSeconds());

int hour = tmpTime.getHour();
int min = tmpTime.getMinute();
int sec = tmpTime.getSecond();
int nano = du.getNano();
```

