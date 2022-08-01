n=list(input())
cnt=0
for i in range(0,len(n)-1):
    if n[i]!=n[i+1]:
        cnt+=1
print((cnt+1)//2)
