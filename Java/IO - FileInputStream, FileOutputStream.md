# IO - FileInputStream, FileOutputStream

- 실제 프로그래밍에 많이 사용되는 스트림 중 하나

- FileInputStream과 FileOutputStream의 생성자

| 생성자                                        | 설명                                                         |
| --------------------------------------------- | ------------------------------------------------------------ |
| FiIeInputStream(String name)                  | 지정된 파일이름을 가진 실제 파일과 연결된 FileInputStream을 생성 |
| FileInputStream(File file)                    | 파일의 이름이 String이 아닌 File 인스턴스로 지정해주어야 하는 점을 제외하고 위와 같음 |
| FileInputStream(FileDescriptor fdObj)         | 파일 디스크립터(fdObj)로 FileInputStream을 생성              |
| FileOutputStream(String name)                 | 지정된 파일이름을 가진 실제 파일과 연결된 FileOutputStream생성 |
| FileOutputStream(String name, boolean append) | 지정된 파일이름을 가진 실제 파일과 연결된 FIleOutputStream을 생성. 두번째 인자인 append를 true로 하면 출력 시 기존의 파일 ㅓ내용의 마지막에 덧붙임. false면 기존의 파일 내용을 덮어 씀 |
| FileOutputStream(File file)                   | 파일의 이름을 String이 아닌 File 인스턴스로 지정해주어야 하는 점을 제외하고 FileOutputStrema(String name)과 동일 |
| FileOutputStream(File name, boolean append)   |                                                              |
| FileOutputStream(FileDescriptor fdObj)        | 파일 디스크립터(fdObj)로 FileOutputStream생성                |

- FileViewer

```java
public class FileViewer {

    public static void main(String[] args) throws IOException {
        FileInputStream fis = new FileInputStream(args[0]);
        int data = 0;

        while((data=fis.read()) != -1){
            char c = (char) data;
            System.out.print(c);
        }
    }
}

//terminal
java FileViewer FileViewer.java
```

- FileCopy

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class FileCopy {
    public static void main(String[] args) {
        try{
            FileInputStream fis = new FileInputStream(args[0]);
            FileOutputStream fos = new FileOutputStream(args[1]);

            int data = 0;
            while((data=fis.read()) != -1){
                fos.write(data); //void write(int b)
            }

            fis.close();
            fos.close();
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}

//termianl
java FileCopy FileCopy.java FileCopy.bak
```

