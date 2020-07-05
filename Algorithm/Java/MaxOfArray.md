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

- 난수로 설정된 배열에서 최댓값 찾기

```java
import java.util.Random;
import java.util.Scanner;

//배열 요소의 최댓값을 나타냄(값은 난수로 생성)

public class MaxOfArrayRand {
    static int maxOfArr(int[] arr){
        int max = arr[0];
        for (int i = 1; i < arr.length; i++){
            if (arr[i] > max)
                max = arr[i];
        }

        return max;
    }
    public static void main(String[] args) {
        Random rand = new Random(); //난수 변수 선언
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이 : ");
        int len = stdIn.nextInt();

        int[] intArr = new int[len];

        for (int i = 0; i < len; i++){
            intArr[i] = 100 + rand.nextInt(90); //요소의 값을 난수로 설정
            System.out.println("intArr[" + i + "] = " + intArr[i]);
        }

        System.out.println("최댓값은 " + maxOfArr(intArr));
    }//main
}
```

```java
//결과
배열의 길이 : 
3
intArr[0] = 187
intArr[1] = 157
intArr[2] = 166
최댓값은 187
```

