# IO - Byte-based auxiliary stream(바이트기반의 보조스트림)

### 보조 스트림

- 스트림 기능을 보완하기 위한 스트림
- 입출력이 불가능하고 스트림을 먼저 생성한 후 보조 스트림을 생성해야함

```java
//먼저 기반 스트림을 생성
FileInputStream fis = new FileInputStream("test.txt");

//기반 스트림을 이용해 보조 스트림 생성
BuffredInputStream bis = new BufferedInputStream(fis);

bis.read(); //보조 스트림인 BufferedInputStream으로부터 데이터를 읽음
```

- 보조스트림에서는 버퍼만 제공하고 기반 스트림에서 파일을 읽음
- 버퍼를 사용한 입출력과 사용하지 않은 입출력간의 성능차이는 심하기 때문에 보통 버퍼를 사용함

## FilterInput,Output Stream

- InputStream 의 자손이면서 모든 보조 스트림의 조상
- 보조스트림은 자체적으로 입출력을 수행할 수 없기 때문에 기반스트림을 필요로 함

```java
protected FilterInputStream(InputStream in)
public FilterOutputStream(OutputStream out)
```

```java
public class FilterInputStream extends InputStream {
  protected volatile InputStream in;
  protected FilterInputStream(InputStream in){
    this.in = in;
  }
  public int read() throws IOException{
    return in.read();
  }
  ...
}
```

## BufferedInput,Output Stream

- 스트림의 입출력 효율을 높이기 위해 버퍼를 사용하는 보조 스트림
- 한 바이트씩 입출력하는 것 보다는 버퍼(바이트배열)를 이용해서 한 번에 여러 바이트를 입출력하는 것이 빠름

- BufferedInputStream 생성자

| 생성자                                        | 설명                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| BufferedInputStream(InputStream in, int size) | 주어진 InputSTream인스턴스를 입력소스로 하며 지정된 크기(byte 단위)의 버퍼를 갖는 BufferedInputStream인스턴스를 생성 |
| BufferedInputStream(InputStream in)           | 주어진 InputSTream인스턴스를 입력소스로 하며 버퍼의 크기를 지정해주지 않으므로 기본적으로 8192 byte 크기의 버퍼를 갖게 됨 |

- BufferedOutputStream 생성자

| 메서드/생성자                                   | 설명                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| BuffredOutputStream(OutputStream out, int size) | 주어진 OutputStream 인스턴스를 출력소스로 하며 지정된 크기의 버퍼를 갖는 BufferedOutputStream인스턴스를 생성 |
| BufferedOutputStream(OutputStream out)          | 주어진 OutputStream인스턴스를 출력소스로 하며 버퍼의 크기를 지정해주지 않으므로 기본적으로 8192byte 크기의 버퍼를 갖게 됨 |
| flush()                                         | 버퍼의 모든 내용을 출력소스에 출력한 다음, 버퍼를 비움       |
| close()                                         | flush()를 호출해서 버퍼의 모든 내용을 출력소스에 출력하고, BufferedOutputStream인스턴스가 사용하던 모든 자원을 반환 |

```java
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class BufferedOutputStreamEx {
    public static void main(String[] args) {
        try{
            FileOutputStream fos = new FileOutputStream("123.txt");

            //BufferedOutputStream의 버퍼 크기를 5로 함
            BufferedOutputStream bos = new BufferedOutputStream(fos, 5);

            //파일 123.txt에 1부터 9까지 출력
            for(int i ='1'; i <= '9'; i++){
                bos.write(i);
            }

            fos.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}

//123.txt --> 5크기의 버퍼이므로 5까지만 출력되어있음
12345
```

## DataInput,OutputStream

- 각 자료형의 크기가 다르므로, 출력한 데이터를 다시 읽어 올 때는 출력했을 때의 순서를 염두에 두어야 함

- DataInputStream의 생성자와 메서드

| 메서드/생성자                                                | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| DataInputStream(InputStream in)                              | 주어진 InputStream 인스턴스를 기반으로하는 DataInputStream인스턴스 생성 |
| booelan readBoolean()<br />byte readByte()...                | 각 타입에 맞게 값을 읽어 옴. 더 이상 읽을 값이 없으면 EOFExecption 발생 |
| void readFully(byte[] b)<br />void readFully(byte[] b, int off. int len) | 입력 스트림에서 지정된 배열의 크기만큼 또는 지정된 위치에서 len 만큼 데이터를 읽어 옴. 파일의 끝에 도달하면 EOFExeption이 발생하고 IO에러가 발생하면 IOExecption이 발생 |
| String readUTF()                                             | UTF-8형식으로 쓰여진 문자를 읽음                             |
| static STring readUTF(DataInput in)                          | 입력스트림에서 UTF-8형식의 유니코드를 읽음                   |
| int skipBytes(int n)                                         | 현재 읽고 있는 위치에서 지정된 숫자(n) 만큼 건너 뜀          |

