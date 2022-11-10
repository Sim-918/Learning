# BFS 넓이 우선 탐색
# 동작과 구현을 큐를 이용해
# 1은 길 0은 벽
# 0,0부터 n,m까지 얼마나 이동해야하는가
from collections import deque
n,m=map(int,input().split())

graph=[]

for i in range(n):
        graph.append(list(map(int,input())))
# 이동할거리 상,하,좌,우
dx=[0,-1,0,1]
dy=[1,0,-1,0]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    print(queue)
    # 큐가 빌때 까지 반복
    while queue:
        x,y=queue.popleft()
        # print(x)
        # print(y)
        print(queue)
        # 상,하,좌,우 검사
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 만약 범위를 벗어났다면
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽일 경우 다시 루프
            if graph[nx][ny]==0:
                continue
            # 길일 경우
            if graph[nx][ny]==1:
                # 현위치에서 +1카운트
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

# 0,0부터 시작
print(bfs(0,0))
