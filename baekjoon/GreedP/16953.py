'''정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다. 
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
'''
import sys

input=sys.stdin.readline

a,b=map(int,input().split())
cnt=1
#A->B 가 아닌 B->A 
#마지막 수가 1인가?
#   맞으면 1을 없앰
#   아니면 //2 
#   테스트를 모두 통과하고 값이 같지않으면 -1

while True:
    if b==a:
        break
    elif (b%2!=0 and b%10!=1) or b<a:
        cnt=-1
        break
    else:
        if b%10==1:
            b=b//10
            cnt+=1
        elif b%2==0:
            b=b//2
            cnt+=1
print(cnt)
