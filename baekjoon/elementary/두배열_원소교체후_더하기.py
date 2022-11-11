arlen,key=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
reslut=0
a.sort()
b=sorted(b,reverse=True)

for i in range(key):
    a[i]=b[i]
for i in a:
    reslut+=i
print(reslut)
