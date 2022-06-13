# '''
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 1. 평균을 구하고
# 2. 평균이 넘지못하는 사람 if n[0][i]>average
# '''

# #sum함수사용

import sys 
input=sys.stdin.readline 

c=int(input())


for i in range(c):
    n=list(map(int,input().split()))
    avg=sum(n[1:])//n[0]
    cnt=0
    for j in range(1,len(n)):
        if n[j]>avg:
            cnt+=1
    reslut=cnt/n[0]*100
    print("%.3f"%reslut+'%')
