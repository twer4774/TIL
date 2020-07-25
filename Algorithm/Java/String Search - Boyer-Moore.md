# String Search - Boyer-Moore

KMP보다 효율이 더 좋음 -> 최대 패턴의 길이만큼 건너뛰기 가능

- KMP와 마찬가지로 건너뛰기 표를 만들어야 함
- Bad Character Method와 Good Suffix Method 두 가지방식을 혼합하여 사용
  - Bad Character Method : T(문자열)과 P(패턴)을 비교하여 Skip Table 작성
    - 오른쪽에서 왼쪽으로 이동하며 Skip Table을 작성하며, 최대 건너뛰기는 P의 길이만큼
  - Good Suffix Method: 패턴의 접미부와 일치하는 문자 -> 패턴(P)의 일정한 패턴확인
    - 일치하는 패턴의 뒷 그룹으로 P를 이동시켜 검사

## Bad Character Method

Text: There would have been a time for such a word

Pattern: word

Skip Table

| w    | o    | r    | d    |
| ---- | ---- | ---- | ---- |
|      | 2    | 1    |      |

### Step1.

There would have been a time for such a word

word

- r과 d는 불일치. bad character -> 패턴에서 r의 값은 오른쪽으로 부터 1이동 한 값이므로, Skip Table의 r은 1이 됨
- 1만큼 패턴을 이동시킨다.

### Step2.

There would have been a time for such a word

 word

- e는 패턴에 없는 값이므로, 패턴의 길이 4만큼 이동함

…. 반복

...

### Step n-1.

There would have been a time for such a word

​                                                                      word

- o와 d는 불일치. bad character -> 패턴에서 o의 값은 오른쪽으로부터 2이동 한 값이므로, Skip Table의 o는 2가 됨
- 2만큼 패턴을 이동시킨다.

### Step n.

There would have been a time for such a word

​                                                                          word

- 일치하면 종료

```java
//Boyer-Moore의 bad character 방식 이용. Good suffix method는 적용하지 않았음

public class BMmatch {
    
    static int bmMatch(String text, String pattern){
        int textPoint; //text커서
        int patternPoint; //pattern 커서
        int textLen = text.length();
        int patternLen = pattern.length();
        int[] skip = new int[Character.MAX_VALUE + 1]; //건너뛰기 표 - 모든 문자의 크기 256개 설정
        
        //건너뛰기 표 만들기
        for (textPoint = 0; textPoint <= Character.MAX_VALUE; textPoint++) {
            skip[textPoint] = patternLen;
        }
        
        for(textPoint = 0; textPoint < patternLen - 1; textPoint++){
            skip[pattern.charAt(textPoint)] = patternLen - textPoint - 1; //textPoint == patternLen - 1
        }
        
        //검색
        while (textPoint < textLen) {
            patternPoint = patternLen - 1; //pattern의 끝문자에 주목

            while (text.charAt(textPoint) == pattern.charAt(patternPoint)) {
                if (patternPoint == 0) {
                    return textPoint; //검색 성공
                }
                patternPoint--;
                textPoint--;
            }
            textPoint += (skip[text.charAt(textPoint)] > patternLen - patternPoint) ? skip[text.charAt(textPoint)] : patternLen - patternPoint;
        }
        return -1; //검색실패
    }
    public static void main(String[] args) {

    }//main
}
```

