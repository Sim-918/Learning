'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 
그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''
import sys
input=sys.stdin.readline

n=input().split("-")
ans=0

for i in n[0].split("+"):       #split함수를 통해 n[0]은 "-"가 나오기 바로 전
    ans+=int(i)

for i in n[1:]:                 #n[:1]->"-"함수 뒤부터
    for j in i.split("+"):      #"+"를 기준으로
        ans-=int(j)             
print(ans)
