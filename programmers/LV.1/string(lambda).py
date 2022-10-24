# def solution(strings, n):
#     dic={}
#     for i in range(len(strings)):
#         # ar.append(arr1[i][2:3])
#         dic[arr1[i]]=arr1[i][n:n+1]

#     ans=sorted(dic.items(), key = lambda item: item[1])

#     # print(ans[0][0])
#     for i in range(len(arr1)):
#         print(ans[i][0])
#     answer = []
#     return answer
def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])
