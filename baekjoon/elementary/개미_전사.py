# 식량창고는 일직선
# 선택적으로 약탈
# 약탈하고 최소 한칸이상 떨어진 식량창고를 털어야함
# 최대한 많은 양의 식량을 털어야함
# Ai=max(Ai-1,Ai-2+Ki)
n=int(input())
ar=list(map(int,input().split()))

d=[0]*(n+1)
d[0]=ar[0]
d[1]=max(ar[0],ar[1])
# 어쩌피 2번째부터 시작할거임 왜냐하면 0번째와 1번째를 알기때문
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+ar[i])

print(d[n-1])
