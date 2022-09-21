import sys
input=sys.stdin.readline
n=input()
def solution(dartResult):
    dic = {"S": 1, "D": 2, "T": 3}
    dartResult = dartResult.replace("10", "X")
    stack = []

    for i in dartResult:
        if i.isdigit() or i == "X":
            stack.append(10 if i == "X" else int(i))
        elif i in ["S", "D", "T"]:
            num = stack.pop()
            stack.append(num ** dic[i])
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2 * num)


    return sum(stack)

print(solution(n))
