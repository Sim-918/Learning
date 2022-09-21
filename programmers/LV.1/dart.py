import sys
input=sys.stdin.readline
n=input()
def solution(dartResult):
    dic = {"S": 1, "D": 2, "T": 3}
    #딕셔너리 형식으로 SDT를 정의함
    dartResult = dartResult.replace("10", "X")
    #10이라는 정수가나오면 X
    stack = []
    #민약 1S2D*3T 이라는 input이 있다면
    for i in dartResult:                #i=1,S,2,D,*,3,T
        #isdigit->dartResult이 숫자로 이뤄졌는지
        if i.isdigit() or i == "X":
            #여기서 10이라는 정수를 잡아주면서 append한다
            stack.append(10 if i == "X" else int(i))      
       
        elif i in ["S", "D", "T"]:          #만약 i에 SDT라는 문자가 있으면
            num = stack.pop()               #stack=[pop을 당하 후의 값] num=stack의 마지막을 없앤 값
            stack.append(num ** dic[i])     #dic의 있는 i를 정수를 제곱
        elif i == "#":                  #i에 #이라는 문자가 있으면
            stack[-1] *= -1             #stack의 끝에 있는 리스트를 -1로 만듦
        elif i == "*":                  #i에 *이라는 문자가 있으면
            num = stack.pop()           #pop하고
            if len(stack):              
                stack[-1] *= 2
            stack.append(2 * num)


    return sum(stack)
  
print(solution(n))

# a=['a','b','c','d','e']
# q=a.pop()
# # for i in a:
# #     print(i)
# print(a)
# print(q)

