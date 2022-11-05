# n*m행렬
# 
n,m=map(int,input().split())
reslut=0

for i in range(n):
    data=list(map(int,input().split()))
    min_v=min(data)
    # reslut=max(reslut,min_v)
print(min_v)
