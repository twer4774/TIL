# CollectionFramwork - HashMap

- HashMap
  - HashTable을 개선한 새로운 버전 => 해시테이블보다 해시맵을 사용할 것
  - map을 이용하여 키와 값으로 데이터 저장
  - 해싱을 이용하여 많은 양의 데이터를 검색하는데 뛰어난 성능을 보임

| 생성자 또는 메서드                                           | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| HashMap()                                                    |                                                              |
| HashMap(int initialCpacity)                                  |                                                              |
| HashMap(int initialCapacity, float loadFactor)               | 지정된 초기용량과 load factor의 HashMap 생성                 |
| void clear() / Object clone()                                |                                                              |
| boolean containsKey(Object key) <br />booelan containsValue(Object value) |                                                              |
| Set entrySet()                                               | HashMap에 저장된 키와 값을 엔트리(키와 값의 결합)형태로 Set에 저장해서 반환 |
| Set keySet()                                                 | HashMap에 저장된 모든 키를 Set으로 반환                      |
| Object get(Object key)<br />Object getOrDefault(Object key, Object defaultValue) |                                                              |
| boolean isEmpty()                                            |                                                              |
| Object put(Object key, Object value)<br />void pullAll(Map m) | 저장된 키와 값을 HashMap에 저장<br />Map에 저장된 모든 요소를 HashMap에 저장 |
| Object remove(Object key)                                    |                                                              |
| Object replace(Object key, Object value)                     | 해당 키의 값을 지정된 value로 대체                           |
| boolean replace(Object key, Object oldValue, Object new Value) | 지정된 키와 객체(oldValue)가 모두 일치하는 경우에만 새로운 객체로 대체 |
| int size()                                                   |                                                              |
| Collection values()                                          | HashMap에 저장된 모든 값을 컬렉션의 형태로 반환              |

### 사용자ID와 비밀번호 저장

```java
package JavaStandard;

import java.util.HashMap;
import java.util.Scanner;

/**
 * 사용자 ID와 비밀번호 저장
 */
public class HashMapUser {

    public static void main(String[] args) {
        HashMap map = new HashMap();
        map.put("myId", "1234");
        map.put("asdf", "1111");
        map.put("asdf", "1234");
        
      
      	System.out.println(map); //{myId=1234, asdf=1234}
      
        Scanner s = new Scanner(System.in);
        
        while(true){
            System.out.println("id와 pw를 입력 : ");
            System.out.print("id : ");
            String id = s.nextLine().trim();

            System.out.print("pw : ");
            String pw = s.nextLine().trim();
            System.out.println();

            if (!map.containsKey(id)) {

                System.out.println("입력한 id는 존재하지 않음");
                continue;
            } else {
                if (!(map.get(id).equals(pw))) {
                    System.out.println("비밀번호가 다름");
                } else {
                    System.out.println("id, 비밀번호가 일치");
                    break;
                }
            }
        }
    }
}
/*
id와 pw를 입력 : 
id : asdf
pw : 1234

id, 비밀번호가 일치
*/
```

- 키 값이 중복될 경우 새로 추가된 값이 덮어 씌우는 것에 주의

### HashMap 데이터 저장, 불러오기

```java
import java.util.*;

public class HashMapSaveLoad {
    public static void main(String[] args) {
        HashMap map = new HashMap();
        map.put("김자바", new Integer(90));
        map.put("김자바", new Integer(100));
        map.put("이자바", new Integer(100));
        map.put("강자바", new Integer(80));
        map.put("안자바", new Integer(90));

        Set set = map.entrySet();
        System.out.println("entrySet형태 : " + set);

        Iterator it = set.iterator();

        while (it.hasNext()) {
            Map.Entry e = (Map.Entry) it.next();
            System.out.println("이름 : " + e.getKey() + ", 점수 : " + e.getValue());
        }

      	//키만 필요할 때
        set = map.keySet();
        System.out.println("참가자 명단 :  " + set);

      	//값만 필요할 때
        Collection values = map.values();
        it = values.iterator();

        int total = 0;
        while (it.hasNext()) {
            Integer i = (Integer) it.next();
            total += i.intValue();
        }

        System.out.println("총점 : " + total);
        System.out.println("평균 : " + (float)total/set.size());
        System.out.println("최고점수 : " + Collections.max(values));
        System.out.println("최저점수 : " + Collections.min(values));
    }
}

/*
entrySet형태 : [안자바=90, 김자바=100, 강자바=80, 이자바=100]
이름 : 안자바, 점수 : 90
이름 : 김자바, 점수 : 100
이름 : 강자바, 점수 : 80
이름 : 이자바, 점수 : 100
참가자 명단 :  [안자바, 김자바, 강자바, 이자바]
총점 : 370
평균 : 92.5
최고점수 : 100
최저점수 : 80
*/
```

### HashMap Value에 HashMap 형태로 저장 => 전화번호부 만들기

- 해시맵의 key, value는 모두 Object값을 저장할 수 있으므로 HashMap형태로 키와 값을 저장할 수 있음

```java
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class HashMapPhoneBook {

    static HashMap phoneBook = new HashMap();


    public static void main(String[] args) {
        addPhoneNo("친구", "이자바", "010-1111-1111");
        addPhoneNo("친구", "김자바", "010-2222-1111");
        addPhoneNo("친구", "감자바", "010-3333-1111");
        addPhoneNo("회사", "이대리", "010-4444-1111");
        addPhoneNo("회사", "강부장", "010-5555-1111");
        addPhoneNo("컴퓨터수리", "010-6666-1111");
        addPhoneNo("세탁", "010-7777-1111");

        printList();
    }

    private static void addPhoneNo(String groupName, String name, String tel){
        addGroup(groupName);
        HashMap group = (HashMap) phoneBook.get(groupName);
        group.put(tel, name);

    }

    //매개 변수가 다른 메서드를 넣어 groupName이 없는 경우 기타로 처리
    private static void addPhoneNo(String name, String tel){
        addPhoneNo("기타", name, tel);
    }
    
    private static void addGroup(String groupName) {
        if (!phoneBook.containsKey(groupName)) {
            phoneBook.put(groupName, new HashMap());
        }
    }

    //전화번호부 전체 출력
    private static void printList(){
        Set set = phoneBook.entrySet();
        Iterator it = set.iterator();

        while (it.hasNext()) {
            Map.Entry e = (Map.Entry) it.next();

            Set subSet = ((HashMap) e.getValue()).entrySet();
            Iterator subIt = subSet.iterator();

            System.out.println(" *  "+e.getKey()+"["+subSet.size()+"]");

            while (subIt.hasNext()) {
                Map.Entry subE = (Map.Entry) subIt.next();
                String telNo = (String)subE.getKey();
                String name = (String)subE.getValue();
                System.out.println(name + " " + telNo);
            }

            System.out.println();
        }
    }
}

/*
 *  기타[2]
세탁 010-7777-1111
컴퓨터수리 010-6666-1111

 *  친구[3]
이자바 010-1111-1111
김자바 010-2222-1111
감자바 010-3333-1111

 *  회사[2]
이대리 010-4444-1111
강부장 010-5555-1111
*/
```

