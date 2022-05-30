#only 3kg 5kg
#18-> 5, 5, 5, 3 5kg=3 3kg=1

#######if 3~20 in the testcase#########

#test case #1 나누어 지는 수
#20,19,18,17,16,15,14,13,12,11,10,9,8,6,5,3

#test case #2  5kg,3kg 둘 중 하나만 필요한 수   n%5==0 and n%3==0
#20,15,12,10,9,6,5,3

#test case #3 5의 배수거나 3의 배수인 수    n%5==0 or n%3==0
#20,18,15,12,10,9,6,5,3

#test case #4 5kg과 3kg모두 담아야 되는 수  
#19,18,17,16,14,13,11,8

#test case #5 3,5배수가 아닌 수
#19,17,16,14,13,11,8,

#test case #2 나누어 지지 않는 수
#7,4   ..22

n=int(input())
box=0
while n>=0:
    if n%5==0:
        box=box+n//5
        print(box)
        break
    n-=3
    box+=1
else:
    print(-1)

