# Bubble Sort(버블정렬)

이웃한 두 요소의 대소 관계를 비교하여 교환을 반복

- 오름 차순으로 정렬하는 경우
  - 오른쪽 끝에 있는 값부터 시작

| 6    | 4    | 3    | 7    | 1    | 9    | 8    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 6    | 4    | 3    | 7    | 1    | 8    | 9    |
| 6    | 4    | 3    | 1    | 7    | 8    | 9    |
| 6    | 4    | 1    | 3    | 7    | 8    | 9    |
| 6    | 1    | 4    | 3    | 7    | 8    | 9    |
| 1    | 6    | 4    | 3    | 7    | 8    | 9    |

- 첫 번째 패스 정렬
- 요소의 개수가 n개인 배열에서 n-1회 비교, 교환을 하고 나면 가장 작은요소가 맨 처음으로 이동함

| 1    | 6    | 4    | 3    | 7    | 8    | 9    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 6    | 3    | 4    | 7    | 8    | 9    |
| 1    | 3    | 6    | 4    | 7    | 8    | 9    |

- 두 번째 패스 정렬. n-2회 비교, 교환
- 패스를 K회 수행하면 앞쪽의 요소 K개가 정렬됨 => 모든 정렬이 끝나려면 n - 1회의 패스가 수행되어야 함

## 정렬 프로그램

```java
import java.util.Scanner;

//Bubble Sorting(Version 1)

public class BubbleSort {

    //swap
    static void swap(int[] arr, int idx1, int idx2){
        int t = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = t;
    }

    //Buble Sorting
    static void bubbleSort(int[] arr, int n){
        for (int i = 0; i < n - 1; i++){
            for(int j = n - 1; j > i; j--){
                if(arr[j - 1] > arr[j]){
                    swap(arr, j - 1, j);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이: ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "] : ");
            x[i] = stdIn.nextInt();
        }

        bubbleSort(x, nx); //배열 x를 버블 정렬

        System.out.println("오름차순으로 정렬");
        for( int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```

## 알고리즘 개선

- 정렬을 하다 보면 이전 패스에서 이미 정렬이 되어 해당 패스에서는 교환이 이루어지지 않는 부분들이 존재
- 교환할 요소가 없다 == 정렬이 완료되었다. (다음 요소를 비교하여 정렬할 필요가 없다) ==> 교환하는 요소가 없으면 멈춘다
- ===> 어느 시점부터 교환이 이루어지지 않았다면, 그보다 앞쪽의 요소는 이미 정렬을 마친상태라고 생각해도 됨

```java
static void bubbleSort(int[] arr, int n){
        int k  = 0; //a[k]보다 앞쪽은 정렬을 마친 상태. 0으로 초기화하는 이유: 첫 번째 패스는 무조건 모든요소 검사
        while (k < n - 1){
            int last = n - 1; //마지막으로 요소를 교환한 위치
            for (int j = n - 1; j > k; j--){
                if (arr[j - 1] > arr[j]){
                    swap(arr, j - 1, j);
                    last = j;
                }
                k = last;
            }
        }
    }
```

- last는 각 패스에서 마지막으로 교환한 두 요소 가운데 오른쪽 요소의 인덱스를 저장하는 변수. 교환수행시 오른쪽 요소의 값을 last에 저장 - 패스를 마치고 last값을 k에 저장하여 수행할 패스의 범위를 제한함
- => 다음 패스에서 마지막으로 비교할 두 요소는 a[k]와 a[k+1]이 됨
- 이때 메서드의 시작부분에서 k값을 0으로 초기화 : 첫 번째 패스에서는 모든 요소를 검사해야 하기 때문

## 양방향 버블정렬(bidirection bubble) or 칵테일 정렬(cocktail) or 셰이커 정렬(shaker)

[9 , 1, 3, 4, 6, 7, 8]을 정렬할 때

- 한쪽으로만 버블정렬을 수행하면 많은 패스를 통과해야 함(9가 제일 오른쪽으로 가야하므로)
- 홀수 번째는 가장 작은 요소를 맨 앞으로 옮기고, 짝수 번째는 가장 큰 요소를 맨 뒤로 옮기면 적은 횟수로 정렬가능(양방향 버블)

```java
import java.util.Scanner;

//양방향 버블, 쉐이커, 칵테일

public class ShakerSort {

    //배열의 요소 arr[iix1]과 arr[idx2]를 교환
    static void swap(int[] arr, int idx1, int idx2){
        int t = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = t;
    }

    //양방향 버블정렬
    static void shakerSort(int[] arr, int n){
        int left = 0;
        int right = n - 1;
        int last = right;

        while (left < right){
            //패스 한번에 정렬을 두개 넣음로
            //홀수번째는 가장 작은 요소를 맨앞으로
            for(int j = right; j > left; j--){
                if(arr[j - 1] > arr[j]){
                    swap(arr, j - 1, j);
                    last = j;
                }
            }
            left = last;
            
            //짝수번째는 가장 큰 요소를 맨 뒤로
            for (int j = left; j < right; j++) {
                if (arr[j] > arr[j + 1]) {
                    swap(arr, j, j+1);
                    last = j;
                }
            }
            right = last;
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("쉐이커 정렬의 배열 수 : ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]:");
            x[i] = stdIn.nextInt();
        }

        shakerSort(x, nx);

        System.out.println("오름차순 정렬");
        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```

