# nxm
# 0이면 얼음생성 ->Ture
# 1이면 False

n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
# print(graph)


def dfs(x,y):
    # 범위를 초과하면
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 방문처리가 아직안된 노드
    if graph[x][y]==0:
        # 방문처리
        graph[x][y]=1
        # 상,하,좌,우 처리
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False
cnt=0

for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            cnt+=1
print(cnt)
