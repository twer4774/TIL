# Heap Sort

선택 정렬을 응용한 알고리즘

- 부모의 값은 항상 자식의 값보다 크다는 특징을 가진 완전이진트리

  - 완전이진트리

    - 부모는 자식을 왼쪽으로 부터 추가 가능하며 최대 2개의 자식을 가짐

  - 힙의 특징

    - 부모는 자식보다 크다 or 작다라는 일정한 관계를 갖는다
    - root 노드(가장 큰 부모)가 가장 큰 값
    - 형제관계의 대소관계는 없다 => 부분순서트리 라고 불리는 이유

  - 인덱스 값 찾기

    - 부모 = arr[(i-1) / 2] 
    - 왼쪽자식 = arr[i * 2 + 1]
    - 오른쪽자식 = arr[i * 2 + 2]

    ex) arr[3]의 부모값은 arr[1], 자식들은 arr[7], arr[8]

## 루트를 없애고 힙 유지

1. 루트를 없앤 후 마지막요소를 루트로 보냄. 이때, 나머지 요소들은 힙상태를 유지한다.
2. 마지막 요소의 적절한 위치를 찾기 시작. 부모 >= 자식 특성 이용
3. 비교하는 값들 중 가장 큰 값이 부모가 됨 => 완전이진트리이므로 찾는값을 포함해 총 3개의 대소관계비교
4. 주의점 - 초기 상태의 배열이 힙상태가 아닐 수도 있다 => 힙상태로 먼저 만들어줘야 함



## 코드

```java
import java.util.Scanner;

//힙 정렬

public class HeapSort {
    //Swap
    static void swap(int[] arr, int idx1, int idx2){
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }

    //arr[left] ~ arr[right]를 힙으로 만듦
    static void downHeap(int[] arr, int left, int right) {
        int temp = arr[left]; //루트의 값
        int parent;           //부모
        int child;            //비교하는 자식들 중(왼쪽자식, 오른쪽자식) 큰 값을 가지는 자식 저장

        for(parent = left; parent < (right + 1) / 2; parent = child){
            int leftChild = parent * 2 + 1;
            int rightChild = parent * 2 + 2;
            child = (rightChild <= right && arr[rightChild] > arr[leftChild]) ? rightChild : leftChild; //큰 값을 가지는 자식 저장
            
            //temp가 arr[child]값 보다 크면 for문 종료 => 루트값이 젤일 큰 값이므로 힙으로 만들 필요 없음
            if(temp >= arr[child]){
                break;
            }
            arr[parent] = arr[child]; //parent 위치에 child의 값 저장
        } //for
        arr[parent] = temp; //parent위치에 temp값 저장
    }
    
    //힙 정렬
    static void heapSort(int[] arr, int n){
        for (int i = (n - 1) / 2; i >= 0; i--) { //arr[i] ~ arr[n-1]을 힙으로 만들기
            downHeap(arr, i, n-1);
        }
        
        for(int i = n - 1; i > 0; i--){
            swap(arr, 0, i); //가장 큰 요소와 아직 정렬되지 않은 부분의 마지막 요소를 교혼
            downHeap(arr, 0, i - 1); //arr[0] ~ arr[i-1]을 힙으로 만듦
        }
    }
    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("힙 정렬 요소수: ");
        int nx = stdIn.nextInt();
        int[] x = new int[nx];

        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "]: ");
            x[i] = stdIn.nextInt();
        }

        heapSort(x, nx);

        System.out.println("오름차순으로 정렬");
        for (int i = 0; i < nx; i++) {
            System.out.println("x[" + i + "]=" + x[i]);
        }
    }//main
}
```



## 힙정렬의 시간복잡도

- 선택정렬을 응용한 알고리즘으로 선택정렬의 시간복잡도와 비교함
- 힙의 특성상 첫요소가 가장 큰 값이므로, 첫요소를 꺼내면 가장 큰 값이다 => O(n)
- 단, 요소를 꺼낸 후 힙으로 만들어야 하므로 힙을 만드는 시간복잡도 O(log n)필요

=> 단순선택정렬의 시간 복잡도 O(n^2)

==> 힙정렬의 시간복잡도 O(n log n)으로 크게 감소함

