# 표준 입출력

## 표준 입출력 - System.in, System.out, Syste.err

```java
package JavaStandard;

import java.io.IOException;

/**
 * 표준 입출력
 */
public class StandardIOEx1 {

    public static void main(String[] args) {
        try{
            int input = 0;
            
            while((input=System.in.read()) != -1){
                System.out.println("input :" + input + ", (char)input : " + (char) input);
            }
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}

/*
hello

> Task :StandardIOEx1.main()
input :104, (char)input : h
input :101, (char)input : e
input :108, (char)input : l
input :108, (char)input : l
input :111, (char)input : o
input :10, (char)input : 

/r
input :47, (char)input : /
input :114, (char)input : r
input :10, (char)input : 

/n
input :47, (char)input : /
input :110, (char)input : n
input :10, (char)input : 


*/
//cmd + d 를 누르면 종료
```

## 표준 입출력의 대상변경 - setOut(), setErr(), setIn()

| 메소드                              | 설명                                            |
| ----------------------------------- | ----------------------------------------------- |
| static void setOut(PrintStream out) | System.out의 출력을 지정된 PrintStream으로 변경 |
| static void setErr(PrintStream err) | System.err의 출력을 지정한 PrintStream으로 변경 |
| static void setIn(InputStream in)   | System.in의 입력을 지정한 InputStream으로 변경  |

## RandomAccessFile

- 자바에서는 입출력이 분리되어 별도로 작업하도록 설계
- RandomAccessFile만은 하나의 클래스로 파일에 대한 입출력을 모두 할 수 있도록 되어 있음
- 장점
  - 파일의 어느 위치에나 읽기/쓰기가 가능
    - 파일 내부에서 포인터 사용
- RandomAccessFile의 생성자와 메소드

| 생성자/메소드                                                | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| RandomAccessFile(File file, String mode)<br />RandomAccessFile(String fileName, String mode) | 주어진 file에 읽기 또는 읽기와 쓰기를 하기 위한 RandomAccessFile인스턴스를 생성<br />mode의 값은 "r", "rw", "rws", "rwd"를 지정할 수 있음<br />r - 읽기전용 / rw- 읽기쓰기 / rws - 읽기쓰기(파일지연없이쓰기) /rwd - 읽기쓰기(메타정보포함) |
| FileChannel getChannel()                                     | 파일의 파일 채널 반환                                        |
| FIleDescriptor getFD()                                       | 파일의 파일 디스크립터를 반환                                |
| long getFilePointer()                                        | 파일 포인터의 위치를 알려줌                                  |
| long length()                                                | 파일의 크기를 얻을 수 있음                                   |
| void seek(long pos)                                          | 파일 포인터의 위치를 변경. 위치는 파일의 첫 부분부터 pos크기만큼 떨어진 곳 |
| void setLength(long newLength)                               | 파일의 크기를 지정된 길이로 변경                             |
| int skipBytes(int n)                                         | 지정된 수만큼의 byte를 건너띔                                |

```java
import java.io.*;

class RandomAccessFileEx{
  public static void main(String[] args){
    try{
       RandomAccessFile raf = new RandomAccessFile("test.dat", "rw");
      System.out.println("파일 포인터의 위치:" + raf.getFilePointer());
      raf.writeInt(100);
      System.out.println("파일 포인터의 위치:" + raf.getFilePointer());
      raf.writeLong(100L);
      System.out.println("파일 포인터의 위치:" + raf.getFilePointer());
    } catch (IOException e){
      e.printStackTrace();
    }
  }
}
```

- 배열에서의 사용

```java
import java.io.*;

class RandomAccessFileEx2{
  public static void main(String[] args[]){
    //							번호, 국어 ,영어, 수학
    int[] score = {	1,	100,	90, 90,
 								    2, 	70,	 	90, 100, 
                    3,	100,	100,100,
                    4,	70,		60,	80,
                    5, 	70,		90,	100	
    };	
    
    try{
     	RandomAccessFile raf = new RandomAccessFile("score2.dat", "rw");
      for(int i = 0; i < score.length; i++){
        raf.writerInt(score[i]);
      }
      while(true){
        system.out.println(raf.readLine());
      }
    } catch(EOFException eof){
      //readInt()를 호출했을 때 더이상 읽을 내용이 없으면 발생
    } catch(IOException e){
      e.printStackTrace();
    }
  }
}
```

