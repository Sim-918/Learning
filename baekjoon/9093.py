import sys

n=int(input())
arr=[]
st=""
for _ in range(n):
    word=input().split()
    for i in word:
        print(i[::-1],end=' ')
    print()
