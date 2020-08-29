# BFS

- Breadth First Search
- 기존노드(루트노드 or 임의의 노드)에서 시작해 인접노드를 모두 탐색하는 방법
- 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을때 이용
- 재귀적으로 동작하지 않음
- 노드의 방문여부를 반드시 검사(무한루프 방지)
- Queue를 이용하여 방문한 노드들을 차례로 저장하고 꺼낼 수 있음

### 구현

```
															1
														 / \
														4   5
                           /     \
                          3       2
```

위의 순서대로 BFS 실행

결과값 : 1, 4, 5, 3, 2

```java
package com.company;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class StudyBFS {

    static int Vn; //정점의 수
    static int En; //간선의 수
    static int[][] graph; //그래프 저장
    static boolean[] visit;
    
    
    public static void bfs(int start){
        Queue<Integer> que = new LinkedList<Integer>();
        
        visit[start] = true;
        que.offer(start); //시작점을 집어 넣는다.
        
        //que가 빌때까지 실행 - 큐가 비었으면 검색 종료
        while(!que.isEmpty()){
            int x = que.poll();
            System.out.print(x + " ");

            for (int i = 1; i < graph.length ; i++) {
                if (graph[x][i] == 1 && visit[i] == false) {
                    que.offer(i); //방문하지 않았으면 que에 i의 값 저장
                    visit[i] = true; //방문했음을 표시
                }

            }
        }
        
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Vn = 5;
        En = 4;
        graph = new int[Vn+1][Vn+1];
        visit = new boolean[Vn+1];

        
        /*//간선 연결
        for (int i = 0; i < En; i++) {
         int t1, t2;
         t1 = scan.nextInt();
         t2 = scan.nextInt();
         
         graph[t1][t2] = graph[t2][t1] = 1;
        }*/

        graph[1][4] = graph[4][1] = 1;
        graph[1][5] = graph[5][1] = 1;
        graph[3][4] = graph[4][3] = 1;
        graph[5][2] = graph[2][5] = 1;

        //기댓값 : 1, 4, 5, 3, 2

        bfs(1);
    }    
}

```

