# 얕은 복사와 깊은 복사(ShallowDeepCopy)

- clone() 메서드는 객체에 저장된 값을 그대로 복제할 뿐, 객체가 참조하고 있는 객체까지 복제하지 않음 => 얕은 복사
  - 얕은 복사 : 객체의 값만 그대로 복사. 객체가 참조하는 것을 복사하지는 않음
- 깊은 복사 : 원본이 참조하고 있는 객체까지 복사

```java
class Circel implements Cloneable{
  Point p;
  double r;
  
  Circle(Point p, double r){
    this.p = p;
    this.r = r;
  }
  
  public Circle shallowCopy() { //얕은복사
    Object obj = null;
    
    try{
      obj = super.clone(); //조상인 Object의 clone()호출
    } catch(CloneNotSupportedException e){
    
    }
    return (Circle) obj;
  }
  
  
  public Circle deppCopy(){ //깊은복사
    Object obj = null;
    
    try{
      obj = super.clone();
    } catch(CloneNotSupportedException e){
      
    }
    
    Circle c = (Circle) obj;
    c.p = new Point(this.p.x, this.p.y);
    
    return c;
  }
  
  public String toString(){
    return "[p=" + p + ", r=" + r +"]";
  }
}

class Point{
  int x,y;
  
  Point(int x, int y){
    this.x = x;
    this.y = y;
  }
  
  public String toString(){
    return "("+x+", "+y+")";
  }
}

class ShallowDeepCopy{
  public static void main(String[] args){
    Circle c1 = new Circle(new Point(1, 1), 2.0);
    Circle c2 = c1.shallowCopy();
    Circle c3 = c1.deepCopy();
    
    System.out.println("c1="+c1); //p=1,1 r=2.0
    System.out.println("c2="+c2); //p=1,1 r=2.0
    System.out.println("c3="+c3); //p=1,1 r=2.0
    
    c1.p.x = 9;
    c1.p.y = 9;
    
    System.out.println("c1="+c1); //p=9,9 r=2.0
    System.out.println("c2="+c2); //p=9,9 r=2.0
    System.out.println("c3="+c3); //p=1,1 r=2.0 깊은복사는 객체를 참조하므로 단순 변경된 값은 반영되지 않음
  }
}
```

