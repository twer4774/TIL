# IO - 문자기반 스트림(Charater Stream)

- 문자 데이터를 다루는데 사용됨. 바이트기반과 문자열을 다룬다는 것을 제외하고 동일

## Reader와 Writer

- 바이트 기반 스트림의 조상이 InputStream/OutputStream인 것과 같이 문자기반의 스트림에서는 Reader/Writer가 그와 같은 역할을 함

- Reader의 메서드

| 메서드                                        | 설명                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| abstract void close()                         | 입력스트림을 닫음으로써 사용하고 있던 자원 반환              |
| void mark(int readlimit)                      | 현재위치를 표시. 후에 reset()에 의해서 표시해 놓은 위치로 다시 돌아갈 수 있음 |
| boolean markSupported()                       | mark()와 reset()을 지원하는지 알려줌                         |
| int read()                                    | 입력소스로부터 하나의 문자를 읽어 옴. char의 범위인 0~65535범위의 정수를 반환하며, 입력스트림의 마지막 데이터를 도달하면, -1을 반환 |
| int read(char[] c)                            | 입력소스로부터 매개변수로 주어진 배열 c의 크기만큼 읽어서 배열 c에 저장 |
| abstract int read(char[] c, int off, int len) | 입력소스로부터 최대 len개의 문자를 읽어서, 배열 c의 지정된 위치(off)부터 읽은 만큼 저장. 읽어 온 데이터의 수 또는 -1 반환 |
| int read(CharBuffer target)                   | 입력소스로부터 읽어서 문자버퍼에 저장                        |
| boolean ready()                               | 입력소스로부터 데이터를 읽을 준비가 되어있는지 알려줌        |
| void reset()                                  | 입력소스에서의 위치를 마지막으로 mark()가 호출되었던 위치로 되돌림 |
| long skip(long n)                             | 현재 위치에서 주어진 문자 수(n)만큼을 건너띔                 |

- Writer의 메서드

| 메서드                                             | 설명                                                         |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Writer append(char c)                              | 지정된 문자를 출력소스에 출력                                |
| Writer append(CharSequence c)                      | 지정된 문자열(CharSequence)을 출력소스에 출력                |
| Writer append(CharSequence ce, int start, int end) | 지정된 문자열(CharSequence)의 일부를 출력소스에출력          |
| abstract void close()                              | 출력스트림을 닫음으로써 사용하고 있던 자원 반환              |
| abstract void flush()                              | 스트림의 버퍼에 있는 모든 내용을 출력소스에 씀(버퍼가 있는 스트림에만 해당) |
| void wirte(int b)                                  | 주어진 값을 출력소스에 씀                                    |
| void write(char[] c)                               | 주어진 배열 c에 저장된 모든 내용을 출력소스에 씀             |
| abstract void write(char[] c, int off, int len)    | 주어진 배열 c에 저장된 내용 중에서 off번째부터 len길이만큼 출력소스에 씀 |
| void write(Stirng str)                             | 주어진 문자열(str)을 출력소스에 씀                           |
| void write(String str, int off, int len)           | 주어진 문자열(str)의 일부를 출력소스에 씀(off번째 문자부터 len개 만큼의 문자열) |

## FileReader와 FileWriter

- 파일로부터 텍스트 데이터를 읽고, 파일을 쓰는데 이용
  - 주의: FileInputStream으로 이용하면 한글이 깨짐

```java
//FileReaderEx
package JavaStandard;

import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderEx1 {
    public static void main(String[] args) {
        
        try{
           String fileName = "test.txt";
           FileInputStream fis = new FileInputStream(fileName);
           FileReader fr = new FileReader(fileName);
           
           int data = 0;
           //FileInputStream을 이용해서 파일내용을 읽어 화면에 출력
            while((data=fis.read()) != -1){
                System.out.print((char) data);
            }
            System.out.println();
            fis.close();
            
            //FileReader를 이용해서 파일내용을 읽어 화면에 출력
            while((data=fr.read()) != -1){
                System.out.println((char) data);
                System.out.println();
                fr.close();
            }
        } catch(IOException e){
            e.printStackTrace();
        }
    }

}
```

## PipedReader와 PipedWriter

- 쓰레드 간에 데이터를 주고 받을 때 사용
- 다른 스트림과 다르게 입력과 출력스트림을 하나의 스트림으로 연결하여 사용
  - 한쪽 스트림만 닫아도 반대쪽이 자동으로 닫힘

```java
package JavaStandard;

import java.io.*;

/**
 * 쓰레드 간에 데이터 전송
 * 한쪽을 닫으면 반대쪽이 자동으로 닫힘
 */
public class PipedReaderWriter {
    public static void main(String[] args) {
        InputThread inThread = new InputThread("InutThread");
        
    }
}

class InputThread extends Thread{
    PipedReader input = new PipedReader();
    StringWriter sw = new StringWriter();

    InputThread(String name){
        super(name); //Thread(String name);
    }
    
    public void run(){
        try{
            int data = 0;
            
            while((data=input.read()) != -1){
                sw.write(data);
            }

            System.out.println(getName() + " received : " + sw.toString());
        } catch (IOException e){}
    }//run()
    
    public PipedReader getInput(){
        return input;
    }
    
    public void connect(PipedWriter output){
        try{
            input.connect(output);
        } catch(IOException e){}
    }//connect()
}

class OutputThread extends Thread{
    PipedWriter output = new PipedWriter();
    
    OutputThread(String name){
        super(name); //Thread(String name);
    }
    
    public void run(){
        try{
            String msg = "Hello";
            System.out.println(getName() + " sent : " + msg);
            output.write(msg);
            output.close();
        } catch(IOException e) {}
    }//run()
    
    
    public PipedWriter getOutput(){
        return output;
    }
    
    public void connect(PipedReader input){
        try{
            output.connect(input);
        } catch(IOException e){
            
        }
        
    }
}
/*결과
OutputThread sent : Hello
InputThread receive : Hello
*/
```

## StringReader와 StringWriter

- 입출력 대상이 메모리인 스트림
- 데이터는 내부의 StirngBuffer에 저장되며 StringWriter의 다음과 같은 메서드를 이용해 저장된 데이터를 얻을 수 있음
  - StirngBuffer getBuffer() : StringWriter에 출력한 데이터가 저장된 StringBuffer를 반환
  - Stirng toString() : StringWriter에 출력된(StringBuffer에 저장된) 문자열 반환