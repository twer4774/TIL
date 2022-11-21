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
``` python
from collections import deque  
  
print('n ,m 입력')  
n, m = map(int, input().split())  
  
print('맵 입력')  
graph = []  
for i in range(n):  
    graph.append(list(map(int, input())))  
  
  
# 상하좌우  
dx = [0, 0, -1, 1]  
dy = [-1, 1, 0, 0]  
  
def bfs(x,y):  
    que = deque()  
    que.append((x,y))  
  
    # 큐가 빌 때까지 반복  
    while que:  
        x, y = que.popleft()  
  
        for i in range(4):  
            nx = x + dx[i]  
            ny = y + dy[i]  
  
            # 범위 넘어간 경우 무시  
            if nx < 0 or ny < 0 or nx >= n or ny >= m:  
                continue  
  
            # 괴물이 있는 경우 무시  
            if graph[nx][ny] == 0:  
                continue  
  
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록  
            if graph[nx][ny] == 1:  
                graph[nx][ny] = graph[x][y] + 1 # 최단 거리 기록  
                # que에 위치정보 저장  
                que.append((nx, ny))  
    # 가장 오른쪽 아래까지의 최단 거리 반환  
    return graph[n-1][m-1]  
  
print(bfs(0,0))

```