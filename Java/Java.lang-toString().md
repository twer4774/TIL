# Java.lang - toString()

- 인스턴스에 대한 정보를 문자열로 제공

```java
class Card {
  String kind;
  int number;
  Card() {
    this("SPADE", 1);
  }
  Card(String kind, int number){
    this.kind = kind;
    this.number = number;
  }
  
	public String toString(){
    return "kind : " + kind + ", number : " + number;
  }
}

class CardToString{
  public static void main(Strng[] args){
    /*Card클래스에 toString()이 없을 때*/
    // Card c1 = new Card();
    // Card c2 = new Card();
   	// System.out.println(c1.toString()); //Card@19e0bfd
   	// System.out.println(c2.toString()); //Card@130a55
    
    /*Card클래스에 toString()이 있을 때*/
    Card c1 = new Card();
    Card c2 = new Card("HEART", 10);
    System.out.println(c1.toString()); //kind : SPADE, number : 1
    System.out.println(c2.toString()); //kind : HEART, number : 10
    
  }
}
```

