# 25/5= 5
# 5/5=1
# ->몫이 1이 될때까지

# 먼저 n/k가 0인가
# 아닐시 1번(n-1)을 실행
# 그리고 다시 검사
# 만약 맞으면 2번(n/k)진행

n,k=map(int,input().split())
cnt=0

while True:
    if n%k==0:
        n//=k
        cnt+=1
    elif n==1:
        break
    elif n%k!=0:
        n-=1
        cnt+=1
print(cnt)
