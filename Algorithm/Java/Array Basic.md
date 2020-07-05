# Array

- 같은 자료형의 변수로 이루어진 구성요소의 모임

- ```java
  int[] a;
  a = new int[5]; //길이가 5인 정수 배열
  a.length //5
  ```

- 기본

```java
//구성 요소의 자료형이 int형인 배열

public class IntArray {
    public static void main(String[] args) {
        int[] a = new int[5];

        a[1] = 37;
        a[2] = 51;
        a[4] = a[1] * 2;

        for (int i = 0; i < a.length; i++){
            System.out.println("a["+ i +"] = " + a[i]);
        }
    }//main
}
```

```java
//결과
a[0] = 0
a[1] = 37
a[2] = 51
a[3] = 0
a[4] = 74
```

- 배열 선인 및 초기화

```java
public class IntArrayInit {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};

        for (int i = 0; i < a.length; i++){
            System.out.println("a[" + i + "] = " + a[i]);
        }
    }//main
}
```

- 배열의 복제(클론)

```java
public class CloneArray {
    public static void main(String[] args) {
        int[] a = {1, 2, 3, 4, 5};
        int[] b = a.clone(); //b는 a의 복제를 참조한다.

        b[3] = 0; //b의 3번째 요소에 0을 대입한다.

        System.out.println("a =");
        for (int i = 0; i < a.length; i++){
            System.out.print(" " + a[i]);
        }

        System.out.println("\nb = ");
        for (int i = 0; i < b.length; i++) {
            System.out.print(" " + b[i]);
        }
    }//main
}
```

```
//결과
a = 1 2 3 4 5
b = 1 2 3 0 5
```

