# 영역구하기
- https://www.acmicpc.net/problem/2583
- DFS로 푸는 방법이 쉽고 빠르다.


# 문제
눈금의 간격이 1인 M×N(M,N≤100)크기의 모눈종이가 있다. 이 모눈종이 위에 눈금에 맞추어 K개의 직사각형을 그릴 때, 이들 K개의 직사각형의 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어진다.

예를 들어 M=5, N=7 인 모눈종이 위에 <그림 1>과 같이 직사각형 3개를 그렸다면, 그 나머지 영역은 <그림 2>와 같이 3개의 분리된 영역으로 나누어지게 된다.

![](https://www.acmicpc.net/upload/images/zzJD2aQyF5Rm4IlOt.png)

<그림 2>와 같이 분리된 세 영역의 넓이는 각각 1, 7, 13이 된다.

M, N과 K 그리고 K개의 직사각형의 좌표가 주어질 때, K개의 직사각형 내부를 제외한 나머지 부분이 몇 개의 분리된 영역으로 나누어지는지, 그리고 분리된 각 영역의 넓이가 얼마인지를 구하여 이를 출력하는 프로그램을 작성하시오.

## 입력
첫째 줄에 M과 N, 그리고 K가 빈칸을 사이에 두고 차례로 주어진다. M, N, K는 모두 100 이하의 자연수이다. 둘째 줄부터 K개의 줄에는 한 줄에 하나씩 직사각형의 왼쪽 아래 꼭짓점의 x, y좌표값과 오른쪽 위 꼭짓점의 x, y좌표값이 빈칸을 사이에 두고 차례로 주어진다. 모눈종이의 왼쪽 아래 꼭짓점의 좌표는 (0,0)이고, 오른쪽 위 꼭짓점의 좌표는(N,M)이다. 입력되는 K개의 직사각형들이 모눈종이 전체를 채우는 경우는 없다.

## 출력
첫째 줄에 분리되어 나누어지는 영역의 개수를 출력한다. 둘째 줄에는 각 영역의 넓이를 오름차순으로 정렬하여 빈칸을 사이에 두고 출력한다.

## 입력 예
```
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
```

## 출력 예
```
3
1 7 13
```



# 풀이
- 총 영역의 개수(count)는 DFS를 실행한 개수
- 영역의 너비는 0으로만 이어지는 개수
- StringTokenizer를 이용하여 문자열 자르기 이용
	- split를 이용해도 상관없다. (오히려 자유도가 더 높을 수 있다. ex. 변수에 필요한 index의 값을 넣을때)
- 현실과의 패러다임 불일치가 발생할 수 있다.
	- 뒤집어져있다 => 현실의 모눈종이에서는 (0,0)은 왼쪽 아래부분에 있지만, 프로그래밍의 (0,0)은 왼쪽 위부터 시작한다. 
	- x, y 축을 뒤집어서 배열에 넣어야 한다.
		- 배열을 초기화할 때의 행,열과 반대이다.
- 영역의 너비(areaWidth)를 DFS가 종료 된 후 초기화를 해준다.
``` java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main{

    static int m;
    static int n;
    static int k;

    static int[][] map;
    static boolean[][] visited;

    static int count; // 총 영역의 개수
    static int areaWidth = 1; // 영역의 너비

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        map = new int[m][n];
        visited = new boolean[m][n];

        for (int i = 0; i < k; i++) {
            StringTokenizer squarePoints = new StringTokenizer(br.readLine());

            // 왼쪽 아래 x, 왼쪽 아래 y => 패러다임 불일치2. x,y 축이 반대이다.
            int dy = Integer.parseInt(squarePoints.nextToken());
            int dx = m - Integer.parseInt(squarePoints.nextToken());

            // 오른쪽 위 x, 오른쪽 위 y
            int uy = Integer.parseInt(squarePoints.nextToken());
            int ux = m - Integer.parseInt(squarePoints.nextToken());

            // 직사각형 영역 1로 채우기
            fillSquare(dx, dy, ux, uy);
        }

       /* for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(map[i][j]);
            }

            System.out.println();
        }*/

        List areaList = new ArrayList();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(map[i][j] == 0 && !visited[i][j]){
                    areaList.add(dfs(i,j));
                    count++; // 총 영역의 개수 증가
                    areaWidth = 1; // 초기화
                }
            }
        }

		// 총 영역의 개수
        System.out.println(count);
        Collections.sort(areaList); // 오름차순으로 정렬 및 출력
        for (int i = 0; i < areaList.size(); i++) {
            System.out.print(areaList.get(i) + " ");
        }
    }

    private static void fillSquare(int dx, int dy, int ux, int uy){

        for (int i = ux; i < dx; i++) {
            for (int j = dy; j < uy; j++) {
                map[i][j] = 1;
            }
        }
    }

    private static int dfs(int x, int y){

        visited[x][y] = true;

        // 상하좌우 탐색
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && nx < m && ny >= 0 && ny < n && map[nx][ny] == 0 && !visited[nx][ny]){
                areaWidth++;
                dfs(nx, ny);

            }
        }

        return areaWidth;
    }
}
```