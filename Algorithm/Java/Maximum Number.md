# Maximum number(최댓값 구하기)

### Maximum of three numbers(세 값의 최댓값)

```java
import java.util.Scanner;

//3개의 정숫값을 입력하고 최댓값을 구하기

public class Max3 {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("세 정수의 최댓값을 구하기");
        System.out.println("a의 값 : "); int a = stdIn.nextInt();
        System.out.println("b의 값 : "); int b = stdIn.nextInt();
        System.out.println("c의 값 : "); int c = stdIn.nextInt();

        int max = a;
        if (b > max) max = b;
        if (c > max) max = c;

        System.out.println("최댓값은 " + max + "입니다");
    }//main
}

```

### Maximum of four(네 값의 최댓값)

```java
import java.util.Scanner;

public class practice_max4 {

    static int max4(int a, int b, int c, int d){
        int max = a;
        if(b > max)
            max = b;
        if(c > max)
            max = c;
        if(d > max)
            max = d;

        return max;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int a, b, c, d;
        int max;

        System.out.println("4개의 정수 입력: ");
        System.out.println("a:");
        a = stdIn.nextInt();
        System.out.println("b:");
        b = stdIn.nextInt();
        System.out.println("c:");
        c = stdIn.nextInt();
        System.out.println("d:");
        d = stdIn.nextInt();

        max = max4(a,b,c,d);
        System.out.println("최댓값은 " + max + "입니다.");
    }//main
}

```