- DataOutputStream의 생성자와 메서드

| 메서드/생성자                                              | 설명                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------ |
| DataOutputStream(OutputStream out)                         | 주어진 OutputSTream인스턴스를 기반스트림으로 하는 DataOutputStream인스턴스 생성 |
| void writeBoolean(boolean b)<br />void writeByte(int b) …. | 각 자료형에 알맞은 값들을 출력                               |
| void writeUTF(String s)                                    | UTF형식으로 문자 출력                                        |
| void writeChars(String s)                                  | 주어진 문자열을 출력. writeChar(int c)메서드를 여러번 호출한 결과오 ㅏ같음 |
| int size()                                                 | 지금까지 DataOutputStream에 쓰여진 byte의 수를 알려줌        |

- DataOutputStream
  - 주의점: 여러 종류의 자료형으로 출력할 경우 반드시 쓰인 순서대로 읽어야 함

```java
import java.io.ByteArrayOutputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.util.Arrays;

public class DataOutputStreamEx {

    public static void main(String[] args) {
        ByteArrayOutputStream bos = null;
        DataOutputStream dos = null;

        byte[] result = null;

        try{
            bos = new ByteArrayOutputStream();
            dos = new DataOutputStream(bos);

            dos.write(10);
            dos.writeFloat(20.0f);
            dos.writeBoolean(true);

            result = bos.toByteArray();

            String[] hex = new String[result.length];

            for (int i = 0; i < result.length; i++) {

                if(result[i] < 0){
                    hex[i] = String.format("%02x", result[i] + 256);
                } else {
                    hex[i] = String.format("%02x", result[i]);
                }
            }

            System.out.println("10진수 : " + Arrays.toString(result));
            System.out.println("16진수 : " + Arrays.toString(hex));

            dos.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}

/*
10진수 : [10, 65, -96, 0, 0, 1]
16진수 : [0a, 41, a0, 00, 00, 01]
*/
```

- DataInputStream

```java
import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

public class DataInputStreamEx {

    public static void main(String[] args) {
        try{

            FileInputStream fis = new FileInputStream("sample.dat");
            DataInputStream dis = new DataInputStream(fis);

            System.out.println(dis.readInt());
            System.out.println(dis.readFloat());
            System.out.println(dis.readBoolean());
            
            dis.close();
            
        } catch(IOException e){
            e.printStackTrace();
        }
    }
}
/*
10
20.0
true
*/
```

- 스코어 파일 점수계산

```java
import java.io.DataOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class DataOutputStreamScore {
    public static void main(String[] args) {
        int[] score = { 100, 90, 95, 85, 50 };

        try{
            FileOutputStream fos = new FileOutputStream("score.dat");
            DataOutputStream dos = new DataOutputStream(fos);

            for (int i = 0; i < score.length; i++) {
                dos.writeInt(score[i]);
            }

            dos.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }

}
/*terminal
java dataOutputStreamSrcoe
type score.dat
*/

public class DataInputStreamScore {

    public static void main(String[] args) {
        int sum = 0;
        int score = 0;

        try(FileInputStream fis = new FileInputStream("score.dat");
            DataInputStream dis = new DataInputStream(fis)){
            
            while(true){
                score = dis.readInt();
                System.out.println(score);
                sum += score;
            }
            
        } catch (EOFException e){
            System.out.println("점수의 총합은 " + sum);
        } catch (IOException ie){
            ie.printStackTrace();
        }     
    }
}
```

## SequenceInputStrem

- 여러개의 입력스트리므을 연속적으로 연결해서 하나의 스트림으로부터 데이터를 읽는 것과 같이 처리할 수 있도록 도와줌
  - SequenceInputStream의 생성자를 제외하고 나머지 작업은 다른 입력스트림과 동일
  - 큰 파일을 여러 개의 작은 파일로 나누었다가 하나의 파일로 합치는 것과 같은 작업을 수행할 때 사용하면 좋음
- SequenceInputStream의 생성자

