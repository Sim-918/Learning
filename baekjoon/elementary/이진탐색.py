# 재귀함수로 구현한 이진 탐색코드
'''
def bin_search(arr,target,start,end):
    # 예외처리
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return bin_search(arr,target,start,mid-1)
    else:
        return bin_search(arr,target,mid+1,end)
# 원소의 개수와 찾고자하는 문자열 입력
n,target=list(map(int,input().split()))
# 고정된 리스트데이터 받기
arr=list(map(int,input().split()))
# start=0 end=9
reslut=bin_search(arr,target,0,n-1)
if reslut==None:
    print('없습니다')
else:
    print(reslut+1)
'''
# 반목문으로 구현한 이진 탐색
'''
def bin_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
n,target=list(map(int,input().split()))
arr=list(map(int,input().split()))
result=bin_search(arr,target,0,n-1)
if result==None:
    print('없습니다')
else:
    print(result+1)
'''
