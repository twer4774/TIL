# Binary Search(이진 검색)

일정한 규칙으로 늘어놓은 데이터 모임에서 아주 빠른 검색 수행 log n의 평균값

- 요소가 오름차순 또는 내림차순 <u>정렬된 배열</u>에서 검색하는 알고리즘

- 검색 방법

  1. 배열의 중앙에 위치한 값과 key값을 비교
  2. 오름차순 기준으로, key값과 중앙값을 비교하여 작으면 왼쪽으로 / 크면 오른쪽으로 이동
  3. 이동한 값들중에서 다시 중앙 값을 찾아 key값과 비교
  4. 위의 과정을 반복

- 한 단계씩 진행할 때 마다 검색범위가 반으로 줄어든다.

  => 검색을 시작할 때 pl은 0 -> 검색범위의 첫 인덱스/ pr은 n-1  -> 검색범위의 끝 인덱스/ pc는 (n-1)/2로 초기화

- 종료조건

  - 배열의 값에 key가 일치하는 경우 - 성공 a[pc] == key  (log n - 1 회)
  - 배열을 더 이상 검색할 수 없을 경우 - 실패 pl이 pr보다 커지면서 검색범위를 더 이상 계산할 수 없음 (long(n+1) 회)

```java
import java.util.Scanner;

//이진 검색

public class BinarySearch {

    static int binarySearch(int[] arr, int n, int key){
        int pl = 0; //검색 범위의 첫 인덱스
        int pr = n - 1; //검색 범위의 마지막 인덱스

        do{
            int pc = (pl + pr) / 2; //중앙 요소의 인덱스
            if(arr[pc] == key){
                return pc; //검색 성공
            } else if (arr[pc] < key) {
                pl = pc + 1; //검색 범위를 뒤쪽 절반으로 좁힘
            } else {
                pr = pc - 1; //검색 범위를 앞쪽 절반으로 좁힘
            }
        }while( pl <= pr );

        return -1; //검색 실패
   }

    public static void main(String[] args) {
        Scanner stdIn = new Scanner(System.in);

        System.out.println("배열의 길이: ");
        int num = stdIn.nextInt();
        int[] arr = new int[num];

        System.out.println("오름차순으로 입력");

        System.out.println("arr[0] : ");
        arr[0] = stdIn.nextInt();

        for (int i = 1; i < num; i++){
            do {
                System.out.println("arr[" + i + "] :");
                arr[i] = stdIn.nextInt();
            } while(arr[i] < arr[i-1]); //바로 앞의 요소보다 작으면 다시 입력(오름차순입력)
        }

        System.out.println("검색할 Key값 : ");
        int key = stdIn.nextInt();

        int idx = binarySearch(arr, num, key); //배열 arr에서 값이 key인 요소 검색

        if (idx == -1){
            System.out.println("값이 없음");
        } else {
            System.out.println(key+ "는 arr[" + idx + "]에 있음");
        }
    }//main
}
```



