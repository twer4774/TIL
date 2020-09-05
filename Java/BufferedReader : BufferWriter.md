# BufferedReader / BufferWriter

- 버퍼를 이용하여 입출력
- 효율이 좋아짐

- 버퍼를 사용하지 않는 입력의 경우
  - 키보드의 입력이 키를 누르는 즉시 바로 전달
- 버퍼를 사용하는 입력
  - 키보드의 입력이 있을때마다 한 문자씩 버퍼로 전송
  - 버퍼가 가득차거나, 개행 문자가 나타나면 버퍼의 내용을 한 번에 전송
- 중간에 메모리 버퍼를 두어 데이터를 한번에 묶어 이동시키는것이 효율적이고 빨라짐

### BufferedReader

- Scanner함수를 이용하면 띄어쓰기와 엔터를 경계로 입력 값을 인식함. 따로 데이터를 가공할 필요가 없음
- 반면, BufferedReader는 엔터만 경계로 인식하고 받은 데이터가 String으로 고정되기 때문에 데이터를 따로 가공해야함
  - 하지만 Scanner보다 상대적으로 빠름
- 많은 데이터를 입력받아야 할 상황에서는 BufferedReader를 이용하면 좋음
- 사용법
  - BufferedReader의 readLine()을 사용하면 데이터를 라인 단위로 읽을 수 있음
  - readLine함수의 리턴 값은 String으로 고정되기 때문에 String이 아닌 다른 타입으로 입력을 받으려면 형변환를 꼭 해줘야 함

```java
package com.company;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BufferedReaderEx {

    public static void main(String[] args) {
        //예외처리를 필수로 함. 또는 throwsIOException을 해준다.
        try{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            //파일에서 입력받을 경우
            FileReader fr = new FileReader("BufferedReaderEx1.java");
            BufferedReader br_f = new BufferedReader(fr);

            //리턴 값이 String으로 고정되므로 int형으로 사용시 형변환
            int num = Integer.parseInt(br.readLine());
            br.close();

            //파일을 한줄씩 읽어서 출력
            String line = "";
            for(int i = 1; (line = br_f.readLine()) != null; i++){
                System.out.println(line);
            }
        } catch (IOException e){
            e.printStackTrace();
            System.out.println(e.getMessage());
        }
    }
}
```

### BufferWriter

```java
import java.util.*;
public class BufferedWirterEx{	
	public static void main(String[] args) throws IOException{
        BufferedWriter bw = new BufferedWriter(new FileWriter("bufferedWriter.txt"));
        bw.write("hello\n");
        bw.newLine(); //개행
        bw.flush(); //남아있는 데이터를 모두 출력
        bw.close(); //클로즈
    }
  }
```

