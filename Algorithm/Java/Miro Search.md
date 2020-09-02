# (Miro Search) 미로탐색

> ## 문제
>
> N×M크기의 배열로 표현되는 미로가 있다.
>
> | 1    | 0    | 1    | 1    | 1    | 1    |
> | ---- | ---- | ---- | ---- | ---- | ---- |
> | 1    | 0    | 1    | 0    | 1    | 0    |
> | 1    | 0    | 1    | 0    | 1    | 1    |
> | 1    | 1    | 1    | 0    | 1    | 1    |
>
> 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
>
> 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
>
> ## 입력
>
> 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 **붙어서** 입력으로 주어진다.
>
> ## 출력
>
> 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
>
> 
>
> ## 예제 입력 1
>
> ```
> 4 6
> 101111
> 101010
> 101011
> 111011
> ```
>
> ## 예제 출력 1
>
> ```
> 15
> ```
>
> ## 예제 입력 2
>
> ```
> 4 6
> 110110
> 110110
> 111111
> 111101
> ```
>
> ## 예제 출력 2
>
> ```
> 9
> ```
>
> ## 예제 입력 3
>
> ```
> 2 25
> 1011101110111011101110111
> 1110111011101110111011101
> ```
>
> ## 예제 출력 3 
>
> ```
> 38
> ```
>
> ## 예제 입력 4 
>
> ```
> 7 7
> 1011111
> 1110001
> 1000001
> 1000001
> 1000001
> 1000001
> 1111111
> ```
>
> ## 예제 출력 4 
>
> ```
> 13
> ```
>
> 
>
> ## 출처
>
> - 데이터를 추가한 사람: [djm03178](https://www.acmicpc.net/user/djm03178) [jh05013](https://www.acmicpc.net/user/jh05013) [poia0304](https://www.acmicpc.net/user/poia0304)
>
> ## 알고리즘 분류
>
> - [그래프 이론](https://www.acmicpc.net/problem/tag/7)
> - [그래프 탐색](https://www.acmicpc.net/problem/tag/11)
> - [너비 우선 탐색](https://www.acmicpc.net/problem/tag/126)

## 풀이

- BFS를 응용한 문제
- 상하좌우탐색법(Nswe Search)를 참고하여 기준점의 상하좌우 데이터를 확인하는 방법을 먼저 익히고 시도할 것
- charAt(i) - '0' : 문자열에서 인덱스에 저장되어 있는 값을 구분할 때 쓰임
- 최종적인 결과는 미로를 탐색하면서 방문한 정점에 해당 정점까지의 길이를 저장해놓고, 마지막에 마지막 정점을 출력하면 된다.
- Queue는 LinkedList로 응용하여 구현함
  - 응용할 필요는 없었지만 연습할 겸 써봄

```java
package com.company;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class MiroSearch {

    static int[][] map;
    static boolean[][] visited;
    static int N; //행
    static int M; //열
    //상하좌우 탐색을 위한 좌표
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static class Point{
        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void bfs(){
        //다음 탐색할 좌표를 저장하는 큐
        Queue<Point> que = new LinkedList<Point>();
        //처음으로 탐색을 시작하기 위해 0,0을 넣어준다.
        que.add(new Point(0,0));

        //첫번째 요소에 방문했음을 표시
        visited[0][0] = true;

        //큐가 비어있을 때 까지 반복
        while(!que.isEmpty()){
            //큐에서 좌표를 가져온다.
            Point p = que.poll();

            //상하좌우 탐색법 이용
            for (int i = 0; i < 4; i++) {
                //주의 - x와 y의 행과 열구분이 헷갈릴 수 있다.
                int nextX = p.x + dx[i]; //다음 탐색할 x좌표 - 열
                int nextY = p.y + dy[i]; //다음 탐색할 y좌표 - 행


                //범위를 벗어나는 경우에는 탐색을 하지 않음
                if(nextX < 0 || nextX >= N || nextY < 0 || nextY >= M){
                    continue;
                }
                //0인 경우 탐색을 하지 않음
                if(map[nextX][nextY] == 0){
                    continue;
                }
                //이미 방문을 한 경우 탐색을 하지 않음
                if(visited[nextX][nextY] == true){
                    continue;
                }

                //방문을 하는 경우
                //큐에 저장
                que.add(new Point(nextX, nextY));

                //방문한 위치에는 몇번째에 방문했는지를 저장해놓는다.
                map[nextX][nextY] = map[p.x][p.y] + 1;
                //마지막으로 방문했음을 표시해놓는다.
                visited[nextX][nextY] = true;
            }
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        N = scan.nextInt();
        M = scan.nextInt();

        //줄단위로 입력받기위해서 nextLine() 이용 - 한 행을 전체 입력받음
        scan.nextLine();

        //배열 초기화
        map = new int[N][M];
        visited = new boolean[N][M];

        //행렬 입력하기
        for (int i = 0; i < N; i++) {
            String str = scan.nextLine();
            for (int j = 0; j < M; j++) {
                /*
                  nextLine()으로 입력된 문자열에서 한 문자씩 추출하기 위해 charAt(i)를 이용한다.
                  '0' 또는 48을 빼주어 ASCII 숫자로 변환시켜준다.
                 */
                map[i][j] = str.charAt(j) - '0';

                //모든 방문위치 초기화
                visited[i][j] = false;
            }
        }
        bfs();
        //결과값 => 방문한 좌표에 방문한길이를 저장했으므로 마지막 방문점의 값을 출력하면된다.
        //좌표값이기 때문에 1씩 빼준다.
        System.out.println(map[N-1][M-1]);
    }
}
```

