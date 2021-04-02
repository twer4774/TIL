# [전체 탐색] 회문

> 회문
>
> 앞에서 읽으나 뒤에서 읽으나 같은 단어
>
> 입력된 단어의 최소 길이의 회문 길이를 리턴하시오
>
> ```
> abab => ababa ==> 5
> abacaba => 입력자체가 회문 ==> 7
> qwert => qwertrewq => 모든문자가 다름 ==> 11
> abdfhdyrbdbsdfghjkllkjhgfds => abdfhdyrbdbsdfghjkllkjhgfdsbdbrydhfdba => 중간부터 회문 ==> 38 
> ```

## 풀이

```java
/**
 * 회문
 * 앞에서 읽으나 뒤에서 읽으나 같은 단어
 * 입력된 단어의 최소 길이의 회문 길이를 리턴하시오
 */
public class ThePalindrome {

    static int find(String s){
        //문자 길이 결정
        //첫 시작을 문자열의 길이부터 시작한다.
        for (int i = s.length(); ;i++) {
            boolean flag = true; //기본 플래그 값 설정

            for (int j = 0; j < s.length(); j++) {

                //반대쪽에 문자가 존재하는 데
                if((i-j-1) < s.length()){
                    //그 문자가 다를 경우 플래그 변경
                    if(s.charAt(j) != s.charAt(i-j-1)) {
                        flag = false;
                        break;
                    }
                }
            } //for

            //조건을 모두 만족하면 답을 리턴
            if(flag) return i;

        } //for
    }
    

    public static void main(String[] args) {
        System.out.println(find("abab")); //5
        System.out.println(find("abacaba")); //7
        System.out.println(find("qwerty")); //11
        System.out.println(find("abdfhdyrbdbsdfghjkllkjhgfds")); //38

    }
}
```

