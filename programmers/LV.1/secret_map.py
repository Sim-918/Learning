def solution(n, arr1, arr2):
    answer=[]
    for i in range(n):
        tmp=bin(arr1[i]|arr2[i])
        tmp=tmp[2:].zfill(n)        #zfill->앞에 n개 만큼 0을 채워주는 함수
        tmp=tmp.replace('1','#').replace('0',' ')
        answer.append(tmp)
    return answer
