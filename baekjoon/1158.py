# 제일 마지막으로 죽은 사람다음이 첫번째 로 바뀜
n,k=map(int,input().split())
# n=7
# k=3
num_ar=[i for i in range(1,n+1)]

yosae=[]
cnt=0
for _ in range(n):
    cnt+=k-1
    if cnt>=len(num_ar):
        cnt%=len(num_ar)
    yosae.append(str(num_ar.pop(cnt)))
print("<"+", ".join(yosae)+">")
