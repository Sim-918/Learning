#조규현 (x1,y1)->Jo     0,0
#백승환 (x2,y2)->Beak   40,0
#조규헌 ->류재명 거리 r1    13
#백승환 ->류재명 거리 r2    37
#결론은 둘 사이의 거리가 
#그리고 접점의 개수를 구함
import math

t=int(input())

for i in range(0,t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    distance=math.sqrt(((x2-x1)**2) +((y2-y1)**2))  #조규현과 백승환의 거리는 40
    if x1==x2 and y1==y2:                           #두 원의 좌표가 같을때
        if r1==r2:                                  #원의 반지름이 둘다 같을때 ※접점이 무한일때 이다.
            print(-1)
        else:                                       
            print(0)

    else:
        if r1>distance+r2 or r2>distance+r1 or distance>r1+r2:  #13>40+37 or 37>40+13 or 40>13+37 접점이 하나도 없을 때 distance를 이용해 테스트케이스 create
            print(0)
        elif abs(r1-r2)==distance or abs(r1+r2)==distance:      #두 원 사이 거리랑 distance가 같으면 접점은 한개
            print(1)
        else:
            print(2)                    


