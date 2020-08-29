# DFS

- Depth First Search
- 모든 정점을 확인할 때 쓰인다.
- 인접행렬과 연결리스트로 구현할 수 있다.
  - 인접행렬 : 정점의 수가 적을 때 유용하게 이용 가능. 수가 많아지면 느려진다.
- BFS보다는 구현하기 편하지만, 속도면에서 느리다

```
											1
											|
								      5
								      |
								      4
								     / \
                    2   3
```

위와 같은 그래프 모양이 있다고 가정하여 진행

결과 값 : 1 5 4 2 3 or 1 5 4 3 2

### 인접행렬

```java
package com.company;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Root Node 혹은 다른 임의의 Node에서 다음 분기(Branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법이다.
 * 경로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게되면 다른 방향으로 다시 탐색을 진행
 * 모든 노드를 방문하는 경우에 이 방법을 사용한다.
 *
 * V : 정점 / E : 간선
 */

//인접행렬(Adjency Matrix) / 인접리스트 이용
public class StudyDFS {
    static int V; //정점
    static int E; //간선
    static boolean[] visit; //방문여부

    static int[][] adj; //인접행렬

    //인접행렬 이용
    public static void dfsAdj(int i){
        visit[i] = true; //함수호출 시, visit했음을 표시
        System.out.print(i + " ");

        for (int j = 1; j < V+1; j++) {
            //j를 방문하지 않았으면 j를 방문한다.
            if(adj[i][j] == 1 && visit[j] == false){
                dfsAdj(j);
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        /* Scanner로 값을 입력받는 부분을 삭제함
        System.out.println("정점의 수 입력 : ");
        V = scan.nextInt(); //정점의 수
        System.out.println("간선의 수 입력 : ");
        E = scan.nextInt(); //간선의 수
         */
      	
      	//위의 그래프와 맞추기 위해 값을 지정
        V = 5;
        E = 4;

        
        //인접행렬 이용
        adj = new int[V+1][V+1];
        visit = new boolean[V+1];


//        for (int i = 0; i < E; i++) {
//            System.out.println("정점끼리 잇기");
//            System.out.println("t1 ["+i+"] 번째");
//            int t1 = scan.nextInt();
//            System.out.println("t2 ["+i+"] 번째");
//            int t2 = scan.nextInt();
//
//            adj[t1][t2] = adj[t2][t1] = 1;
//        }

				//위의 그래프와 맞추기위해 값을 지정
        adj[5][4] = adj[4][5] = 1;
        adj[4][3] = adj[3][4] = 1;
        adj[4][2] = adj[2][4] = 1;
        adj[1][5] = adj[5][1] = 1;
        //기댓값 : 1 5 4 2 3

        dfsAdj(1); //1부터 시작
        //------- 인접행렬 이용
}

```

### 인접리스트

```java
package com.company;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

/**
 * Root Node 혹은 다른 임의의 Node에서 다음 분기(Branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법이다.
 * 경로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게되면 다른 방향으로 다시 탐색을 진행
 * 모든 노드를 방문하는 경우에 이 방법을 사용한다.
 *
 * V : 정점 / E : 간선
 */

//인접행렬(Adjency Matrix) / 인접리스트 이용
public class StudyDFS {
    static int V; //정점
    static int E; //간선
    static boolean[] visit; //방문여부
  
    static ArrayList<ArrayList<Integer>> dfsArray; //인접리스트

    //인접리스트 이용
    public static void dfsList(int i){
        visit[i] = true;

        System.out.print(i + " ");

        for(int j : dfsArray.get(i)) {
            if (visit[j] == false) {
                dfsList(j);
            }
        }
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        /* Scanner로 값을 입력받는 부분을 삭제함
        System.out.println("정점의 수 입력 : ");
        V = scan.nextInt(); //정점의 수
        System.out.println("간선의 수 입력 : ");
        E = scan.nextInt(); //간선의 수
         */
      	
      	//위의 그래프와 맞추기 위해 값을 지정
        V = 5;
        E = 4;

        //인접리스트 이용
        dfsArray = new ArrayList(V+1); //인접리스트 초기화
        visit = new boolean[V+1]; //visit배열 초기화

        //인접 리스트 속의 리스트를 초기화한다.
        for (int i = 0; i < V+1; i++) {
            dfsArray.add(new ArrayList());
        }

//        for(int i = 0; i < E; i++){
//            int t1 = scan.nextInt();;
//            int t2 = scan.nextInt();
//
//            //양방향 그래프이므로 서로의 방향에 저장한다.
//            dfsArray.get(t1).add(t2);
//            dfsArray.get(t2).add(t1);
//        }

        dfsArray.get(5).add(4);
        dfsArray.get(4).add(5);
        dfsArray.get(4).add(3);
        dfsArray.get(3).add(4);
        dfsArray.get(4).add(2);
        dfsArray.get(2).add(4);
        dfsArray.get(1).add(5);
        dfsArray.get(5).add(1);
        //기댓값 : 1 5 4 3 2
        dfsList(1);
        //---인접리스트 이용
    }
}

```

