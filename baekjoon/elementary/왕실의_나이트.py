# 8x8 체스판에서 n이 주어졌을때 나이트가 갈수 있는 길은 몇개가 있는가
# x->a,b,c...h
# y->1,2,3..8

# a1이 입력됬을 때 나이트가 갈수있는 길은 2개
# (c,2) -> x+3,y+1
# (b,3) -> x+1,y+3
# 나이트가 중앙 쯤에 있을때 모두 갈수있는 길은 총8개이다
### 나의정답 ###
night=[(-1,-2),(1,-2),(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1)]
n=list(input())
x=ord(n[0]) #97
y=n[1]
cnt=0

for i in range(len(night)):
    nx=x+night[i][0]
    ny=int(y)+night[i][1]
    # print(chr(nx),ny)
    if nx<97 or nx>104 or ny<1 or ny>8:
        # print(nx,ny)
        continue
    cnt+=1
    # print(chr(nx),ny)
print(cnt)
