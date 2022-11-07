# 3중 for문을 사용함 첫번째 i 즉 시간에서 j와 k 3이있는지...

h=int(input())
cnt=0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                cnt+=1
print(cnt)

