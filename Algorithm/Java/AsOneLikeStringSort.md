# 내 마음대로 문자열 정렬 - AsOneLikeStringSort

> ###### 문제 설명
>
> 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.
>
> ##### 제한 조건
>
> - strings는 길이 1 이상, 50이하인 배열입니다.
> - strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
> - strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
> - 모든 strings의 원소의 길이는 n보다 큽니다.
> - 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
>
> ##### 입출력 예
>
> | strings           | n    | return            |
> | ----------------- | ---- | ----------------- |
> | [sun, bed, car]   | 1    | [car, bed, sun]   |
> | [abce, abcd, cdx] | 2    | [abcd, abce, cdx] |
>
> ##### 입출력 예 설명
>
> **입출력 예 1**
> sun, bed, car의 1번째 인덱스 값은 각각 u, e, a 입니다. 이를 기준으로 strings를 정렬하면 [car, bed, sun] 입니다.
>
> **입출력 예 2**
> abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다. 따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다. abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.

## 내 풀이

- 마지막 조건의 사전순 정렬을 위해 가장 처음 배열을 사전순으로 정렬한다.
- 그 후 n번째 요소를 뽑아 정렬을 한다 -> 버블정렬 이용

```java
import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        
        //사전순으로 정렬을 먼저 함
        Arrays.sort(strings);
        
        //strings[i].charAt(n)으로 값을 뽑아 정렬한다
        //정렬은 버블정렬로
        for (int i = 0; i < strings.length-1; i++) {
            for (int j = strings.length-1; j > i; j--) {
                if (strings[j - 1].charAt(n) > strings[j].charAt(n)) {
                    swap(strings, j-1, j);
                }
            }
        }
        answer = strings;   
        return answer;
    }
    
     public static void swap(String[] strings, int idx1, int idx2){
        String t = strings[idx1];
        strings[idx1] = strings[idx2];
        strings[idx2] = t;
    }
}
```

![image-20201229111655186](/Users/wonik/Library/Application Support/typora-user-images/image-20201229111655186.png)

