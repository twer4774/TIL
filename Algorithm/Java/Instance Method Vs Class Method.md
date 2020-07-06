# Instance Method VS Class Method

### Instance Method(비정적 메서드)

- static을 안붙임
- 인스턴스 개별에 객체에 대한 처리 담당
- 호출방식 : 클래스형 변수 이름.메서드 이름

### Class Method(정적 메서드)

- static을 붙임
- 클래스 전체에 대한 처리를 담당
- 인스턴스 메서드와 처리 영역을 구분하기 위해 주로 사용
- 호출방식 : 클래스 이름.메서드 이름



```java
//아이디를 부여하는 클래스

class Id {
  private static int counter = 0; //아이디를 몇개 부여했는지 저장
  private int id; //아이디
  
  //생성자
  public Id() { id = ++coutner; }
  
  //아이디를 반환하는 인스턴스 메서드
  public int getId() { return id; }
  
	//counter를 반환하는 클래스 메서드
  public static int getCounter() { return counter; }
}

public class IdTester{
  public static void main(String[] args){
    Id a = new Id(); //클래스형 변수
    id b = new Id();
    
    System.out.println("a의 아이디 : " + a.getId());
		System.out.println("b의 아이디 : " + b.getId()); //호출방식이 클래스형변수이름.메서드이름
     
   	Syste.out.println("부여한 아이디의 개수 : " + Id.getCounter()); //호출방식이 클래스이름.메서드이름
  }
}
```

