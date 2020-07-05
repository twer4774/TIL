# Revers Array(배열의 역순 정렬)

- 입력받은 배열을 역순으로 정렬하여 출력함

```java
import java.util.Scanner;

//배열을 읽어들여 역순으로 정렬

public class ReverseArray {
    //swap
    static void swap(int[] arr, int idx1, int idx2){
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

    //reverse 역순 정렬
    static void reverse(int[] arr){
      //배열 길이의 반을 정렬하면 나머지도 정렬되므로 arr.lenght/2
        for (int i = 0; i < arr.length / 2; i++){
          //swap 메서드 호출
            swap(arr, i, arr.length - i - 1);
        }
    }
  
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이: ");
        int num = stdIn.nextInt();

        int[] x = new int[num];

        for(int i = 0; i < num; i++){
            System.out.println("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        //배열을 역순으로 정렬
        reverse(x);

        System.out.println("요소를 역순으로 정렬했습니다.");
        for(int i = 0; i < num; i++){
            System.out.println("x[" + i + "] = " + x[i]);
        }
    }//main
}
```

```
//결과
배열의 길이: 
3
x[0] : 
2
x[1] : 
1
x[2] : 
4
요소를 역순으로 정렬했습니다.
x[0] = 4
x[1] = 1
x[2] = 2
```

