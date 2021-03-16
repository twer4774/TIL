# 직렬화(Serialization)

- 객체를 데이터 스트림으로 만드는 것
  - 객체에 저장된 데이터를 스트림에 쓰기위해 연속적인 데이터로 만드는 것

## ObjectInputStream, ObjectOutputStream

```java
//직렬화
FileOutputStream fos = new FileOutputStream("objectfile.ser");
ObjectOutputStream out  = new ObjectOutputStream(fos);

out.writeObject(new UserInfo());

//역직렬화
FileInputStream fis = new FileInputStream("objectfile.ser");
ObjectInputStream in = new ObjectInputStream(fis);

UserInfo info = (UserInfo) in.readObject();
```

## 직렬화가 가능한 클래스 만들기 - Serializable, transient

```java
public class UserInfo implements java.io.Serializable{
  String name;
  String password;
  int age;
  
  public UserInfo(){
    this("Unknown", "1111", 0);
  }
  
  public UserInfo(String name, String password, int age){
    this.name = name;
    this.password = password;
    this.age = age;
  }
  
  public String toString(){
    return "("+ name + "," + password + "," + age + ")";
  }
}
```

```java
import java.io.*;
import java.util.ArrayList;

public class SerialEx1{
  public static void main(String[] args){
    try{
      String fileName = "UserInfo.ser";
      FileOutputStream fos = new FileOutputStream(fileName);
      BufferedOutputStream bos = new BufferedOutputStream(fos);
      
      ObjectOutputStream out = new ObjectOutputStream(bos);
      
      UserInfo u1 = new UserInfo("JavaMan", "1234", 30);
      UserInfo u2 = new UserInfo("JavaWoman", "4321", 26);
      
      ArrayList<UserInfo> list = new ArrayList<>();
      list.add(u1);
      list.add(u2);
      
      //객체 직렬화
      out.writeObject(u1);
      out.writeObject(u2);
      out.writeObject(list);
      out.close();
      System.out.println("직렬화가 끝났습니다.");
    } catch (IOExeption e){
      e.printStackTrace();
    }
  }
}

//역직렬화
public class SerialEx2{
  public static void main(String[] args){
    try{
      String fileName = "UserInfo.ser";
      FileInputStream fis = new FileInputStream(fileName);
      BufferedInputStream bis = new BufferedInputStream(fis);
      
      ObjectInputStream in = new ObjectInputStream(bis);
      
      //객체를 읽을때는 출력한 순서와 일치해야 함
      UserInfo u1 = (UserInfo)in.readOjbect();
      UserInfo u2 = (UserInfo)in.readOjbect();
 			ArrayList list = (ArrayList)in.readObject();

      System.out.println(u1);
      System.out.println(u2);
      
      //개별로 역직렬화하는 것보단 list를 이용하면 순서에 상관안해도 되서 좋음
      System.out.println(list);
      
      in.close();
    } catch (IOExeption e){
      e.printStackTrace();
    }
  }
}
```

