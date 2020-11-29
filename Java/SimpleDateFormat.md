# SimpleDateFormat

- Date와 Calendar로 원하는 형태로 출력하는 것은 불편함
- SimpleDateFormat으로 간단하게 할 수 있음
  - DateFormat은 추상클래스로 SimpleDateFormat의 조상

| 기호      | 의미                                                        | 보기              |
| --------- | ----------------------------------------------------------- | ----------------- |
| G         | 연대(BC, AD)                                                | AD                |
| y         | 년도                                                        | 2020              |
| M         | 월(1~12)                                                    | 10, 10월 또는 Oct |
| w / W     | 년의 몇 번째 주(1~53) / 월의 몇 번째 주(1~5)                | 50 / 4            |
| d / D     | 월의 몇 번째 일(1~31) / 년의 몇 번째 일(1~366)              | 15 / 100          |
| F         | 월의 몇 번째 요일(1~5)                                      | 1                 |
| E         | 요일                                                        | 월                |
| a         | 오전/오후(AM,PM)                                            | AM                |
| H         | 시간(0~23)                                                  | 20                |
| k / K / h | 시간(1~24) / (0~11) / (1~12)                                | 21 / 3 / 2        |
| m / s / S | 분(0~59) / 초(0~59) / 천분의 일초(0~999)                    | 35 / 55 / 253     |
| z / Z     | Time zone(General Time Zone) / Time zone(RFC 822 Time Zone) | GMT+9:00 / +0900  |
| '         | escape문자(특수문자 표현에 사용)                            |                   |

```java
import java.util.*;
import java.text.*;

class DateFormatEx{
  public static void main(String[] args){
    Date today new Date();
    
    SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
    SimpleDateFormat sdf5, sdf6, sdf7, sdf8, sdf9;
    
    sdf1 = new SimpleDateFormat("yyyy-MM-dd");
    sdf2 = new SimpleDateFormat("''yy년 MMM dd일 E요일"); //홑따옴표는 escape문자열이므로 표시를위해 두번써야함
    sdf3 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
    sdf4 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss a");
    
    sdf5 = new SimpleDateFormat("오늘은 올 해의 D번째 날입니다.");
    sdf6 = new SimpleDateFormat("오늘은 이 달의 d번째 날입니다.");
    sdf7 = new SimpleDateFormat("오늘은 올 해의 w번째 주입니다.");
    sdf8 = new SimpleDateFormat("오늘은 이 달의 W번째 주입니다.");
    sdf9 = new SimpleDateFormat("오늘은 이 달의 F번째 요일입니다.");

    System.out.println(sdf1.format(today)); //2015-11-23
    System.out.println(sdf2.format(today)); //'15년 11월 23일 월요일
    System.out.println(sdf3.format(today)); //2015-11-23 12:18:49.235
    System.out.println(sdf4.format(today)); //2015-11-23 03:46:49 오후
    System.out.println();
    System.out.println(sdf5.format(today)); //오늘은 올 해의 327번째 날입니다.
    System.out.println(sdf6.format(today)); //오늘은 이 달의 23번째 날입니다.
    System.out.println(sdf7.format(today)); //오늘은 올 해의 48번째 주입니다.
    System.out.println(sdf8.format(today)); //오늘은 이 달의 4번째 주입니다.
    System.out.println(sdf9.format(today)); //오늘은 이 달의 4번째 월요일입니다.
  }
}
```

- Calendar인스턴스를 받아 Date인스턴스로 변환하는 방법
  - format은 Date인스턴스만 사용 가능

```java
import java.util.*;
import java.text.*;

class DateFormatEx{
  public static void main(String[] args){
    Calendar cal = Calednar.getInstanace();
    cal.set(2005, 9, 3); //2005년 10월 3일 - Month는 0~11의 범위를 갖음
    
    Date day = cal.getItme(); //Calendar를 Date로 변환
    
    SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
    sdf1 = new SimpleDateFormat("yyyy-MM-dd");
    sdf2 = new SimpleDateFormat("yy-MM-dd E요일");
    sdf3 = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
    sdf4 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss a");
    
    System.out.println(sdf1.format(day)); //2015-10-03
    System.out.println(sdf2.format(day)); //15-10-03 토요일
    System.out.println(sdf3.format(day)); //2015-10-03 15:47:47.297
    System.out.println(sdf4.format(day)); //2015-10-03 03:47:47 오후
  }
  
}
```

- pare(String source)를 사용한 출력형식 변환

```java
import java.util.*;
import java.text.*;

class DateFormatEx{
  public static void main(STring[] argS){
    DateFormat df = new SimpleDateFormat("yyyy년 MM월 dd일");
    DateFormat df2 = new SimpleDateFormat("yyyy/MM/dd");
    
    try{
      Date d = df.jparse("2015년 11월 23일");
      System.out.println(df2.format(d));
    } catch(Exception e){}
  }
}
//2015/11/23
```

- 입력의 제한걸기

```java
import java.util.*;
import java.text,*;

class DateFormatEx{
  public static void main(String[] args){
    String pattern = "yyyy/MM/dd";
    DateFormat df = new SimpleDateFormat(pattern);
    Scanner s = new Scanner(System.in);
    
    Date inDate = null;
    
    System.out.println("날짜를 " + pattern + "의 형태로 입력해주세요.(입력예:2015/12/31)");
    
    while(s.hasNextLine()){
      try{
        inDate = df.parse(s.nextLine());
        break;
      } catch(Exception e){
				 System.out.println("날짜를 " + pattern + "의 형태로 입력해주세요.(입력예:2015/12/31)");
      }
    }//while
    
    Calnedar cal = Calnedar.getInstance();
    cal.setTieme(inDate);
    Calendar today = Calendar.getInstance();
    long day = (cal.getTimeInMillis() - today.getTimeInMillis())/(60*60*1000);
    System.out.println("입력하신 날짜는 현재와 " + day + "시간 차이가 있습니다.");
  }//main
}
```

