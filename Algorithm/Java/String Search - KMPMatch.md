# String Search - KMP법

- 처음부터 검사하는 브루트-포스법과는 다르게 중간 검사 결과를 효율적으로 사용. 그러나 브루트-포스법보다는 복잡하고 Boyer-Moore법과는 성능이 같거나 좋지 않아 실제 프로그램에서 거의 사용하지 않음

  - 브루트-포스법은 검사했던 위치결과를 버리고 다음텍스트로 1칸이동 뒤 처음부터 재검사

- 찾고자하는 문자열 패턴을 이용해 건너띄기 표를 먼저 작성해야함

  - 찾고자하는 문자열 패턴을 하나 더 만들어 두 값의 인덱스를 비교하여 표 작성

  - ABCABD을 찾고자하는 문자열 패턴이라고 할 때,

    - ABCABD
        ABCABD

    - ABCABD
           ABCABD

    - ABCABD

      ​       ABCABD

    - ABCABD
                   ABCABD

      | A    | B    | C    | A    | B    | D    |
      | ---- | ---- | ---- | ---- | ---- | ---- |
      | -    | 0    | 0    | 1    | 2    | 0    |

```java
//KMP를 이용한 문자열 검색
public class KMPmatch {
    static int kmpMatch(String txt, String pattern){
        int textPointer = 1; //txt 커서
        int patternPointer = 0; //pattern 커서
        int[] skipTable = new int[pattern.length() + 1]; //건너뛰기 표
        
        //건너뛰기표 만들기
        skipTable[textPointer] = 0;
        while (textPointer != pattern.length()) {
            if (pattern.charAt(textPointer) == pattern.charAt(patternPointer)) {
                skipTable[++textPointer] = ++patternPointer;
            } else if (patternPointer == 0){
                skipTable[++textPointer] = patternPointer;
            } else {
                patternPointer = skipTable[patternPointer];
            }
        }
        
        //검색
        textPointer = patternPointer = 0;
        while (textPointer != txt.length() && patternPointer != pattern.length()){
            if (txt.charAt(textPointer) == pattern.charAt(patternPointer)){
                textPointer++;
                patternPointer++;
            } else if (patternPointer == 0){
                textPointer++;
            } else {
                patternPointer = skipTable[patternPointer];
            }
            
        }
        
        if (patternPointer == pattern.length()){ //textPoint - patternPoint를 반환
            return textPointer - patternPointer;
        }
        return -1; //검색 실패
    }
    
    public static void main(String[] args) {

    }//main
}
```

