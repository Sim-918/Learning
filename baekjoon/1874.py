from collections import deque
n=int(input())
push_arr=[]
pop_arr=[]
result=[]
for i in range(1,n+1):
    push_arr.append(i)
    pop_arr.append(int(input()))
    result.append('+')
    if push_arr[-1]==pop_arr[0]:
        while push_arr[-1]==pop_arr[0]:
            result.append('-')
            push_arr.pop(-1)
            pop_arr.pop(0)
            if len(push_arr)==0:
                break
if result.count('+')!=result.count('-'):
    print('NO')
else:
    for r in result:
        print(r)
# ar을 1부터 n까지 차례로 append 하는중(push) tmp배열의 popleft가 같으면 pop출력
