def solution(array, commands):
    ans=[]
    arr=[]
    tmp=[]
    for i in range(len(commands)):
        ans=array[(commands[i][0]-1):commands[i][1]] 
        ans.sort()
        arr.append(ans)
        tmp.append(arr[i][(commands[i][2])-1])
    return tmp
