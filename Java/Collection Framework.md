# Collection Framework

- 데이터 그룹을 다루고 표현하기 위한 단일화된 구조
- Vector, Hashtable, Properites와 같은 컬렉션 클래스를 컬렉션 프레임워크가 등장하면서 표준화 시킬 수 있음
  - Vector, Hashtable 등은 가능하면 사용하지 말고 컬렉션프레임워크로 ArrayLis, HashMap등을 사용 권장
- 객체지향적 설계를 통해 표준화되어 있기 때문에 사용법을 익히기도 편하고 재사용 활용이 높음

### 컬렉션 프레임워크의 핵심 인터페이스

- 3가지 타입이 존재
  - Collection의 자손으로 List, Set
  - Map

- List : 순서가 있는 데이터의 집합, 데이터의 중복을 허용
  - ArrayList, LinkedList, Stack, Vector
- Set : 순서를 유지하지 않는 데이터의 집합, 데이터의 중복을 허용하지 않음
  - HashSet, TreeSet
- 키와 값의 쌍으로 이루어진 데이터의 집합, 순서를 유지 하지 않으며 키는 중복을 허용하지 않고, 값은 중복을 허용
  - HashMap, TreeMap, HashTable, Properties

### List와 Set의 조상 Collection인터페이스

- Collection에 공통으로 정의되어 있는 메서드

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean add(Object o)<br />boolean addAll(Collection c)      | 저장된 객체(o)또는 Collection(c)의 객체들을 Collection에 추가 |
| void clear()                                                 | Collection의 모든 객체 삭제                                  |
| boolean contains(Object o)<br />boolean containsAll(Collection c) | 지정된 객체(o)또는 Collection의 객체들이 Collection에 포함되어 있는지 확인 |
| boolean equals(Object o)                                     | 동일한 Collection인지 비교                                   |
| int hashCode()                                               | Collection의 hash code 반환                                  |
| boolean isEmpty()                                            | Collection이 비었는지 확인                                   |
| Iterator iterator()                                          | Collection의 Iterator를 얻어서 반환                          |
| boolean remove(Object o)                                     | 지정된 객체 삭제                                             |
| boolean removeAll(Collection c)                              | 지정된 Collection에 포함된 객체들을 삭제                     |
| boolean retainAll(Collection c)                              | 지정된 Collection에 포함된 객체만을 남기고 다른 객체들을 Collection에서 삭제. 이 작업으로 Collection에 변화가 있으면 true, 없으면 false 반환 |
| int size()                                                   | Collection에 저장된 객체의 개수 반환                         |
| Object[] toArray()                                           | Collection에 저장된 객체를 객체배열(Object[])로 반환         |
| Object[] toArray(Object[] a)                                 | 지정된 배열에 Collection의 객체를 저장해서 반환              |

- Java API문서를 보면 Object를 E로 표현하고 있음 => E는 특정 타입을 의미하는 것으로 Generic 표기

#### List 인터페이스

- 정의 메서드

  - void add(int index, Object element)
  - boolean addAll(int index, Collection c)

  => 지정된 index에 객체 또는 컬렉션의 객체들을 추가

  - Object get(int index) : index의 객체 반환
  - int indexOf(Object o) : 지정된 객체의 index 반환
  - int lastIndexOf(Object o) : 지정된 객체의 index반환 (역순)
  - ListIterator listIterator() : List의 객체에 접근할 수 있는 ListIterator반환
  - Object remove(int index) : 지정된 index의 객체를 삭제하고 삭제도니 객체 반환
  - Object set(int index, Object element) : 지정된 index에 객체 저장 (add는 추가, set은 수정)
  - void sort(Comparator c) : 지정도니 비교자로 List를 정렬
  - List subList(int fromIndex, int toIndex) : 지정된 범위(form~to)에 있는 객체 반환

#### Set 인터페이스

- Collection 클래스를 구현하는데 사용 (따로 정의된 메서드는 사용하면서 찾을 것)

### Map 인터페이스

| 메서드                               | 설명                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| void clear()                         | Map의 모든 객체 삭제                                         |
| boolean containsKey(Object key)      | 지정된 key객체와 일치하는 Map의 key객체가 있는지 확인        |
| boolean containsValue(Object value)  | 지정된 value객체와 일치하는 Map의 value객체가 있는지 확인    |
| Set entrySet()                       | Map에 저장되어 있는 key-value쌍을 Map.Entry타입의 객체로 저장한 Set으로 반환 |
| boolean equals(Object o)             | 동일한 Map인지 비교                                          |
| Object get(Ojbect key)               | 지정한 key객체에 대응하는 value객체를 찾아 반환              |
| int hashCode()                       | 해시코드 반환                                                |
| boolean isEmpty()                    | Map이 비었는지 확인                                          |
| Set keySet()                         | Map에 저장된 모든 key 반환                                   |
| Ojbect put(Object key, Object value) | Map에 value객체를 key객체에 연결하여 저장                    |
| void putAll(Map t)                   | 지정된 Map의 모든 key-value쌍을 추가                         |
| Object remove(Object key)            | 지정한 key객체와 일치하는 key-value쌍 삭제                   |
| int size()                           | Map에 저장된 key-value쌍의 개수 반환                         |
| Collection values()                  | Map에 저장된 value객체를 반환                                |

#### Map.Entry인터페이스 

- Map인터페이스의 내부 인터페이스
- Map에 저장되는 key-value쌍을 다루기 위해 내부적으로 Entry 인터페이스를 정의함

```java
public interface Map {
  
  ....
    interface Entry {
    	Object getKey();
    	Object getValue();
    	Object setValue(Object value);
    	boolean equals(Object o);
    	int hashCode();
    	...
  }
}
```

