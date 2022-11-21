# 문제
~~~
미로탈출  
N * M 직사각형 형태의 미로  
시작위치는 (1,1)이고 미로 출구는 (N,M)한 번에 한 칸씩 이동 가능  
괴물이 있는 곳 0, 괴물이 없는 곳 1반드시 탈출 가능한 미로 형태로 제시된다.  
탈출을 위해 움직이는 최소한의 칸의 개수 구하기  
  
입력조건  
첫째 줄에 두 정수 N,M (N<=N, M<=200)이 주어진다.  
다음 N개의 줄에는 미로의 형태가 주어진다. 시작칸과 마지막 칸은 항상 1이다.  
  
입력 예  
5 6  
101010  
111111  
000001  
111111  
111111  
  
출력 예  
10
~~~

# 풀이
 - BFS로 최단 거리 찾기 문제
 - 해당 맵에 최단거리를 넣는 방식 이용 (visited 이용 하지 않음)
``` java
public class Miro {  
  
    static int n;  
    static int m;  
    static int[][] graph;  
  
    public static void main(String[] args) throws IOException {  
  
        System.out.println("n, m 입력");  
        Scanner sc = new Scanner(System.in);  
  
        n = sc.nextInt();  
        m = sc.nextInt();  
  
        graph = new int[n][m];  
  
        System.out.println("graph 입력");  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
  
        for (int i = 0; i < n; i++) {  
            String readLine = br.readLine();  
            for (int j = 0; j < m; j++) {  
                graph[i][j] = readLine.charAt(j) - '0';  
            }  
        }  
  
  
        System.out.println(bfs(new Point(0,0)));  
    }  
  
    private static int bfs(Point point){  
        // 상하좌우  
        int[] dx = {0, 0, -1, 1};  
        int[] dy = {-1, 1, 0, 0};  
  
  
        Queue<Point> que = new LinkedList<Point>();  
  
        que.add(point);  
  
        // 큐가 빌 때까지 반복  
        while(!que.isEmpty()){  
  
            Point quePoint = que.poll();  
            int x = quePoint.x;  
            int y = quePoint.y;  
  
            for (int i = 0; i < 4; i++) {  
                int nx = x + dx[i];  
                int ny = y + dy[i];  
  
  
                // 범위를 벗어날 경우  
                if(nx < 0 || nx >= n || ny < 0 || ny >= m){  
                    continue;  
                }  
  
                // 괴물이 있는 경우  
                if(graph[nx][ny] == 0){  
                    continue;  
                }  
  
                // 방문하지 않은 길만 탐색 -> 방문 한 길은 거리를 저장한다.  
                if(graph[nx][ny] == 1){  
                    // 거리 저장  
                    graph[nx][ny] = graph[x][y] + 1;  
  
                    // que에 다음 포인터 저장  
                    que.add(new Point(nx, ny));  
                }  
            }  
        }  
  
  
        return graph[n-1][m-1];  
    }  
  
}

class Point {  
    int x;  
    int y;  
  
    public Point(int x, int y) {  
        this.x = x;  
        this.y = y;  
    }  
}
```