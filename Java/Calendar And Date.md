# Calendar And Date

## Calendar와 GregorianCalendar

- Calendar는 추상클래스이기 때문에 직접 객체를 생성할 수 없고 메서드를 통해 완전히 구현된 클래스의 인스턴스를 얻어야 함

- ```java
  Calendar cal = new Calendar(); //인스턴스 생성 불가
  
  Calendar cal = Calendar.getInstatnce(); //불완전 클래스를 구현한 인스턴스 반환
  ```

- GregorianCalendar

  - 태국을 제외한 국가에서는 그레고리안을 사용함
  - getInstance()를 이용하면 시스템 설정에 맞는 달력을 가져옴

## Date와 Calendar간의 변환

- Calendar가 추가되면서 Date의 메서드 대부분이 deprecated 됨
- Calendar와 Date 간의 형변환

```java
//1.Calendar to Date
Calendar cal = Calendar.getInstance();
Date d = new Date(cal.getTimeInMillis()); //Date(long date)

//2.Date를 Calendar로 변환
Date d = new Date();
Calendar cal = Calendar.getInstance();
cal.setTime(d)
```

```java
import java.util.*;

class CalendarEx{
  public static void main(String[] args){
    //기본적으로 현재 날짜와 시간으로 설정
    Calendar today = Calendar.getInstance();
    System.out.println("Year: " + today.get(Calendar.YEAR));
    System.out.println("월(0~11): 0:1" + today.get(Calendar.MONTH));
    System.out.println("이 해의 몇 째 주: " + today.get(Calendar.WEEK_OF_YEAR));
    System.out.println("이 달의 몇 째 주: " + today.get(Calendar.WEEK_OF_MONTH));
    
    //DATE와 DAY_OF_MONTH는 같음
    System.out.println("이 달의 몇일 : " + today.get(Calendar.DATE));
    System.out.println("이 달의 몇일 : " + today.get(Calendar.DAY_OF_MONTH));
    System.out.println("이 해의 몇일 : " + today.get(Calendar.DAY_OF_YEAR));
    System.out.println("요일(1~7, 1:일요일)" + today.get(Calendar.DAY_OF_WEEK));
    
    //시간
    System.out.println("시간(0~11): " + today.get(Calednar.HOUR));
    System.out.println("시간(0~23): " + today.get(Calednar.HOUR_OF_DAY));
    System.out.println("분(0~59): " + today.get(Calednar.MINUTE));
    System.out.println("초(0~59): " + today.get(Calednar.SECOND));
    
    System.out.println("1000분의 1초(0~999): " + today.get(Calendar.MILLISECOND));
    //1000분의 1초를 시간으로 표시하기 위해 3600000으로 나눔(1시간 = 60*60초)
    System.out.println("TimeZone(-12~+12): " + (today.get(Calendar.ZONE_OFFSET)/(60*60*1000)));
    System.out.println("이 달의 마지막 날: " + today.getActualMaximum(Calendar.DATE));
  }
}
```

- 주의할점 :월, 요일, 시간, 분, 초 등이 우리가 일상적으로 생각하는 것과 다름(보통 -1을해야함 ex)8월은 7로 표시 )

### 두 날짜 간의 차이 얻기

```java
import java.util.*;

class CalendarEx{
  public static void main(String[] args){
    	Calendar date1 = Calendar.getInstance();
    	Calendar date2 = Calendar.getInstance();
   
    long difference = (date2.getTimeInMillios() - date1.getTimeInMillis())/1000;
    
    System.out.println("차이 : " + differecne);
    System.out.println("일로 계산: " + difference/(24*60*60) + "일이 지남");
  }
}
```

### 날짜와 시간을 원하는 값을 변경 - set

```java
import java.util.*;

class CalendarEx{
  public static void main(String[] args){
    	Calendar time1 = Calendar.getInstance();
    	Calendar time2 = Calendar.getInstance();
   
    	//10시 20분 30초로 설정
    	time1.set(Calendar.HOUR_OF_DAY, 10);
    	time1.set(Calendar.MINUTE, 20);
    	time1.set(Calendar.SECOND, 30);
  }
}
```

### 일자 더하기

```java
import java.util.*;

class CalendarEx{
  public static void main(String[] args){
    Calendar date = Calendar.getInstance();
    date.set(2020, 11, 25);
    
    System.out.println("1일 후 :");
   	date.add(Calendar.DATE, 1);
    System.out.println(toString(date));
    
    System.out.println("6달 후 :");
   	date.add(Calendar.MONTH, -6);
    System.out.println(toString(date));
    
    System.out.println("31일 후 :");
   	date.add(Calendar.DATE, 31);
    System.out.println(toString(date));
    
  }
  public static String toString(Calendar date){
    return date.get(Calendar.YEAR) + "/" +(date.get(Calendar.MOTNH)+1)+ "/" + date.get(Calendar.DATE));
  }
}
```

