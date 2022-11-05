# 2 4 5 4 6 list
# m=8, k=3
# 주어진 배열이 있을 때 m번 더하여 가장큰수를 만듦 , 단 연속으로 k번을 초과하여 더할수 없다
# 6+6+6+5+6+6+6+5=46

# 가장큰수를 k번더하고 두번째로 큰수 한번더하고 다시 가장큰수 k번더하고 두번째로 큰수
arrlen,m,k=map(int,input().split())
arr=list(map(int,input().split()))
result=0
arr.sort(reverse=True)

fristnum=arr[0]
secondnum=arr[1]

while True:
    for i in range(k):
        if m==0:
            break
        result+=fristnum
        m-=1
    if m==0:
        break
    result+=secondnum
    m-=1
    
print(result)
