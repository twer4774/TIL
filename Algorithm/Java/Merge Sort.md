# Merge Sort(병합정렬)

- 정렬을 마친 배열의 병합을 이용하여 분할 정복법에 따라 정렬하는 알고리즘
- 배열을 중간에 위치한 요소를 기준으로 앞부분과 뒷부분으로 나누어 각각 병합정렬을 하여 최종적으로 병합하는 정렬

## 정렬을 마친 배열의 병합

Arr = [2, 4, 6, 8, 11, 13, 1, 2, 3, 4, 9 , 16, 21]

​	A = [2, 4, 6, 8, 11, 13]

​	B = [1, 2, 3, 4, 9 , 16, 21]

​	C = [1, 2, 2, 3, 4, 4, 6, 8, 9, 11, 13, 16, 21]

요소의 인덱스(cursor)를 pa, pb, pc 로 명명하며, 초깃값은 0

cursor가 A or B의 끝에 다다르면 작업 종료

```java
import java.util.Scanner;

//정렬을 마친 배열의 병합(병합정렬의 뼈대)

public class MergeArray {
    //정렬을 마친 배열 a,b를 병합하여 c에 저장
    static void merge(int[] a, int na, int[] b, int nb, int[] c){
        int pa = 0;
        int pb = 0;
        int pc = 0;

        //작은 값 저장
        while (pa < na && pb < nb) {
            c[pc++] = (a[pa] <= b[pb]) ? a[pa++] : b[pb++];
        }

        //a에 남아 있는 요소를 복사
        while (pa < na) {
            c[pc++] = a[pa++];
        }

        //b에 남아 있는 요소를 복사
        while (pb < nb){
            c[pc++] = b[pb++];
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int[] a = {2, 4, 6, 7, 11, 13};
        int[] b = {1, 2, 3, 4, 9, 16, 21};
        int[] c = new int[13];

        System.out.println("두 배열의 병합");

        merge(a, a.length, b, b.length, c);

        System.out.println("배열 a: ");
        for (int i = 0; i < a.length; i++) {
            System.out.println("a[" + i + "] = " + a[i]);
        }

        System.out.println("배열 b: ");
        for (int i = 0; i < b.length; i++) {
            System.out.println("b[" + i + "] = " + b[i]);
        }

        System.out.println("배열 c: ");
        for (int i = 0; i < c.length; i++) {
            System.out.println("c[" + i + "] = " + c[i]);
        }
    }//main
}
```

- 병합에 필요한 시간 복잡도는 O(n)

## 병합 정렬

병합정렬 알고리즘

> 요소가 2개 이상인 경우
>
> 1. 배열의 앞 부분을 병합정렬로 정렬
> 2. 배열의 뒷 부분을 병합정렬로 정렬
> 3. 배열의 앞부분과 뒷부분을 병합

```java
import java.util.Scanner;

//병합정렬

public class MergeArray {
    //정렬을 마친 배열 a,b를 병합하여 c에 저장
    static void merge(int[] a, int na, int[] b, int nb, int[] c){
        int pa = 0;
        int pb = 0;
        int pc = 0;package chap06;
import java.util.Scanner;

//병합 정렬

public class MergeSort {

    static int[] buff; //작업용 배열

    //arr[left] ~ arr[right]를 재귀적으로 병합 정렬 - left가 right보다 작을때 동
    static void __mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int i;
            int center = (left + right) / 2;
            int p = 0;
            int j = 0;
            int k = left;

            __mergeSort(arr, left, center); //배열의 앞 부분을 병합정렬
            __mergeSort(arr, center + 1, right); //배열의 뒷 부분을 병합정렬

            //배열의 앞부분을 buff에 복사
            for (i = left; i <= center; i++) {
                buff[p++] = arr[i];
            }
            
            //배열의 뒷부분을 buff로 복사한 배열의 앞부분과 병합한 결과를 배열 a에 저장(배열의 뒷부분과 buff(앞부분)을 병합정렬함)
            while (i <= right && j < p) {
                arr[k++] = (buff[j] <= arr[i]) ? buff[j++] : arr[i++];
            }
            //buff에 남아 있는 요소를 배열 a에 복사
            while (j < p) {
                arr[k++] = buff[j++];
            }
            
        }
    }
    
    //병합 정렬
    static void mergeSort(int[] arr, int n) {
        buff = new int[n]; //작업용 배열 생성
        
        __mergeSort(arr, 0, n - 1); //배열 전체를 병합 정렬
        
        buff = null; //작업용 배열 해제
    }
    
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("병합정렬 요소수 :");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }
        
        mergeSort(x, nx); //배열 x를 병합 정렬함

        System.out.println("오름차순으로 정렬");
        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}


        //작은 값 저장
        while (pa < na && pb < nb) {
            c[pc++] = (a[pa] <= b[pb]) ? a[pa++] : b[pb++];
        }

        //a에 남아 있는 요소를 복사
        while (pa < na) {
            c[pc++] = a[pa++];
        }

        //b에 남아 있는 요소를 복사
        while (pb < nb){
            c[pc++] = b[pb++];
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        int[] a = {2, 4, 6, 7, 11, 13};
        int[] b = {1, 2, 3, 4, 9, 16, 21};
        int[] c = new int[13];

        System.out.println("두 배열의 병합");

        merge(a, a.length, b, b.length, c);

        System.out.println("배열 a: ");
        for (int i = 0; i < a.length; i++) {
            System.out.println("a[" + i + "] = " + a[i]);
        }

        System.out.println("배열 b: ");
        for (int i = 0; i < b.length; i++) {
            System.out.println("b[" + i + "] = " + b[i]);
        }

        System.out.println("배열 c: ");
        for (int i = 0; i < c.length; i++) {
            System.out.println("c[" + i + "] = " + c[i]);
        }
    }//main
}
```

- 배열 병합의 시간복잡도는 O(n), 전체 알고리즘의 시간복잡도는 O(n log n)
- 병합정렬은 서로 떨어져 있는 요소를 교환하는 것이 아니므로 안정적인 정렬방법이라 할 수 있다.