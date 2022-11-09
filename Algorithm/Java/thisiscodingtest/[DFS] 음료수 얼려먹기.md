# 문제
~~~
음료수 얼려 먹기  
N * M 크기의 얼음틀  
뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시  
뚫려 있는 부분끼리 상,하,좌,우로 붙어있는 경우는 서로 연결된 것으로 간주한다.  
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성  
  
입력조건  
- 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로길이 M이 주어진다. (1<=N, M<=1,000)  
- 두 번째 줄부터 N+1번째 줄까지의 얼음 틀의 형태가 주어진다.  
- 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.  
  
출력조건  
- 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.  
  
입력 예시  
15 14  
00000111100000  
11111101111110  
11011101101110  
11011101100000  
11011111111111  
11011111111100  
11000000011111  
01111111111111  
00000000011111  
01111111111000  
00011111111000  
00000001111000  
11111111110011  
11100011111111  
11100011111111  
  
출력예시  
8
~~~

# 풀이
 - DFS 종료 조건을 잘 선택해야 한다. x < n이 아닌 x <= n으로 해야 상하좌우탐색에서 조건이 충족된다.
``` java
public class FreezeDrinks {  
  
  
    static int n;  
    static int m;  
    static int[][] graph = null;  
  
  
    public static void main(String[] args) throws IOException {  
  
        System.out.println("n, m 입력");  
        Scanner sc = new Scanner(System.in);  
  
        n = sc.nextInt();  
        m = sc.nextInt();  
  
        sc.nextLine();  
  
        graph = new int[n][m];  
  
  
        System.out.println("graph 입력");  
  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        for (int i = 0; i < n; i++) {  
            String st = br.readLine();  
            for (int j = 0; j < m; j++) {  
                graph[i][j] = st.charAt(j) - '0'; // 숫자 문자열을 숫자로 만드는 방법  
            }  
        }  
  
        int result = 0;  
  
        // 모든 정점 방문  
        for (int i = 0; i < n; i++) {  
            for (int j = 0; j < m; j++) {  
                if(dfs(i,j) == true){  
                    result++;  
                }  
            }  
        }  
  
  
        System.out.println(result);  
  
    }  
  
    private static boolean dfs(int x, int y){  
        int[] dx = {0, 0, -1, 1};  
        int[] dy = {-1, 1, 0, 0};  
  
        if(x < 0 || x >= n || y < 0 || y >= m) return false;  
  
        if (graph[x][y] == 0){  
            // 방문 처리  
            graph[x][y] = 1;  
  
            for (int i = 0; i < 4; i++) {  
                int nx = x + dx[i];  
                int ny = y + dy[i];  
  
                dfs(nx, ny);  
            }  
  
            return true;  
        }  
        return false;  
    }  
}
```