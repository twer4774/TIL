# [완전탐색]White'sInterestingParty

> 파티에 공통의 관심사를 가진 친구들을 초대
>
> 한 친구당 2개의 관심사를 각각 first[i], second[i]에 저장
> 최대로 많이 초대할 수 있는 친구의 수 구하기
>
> ```
> String[] first = {"fishing", "gardening", "swimming", "fishing"};
> String[] second = {"hunting", "fishing", "fishing", "biting"}; 
> //result: 4
> 
> String[] first2 = {"variety", "diversity", "loquacity", "courtesy"};
> String[] second2 = {"talking", "speaking", "discussion", "meeting"}; 
> //result: 1
> 
> String[] first3 = {"snakes", "programming", "cobra", "monty"};
> String[] second3 = {"python", "python", "anaconda", "python"}; 
> 
> //result: 3
> ```

## 내 풀이

- Hash를 이용해서 key에 value 값 중 가장 큰 값을 리턴

```java
package com.company;

import java.util.HashMap;

public class WhiteInterestingParty {

    public static int bestInvitation(String[] first, String[] second){
        int max = 0;
        // 내 생각 - 해시맵을 이용해서 해당 key가 있는 value의 수를 1씩 증가하여 갯수가 가장 많은 것을 찾는다.
        HashMap<String, Integer> hash = new HashMap<>();

        for (int i = 0; i < first.length; i++) {
            hash.put(first[i], hash.getOrDefault(first[i], 0)+1);
            hash.put(second[i], hash.getOrDefault(second[i], 0)+1);
        }


        for (String s : hash.keySet()) {
            System.out.println("s:"+s+"v:"+hash.get(s));
            max = Math.max(max, hash.get(s));
        }
        System.out.println("max: " + max);
        return max;
    }
    public static void main(String[] args) {

        String[] first = {"fishing", "gardening", "swimming", "fishing"};
        String[] second = {"hunting", "fishing", "fishing", "biting"}; //result: 4

        String[] first2 = {"variety", "diversity", "loquacity", "courtesy"};
        String[] second2 = {"talking", "speaking", "discussion", "meeting"}; //result: 1

        String[] first3 = {"snakes", "programming", "cobra", "monty"};
        String[] second3 = {"python", "python", "anaconda", "python"}; //result: 3

        bestInvitation(first, second);
        bestInvitation(first2, second2);
        bestInvitation(first3, second3);
    }
}
```

- 중첩 for문을 사용해도 되지만 HashMap같은 연관배열을 이용해 for문의 개수를 줄임