     #첫 번째 코드
# '''
#  예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 
#  합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
#  a,b,c-> (a+b)+(a+b+(c))


#  그러나 10장과 40장을 합친 뒤, 
#  합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
# a,b,c->(min(a)+max(c))+((min(a)+max(c))+middle(b))

# 만약 10,20,30,40 의 네 묶의 카드면
# 10+20
# 30+30
# 60+40


# '''

# import sys

# input=sys.stdin.readline

# n=int(input())
# card=[]
# for i in range(n):
#     card.append(int(input()))
# card.sort()
# #print(card)
# '''
# card[0]+card[1]=a
# a+card[2]=b
# a+b=c

# 3개의 리스트는 
# case 1: 첫번째+두번째 [10,20,40]
# case 2: 첫번째+두번째+첫번째+두번째+세번째 [10,20,10,20,40]

# '''
# #card->[10,20,40]
# cnt=0
# for i in range(len(card)-1):
#     card.append(card[i])        #i=0 [10,20,40,10]  
#                                 #i=1 [10,20,40,10,20]
# for i in range(len(card)):
#     cnt+=card[i]
# print(cnt)


          #정답코드
 '''
우선순위 큐 사용->heapq 모듈
card 리스트에 input값을 push해서 card에 넣음
리스트의 가장 작은 숫자 2개를 pop한다음 더함
while 문을 사용해 card의 리스트 길이가 1이 아닐때 까지 반복한다음 더함
'''
import heapq
import sys

input=sys.stdin.readline

n=int(input())

card=[]
for i in range(n):
    num=int(input())
    heapq.heappush(card, num)

result=0
while len(card)!=1:
    st=heapq.heappop(card)
    nd=heapq.heappop(card)
    ssum=st+nd
    result+=ssum
    heapq.heappush(card, st+nd)

print(result)

