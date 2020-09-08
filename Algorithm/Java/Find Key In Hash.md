# Find Key In Hash 

- 해시의 value 값을 이용하여 key 값을 찾는 방법
- 카카오 문제를 풀다가 엉뚱한 방향으로 생각을 해서 이러한 코드를 작성했는데, 나중에 도움이 될꺼 같아 남겨둠

## 코드

```java
package com.company;

import java.util.Collections;
import java.util.HashMap;

public class KakoTuple {

    private static int[] answer;

    private static String Ex1 = "{2},{2,1},{2,1,3},{2,1,3,4}"; //2, 1, 3, 4가 나와야함
    private static HashMap<Integer, Integer> hash;

    public static int[] solution(String s){

        String temp = s.replace("{", "");
        String temp2 = temp.replace("}", "");
        String[] tempString = temp2.split(",");

        //해시에 저장 <숫자, 몇번쓰였는지 카운터>
        for (int i = 0; i < tempString.length; i++) {
            hash.put(Integer.parseInt(tempString[i]), i);
        }

        answer = new int[hash.size()];
        //최소 value 값을 구하고 -> 그 value에 해당하는 key 값을 answer에 넣는다.
        for (int j = 0; j < hash.size(); j++) {
            int min = Collections.min(hash.values());
            int key = getKey(hash, min);
            answer[j] = key;
            hash.put(key, hash.get(key)+10000000);
        }

        for (int i : answer){
            System.out.println(i);
        }
        return answer;
    }

    private static Integer getKey(HashMap<Integer, Integer> hash, int min) {
        for (int i : hash.keySet()){
            if(hash.get(i).equals(min)){
                return i;
            }
        }
        return null;
    }


    public static void main(String[] args) {
        hash = new HashMap<Integer, Integer>();

        solution(Ex1);
    }
}
```

