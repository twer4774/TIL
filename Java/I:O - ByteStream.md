# I/O - ByteStream

### 바이트 기반 스트림 - Input Stream, Output Stream

- FileInputStream, FileOutputStream : 파일
- ByteArrayInputStream, ByteArrayOutputStream : 메모리(byte배열)
- PipedInputStream, PipedOutputStream : 프로세스(프로세스간의 통신)
- AudioInputStream, AudioOutputStream : 오디오 장치

```java
public abstract class InputStream{
  ...
  //입력스트림으로부터 1 byte를 읽어서 반환. 읽을 수 없으면 -1 반환
  abstract int read();
  
  //입력스트림으로부터 len개의 bte를 읽어서 byte 배열 b의 off위치부터 저장
  int read(byte[] b, int off, int len){
    ...
    for(int i = off; i < off + len; i++){
      //read()를 호출해서 데이터를 읽어서 배열을 채움
      b[i] = (byte)read();
    }
    ..
  }
  //입력스트림으로부터 byte배열 b의 크기만큼 데이터를 읽어서 배열 b에 저장
  int read(byte[] b) {
    return read(b, 0, b.length);
  }
}
```

### InputStream 메서드

| 메서드명                             | 설명                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| int available()                      | 스트림으로 부터 읽어 올 수 있는 데이터의 크기 반환           |
| void close()                         | 스트림을 닫음으로써 사용하고 있던 자원을 반환                |
| void mark(int readlimit)             | 현재 위치를 표시해놓음. 후에 reset()에 의해 표시해 놓은 위치로 다시 돌아갈 수 있음 |
| boolean markSupported()              | mark(), reset()을 지원하는지 알려줌. mark, reset()은 선택사항이므로 먼저 markSupported()를 호출하여 여부를 확인 |
| abstract int read()                  | 1 byte를 읽어 옴. 읽어 올 데이터가 없으며 -1 반환            |
| int read(byte[] b)                   | 배열 b의 크기만큼 읽어서 배열을 채우고 읽어 온 데이터의 수 반환 |
| int read(byte[] b, int off, int len) | 최대 len개의 byte의 개수를 읽어서, 배열 b의 지정된 위치(off)부터 저장 |
| void reset()                         | 스트림에서의 위치를 마지막으로 mark()이 호출되었던 위치로 되돌림 |
| long skip(long n)                    | 스트림에서 주어진 길이(n)만큼 건너띔                         |

### OutputStream 메서드

| 메서드명                               | 설명                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| void close()                           | 입력소스를 닫음으로써 자원 반환                              |
| void flush()                           | 스트림 버퍼에 있는 모든 내용을 출력소스에 씀                 |
| abstract void write(int b)             | 주어진 값을 출력 소스에 씀                                   |
| void write(byte[] b)                   | 주어진 배열 b에 저장된 모든 내용을 출력 소스에 씀            |
| void write(byte[] b, int off, int len) | 주어진 배열 b에 저장된 내용 중에서 off번째부터 len개 만큼만 읽어서 출력 소스에 씀 |

## ByteArrayInputStream, ByteArrayOutputStream

- 메모리, 즉 바이트 배열에 데이터를 입출력하는데 사용되는 스트림
- 주로 다른 곳에 입출력하기 전에 데이터를 임시로 바이트 배열에 담아서 변환 작업등의 작업을 하는데 이용
- 자주 사용되지는 않음

```java
import java.io.*;
import java.util.Arrays;

class IOEx1{
  public static void main(String[] args){
    byte[] inSrc = {0,1,2,3,4,5,6,7,8,9};
    byte[] outSrc = null;
    
    ByteArrayInputStream input = null;
    ByteArrayOutputStream output = null;
    
    int data = 0;
   
    while((data = input.read()) != -1){ //read()를 호출한 반한값을 변수 data에 저장후 data에 저장된 값이 -1이 아닌지 비교
      output.write(data); 
    }
    
    outSrc = output.toByteArray(); //스트림의 내용을 byte배열로 반환
    System.out.println("Input Source :" + Arrays.toString(inSrc));
    System.out.println("Output Source :" + Arrays.toString(outSrc));
  }
}

/*
Input Source : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Output Source : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
*/
```

- 배열을 이용해 입출력 작업이 효율적으로 이루어지도록 함
  - 위의 예제와 차이: byte 배열을 사용해서 한번에 배열의 크기만큼 읽고 쓸 수 있음(바구니를 만들어서 한번에 많이 옮기는 효과)

```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.util.Arrays;

/**
 * 배열을 이용하여 입출력 작업을 효율적으로 실행
 */
public class IOByteArrayStreamWithArray {
    public static void main(String[] args) {
        byte[] inSrc = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        byte[] outSrc = null;
        byte[] temp = new byte[10];

        ByteArrayInputStream input = null;
        ByteArrayOutputStream output = null;

        input = new ByteArrayInputStream(inSrc);
        output = new ByteArrayOutputStream();

        input.read(temp, 0, temp.length); //읽어 온 데이터를 배열 temp에 담음
        output.write(temp, 5, 5); //temp[5]부터 5개의 데이터를 write함

        outSrc = output.toByteArray();

        System.out.println("Input Source : " + Arrays.toString(inSrc));
        System.out.println("temp : " + Arrays.toString(inSrc));
        System.out.println("Output Source : " + Arrays.toString(outSrc));
    }
}

/*
Input Source : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Output Source : [5, 6, 7, 8, 9]
*/
```

- try-catch문을 이용해 IOException 피하기

```java
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.util.Arrays;

/**
 * read(), write()는 IOExcetpion을 발생 시킬 수 있기 때문에 try-catch문으로 감싸줌
 */
public class IOByteArrayStreamWithArrayTryCatch {

    public static void main(String[] args) {
        byte[] inSrc = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        byte[] outSrc = null;
        byte[] temp = new byte[4];

        ByteArrayInputStream input = null;
        ByteArrayOutputStream output = null;

        input = new ByteArrayInputStream(inSrc);
        output = new ByteArrayOutputStream();

        try {
            while(input.available() > 0){
                int len = input.read(temp); //읽어 온 데이터의 개수를 반환
                output.write(temp, 0, len); //읽어 온 만틈만 write 함
            }
        } catch (IOException e) {}

        outSrc = output.toByteArray();

        System.out.println("Input Source :" + Arrays.toString(inSrc));
        System.out.println("temp :" + Arrays.toString(temp));
        System.out.println("Output Source :" + Arrays.toString(outSrc));
    }
}
/*
Input Source :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
temp :[8, 9, 6, 7]
Output Source :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
*/
```

