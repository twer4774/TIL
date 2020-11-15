# Java.lang - clone()

- 자신을 복제하여 새로운 인스턴스를 생성하는 메서드
- 어떤 인스턴스에 대해 작업을 할 때, 원래의 인스턴스는 보존하고 clone메서드를 이용해 새로운 인스턴스를 생성하여 작업을 하면 작업 이전의 값이 보존되므로 작업에 실패해 원래의 상태로 되돌리거나 변경되기 전의 값을 참고하는데 도움이 됨
- Object클래스에 정의된 clone()은 단순히 인스턴스변수의 값만 복사하기 때문에 참조타입의 인스턴스 변수가 있는 클래스는 완전한 인스턴스 복제가 이루어지지 않음
  - 배열의 경우,  복제된 인스턴스도 같은 배열의 주소를 갖기 때문에 복제된 인스턴스의 작업이 원래의 인스턴스에 영향을 미치게 됨. 이런 경우 clone메서드를 오버라이딩해 새로운 배열을 생성하고 배열의 내용을 복사하도록 해야 함

```java
class Point implements Cloneable{ //Cloneable인터페이스를 구현한 클래스에서만 clone()을 호출할 수 있음
  int x, y;
  
  Point(int x, int y){
    this.x = x;
    this.y = y;
  }
  
  public String toString(){
    return "x=" + x + ", y=" + y;
  }
  
  public Object clone(){ //public접근자로 해야함. 오버라이딩은 기존의 메서드보다 범위가 커야함
    Object obj = null;
    try {
      obj = super.clone(); //clone()은 반드시 예외처리 필요
    } catch(CloneNotSupportedException e){}
    
    return obj;
  }
  
  class CloneEx{
    public static void main(String[] args){
      Point original = new Point(3, 5);
      Point copy = (Point)original.clone(); //복제하여 새로운 객체 생성
      System.out.println(original); //x=3, y=5
      System.out.println(copy); //x=3, y=5
    }
  }
}
```

