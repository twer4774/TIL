# Star Piramid

```java
import java.util.Scanner;

public class StarPiramid {
    static void pira(int n){
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n-i+1; j++){ //n-i+1개의 공백
                System.out.print(' ');
            }
            for (int j = 1; j <= (i-1)*2+1; j++){ //(i-1)*2+1개의 *
                System.out.print('*');
            }
            System.out.println(); //개행
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        int n;

        do{
            System.out.println("몇단짜리? ");
            n = stdIn.nextInt();
        } while( n <= 0);

        pira(n);
    }//main
}
```

