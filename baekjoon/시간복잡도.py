# O(n^2)시간 복잡도
# n=[4,1,7,9,3,16,5]

# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         if n[i]+n[j]==14:
#             print(n[i],n[j])


# O(nlog(n))시간 복잡도->이진탐색
# n=[4,1,7,9,3,16,5]
# target=14
# def twoSum(n,target):
#     n.sort()
#     start,end=0,len(n)-1
#     while start<end:
#         if target<n[start]+n[end]:
#             end-=1
#         elif target>n[start]+n[end]:
#             start+=1
#         else:
#             return n[start],n[end]
# print(twoSum(n,target))

# O(n)
# n=[4,1,7,9,3,16,5]
# target=14
# def twoSum(n,target):
#     seeb={}
#     for i,v in enumerate(n):
#         final=target-v
#         if filter in seeb:
#             return [seeb[final],i]
#         else:
#             seeb[v]=v
#     return False
