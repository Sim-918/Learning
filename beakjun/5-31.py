'''
input=11 ->회의 수
1 4      ->1,2,3,4                      ->1
3 5      ->3,4,5                        ->x
0 6      ->0,1,2,3,4,5,6                ->x
5 7      ->5,6,7                        ->2
3 8      ->3,4,5,6,7,8                  ->x
5 9      ->5,6,7,8,9                    ->x
6 10     ->6,7,8,9,10                   ->x
8 11     ->9,10                         ->3
8 12     ->9,10,11                      ->x
2 13     ->3,4,5,6,7,8,9,10,11,12       ->x
12 14    ->13                           ->4
'''

#testcase #1 j를 stack으로 쌓는다
#testcase #2 만약 stack안에 같은 j가 2개 이상있다면 count->x continue
#testcase #3 없으면 append and count+=1

'''
for j in range(rt[0],rt[1]+1):
        #print(j) 
'''

n=int(input())
count=0
stack=[]
for i in range(0,n):
    rt=list(map(int,input().split()))
    for j in range(rt[0],rt[1]+1):
        stack.append(j)        #j=[1,2,3,4]
        
print(stack)
    
#stack에 j를 쌓음 ->스택
# stack=[]
# for i in range(0,4):
#     stack.append(i)
# print(stack)
