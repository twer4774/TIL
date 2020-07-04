# Judge Sign(양,음,0 판단)

- 조건문 if를 이용한 양수, 음수, 0 판단

```java
import java.util.Scanner;

//입력한 정숫값이 양수인지 음수인지 0인지 판단

public class JudgeSign {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.println("정수 입력");
        int n = stdIn.nextInt();

        if(n > 0)
            System.out.println("양수");
        else if(n<0)
            System.out.println("음수");
        else
            System.out.println("0입니다");
    }//main
}
```

