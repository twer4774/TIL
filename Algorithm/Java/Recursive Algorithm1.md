# Recursive Algorithm1(재귀 알고리즘)

재귀 : 자기 자신을 포함하고 다시 자기자시능ㄹ 사용하여 정의

재귀를 효과적으로 사용하면 프로그램을 간결하게 할 수 있음 ex) 병합정렬, 퀵정렬, 이진트리

## 팩토리얼 구하기

### 비재귀적으로 구현

```java
import java.util.Scanner;

//비재귀적인 방식으로 팩토리얼 구현

public class FactorialNonRecursive {
    //음이 아닌 정수 값 n의 팩토리얼 값을 반환
    static int factorial(int n){
        int fact = 1;

        while(n > 1){
            fact *= n--;
        }

        return (fact);
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("정수 입력 : ");
        int x = stdIn.nextInt();

        System.out.println(x +"의 팩토리얼은 " + factorial(x) + "입니다.");
    }//main
}
```

### 팩토리얼의 재귀적 정의

```
1. 0! = 1
2. n > 0이면 n! = n * (n-1)!
```

```java
import java.util.Scanner;

//팩토리얼을 재귀적으로 구현

public class Factorial {
    //양의 정수 n의 팩토리얼 반환
    static int factorial(int n) {
        if (n > 0){
            return n * factorial(n - 1);
        } else {
            return 1;
        }
    }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("정수 입력 : ");
        int x = stdIn.nextInt();

        System.out.println(x +"의 팩토리얼은 " + factorial(x) + "입니다.");
    }//main
}
```

- 직접 재귀와 간접 재귀
  - 직접재귀 : 자신과 같은 메서드를 다시 부르는 것. A가 A를 부름
  - 간접재귀 : 다른 메서드를 이용해 다시 원래 메서드를 부르는 것. A->B, B->A

## 유클리드 호제법 - 최대공약수 구하기

> 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), 
> a와 b의 최대공약수는 b와 r의 최대공약수와 같다. 
> 이 성질에 따라, b를 r로 나눈 나머지 r'를 구하고, 다시 r을 r'로 나눈 나머지를 구하는 과정을 반복하여 
> 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.

```java
import java.util.Scanner;

//유클리드 호제법으로 최대 공약수 구하기

public class EuclidGCD {
    //정수 x, y의 최대 공약수를 구하여 반환
    static int gcd(int x, int y){
        if( y == 0){
            return x;
        } else {
            return gcd(y, x % y);
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("두 정수의 최대공약수를 구합니다.");

        System.out.println("정수를 입력하세요 : "); int x = stdIn.nextInt();
        System.out.println("정수를 입력하세요 : "); int y = stdIn.nextInt();

        System.out.println("최대 공약수는 " + gcd(x, y));
    }//main
}
```

## 배열에 있는 모든 요소의 최대공약수 구하기

```java
import java.util.Scanner;

//배열의 모든 요소의 최대공약수를 구하기

public class GCDArray {

    //정수 x, y의 최대 공약수를 비재귀적으로 구하여 반환
    static int gcd(int x, int y){
        while (y!=0){
            int temp = y;
            y = x % y;
            x = temp;
        }
        return (x);
    }

    //n크기의 배열 a가 가진 모든 요소의 최대공약수
    static int gcdArray(int a[], int start, int no){
        if (no == 1) {
            return a[start];
        } else if (no == 2){
            return gcd(a[start], a[start + 1]);
        } else {
            return gcd(a[start], gcdArray(a, start + 1, no - 1));
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.println("정수 몇 개의 최대 공약수를 구할까요?");
        int num;
        do {
            num = stdIn.nextInt();
        } while( num <= 1);

        int[] x = new int[num]; //길이 num인 배열

        for(int i = 0; i < num; i++){
            System.out.println("x[" + i + "]:");
            x[i] = stdIn.nextInt();
        }

        System.out.println("최대 공약수는 " + gcdArray(x, 0, num));
    }//main
}
```

