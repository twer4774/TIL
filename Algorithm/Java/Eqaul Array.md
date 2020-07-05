# Equal Array(두 배열의 비교)

```java
import java.util.Scanner;

// 두 배열이 같은가를 판단

public class EqualArray {
    // 두 배열 a, b의 모든 요소가 같은가?
    static boolean equals(int[] a, int[] b){
        if(a.length != b.length) return false; //배열의 길이가 다르면 무조건 false

        for(int i = 0; i < a.length; i ++){
            if(a[i] != b[i]) return false; //각 배열의 요소가 다르면 false
        }

        return true;
    }
    public static void main(String[] args) {

        Scanner stdIn = new Scanner(System.in);

        System.out.println("a 배열의 길이:");
        int lenA = stdIn.nextInt();

        int[] a = new int[lenA];

        for (int i = 0; i < lenA; i++){
            System.out.println("a[" + i + "] : ");
            a[i] = stdIn.nextInt();
        }

        System.out.println("b 배열의 길이:");
        int lenB = stdIn.nextInt();

        int[] b = new int[lenB];

        for(int i = 0; i < lenB; i++){
            System.out.println("b[" + i + "] :");
            b[i] = stdIn.nextInt();
        }

        System.out.println("배열 a와 b는 " + (equals(a, b) ? "같습니다" : "같지 않습니다."));

    }//main
}
```

