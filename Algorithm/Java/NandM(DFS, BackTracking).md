# N and M (DFS, BackTracking)

> ## 문제
>
> 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
>
> - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
>
> ## 입력
>
> 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
>
> ## 출력
>
> 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
>
> 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
>
> 
>
> ## 예제 입력 1 복사
>
> ```
> 3 1
> ```
>
> ## 예제 출력 1 복사
>
> ```
> 1
> 2
> 3
> ```
>
> ## 예제 입력 2 복사
>
> ```
> 4 2
> ```
>
> ## 예제 출력 2 복사
>
> ```
> 1 2
> 1 3
> 1 4
> 2 1
> 2 3
> 2 4
> 3 1
> 3 2
> 3 4
> 4 1
> 4 2
> 4 3
> ```
>
> ## 예제 입력 3 복사
>
> ```
> 4 4
> ```
>
> ## 예제 출력 3 복사
>
> ```
> 1 2 3 4
> 1 2 4 3
> 1 3 2 4
> 1 3 4 2
> 1 4 2 3
> 1 4 3 2
> 2 1 3 4
> 2 1 4 3
> 2 3 1 4
> 2 3 4 1
> 2 4 1 3
> 2 4 3 1
> 3 1 2 4
> 3 1 4 2
> 3 2 1 4
> 3 2 4 1
> 3 4 1 2
> 3 4 2 1
> 4 1 2 3
> 4 1 3 2
> 4 2 1 3
> 4 2 3 1
> 4 3 1 2
> 4 3 2 1
> ```
>
> 
>
> ## 출처
>
> - 문제를 만든 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
>
> ## 알고리즘 분류
>
> - [백트래킹](https://www.acmicpc.net/problem/tag/5)

## 풀이

```java
package com.company;

/**
 * 문제
 * 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
 *
 * 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
 * 입력
 * 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
 *
 * 출력
 * 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
 *
 * 수열은 사전 순으로 증가하는 순서로 출력해야 한다.
 */

import java.util.Scanner;

public class NandM {
    private static boolean[] visit; //중복되는 방문을 피하기 위함
    private static int[] result; //결과 값들 저장

    /**
     *
     * @param pos 노드의 위치
     * @param N 1부터 N까지 표시할 자연수 N
     * @param M 수열의 길이
     */
    public static void dfs(int pos, int N, int M) {

        // 노드의 위치가 M과 같아지면 결과 출력
        if (pos == M) {
            for (int i : result) {
                System.out.print(i + " ");
            }
            System.out.println();
            return; //재귀함수이므로 리턴값을 넣어야 올바르게 끝남
        }

        for (int i = 1; i <= N; i++) {

            // 노드를 방문했는지 확인 true:방문 / false:방문전
            if (visit[i] == false) {

                visit[i] = true;
                result[pos] = i; //노드에 해당하는 배열값에 i 저장
                dfs(pos+1, N, M);    // 재귀호출

                // 자식노드 방문이 끝나고 돌아오면(백트래킹) 방문노드를 방문하지 않은 상태로 변경
                visit[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int M = scan.nextInt();

        visit = new boolean[N+1];
        result = new int[M];

        dfs(0, N, M);
    }
}

```

