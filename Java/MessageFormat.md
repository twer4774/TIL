# MessageFormat

- 정해진 양식에 맞게 출력할 수 있도록 도와줌
- 데이터가 들어갈 자리를 마련해 놓은 양식을 미리 작성하고 프로그램을 이용해 다수의 데이터를 같은 양식으로 출력할 때 이용
  - 고객들에게 보낼 안내문 등

```java
import java.text.*;

class MessageFormatEx{
  
  public void static main(String[] args){
    String msg = "Name: {0} \nTel: {1} \nAge:{2} \nBirthday:{3}";
    
    Pbject[] arguments = {
      "이자바", "02-123-1234", "27", "07-09"
    };
    
    String result = MessageFormat.format(msg, arguemtns);
    System.out.println(result);
  }
}

/*
Name: 이자바
Tel: 02-123-1234
Age: 27
Birthday: 07-09
*/
```

- DB에 저장하기 위한 MessageFormat

```java
import java.text.*;

public MessageFormatEx{
  public static void main(String[] args){
    String tableName = "CUT_INFO";
    String msg = "INSERT INTO " + tableName + " VALUES (''{0}'', ''{1}'',''{2}'',''{3}'');";
    
    Object[][] arguments = {
      {"이자바", "02-123-1234", "27", "08-09"},
      {"김자바", "01-325-1231", "39", "01-20"},  
    };
    
    
    for(int i=0; i < arguments.length; i++){
      String result = MessagFormat.format(msg, arguments[i]);
      System.out.println(result);
    }
  }
}
}
```

- 파일에서 데이터 뽑아내기

```java
import java.util.*;
import java.text.*;
import java.io.*;

class MessageFormatEx{
  public static void main(String[] args) throws Exception{
    String tableName="CUST_INFO";
    String fileName = "data4.txt";
    String msg = "INSERT INTO " + tableName + " VALUES ({0}, {1}, {2}, {3});";
    
    Scanner s = new Scanner(new File(fileName));
    
    String pattern = "{0}, {1}, {2}, {3}";
    MessageFormat mf = new MessageFormat(pattern);
    
    while(s.hasNextLine()){
      String line = s.nextLine();
      Object[] objs = mf.parse(line);
      System.out.println(MessageFormat.format(msg, objs));
    }
    
    s.close(); //Scanner파일 닫기
  }
}
```

