'''
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다. 
미르코는 30이란 수를 존경하기 때문에, 
그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.
미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.'''

'''
문자열이 입력되고 임의로 바꾼다음 30의 배수가 되면 그 수를 출력
ex) 012 -> 210 
120도 가능하지만 210보다 큰수

먼저 가장크게 정렬을 한다.



'''
import sys
input=sys.stdin.readline

n=list(input())

n.sort(reverse=True)

st=''
for i in range(len(n)-1):
    st+=n[i]

if int(st)%30==0:
    print(st)
else:
    print(-1)
