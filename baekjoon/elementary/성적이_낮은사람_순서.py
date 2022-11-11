n=int(input())
ar=[]
for i in range(n):
    data=input().split()
    # ((이순신,87)) .. (키,값)형식으로 append해야되기 때문에 
    ar.append((data[0],int(data[1])))
ar=sorted(ar,key=lambda x:x[1])
for i in ar:
    print(i[0],end=' ')
