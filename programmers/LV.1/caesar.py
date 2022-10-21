import string

def solution(s, n):
    reslut=""
    base=""
    for i in s:
        if i in string.ascii_uppercase:   #이 모듈을 사용하면 알파벳의 대소문자를 모두 알수있음
            base=string.ascii_uppercase
        elif i in string.ascii_lowercase:
            base=string.ascii_lowercase
        else:
            reslut+=i
            continue
        a=base.index(i)+n                 #base의 위치를 찾은 후 n을 더함
        reslut+=base[a%len(base)]
    return reslut