| 메서드/생성자                                       | 설명                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| SequenceInputStream(Enumeration e)                  | Enumeration에 저장된 순서대로 입력 스트림을 하나의 스트림으로 |
| SequenceInputStream(InputStream s1, InputStream s2) | 두 개의 입력스트림을 하나로 연결                             |

- Vector에 연결할 입력스트림을 저장한 다음 Vector의 Enumeration elments()를 호출해서 생성자의 매개변수로 사용

```java
//사용예 1
Vector files = new Vector();
files.add(new FileInputStream("file.001"));
files.add(new FileInputStream("file.002"));
SequenceInputStream in = new SequenceInputStream(files.elements());

//사용예 2
FileInputStream file1 = new FileInputStream("file.001");
FileInputStream file2 = new FileInputStream("file.002");
SequenceInputStream in = new SequenceInputStream(file1, file2);
```

- InputStream 예

```java
package JavaStandard;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.SequenceInputStream;
import java.util.Arrays;
import java.util.Vector;

public class SequcneInputStreamEx {
    public static void main(String[] args) {
        byte[] arr1 = {0,1,2};
        byte[] arr2 = {3,4,5};
        byte[] arr3 = {6,7,8};
        byte[] outSrc = null;


        Vector v = new Vector();
        v.add(new ByteArrayInputStream(arr1));
        v.add(new ByteArrayInputStream(arr2));
        v.add(new ByteArrayInputStream(arr3));

        SequenceInputStream input = new SequenceInputStream(v.elements());
        ByteArrayOutputStream output = new ByteArrayOutputStream();

        int data = 0;

        try{
            while((data = input.read()) != -1){
                output.write(data);
            }
        } catch (IOException e) {}


        outSrc = output.toByteArray();

        System.out.println("Input Source1 : " + Arrays.toString(arr1));
        System.out.println("Input Source1 : " + Arrays.toString(arr2));
        System.out.println("Input Source1 : " + Arrays.toString(arr3));
        System.out.println("Input Source1 : " + Arrays.toString(outSrc));

    }

}


//결과
Input Source1 : [0, 1, 2]
Input Source1 : [3, 4, 5]
Input Source1 : [6, 7, 8]
Input Source1 : [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

## PrintSteam

- 데이터를 기반스트림에 다양한 형태로 출력할 수 있는 print, println, printf와 같은 메서드를 오버로딩하여 제공

| 생성자/메서드                                                | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| PrintStream(Fiel file)<br />PrintStream(File file, String csn)<br />PrintStream(OutputStream out)<br />PrintStream(OutputStream out, boolean autoFlush)<br />PrintStream(OutputStream out, boolean autoFlush, String encoding)<br />PrintStream(String fileName)<br />PrintStream(String fileName, Stirng csn) | 지정된 출력스트림을 기반으로 하는 Printstream인 인스턴스를 생성. autoFlush의 값을 true로 하면 println메서드가 호출되거나 개행문자가 출력도리 때 자동으로 flush됨. 기본값은 false |
| boolean checkError()                                         | 스트림을 flush하고 에러가 발생했는지 알려줌                  |
| void print(각 타입 t)                                        | 인자로 주어진 값을 출력소스에 문자로 출력. println메서드는 출력 후 줄바꿈을 하고, print메서드는 줄을 바꾸지 않음 |
| void pirnt()                                                 | 줄바꿈 문자(line separator)를 출력함으로써 줄을 바꿈         |
| PrintStream printf(String format, Object… args)              | 정형화된(formatted) 출력을 가능학 ㅔ함                       |
| protectecd void setError()                                   | 작업 중에 오류가 발생햇음을 알림. (setError()를 호출한 후에, checkError()를 호출하면 true를 반환) |

- 정수의 출력에 사용될 수 있는 옵션

| format | 설명                                          | 결과(int i=65) |
| ------ | --------------------------------------------- | -------------- |
| %d     | 10진수(decimal integer)                       | 65             |
| %o     | 8진수(octal integer)                          | 101            |
| %x     | 16진수(hexadecimal integer)                   | 41             |
| %c     | 문자                                          | A              |
| %s     | 문자열                                        | 65             |
| %5d    | 5자리 숫자. 빈자리는 공백                     | 65             |
| %-5d   | 5자리 숫자. 빈자리는 공백으로 채움(왼쪽 정렬) | 65             |
| %05d   | 5자리 숫자. 빈자리는 0으로 채움               | 00065          |



