# Java.util.StringTokenizer

- 지정된 구분자(delimiter)를 기준으로 토큰이라는 단위로 잘라내는데 사용
- split로 이용해도 됨
  - String[] result = "100, 200, 300, 400".split(",");
  - Scanner sc2 = new Scanner("100,200,300,400").useDelimiter(",");
- 정규식이 익숙하지 않은 경우 StringTokenizer를 사용하는 것이 좋음(정규식보다 직관적으로 패턴을 볼 수 있음)
  - 단, StringTokenizer는 구분자로 단 하나의 문자만 사용가능하기 때문에 복잡한 형태의 구분자로 나눌때는 정규식을 사용해야 함

```java
import java.util.*;

class StringTokenizerEx{
  public static void main(String[] args){
    String source = "100,200,300,400";
    StringTokenizer st = new StringTokenizer(source, ",");
    
    while(st.hasMoreTokens()){
      System.out.println(st.nextToken());
    }
  }
}
/*
100
200
300
400
*/
```

```java
import java.util.*;

class StirngTokenizerEx{
  public static void main(String[] args){
    String expression = "x=100*(200+300)/2";
    //여러 문자들을 구분자로 지정(정규식 보다 직관적)
    StringTokenizer st = new StringTokenizer(expression, "+-*/=()", true);
    
    while(st.hasMoreTokens()){
      System.out.println(st.nextToken());
    }
  }
}

/*
x
=
100
*
(
200
+
300
)
/
2
*/
```

- +-*/=()는 각각이 모두 구분자로 인식함
  - += 처럼 두문자이상이 하나로의 구분자로 역하을 하려면 split메서드 이용

### Split()와 비교

```java
import java.util.*;
class StringTokenizerEx{
  public static void main(String[] args){
    String data = "100,,,200,300";
    
    String[] result = data.split(",");
    StringTokenizer st = new StringTokenizr(data, ",");
    
    for(int i=0; i < result.length; i++){
      System.out.println(result[i]+"|");
    }
    
    System.out.println("개수:"+result.length);
    
    int i=0;
    for(;st.hasMoreTokens();i++){
      System.out.println(st.nextToken()+"|");
      
      System.out.println("개수:"+i);
    }
  }
}

/*
100| ||200|300|개수:5 => split()
100|200|300|개수:3 => StringTokenizer
*/
```

- split()은 빈 문자열도 토큰으로 인식
- split()은 반환시 배열에 담아서 반환하므로 성능적으로 StringTokenizer보다 조금 더 느림