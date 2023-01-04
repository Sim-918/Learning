n=int(input())
ans=[]
stack=[]
for i in range(n):
    ans.append(input())
for j in ans:
    if len(j)>5:
       stack.append(j.split()[-1])
    elif j=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
    elif j=='size':
        if len(stack)==0:
            print(0)
        elif len(stack)>0:
            print(len(stack))
    elif j=='empty':
        if len(stack)==0:
            print(1)
        elif len(stack)>0:
            print(0)
    elif j=='pop':
        if len(stack)==0:
            print(-1)
            stack=[]
        else:
            print(stack.pop(-1))
