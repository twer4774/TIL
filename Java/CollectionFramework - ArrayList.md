# CollectionFramework - ArrayList

- List 인터페이스를 구현하기 때문에 순서를 가지고, 중복을 허용한다는 특징이 있음
- ArrayList는 기존의 Vector 컬렉션 클래스를 개선한것으로 기능적인 측면에서는 동일
  - 가능하면 ArrayList로 사용할 것

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ArrayList()                                                  | 크기가 10인 ArrayList 생성                                   |
| ArrayList(Collection c)                                      | 주어진 컬렉션이 저장된 ArrayList 생성                        |
| ArrayList(int initialCapacity)                               | ArrayList의 기본 크기 지정                                   |
| boolean add(Object o)                                        | ArrayList마지막에 객체 저장 성공, 실패 여부                  |
| void add(int index, Object element)                          | 지정된 위치에 객체 저장                                      |
| boolean addAll(Collection c)                                 | 주어진 컬렉션의 모든 객체 저장                               |
| boolean addAll(int index, Collection c)                      | 지정된 위치부터 주어진 컬렉션의 모든 객체 저장               |
| void clear()                                                 | ArrayList를 비움                                             |
| Object clone()                                               | ArrayList 복제                                               |
| boolean contains(Object o)                                   | 객체가 ArrayList에 포함되어있는지 확인                       |
| void ensureCapacity(int minCapacity)                         | ArrayList의 용량이 최소한 minCapacity가 되도록 함            |
| Object get(int index)                                        | 지정위치의 객체 반환                                         |
| indt indexOf(Object o)                                       | 객체의 위치 반환                                             |
| boolean isEmpty                                              | 비었는지 확인                                                |
| iterator iterator()                                          | Iterator객체 반환                                            |
| int lastIndexOf(Object o)                                    | 객체가 저장된 위치를 끝부터 역방향으로 검색해서 반환         |
| ListIterator listIterator() / ListIterator listIterator(int index) | ListIterator반환 / 지정된 위치부터 ListIterator 반환         |
| Object remove(Objec o)                                       | 지정된 객체 제거                                             |
| boolean retainAll(Collection c)                              | ArrayList에 저장된 객체 중 주어진 컬렉션과 공통된 것들만 남기고 나머지 삭제 |
| Object set(int index, Object element)                        | 주어진 객체를 지정된 위치에 저장                             |
| int size()                                                   |                                                              |
| void sort(Comparator c)                                      |                                                              |
| List subList(int formIndex, int toIndex)                     | 범위에 저장된 객체 반환                                      |
| Object[] toArray() / Object[] toArray(Object[] a)            | 객체 배열로 반환 / 모든 객체를 객체배열 a에 담아 반환        |
| void trimToSize()                                            | 용량을 크기에 맞게 줄임(빈 공간을 없앤다)                    |

```java
import java.util.*;

class ArrayListEx{
 	public static void main(String[] args){
    ArrayList list1 = new ArrayList(10);
    list1.add(new Integer(5));
    list1.add(new Integer(4));
    list1.add(new Integer(2));
    list1.add(new Integer(0));
    list1.add(new Integer(1));
    list1.add(new Integer(3));
    
    ArrayList list2 = new ArrayList(list1.subList(1,4));
    print(list1, list2);
    /*
    list1:[5, 4, 2, 0, 1, 3]
    list2:[4, 2, 0]
    */
    
    //list1과 list2 정렬
    Collections.sort(list1); 
    Collections.sort(list2);
    /*
    list1:[0, 1, 2, 3, 4, 5]
    list2:[0, 2, 4]
    */
    
    System.out.println("list1.containsAll(list2): " + list1.containsAll(list2));
    //true
    
    list2.add("B");
    list2.add("C");
    list2.add("A");
    print(list1, list2);
    /*
    list1:[0, 1, 2, 3, 4, 5]
    list2:[0, 2, 4, A, B, C]
    */
    
    list2.set(3, "AA");
    print(list1, list2);
    /*
    list1:[0, 1, 2, 3, 4, 5]
    list2:[0, 2, 4, AA, B, C]
    */
    
    //list1에서 list2와 겹치는 부분만 남기고 나머지 삭제
    System.out.println("list1.retainAll(list2):" + list1.retainAll(list2)); //true
    print(list1, list2);
    /*
    list1:[0, 2, 4] -> 공통요소 이외는 모두 삭제 변화가 있었으므로 retainAll이 true 반환
    list2:[0, 2, 4, AA, B, C]
    */
    
    //list2에서 list1에 포함된 객체들 삭제
    for(int i = list2.size()-1; i >= 0; i--){
      if(list1.contains(list2.get(i))){
        list2.remove(i);
      } //if
    }//for
    print(list1, list2);
    /*
    list1:[0, 2, 4]
    list2:[AA, B, C]
    */
  } //main
  
  static void print(ArrayList list1, ArrayList list2){
    System.out.println("list1:"+list1);
    System.out.println("list2:"+list2);
    System.out.println();
  }
}
```

- 주의 - for문을 돌릴때 list2.size()-1 부터 시작하여 i값을 감소시킴
  - 0부터 증가하게 되면 리스트의 빈공간을 채우기 위해 자리이동이 필요함

### 긴 문자열 데이터를 원하는 크기로 잘라서 반환

```java
import java.util.*;

class ArrayListEx{
  public static void main(String[] args){
    final int LIMIT = 10; //자르고자 하는 글자의 개수 지정
    String source = "0123456789abcdefghijABCDEFGHIJ!@#$%^&*()zzz";
    int length = soruce.length();
    
    List list = new ArrayList(length/LIMIT + 10); //크기를 약간 여유있게 잡음
    
    for(int i=0; i < length; i+=LIMIT){
      if(i+LIMIT < length){
        list.add(source.substring(i, i+LIMIT));
      } else {
        list.add(source.substring(i));
      } //else
    } //for
    
    for(int i=0; i<list.size(); i++){
        System.out.println(list.get(i));
     } //for
    
  }//main()
  
}//class
```

