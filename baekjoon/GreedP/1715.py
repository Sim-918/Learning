'''
 예를 들어 10장, 20장, 40장의 묶음이 있다면 10장과 20장을 합친 뒤, 
 합친 30장 묶음과 40장을 합친다면 (10 + 20) + (30 + 40) = 100번의 비교가 필요하다.
 a,b,c-> (a+b)+(a+b+(c))


 그러나 10장과 40장을 합친 뒤, 
 합친 50장 묶음과 20장을 합친다면 (10 + 40) + (50 + 20) = 120 번의 비교가 필요하므로 덜 효율적인 방법이다.
a,b,c->(min(a)+max(c))+((min(a)+max(c))+middle(b))



'''

import sys

input=sys.stdin.readline

n=int(input())
card=[]
for i in range(n):
    card.append(int(input()))
card.sort()
#print(card)
'''
card[0]+card[1]=a
a+card[2]=b
a+b=c

'''

