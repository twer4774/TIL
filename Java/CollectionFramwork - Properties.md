# CollectionFramewrok - Properties

- HashMap의 구 버전인 Hashtable을 상속받아 구현한 것으로  String, String의 key, value 값으로 한정하여 사용
- 주로 환경설정과 같은 속성을 저장하는데 사용

| 메서드                                                       | 설명                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Properties()                                                 |                                                              |
| Properties(Porperties defaults)                              | 지정된 Properties에 저장된 목록을 가진 Properties객체를 생성 |
| String getProperty(String key)                               | 지정된 키의 값 반환                                          |
| String getProperty(String key, String defaultValue)          | 지정된 키와 값을 반환. 키를 못찾으면 defaultValue 반환       |
| void list(PrintStrema out)                                   | 지정된 PrintStream에 저장된 목록 출력                        |
| void list(PrintWriter out)                                   | 지정된 PrintWriter에 저장된 목록 출력                        |
| void load(InputStream inStream)                              | 지정된 inputStream으로 부터 목록을 읽어서 저장               |
| void load(Reader reader)                                     | 지정된 Reader으로 부터 목록을 읽어서 저장                    |
| void loadFromXML(InputStream in)                             | 지정된 InputStream으로부터 XML문서를 읽어서 XML문서에 저장된 목록을 읽어 담음(load & store) |
| Enumeration propertyNames()                                  | 목록의 모든 키가 담긴 Enumeration반환                        |
| void save(OutputStream out, String header)                   | Deprecated. 대신 store()사용                                 |
| void store(OutStream out, String comments)                   | 저장된 목록을 지정된 OUtputStream에 출력                     |
| void store(Writer writer, String comments)                   | 저정된 목록을 지정된 Writer에 출력                           |
| void storeToXML(OutputSTream os, String comment)             | 저장된 목록을 지정된 출력 스트림에 XML문서로 출력            |
| void storeToXML(OutputSTream os, String comment, String encoding) | 저장된 목록을 지정된 출력스트림에 해당 인코딩의 XML문서로 출력 |
| Object setProperty(String key, String value)                 | 업데이트 혹은 값이 없을때는 store 역할                       |
| Set stringPropertyNames()                                    | Properties에 저장되어 있는 키를 Set에 담아 반환              |

### Properties의 저장, 읽어오기

```java
import java.util.Enumeration;
import java.util.Properties;

/**
 * String, String 형태의 키, 값으로 저장하는 컬렉션프레임워크
 */
public class PropertiesExStoreLoad {
    public static void main(String[] args) {
        Properties prop = new Properties();

        //prop에 키, 값 저장
        prop.setProperty("timeout", "30");
        prop.setProperty("language", "kr");
        prop.setProperty("size", "10");
        prop.setProperty("capacity", "10");

        //prop에 저장된 요소들을 Enumeration을 이용해 출력
        Enumeration e = prop.propertyNames();

        while (e.hasMoreElements()) {
            String element = (String) e.nextElement();
            System.out.println(element + "=" + prop.getProperty(element));
        }

        System.out.println();
        //size 변경
        prop.setProperty("size", "20");

        System.out.println("size=" + prop.getProperty("size"));
        System.out.println("capacity=" + prop.getProperty("capacity", "20"));
        System.out.println("loadfactor=" + prop.getProperty("loadfactor", "0.75"));
        System.out.println("전체출력: " + prop);
        //prop에 저장된 것들을 화면에 출력
        prop.list(System.out);
    }

}

/*
capacity=10
size=10
timeout=30
language=kr

size=20
capacity=10
loadfactor=0.75
전체출력: {capacity=10, size=20, timeout=30, language=kr}
-- listing properties --
capacity=10
size=20
timeout=30
*/
```

