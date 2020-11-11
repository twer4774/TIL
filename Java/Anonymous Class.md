# Anonymous Class(익명 클래스)

- 내부 클래스 중 하나 
  - 내부 클래스는 GUI 이벤트 처리를 위한 AWT, Swing을 제외하고 잘 사용되지 않음
- 다른 내부클래스들과는 다르게 이름이 없음
- 클래스의 선언과 객체의 생성을 동시에 하기 때문에 단 한번만 사용될 수 있고 오직 하나의 객체만을 생성하는 일회용 클래스

```java
new 조상클래스이름() {
  //멤버 선언
}

//또다른 형태
new 구현인터페이스이름(){
  //멤버 선언
}

class InnerEx{
  Object iv = new Object() { void method() {} }; //익명클래스
  static Object cv = new Object() { void method() {} }; //익명클래스
  
  void myMethod() {
    Object lv = new Object() { void method() {} }; //익명클래스
  }
}
```

```java
import java.awt.*;
import java.awt.event.*;

class InnerEx{
  public static void main(String[] args) {
    Button b = new Button("start");
    b.addActionListener(new ActionListener(){
      public void actionPerformed(ActionEvent e){
        System.out.println("ActionEvent occurred!!!");
      }
    } //익명클래스 끝
   );
  } //main
} //InnerEx
```

