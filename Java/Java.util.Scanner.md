# Java.util.Scanner

- 정규식 표현을 이용한 라인단위의 검색을 지원하여 구분자(delimiter)에도 정규식 표현을 사용할 수 있어서 복잡한 형태의 구분자도 처리 가능
  - Scanner useDelimiter(Pattern pattern)
  - Scanner useDelimiter(String pattern)

```java
import java.util.*;

class ScannerEx{
  public static void main(String[] args){
    Scanner s = new Scanner(System.in);
    String[] argArr = null;
    
    while(true){
      String prompt = ">>";
      System.out.print(promt);
      
      //화면으로부터 라인단위로 입력받는다.
      String input = s.nextLine();
      
      input = input.trim(); //입력받은 값에서 불필요한 앞뒤 공백을 제거
      argArr = input.split(" +"); //입력받은 내용을 공백을 구분자로 자름
      
			String command = argArr[0].trim();
      
      if("".equals(command)) continue;
      
      //명령어를 소문자로 바꿈
      command = command.toLowerCase();
      
      //q또는 Q를 입력하면 실행종료
      if(command.equals("q")){
        System.exit(0);
      } else {
        for( int i = 0; i < argArr.length; i++){
          System.out.println(argArr[i]);
        }
      }
    }
  }
}
```

### Text파일에서 합계 계산하기

```java
import java.util.Scanner;
import java.io.File;

class ScannerEx{
  public static void main(String[] args) throws Exception{
    Scanner sc = new Scanner(new File("data2.txt"));
    int sum = 0;
    int cnt = 0;
    
    while(sc.hasNextInt()){
      sum += sc.nextInt();
      cnt++;
    }
    
    System.out.println("sum="+sum);
    System.out.println("average="+ (double)sum/cnt);
  }
}
```

