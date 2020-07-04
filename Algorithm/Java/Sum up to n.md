# Sum up to n

- 1부터 n까지의 합 구하기

### While

```java
import java.util.Scanner;

//1~n까지의 합 구하기

public class SumWhile {
    public static void main(String[] args) {
    Scanner stdIn = new Scanner(System.in);

        System.out.println("1부터 n까지의 합 구하기");
        System.out.println("n : ");
        int n = stdIn.nextInt();

        int sum = 0;
        int i = 1;

        while(i <= n) {
            sum += i;
            i++;
        }
        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }//main
}
```

### Do-While

- 무조건 한번은 실행되어야 하는 경우 쓰임.
- 음수가 입력되면 무한 입력

```java
import java.util.Scanner;

public class SumForPos {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        System.out.println("1부터 n까지의 합 구하기");
        do {
            System.out.println("n : ");
            n = stdIn.nextInt();
        }while( n <= 0);
      
        int sum = 0;

        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }//main
}

```

### For

```java
import java.util.Scanner;

public class SumFor {
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("1부터 n까지의 합 구하기");
        System.out.println("n : ");
        int n = stdIn.nextInt();

        int sum = 0;

        for(int i = 1; i <= n; i++) {
            sum += i;
        }
        System.out.println("1부터 " + n + "까지의 합은 " + sum + "입니다.");
    }//main
}
```

### Gauss

```java
import java.util.Scanner;

//가우스의 법칙을 이용하여 n까지의 합 구하기

public class practice_SumGauss {
    static int sumGauss(int n){
        int sum = 0;
        int median = n/2;
        //가우스의 덧셈법 1부터 n까지의 숫자를 더하고 n의 중간값을 곱한다. 이때, n이 홀수이면 (n+1)/2를 한 값을 더해주고 짝수이면 0을 더한다
        sum = (1 + n) * median + (n % 2 == 1 ? (n+1)/2 : 0);
        return sum;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("n의 값 입력");
        int n  = stdIn.nextInt();
        System.out.println("1에서 " +n+ "까지의 합은 " + sumGauss(n) + "입니다.");
    }//main
}
```

- 정수 a,b를 포함하여 그 사이의 모든 정수의 합

```java
import java.util.Scanner;

public class practice_SumAtoB {
    static int sumof(int a, int b){
        int sum = 0;
        int max, min = 0;
        if (a > b){
            max = a;
            min = b;
        } else {
            max = b;
            min = a;
        }
        for(int i = min; i <= max; i++){
            sum += i;
        }

        return sum;
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("a 값 입력");
        int a = stdIn.nextInt();
        System.out.println("b 값 입력");
        int b = stdIn.nextInt();

        System.out.println(a+"에서 "+b+"까지의 합은 :" + sumof(a, b));
    }//main
}
```

### 