# Median number(세 값의 중앙값)

- 최댓값, 최솟값 보다 구하기 어려움

```java
import java.util.Scanner;

//3개의 정숫값을 입력하고 중앙값을 구한다.

public class median {
    static int med3(int a, int b, int c){
        if (a >= b)
            //b가 중앙값
            if(b >= c)
                return b;
            //a가 중앙값
            else if (a <= c)
                return a;
            //c가 중앙값
            else
                return c;
        //b가 a보다 큰 경우,
        //a가 c보다 크면 a가 중앙값
        else if (a > c)
            return a;
        //b가 c보다 크면 c가 중앙값 - b가 이미 a보다 크니까
        else if (b > c)
            return c;
        //b가 a보다 크고, a는 c보다 작지만, b는 c보다 작음 => c > b > a
        else
            return b;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("세 정수의 중앙값");
        System.out.println("a : ");
        int a = stdIn.nextInt();
        System.out.println("b : ");
        int b = stdIn.nextInt();
        System.out.println("c : ");
        int c = stdIn.nextInt();

        System.out.println("중앙값은 " + med3(a, b, c) + "입니다.");
    }//main
}

```

