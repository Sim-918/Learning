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
    price,num=input().split()
    d1.append(int(price))
    d2.append(int(num))

d1.sort()
d2.sort()

'''
살 기타줄이 6개이상 일때는 패키지가격이 가장작은 것을
사면됨 아니면 낱개에 개수가 가장작은것 단 패키지로 사는 가격이 더쌀경우 패키지
하지만 패키지를 사고 더 살 줄이 남아있다면 n-=6
낱개 가격이 가장 작을 것을 사면됨 단 패키지로 사는 가격이 더 쌀경우
패키지로 구매
'''
