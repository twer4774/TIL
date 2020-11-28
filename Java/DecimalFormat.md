## DecimalFormat

- 숫자 형식화에 사용
- 숫자 데이터를 정수, 부동소수점, 금액 등의 다양한 형식으로 표현 가능
  - 0 : 10진수(값이 없을때는 0)
  - \#: 10진수
  - . : 소수점
  - -: 음수부호
  - E: 지수 기호
  - ;: 패턴구분자
  - %: 퍼센트
  - \u00A4: 통화(원화표시)
  - ': escape문자

```java
double number = 1234567.89;
DecimalFormat df = new DecimalFormat("#.#E0");
String result = df.format(number);
```

```java
import java.text.*;

class DecimalFormatEx{
  public static void main(STring[] args){
    DecimalFormat df = new DecimalFormat("#, ###.##");
    DecimalFormat df2 = new DecimalFormat("#.###E0");
    
    try{
      Number num = df.parse("1, 2234, 567.89");
      SYstem.out.println("1,234,567.89" + " => ");
      
      double d = num.doubleValue();
      System.out.println(d + " -> ");
      System.out.println(df2.format(num));
    } catch(Exception e){}
  }
}

//1, 234, 567.89 => 1234567.89 -> 1.235E6
```

