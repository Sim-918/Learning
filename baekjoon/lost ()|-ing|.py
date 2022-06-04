'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''
import sys
input=sys.stdin.readline

n=list(input())

for i in range(len(n)-1):
    if n[i]=='-' or n[i]=='+':
        print(i)
        #-가 들어오면 -다음부터 모두 더하고 음수로 바꿈
    # elif n[i]=='+':
    #     print(i)
    #     #+가 들어오면 
