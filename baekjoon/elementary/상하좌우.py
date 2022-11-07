# # 먼저 튜플형식으로 만듦 (1,1)로 시작
# # 만약 공간이 없는 상태에서 더 가면 무시
# # R,L,U,D 으론쪽 왼쪽 위쪽 아랫쪽

# # 내정답
# n=int(input())
# x,y=1,1
# move=input().split()

# for i in move:
#     if i=='R':
#         dy=y+1
#     elif i=='L':
#         dy=y-1
#     elif i=='U':
#         dx=x-1
#     elif i=='D':
#         dx=x+1
#     elif x<1 or y<1 or x>n or y>n:
#         continue
#     # x또는 y가 5를 넘거나 
#     # x또는 y가 0이게 되면 그 전 값에서 다시시작

# print(dx,dy)

n=int(input())
move_on=input().split()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_type=['L','R','U','D']
x,y=1,1

for move in move_on:
    for i in range(len(move_type)):
        if move==move_type[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)
