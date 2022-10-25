def solution(arr):
    arr.sort()
    cnt=0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for z in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[z]==0:
                    cnt+=1
    return cnt
