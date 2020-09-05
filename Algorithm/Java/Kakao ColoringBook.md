# Kakao ColoringBook

> ###### 문제 설명
>
> ## 카카오 프렌즈 컬러링북
>
> 출판사의 편집자인 어피치는 네오에게 컬러링북에 들어갈 원화를 그려달라고 부탁하여 여러 장의 그림을 받았다. 여러 장의 그림을 난이도 순으로 컬러링북에 넣고 싶었던 어피치는 영역이 많으면 색칠하기가 까다로워 어려워진다는 사실을 발견하고 그림의 난이도를 영역의 수로 정의하였다. (영역이란 상하좌우로 연결된 같은 색상의 공간을 의미한다.)
>
> 그림에 몇 개의 영역이 있는지와 가장 큰 영역의 넓이는 얼마인지 계산하는 프로그램을 작성해보자.
>
> ![alt text](http://t1.kakaocdn.net/codefestival/apeach.png)
>
> 위의 그림은 총 12개 영역으로 이루어져 있으며, 가장 넓은 영역은 어피치의 얼굴면으로 넓이는 120이다.
>
> ### 입력 형식
>
> 입력은 그림의 크기를 나타내는 `m`과 `n`, 그리고 그림을 나타내는 `m × n` 크기의 2차원 배열 `picture`로 주어진다. 제한조건은 아래와 같다.
>
> - `1 <= m, n <= 100`
> - `picture`의 원소는 `0` 이상 `2^31 - 1` 이하의 임의의 값이다.
> - `picture`의 원소 중 값이 `0`인 경우는 색칠하지 않는 영역을 뜻한다.
>
> ### 출력 형식
>
> 리턴 타입은 원소가 두 개인 정수 배열이다. 그림에 몇 개의 영역이 있는지와 가장 큰 영역은 몇 칸으로 이루어져 있는지를 리턴한다.
>
> ### 예제 입출력
>
> | m    | n    | picture                                                      | answer |
> | ---- | ---- | ------------------------------------------------------------ | ------ |
> | 6    | 4    | [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]] | [4, 5] |
>
> ### 예제에 대한 설명
>
> 예제로 주어진 그림은 총 4개의 영역으로 구성되어 있으며, 왼쪽 위의 영역과 오른쪽의 영역은 모두 `1`로 구성되어 있지만 상하좌우로 이어져있지 않으므로 다른 영역이다. 가장 넓은 영역은 왼쪽 위 `1`이 차지하는 영역으로 총 5칸이다.

## 풀이

- 난이도 중하 정도의 문제라는데 오래걸렸다.
  - 공부순서
    1. BFS
    2. Nswe 탐색법(상하좌우 탐색법)
    3. 백준 미로 알고리즘
    4. 최종 카카오 컬러링북 문제
- 처음에 실행으로 결과는 맞았는데 제출에서 틀렸다고 나왔다.
  - 왜 그런지 모르겠지만, 질문하기에서 변수의 초기화를 solution함수안에서 하면 된다고해서 해보니 맞았다
- 영역의 갯수는 bfs를 실행하는 만큼(visited가 false이면 실행)
- 영역의 최대 넓이는 영역마다 비교해줘야 하므로 임시함수 tempSizeOfOneArea를 만들어서 비교했다.
  - 큐가 empty되면 maxSizeOfOneArea와 tempSizeOfOneArea를 비교해줬다.

```java
import java.util.*;
class Solution {
    private static int numberOfArea;
    //각 영역의 크기는 여기에 저장한 후 영역의 탐색이 끝나면 maxSizeOfOneArea와 크기비교 한다.
    private static int tempSizeOfOneArea;
    private static int maxSizeOfOneArea;
    //방문여부를 확인하는 배열
    private static boolean[][] visited;

    //좌표를 저장할 Point클래스
    static class Point{
        int x, y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void bfs(int startX, int startY, int[][] picture, int m, int n) {
        //상하좌우 순으로 탐색하기 위한 좌표세트
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        //다음 탐색할 좌표를 저장하는 큐
        Queue<Point> que = new LinkedList<Point>();
        //처음으로 탐색을 시작하기 위해 0,0을 que에 저장
        que.add(new Point(startX, startY));

        //첫번재 요소를 방문했음을 표시
        visited[0][0] = true;

        //큐가 빌때까지 반복
        while (!que.isEmpty()) {
            //큐에서 좌표 가져오기
            Point p = que.poll();

            //상하좌우 탐색법 이용
            for (int i = 0; i < 4; i++) {
                //상하좌우로 값을 옮기며 탐색가능해짐
                int nextX = p.x + dx[i];
                int nextY = p.y + dy[i];

                //범위를 벗어나는 경우 탐색을 하지 않는다.
                if (nextX < 0 || nextX >= m || nextY < 0 || nextY >= n) {
                    continue;
                }

                //0인 경우 탐색을 하지 않음
                if (picture[nextX][nextY] == 0) {
                    continue;
                }

                //현재 방문하는 점과 다음 점의 숫자가 달라도 탐색을 중지
                if(picture[p.x][p.y] != picture[nextX][nextY]){
                    continue;
                }

                //이미 방문한 경우 탐색을 하지 않음
                if (visited[nextX][nextY] == true) {
                    continue;
                }

                //방문을 하는 경우
                que.add(new Point(nextX, nextY)); //다음 방문위치를 저장


                //영역의 최대 크기와, 영역의 갯수를 찾아야함
                //현재 값과 다음 값이 같은 숫자일 경우 tempSizeOfOneArea 크기를 늘린다.
                if (picture[p.x][p.y] == picture[nextX][nextY]) {
                    tempSizeOfOneArea = tempSizeOfOneArea + 1;
                }

                //방문했음을 표시
                visited[nextX][nextY] = true;
            }

        }

        //영역의 갯수는 큐가 한번 완전히 비어지면 영역이 끝난것이므로 큐가 완전히 비어지면 1씩 올린다.
        numberOfArea = numberOfArea + 1;

        //영역의 최대 크기를 결정
        if (tempSizeOfOneArea > maxSizeOfOneArea) {
            maxSizeOfOneArea = tempSizeOfOneArea;
        }
        
        tempSizeOfOneArea = 0;
    }
    
    public int[] solution(int m, int n, int[][] picture) {
    
        numberOfArea = 0;
        tempSizeOfOneArea = 1;
        maxSizeOfOneArea = 0;
        int[] answer = new int[2];
        
        //방문여부를 저장하는 배열 초기화
        visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if(visited[i][j] == false && picture[i][j] !=0){
                    bfs(i, j, picture, m, n);
                }
            }
        }
        
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        
        return answer;
    }
}
```

### 깔끔해보이는 BFS(퍼옴) - 백준미로문제에서도 나옴

```java
 static void bfs(int[][] pic, int x, int y, int m, int n){
        queue.add(new Node(x, y));
        visited[x][y] = true;
        
        while(!queue.isEmpty()){
            Node now = queue.poll();
            
            for(int i = 0; i < 4; i++){
                int nx = now.x + dx[i];
                int ny = now.y + dy[i];
                
                if(0 <= nx && nx < m && 0 <= ny && ny < n){
                    if(pic[nx][ny] == pic[x][y] && visited[nx][ny] != true){
                        queue.add(new Node(nx, ny));
                        visited[nx][ny] = true;
                        size++; // 지나온 칸의 개수
                    
                    }
                }
            }
        }
```



## 결과

![image-20200905180319219](/Users/wonik/Library/Application Support/typora-user-images/image-20200905180319219.png)