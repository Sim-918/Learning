import sys
input=sys.stdin.readline
'''
처음 출발할 때 자동차에는 기름이 없어서 주유소에서 
기름을 넣고 출발하여야 한다.
도로를 이용하여 이동할 때 1km마다 1리터의 기름을 사용한다. 
각 도시에는 단 하나의 주유소가 있으며, 
도시 마다 주유소의 리터당 가격은 다를 수 있다. 
가격의 단위는 원을 사용한다.
4
2 3 1 ->다음 도시 거리
5 2 4 1->도시 주유소 리터당 가격(처음에 무조건 다음도시까지의 거리 만큼은 넣어야함)

먼저 첫 주유소에서 무조건 다음 도시의 거리만큼에 기름을 넣어야함
 n[0]*range
    주유소가 가장 싼곳을 찾음(4곳중 가장싼곳) 만약 n[n-1] 번째가 가장싼것은 x->1 2 4 5(2,4만  n[1:n-1])
'''
n=int(input())
ran=list(map(int,input().split()))
sation=list(map(int,input().split()))

oil=sation[0]*ran[0]                     #첫 기름가격

price=0
'''
4
  2   3   1 
5   2   4    1

4
  2   3   1 
5   4   2    1

4
  2   1   3     2
5   3   4    1      2
=10+(3*4)+2'''
for i in range(1,n-1):        #i=1,2    
    if sation[1]<=sation[i]:       #
        price+=ran[i]*sation[1]
    elif sation[1]>sation[i]:
        price+=ran[i]*sation[i]
        

print(price+oil)
'''
testcase #1 만약 s[1]이 다음 주유소'들' 보다 싸거나 같으면 거리를 모두 더한 후 s[1]이랑 곱해버림
testcase #2 만약 s[1]이 다음 주유소'들' 보다 비싸면 최소값이 나올때 까지 더함
즉 s[1]보다 최소값이 나오기 전 까지 곱함
'''



# print(ran)
# print(price[1:len(price)-1])
