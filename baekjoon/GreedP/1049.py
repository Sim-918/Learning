'''
 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 
 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 
 낱개로 살 때의 가격이 주어질 때, 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

'''
import sys

input=sys.stdin.readline

#n->사야될 기타줄   m->살려는 기타줄 브랜드 수
n,m=map(int,input().split())
d1=[]
d2=[]
ans=0
for i in range(m):
    pack,num=input().split()
    d1.append(int(pack))
    d2.append(int(num))

d1.sort()
d2.sort()

'''
패키지의 최소와 낱개의 최소를 구하고
n을 6으로 나눈 나머지와 몫
n//6->1
n%6->4
결국에는 최소 패키지를 (n//6)+1번살것인가
아님 최소패키지를 n//6번사고 최소낱개로 n%6개 구매할것인가
아님 최소낱개로만 구매할것인가
'''

case1=((n//6)+1)*d1[0]
case2=((n//6)*d1[0])+((n%6)*d2[0])
case3=n*d2[0]
ans={case1,case2,case3}
print(min(ans))
