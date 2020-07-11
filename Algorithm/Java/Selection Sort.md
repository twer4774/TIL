# Selection Sort(선택 정렬)

## Straight Selection sort(단순 선택 정렬)

- 가장 작은 요소부터 정렬하는 알고리즘

- 떨어져 있는 요소들의 값이 뒤바뀌어 안정적이지 않음 => 단순 삽입 정렬로 보완

  [6, 4, 8, 3, 1, 9, 7]

  | 6    | 4    | 8    | 3    | 1    | 9    | 7    |
  | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
  | 1    | 4    | 8    | 3    | 6    | 9    | 7    |
  | 1    | 3    | 8    | 4    | 6    | 9    | 7    |
  | 1    | 3    | 4    | 8    | 6    | 9    | 7    |
  | 1    | 3    | 4    | 6    | 8    | 9    | 7    |
  | 1    | 3    | 4    | 6    | 7    | 9    | 8    |
  | 1    | 3    | 4    | 6    | 7    | 8    | 9    |

```java
//단순 선택 정렬
static void selectionSort(int[] arr, int n){
  for( int i = 0; i < n-1; i++){
    int min = i; //아직 정렬되지 않은 부분에서 가장 작은 요소의 인덱스를 기록
    for(int j = i + 1; j < n; j++){
      if(arr[j] < a[min]){
        min = j;
      }
    swap(arr, i, min); //아직 정렬되지 않은 부분의 첫 요소와 가장 작은 요소를 교환
    }
  }
}
```



## Straight insertion sort(단순 삽입 정렬)

- 선택한 요소를 그보다 더 앞쪽의 알맞은 위치에 삽입하는 작업을 반복
- 단순 선택 정렬과의 차이 : 단순선택은 가장 작은 요소를 선택

### 단순 삽입 정렬

| 6    | 4    | 1    | 7    | 3    | 9    | 8    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 4    | 6    | 1    | 7    | 3    | 9    | 8    |
| 1    | 4    | 6    | 7    | 3    | 9    | 8    |
| 1    | 3    | 4    | 6    | 7    | 9    | 8    |
| 1    | 3    | 4    | 6    | 7    | 8    | 9    |

- 2번째 요소(4)부터 선택하여 진행
- 4는 6보다 앞으로 가야하므로, 앞쪽에 '삽입' 후 6을 오른쪽으로 밂
- 정렬되지 않은 부분에서 배열을 다시 구성 n-1회 반복
- 삽입에 대하여
  - Java언어에는 삽입에 관한 명령은 없음
  - 이웃한 값의 대소 관계를 파악하여 선택한 키 값이 왼쪽의 값 보다 작다면, 이동해야 하므로 밀어내야함
  - 다음의 조건 중 하나가 만족해야한다.
    1. 정렬된 열의 왼쪽 끝에 도달
    2. tmp보다 작거나 같은 Key를 갖는 항목 arr[j]를 발견

```java
import java.util.Scanner;


//단순 삽입 정렬
public class InsertionSort {
    
    //단순 삽입 정렬
    static void insertionSort(int[] arr, int n){
        for(int i = 1; i < n; i++){
            int j;
            int tmp = arr[i];
            for(j = i; j > 0 && arr[j - 1] > tmp; j--){
                arr[j] = arr[j - 1];
            }
            arr[j] = tmp;
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.println("단순 삽입 정렬 배열수:");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];
        
        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "] :");
            x[i] =stdIn.nextInt();
        }
        
        insertionSort(x, nx); //배열 x를 단순 삽입 정렬

        System.out.println("오름차순으로 정렬");
        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```

- 단순 삽입 정렬 알고리즘의 장점
  - 떨어져 있는 요소들이 서로 뒤바뀌지 않아 안정적

## 단순 정렬의 복잡도

버블, 선택, 삽입의  시간복잡도는 O(n^2)



## 단순 삽입 정렬 개선법 - 보초법(Sentinel  method) 이용

- 단순 삽입 정렬에서 arr[0]부터 데이터를 저장하지 않고 arr[1]부터 데이터를 저장하면 arr[0]을 보초로 삽입하여 삽입을 마치는 조건을 줄일 수 있다.

```java
import java.util.Scanner;

public class InsertionSortWithSentinel {

    //단순삽입정렬(보초법: 배열의 머리요소는 비어있음)
    static void insertionSort(int[] arr, int n){
        for(int i = 2; i < n; i++){
            int tmp = arr[0] = arr[i]; //arr[0]을 보초로 세움. 보초
            int j = i;
            for(; arr[j - 1] > tmp; j--){
                arr[j] = arr[j-1];
            }
            if(j > 0){
                arr[j] = tmp;
            }
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);
        System.out.println("단순 삽입 정렬 배열수:");
        int nx = stdIn.nextInt();
        int[] x = new int[nx + 1]; //보초를 세워야하므로 1개의 공간 추가 

        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "] :");
            x[i] =stdIn.nextInt();
        }

        insertionSort(x, nx); //배열 x를 단순 삽입 정렬

        System.out.println("오름차순으로 정렬");
        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```



## 단순 삽입 정렬 개선 - 이진 검색 이용

- 단순 삽입 정렬은 배열의 요소수가 많아지면 삽입에 필요한 비교, 대입 비용이 커짐
- 이때 배열에서 이미 정렬된 부분은 이진 검색을 사용할 수 있기 때문에 삽입할 위치를 더 빨리 찾을 수 있음
- 단, 안정적이지는 않음

```java
import java.util.Scanner;


//이진 삽입 정렬
public class InsertionSortWithBinarySearch {
    
    static void binInsertionSort(int[] arr, int n){
        for (int i = 1; i < n; i++){
            int key = arr[i];
            int pl = 0; //검색 범위의 맨 앞 인덱스
            int pr = i - 1; //검색범위의 맨 뒤 인덱스
            int pc; // 중앙의 인덱스
            int pd; //삽입하는 위치의 인덱스
            
            do{
                pc = (pl + pr) / 2;
                if( arr[pc] == key) //검색성공
                    break;
                else if(arr[pc] < key)
                    pl = pc + 1;
                else
                    pr = pc - 1;
            }while(pl <= pr);
            pd = (pl <= pr) ? pc + 1 : pr + 1;
            
            for(int j = i; j > pd; j--){
                arr[j] = arr[j-1];
            }
            arr[pd] = key;
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("이진 삽입 정렬 요소수: ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];
        
        for(int i = 0; i < nx; i++){
            System.out.println("x[" + i + "]:");
            x[i] = stdIn.nextInt();
        }
        
        binInsertionSort(x, nx);
        System.out.println("오름차순으로 정렬했습니다.");
        for (int i = 0; i < nx; i++)
            System.out.println("x[" + i + "]＝" + x[i]);
    }//main
}
```

