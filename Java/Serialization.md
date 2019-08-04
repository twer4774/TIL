# 직렬화(Serialization)

- 객체를 데이터 스트림으로 만드는 것 => 데이터를 스트림에 write하기위해 연속적인 데이터로 ㅂㄴ환
- ObjectInputStream / ObjectOutputStream 이용
- 직렬화가 가능한 클래스 만들기 - Serializable, transient

```java
//SerialEx1에서 사용하는 코드로 미리 컴파일 되어있어야한다.
package Serialization;

public class UserInfo implements java.io.Serializable{
    String name;
    String password;
    int age;
    public UserInfo() {
        this("Unkown", "1111", 0);
    }

    public UserInfo(String name, String password, int age) {
        this.name = name;
        this.password = password;
        this.age = age;
    }

    public String toString() {
        return "(" + name + "," + password + "," + age + ")";
    }
}

```

```java
//직렬화 -> UserInfo먼저 컴파일 후에 실행할것
package Serialization;

import java.io.*;
import java.util.ArrayList;

public class SerialEx1 {
    public static void main(String[] args) {
        try{
            String fileName = "UserInfo.ser";
            FileOutputStream fos = new FileOutputStream((fileName));
            BufferedOutputStream bos = new BufferedOutputStream(fos);

            ObjectOutputStream out = new ObjectOutputStream(bos);

            UserInfo u1 = new UserInfo("JavaMan", "1234", 30);
            UserInfo u2 = new UserInfo("JavaWoman", "4321", 26);

            ArrayList<UserInfo> list = new ArrayList<>();
            list.add(u1);
            list.add(u2);

            //객체를 직렬화한다.
            out.writeObject(u1);
            out.writeObject(u2);
            out.writeObject(list);
            out.close();
            System.out.println("직렬화가 잘 끝났습니다.");
        } catch (IOException e) {
            e.printStackTrace();
        }//catch
    }//main
}

//결과
직렬화가 잘 끝났습니다.
```

```java
//역직렬화
package Serialization;

import java.io.*;
import java.util.ArrayList;

public class SerailEx2 {
    public static void main(String[] args) {
        try {
            String fileName = "UserInfo.ser";
            FileInputStream fis = new FileInputStream(fileName);
            BufferedInputStream bis = new BufferedInputStream(fis);

            ObjectInputStream in = new ObjectInputStream(bis);

            //객체를 읽을때는 출력한 순서와 일치해야한다.
            UserInfo u1 = (UserInfo) in.readObject();
            UserInfo u2 = (UserInfo) in.readObject();
            ArrayList list = (ArrayList)in.readObject();

            System.out.println(u1);
            System.out.println(u2);
            System.out.println(list);
            in.close();
        } catch(Exception e){
            e.printStackTrace();
        }
    }//main
}

//결과
(JavaMan,1234,30)
(JavaWoman,4321,26)
[(JavaMan,1234,30), (JavaWoman,4321,26)]
```

