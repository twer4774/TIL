# Combination - 조합

- n개의 숫자 중에서 r개의 수를 순서없이 뽑는 경우

- 중복을 허용하지 않음
- {1, 2, 3}의 배열에서 2개의 수를 순서 없이 뽑으면
  - {1, 2}, {1, 3}, {2, 1}, {2, 3}, {3, 1}, {3, 2}가 나옴
  - 이때, 중복되는 순서를 제거하면 {1, 2}, {1, 3}, {2, 1}이 나옴
- 핵심
  - 배열을 처음부터 마지막까지 돌며
    - 현재 인덱스를 선택하는 경우
    - 현재 인덱스를 선택하지 않는 경우
    - 위의 두가지로 완전 탐색 실시

## 구현

- 백트래킹 이용방법(선호)
- 재귀를 이용하는방법

```java
//조합
public class Combination {

    public static void main(String[] args) {
         int[] arr= {1,2,3};
         int n = arr.length;
         boolean[] visit = new boolean[n];

         //백트래킹 이용
        for (int i = 0; i <= n; i++) {
            combinationBT(arr, visit, 0, n, i);
        }

        System.out.println();

        //재귀 이용
        for (int i = 0; i <= n ; i++) {
            combinationRC(arr, visit, 0, n, i);
        }
    }



    //백트래킹 사용
    /**
     *
     * @param arr 조합을 뽑아낼 배열
     * @param visit 방문했는지 여부
     * @param start 시작 위치. start 보다 작으면 후보에서 제외, 크면 뽑을 후
     * @param n 배열의 길이
     * @param r 조합의 길이
     * */
    private static void combinationBT(int[] arr, boolean[] visit, int start, int n, int r){

        if(r == 0){
            print(arr, visit, n);
            return;
        }

        for (int i = start; i < n; i++) {
            //인덱스 0의 값 1을 뽑으면 visit[i]는 true
            visit[i] = true;

            //조합의 길이 r을 1씩 줄이면서 백트래킹
           combinationBT(arr, visit, i+1, n, r-1);

            //백트래킹을 하면(자식노드 방문이 끝나고 돌아오면) 방문 노드를 방문하지 않은 상태로 변경함
            visit[i] = false;
        }
    }

    //재귀이용

    /**
     *
     * @param arr
     * @param visit
     * @param depth
     * @param n
     * @param r
     */
    private static void combinationRC(int[] arr, boolean[] visit, int depth, int n, int r) {
        if( r == 0){
            print(arr, visit, n);
            return;
        }

        if(depth == n){
            return;
        }
        visit[depth] = true;
        combinationRC(arr, visit, depth+1, n, r-1);

        visit[depth] = false;
        combinationRC(arr, visit, depth+1,n, r);
    }

    //배열 출력
    private static void print(int[] arr, boolean[] visit, int n) {
        for (int i = 0; i < n; i++) {
            if(visit[i] == true){
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }

}
```

- 결과

```java
1 
2 
3 
1 2 
1 3 
2 3 
1 2 3 


1 
2 
3 
1 2 
1 3 
2 3 
1 2 3 
```

