# DAO VS DTO(=VO)

### DAO

- Data Access Object
- DB의 Data 접근을 위한 객체
- DB의 접근 로직과 비지니스 로직의 분리를 위해 사용
- 설명
  - 웹서버는 DB와 연결을 위해 매번 커넥션 객체를 생성하는데 이것을 해결하기 위해 커넥션 풀을 사용함
  - ConnectionPool : Connection객체를 미리 만들어 놓고 그것을 가져다 씀
    - 오버헤드를 효율적으로 관리할 수 있음
  - DB 접속을 위한 하나의 객체를 만들고 모든 페이지에서 그 객체를 호출하여 사용함
  - 사용자는 자신이 필요한 Interface를 DAO에 던지고, DAO는 인터페이스를 구현한 객체를 사용자에게 반환
  - 다수의 원격 호출을 통한 오버헤드를 VO나 DTO를 통해 줄일 수 있고, 다수의 DB 호출 문제를 해결할 수 있음
  - 또한 다순힌 읽기만 하는 연산이므로 트랜잭션 간의 오버헤드를 감소하는 효과도 있음

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class TestDao {
  public void add(TestDto dto) throws ClassNotFoundException, SQLException{
    Class.forName("com.mysql.jdbc.Driver");
    Connection connection = DriverManger.getConnenctoion("jdbc:mysql://localhost/test", "root", "root");
    
    PreparedStatement preparedStatement = connection.prepareStatement("INSERT INTO USERS(id, name, password) VALUE(?,?,>)");
    
    preparedStatement.setString(1, dto.getName());
    preparedStatement.setInt(2, dto.getValue());
    preparedStatement.setString(3, dto.getData());
    preparedStatement.executeUpdate();
    preparedStatement.close();
    
    connection.close();
  }
}
```



### DTO(=VO)

- Data Tansfer Object = Value Object
- Layer 간의 데이터 교환을 위한 Java Beans
  - Layer: Contoller, View, Business, Persistent
- 일반적인 DTO는 로직을 갖고 있지 않는 순수한 데이터 객체
- 속성과 그 속성을 접근하기 위한 getter, setter 메소드만 가진 클래스

```java
public class TestDto{
  
  private String name;
  private int value;
  private String data;
  
  public String getName(){
    return name;
  }
  
  public void setName(String name){
    this.name = name;
  }
  
  public int getValue(){
    return value;
  }
  
  public void setValue(int value){
    this.value = value;
  }
  
  public String getData(){
 		return data;
  }
  
  public void setData(String data){
    this.data = data;
  }
  
}
```

