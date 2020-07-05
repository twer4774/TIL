# MaxOfArray(배열 요소에서 최댓값 구하기)

```java
import java.util.Scanner;

public class MaxOfArray {
    static int maxOfArray(int[] arr){
        int max = arr[0]; //배열의 첫번째 요소를 max로 지정
        for ( int i = 1; i < arr.length; i++){
            if (arr[i] > max){
                max = arr[i];
            }
        }

        return max;
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이 : ");
        int len = stdIn.nextInt();

        int[] intArr = new int[len]; //배열의 길이 지정

        for (int i = 0; i < len; i++){
            System.out.println("intArr[" + i + "] :");
            intArr[i] = stdIn.nextInt();
        }

        System.out.println("최댓값은 " + maxOfArray(intArr));
    }//main
}
```

```
//결과
배열의 길이 : 
3
intArr[0] :
1
intArr[1] :
4
intArr[2] :
2
최댓값은 4
```

