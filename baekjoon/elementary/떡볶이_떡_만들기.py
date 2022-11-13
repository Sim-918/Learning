# 떡의 개수 =n, 요청한 떡길이=m
n,m=map(int,input().split())
arr=list(map(int,input().split()))

# 절단기로 잘랐을 때 m이 되는 절단기의 길이
# arr의 중간점을 지정하고 먼저 잘라본다
# 하지만 잘린떡들의 길이합이 m을 넘으면 시작점을 +1하고 중간점을 다시 찾음
# 하지만 잘린떡들의 길이합이 m을 넘지못하면 시작점과 끝점을 

start=0
end=max(arr)
result=0

while start<=end:
    total=0
    mid=(start+end)//2
    for i in arr:
        if i>mid:
            total+=i-mid
    if total<m:
        end=mid-1
    else:
        result=mid
        start=mid+1
print(result)
