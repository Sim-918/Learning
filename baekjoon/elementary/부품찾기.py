# 집합 자료로 검사
n=int(input())
arr=set(map(int,input().split()))
m=int(input())
target=list(map(int,input().split()))

for i in target:
    if i in arr:
        print('yes',i,end=' ')
    else:
        print('no',i,end=' ')
        
#  이진자료로 검사
# def bin_search(arr,target,start,end):
#     # 시작점이 끝점보다 작을때 까지         start| |..mid..| |end
#     while start<=end:
#         # 데이터를 반으로 쪼갠다
#         mid=(start+end)//2
#         # 내가 찾는값이 맞으면 
#         if arr[mid]==target:
#             # mid리턴
#             return mid
#         # 만약 내가찾는 리스트보다 
#         elif arr[mid]>target:
#             end=mid-1
#         else:
#             start=mid+1
#     return None

# # 매장의 부품개수의 수
# n=int(input())
# # 매장의 부품리스트
# arr=list(map(int,input().split()))
# arr.sort()
# # 내가찾을 부품의 수
# m=int(input())
# # 내가찾을 부품 리스트
# target=list(map(int,input().split()))

# for i in target:
#     result=bin_search(arr,i,0,n-1)      #bin_search(매장부품,target,0부터시작,매장부품수까지)
#     if result!=None:
#         print('yes',end=' ')
#     else:
#         print('no',end=' ')
