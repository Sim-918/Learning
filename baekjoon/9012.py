from collections import deque
def sol(s):
    q=deque(s)
    tmp=0
    ans='YES'
    while len(q)>0:
        if q.popleft()=='(':
            tmp+=1
        else:
            tmp-=1
        if tmp<0:
            ans='NO' 
            break
    if tmp>0:
        ans='NO'
    return ans
n=int(input())
for _ in range(n):
    gual=input()
    print(sol(gual))
