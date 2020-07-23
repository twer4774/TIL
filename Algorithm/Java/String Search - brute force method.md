# String Search - brute force method

- 브루스-포스법(brute force method) : 문자열 검색 알고리즘으로 가장 단순한 형태

- 단순법, 소박법이라고 불리우며 선형검색을 확장한 알고리즘
- 뒤로 한 칸씩 이동하면서 찾고자하는 패턴(ABC)과 같은지 확인한다. 단, 뒤로 이동할때마다 패턴의 앞부분부터 비교하므로 비효율적이다.

| A    | B    | A    | B    | C    | D    | E    | F    | G    | H    | A    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| A    | B    | C    |      |      |      |      |      |      |      |      |

```java
import java.util.Scanner;

//브루트-포스법으로 문자열을 검색

public class BFmatch {
    //브루트-포스법으로 문자열 검색
    static int bfMatch(String txt, String pat) {
        int textPointer = 0; //txt 커서
        int patternPointer = 0; //pattern 커서

        while (textPointer != txt.length() && patternPointer != pat.length()) {
            if (txt.charAt(textPointer) == pat.charAt(patternPointer)) {
                textPointer++;
                patternPointer++;
            } else {
                textPointer = textPointer - patternPointer + 1;
                patternPointer = 0;
            }
        }
        if ( patternPointer == pat.length()){ //검색 성공
            return textPointer - patternPointer;
        }
        return -1; //검색 실패
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("텍스트 : ");
        String s1 = stdIn.next(); //텍스트용 문자열

        System.out.println("패턴 : ");
        String s2 = stdIn.next(); //패턴용 문자열

        int idx = bfMatch(s1, s2); //문자열 s1에서 문자열 s2를 검색

        if (idx == -1){
            System.out.println("텍스트에 패턴이 없습니다.");
        } else {
            //일치하는 문자 바로 앞까지의 길이를 구함
            int len = 0;
            for (int i = 0; i < idx; i++) {
                len += s1.substring(i, i + 1).getBytes().length;
            }
            len += s2.length();

            System.out.println((idx + 1) + "번째문자부터 일치");
            System.out.println("텍스트 : " + s1);
            System.out.printf(String.format("패턴 : %%%ds\n", len), s2);
        }
    }//main
}

```

- substring - java의 문자열 자르기 메서드
  - substring(int startIndex, int endIndex) - 시작과 끝 인덱스를 지정하여 문자열을 자
- getBytes() - 문자열 인코딩을 해주는 것

=> substring(i , i + 1).getBytes().length 는 잘린 문자열의 인코딩을 통해 길이를 반환해주기 위한것