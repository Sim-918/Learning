import sys
input=sys.stdin.readline

def solution(lottos, win_nums):
    Zero=0      #0이 있는 번호(모르는 번호)
    Winnum=0    #당첨번호
    for i in range(0,len(lottos)):
        if lottos[i] in win_nums:
            Winnum+=1
        if lottos[i]==0:
            Zero+=1
    total=Winnum+Zero       #0+6
    rankDic={6:1,5:2,4:3,3:4,2:5,1:6,0:6}   #복권당첨 딕션어리{key=6이면 맞추면:value=1등}
    answer = [rankDic[total],rankDic[Winnum]]
    return answer

unkown=input().split()
correct=input().split()

print(solution(unkown,correct))
'''
import sys
input=sys.stdin.readline

def solution(lottos, win_nums):
    rank=[6,6,5,4,3,2,1]
    cnt=lottos.count(0)
    ans=0
    for i in win_nums:
        if i in lottos:
            ans+=1

    return rank[cnt+ans],rank[ans]

'''
