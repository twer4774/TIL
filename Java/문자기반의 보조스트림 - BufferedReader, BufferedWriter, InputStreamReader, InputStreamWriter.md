# 문자기반의 보조스트림 - BufferedReader, BufferedWriter, InputStreamReader, InputStreamWriter

## BufferedReader와 BufferedWriter

- 입출력의 효율을 높일 수 있음 - 비교할 수 없을 정도로 효율이 좋아짐
- BufferedReader의 readLine() 메소드를 이용하여 데이터를 라인단위로 읽음

```java
//BufferedReaderEx1

import java.io.*;

class BufferedReaderEx1{
  public static void main(String[] args){
    try{
      FileReader fr = new FileReader("BufferedReaderEx1.java");
      BufferedReader br = new BufferedReader(fr);
      
      String line = "";
      for(int i=1; (line = br.readLine()) != null; i++){
        //";"를 포함한 라인을 출력
        if(line.indexOf(";")!=-1){
          System.out.println(i+":"+line);
        }
      }
      br.close()
    } catch (IOException e){}
  }
}
```

## InputStreamReader와 OutputStreamWriter

- InputStreamReader의 생성자와 메서드

| 생성자/메소드                                     | 설명                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ |
| InputStreamReader(InputStream in)                 | OS에서 사용하는 기본 인코딩의 문자로 변환하는 InputStreamReader생성 |
| InutStreamReader(InputStream in, String encdoing) | 지정된 인코딩을 사용하는 InputStreamReader생성               |
| String getEncoding()                              |                                                              |

- OutputStreamWriter의 생성자와 메소드

| 생성자/메소드                                         | 설명                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------ |
| OutputStreamWriter(OutputStream out)                  | OS에서 사용하는 기본 인코딩의 문자로 변환하는 OutputStreamWriter 생성 |
| OutputStreamWriter(OutputStream out, String encoding) |                                                              |
| String getEncoding()                                  |                                                              |

```java
import java.io.*;

class InputStreamReaderEx{
  public static void main(String[] args){
    String line = "";
    
    try{
			InputStreamReader isr = new InputStreamReader(System.in);
      BufferedReader br = new BufferedReader(isr);
      
      System.out.printn("사용중인 OS의 인코딩 : " + isr.getEncoding());
      
      do{
        System.out.print("문장을 입력하세요. 마치시려면 q를 입력하세요");
        line = br.readLine();
        System.out.println("입력하신 문장 : " + line);
      } while(!line.equalsIgnoreCase("q"));
      
      br.close();
      System.out.println("프로그램을 종료합니다.");
    } catch(IOExeption e){}
  }
}
```

