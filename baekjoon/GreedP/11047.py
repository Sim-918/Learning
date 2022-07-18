k,n=map(int,input().split())
arr=[]
count=0

for i in range(0,k):
    a=int(input())
    arr.append(a)
arr.sort(reverse=True)

for j in range(0,k):
    if n//arr[j]==0:
        continue
    else:
        count+=n//arr[j]
        n=n%arr[j]
print(count)

