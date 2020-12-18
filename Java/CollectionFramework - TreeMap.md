# CollectionFramework - TreeMap

- 이진검색트리의 형태로 키와 값의 쌍으로 이루어진 데이터를 저장
- 검색과 정렬에 적합한 컬렉션 클래스
- HashMap과 TreeMap
  - 검색 성능은 HashMap이 더 좋음
  - 범위 검색이나 정렬이 필요한 경우 TreeMap 이용

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| TreeMap()                                                    |                                                              |
| TreeMap(Comparator c)                                        | Comparator를 기준으로 정렬하는 TreeMap생성                   |
| TreeMap(Map m)                                               | 주어진 Map에 저장된 모든 요소를 포함하는 TreeMap 생성        |
| TreeMap(SortedMap m)                                         | 주어진 SortedMap에 저장된 모든 요소를 포함하는 TreeMap생성   |
| Map.Enry ceilingEntry(Object key)                            | 지정된 key와 일치하거나 큰 것중 제일 작은 것의 키와 값의 쌍(Map.Entry)을 반환. 없으면 null 반환 |
| Map.Entry floorEntry(Object key)                             | 지정된 key와 일치하거나 작은 것중 제일 큰것의 키와 값의 쌍(Map.Entry)을 반환. 없으면 null 반환 |
| Object ceilingKey(Object key)                                | 지정된 key와 일치하거나 큰 것중 제일 작은 것의 키를 반환. 없으면 null 반환 |
| Object floorKey(Object key)                                  | 지정된 key와 일치하거나 작은 것중 제일 큰 것의 키를 반환. 없으면 null 반환 |
| void clear() / Object clone()                                |                                                              |
| Comparator comparator()                                      | TreeMap의 정렬기준이 되는 Comparator를 반환.  Comparator가지정되어 있지 않으면 null반환 |
| boolean containsKey(Object key)                              |                                                              |
| boolean containsValue(Object value)                          |                                                              |
| NavigableSet descendingKeySet()                              | TreeMap에 저장된 키를 역순으로 정렬하여 NavigableSet에 담아서 반환 |
| Set entrySet()                                               | 키와 값을 엔트리 형태로 Set에 저장하여 반환                  |
| Map.Entry firstEntry()                                       | 첫번째(가장 작은) 키와 값의 쌍 반환                          |
| Map.Entry lastEntry()                                        |                                                              |
| Object firstKey()                                            | 첫번째(가장작은) 키 반환                                     |
| Object lastKey()                                             |                                                              |
| Object get(Object key)                                       |                                                              |
| SortedMap headMap(Object toKey)                              | TreeMap에 저장된 첫번째 요소부터 지정된 범위에 속하는 요소가 담긴 SortedMap을 반환(toKey 미포함) |
| NavigableMap headMap(Object toKey, boolean inclusive)        | 첫번재 요소부터 지정된 범위에 속한 모든 요소가 담긴 SortedMap반환. inclsive의 값이 true이면 toKey도 범위에 포함 |
| Map.Entry higherEntry(Object key)                            | 지정된 key보다 큰 키 중에서 제일 작은 키의 쌍을 반환. 없으면 null |
| Map.Entry lowerEntry(Object key)                             |                                                              |
| Object hihgerKey(Object Key)                                 | 지정된 key보다 큰 키 중에서 제일 작은 키 반환                |
| Object lowerKey(Object Key)                                  |                                                              |
| Set keySet()                                                 | 저장된 모든 key를 Set으로 반환                               |
| NavigableSet navigableKeySet()                               | 모든 키가 담긴 NavigableSet 반환                             |
| Map.Entry pollFirstEntry()                                   | 제일 작은 키를 제거하면서 반환                               |
| Map.Entry pollLastEntry()                                    | 제일 큰 키를 제거하면서 반환                                 |
| Object put(Object key, Object value)                         | 저장                                                         |
| NavigableMap subMap(Object fromKey, boolean fromInclusive, Objecy toKey, boolean toInclusive) | 지정된 두 키 사이에 있는 모든 요소를 NavigableMap으로 반환. Inclusive가 true이면 범위에 포함 |
| SortedMap subMap(Object fromKey, Object toKey)               | SortedMap으로 반환(toKey는 포함되지 않음)                    |
| SortedMap tailMap(Object fromKey)                            | 지정된 요소부터 마지막요소까지 SortedMap반환                 |
| NavigableMap tailMap(Object fromKey, booelan inclusive)      | 지정된 키부터 마지막 요소의 범위에 속한 요소가 담긴 NavigableMap을 반환. Inclusive가 ture면 fromKey포함 |
| Collection values()                                          | TreeMap에 저장된 모든 값을 컬렉션의 형태로 반환              |

### TreeMap 기본정렬, 내림차순 정렬

```java
import java.util.*;

/**
 * TreMap을 이용한 기본정렬, 내림차순 정렬
 */
public class TreeMapSort {

    public static void main(String[] args) {
        String[] data = {"A", "K", "A", "K", "D", "K", "A", "K", "K", "K", "Z", "D"};

        TreeMap map = new TreeMap();

        for (int i = 0; i < data.length; i++) {
            //map의 키가 data의 값으로 존재한다면
            if (map.containsKey(data[i])) {
                Integer value = (Integer)map.get(data[i]);
                //키에 맞는 값의 갯수를 1 증가 시킴
                map.put(data[i], new Integer(value.intValue() + 1));
            } else {
                //존재하지 않으면 1로 저장
                map.put(data[i], new Integer(1));
            }
        } //for

        Iterator it = map.entrySet().iterator();

        System.out.println("== 기본정렬 ==");
        while (it.hasNext()) {
            Map.Entry entry = (Map.Entry)it.next();
            int value = ((Integer) entry.getValue()).intValue();
            System.out.println(entry.getKey() + " : " + printBar('#', value) + " " + value);
        }//while

        System.out.println();

        //map을 ArrayList로 변환한 후 Collections.sort()로 정렬
        Set set = map.entrySet();
        List list = new ArrayList(set);

        Collections.sort(list, new ValueComparator());

        it = list.iterator();

        System.out.println("== 값의 크기가 큰 순서로 정렬 ==");
        while (it.hasNext()) {
            Map.Entry entry = (Map.Entry) it.next();
            int value = ((Integer) entry.getValue()).intValue();
            System.out.println(entry.getKey() + " : " + printBar('#', value) + " " + value);
        }

    }//main


    static class ValueComparator implements Comparator{
            public int compare(Object o1, Object o2){
                if (o1 instanceof Map.Entry && o2 instanceof Map.Entry) {
                    Map.Entry e1 = (Map.Entry) o1;
                    Map.Entry e2 = (Map.Entry) o2;

                    int v1 = ((Integer) e1.getValue()).intValue();
                    int v2 = ((Integer) e2.getValue()).intValue();

                    return v2 - v1;
                }
                return -1;
            }
    } //ValueComparator

    public static String printBar(char ch, int value){
        char[] bar = new char[value];

        for (int i = 0; i < bar.length; i++) {
            bar[i] = ch;
        }

        return new String(bar);
    }
}

/*
== 기본정렬 ==
A : ### 3
D : ## 2
K : ###### 6
Z : # 1

== 값의 크기가 큰 순서로 정렬 ==
K : ###### 6
A : ### 3
D : ## 2
Z : # 1
*/
```

