# CollectionFramework - Comparator, Comparable

- Arrays.sort()는 내부적으로 Comparable에 의해 구현됨
- Comparable을 구현한 클래스는 정렬이 가능

```java
public interface Comparator {
  int compare(Object o1, Object o2);
  boolean equals(Objet obj);
}

public interface Comparable{
  public int compareTo(Object o);
}
```

- compare와 compareTo는 두 객체 비교라는 공통의 목적을 가지고 있음
- 아래는 Integer 클래스의 일부로 Comparable의 compareTo(Ojbect o)를 구현해 놓은 것을 볼 수 있음

```java
public final class Integer extends Nubmer implements Comparable {
  ...
    public int compareTo(Object o) {
    return compareTo((Integer)o);
  }
  
  public int compareTo(Integer anotherInteger){
    int thisVal = this.value;
    int anotherVal = anotherInteger.value;
    
    //비교하는 값이 크면 -1, 같으면 0, 작으면 1반환
    return (thisVal<anotherVal ? -1 : (thisVal == anotherVal ? 0 : 1));
  }
}
```

```
Comparable : 기본 정렬 기준을 구현하는데 사용
Comparator : 기본 정렬 기준 외에 다른 기준으로 정렬하고자할 때 사용
```

```java
import java.util.Arrays;
import java.util.Comparator;

public class ComparatorEx {

    public static void main(String[] args) {
        String[] strArr = {"cat", "Dog", "lion", "tiger"};

        Arrays.sort(strArr);
        System.out.println("StrArr=" + Arrays.toString(strArr));

        Arrays.sort(strArr, String.CASE_INSENSITIVE_ORDER); //대소문자 구분 안함
        System.out.println("strArr=" + Arrays.toString(strArr));

        Arrays.sort(strArr, new Descending()); //역순 정렬
        System.out.println("strArr=" + Arrays.toString(strArr));
    }
}

class Descending implements Comparator {
    public int compare(Object o1, Object o2){
        if( o1 instanceof Comparable && o2 instanceof Comparable){
            Comparable c1 = (Comparable)o1;
            Comparable c2 = (Comparable)o2;

            return c1.compareTo(c2) * -1; //-1을 곱해서 기본 정렬의 역순으로 변경 또는 c2.compareTo(c1)이라고 해도 동일한 효과
        }

        return -1;
    }
}

/*
StrArr=[Dog, cat, lion, tiger]
strArr=[cat, Dog, lion, tiger]
strArr=[tiger, lion, cat, Dog]
*/
```

