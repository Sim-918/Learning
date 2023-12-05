import random

word = []
# 문자열 정리 코드
while True:
    input_1 = input("done 입력 시 종료: ")
    if input_1.lower() == 'done':
        break
    
    word_translation = [x.strip() for x in input_1.split('\t', 1)]
    
    word.append(word_translation)

sunji_list=word+word[:3]

correct_cnt=0
now_cnt=len(word)

X=[]

for i in range(len(word)):
    tmp=word.pop(i)
    sunji=[tmp]+random.sample(word,3)
    random.shuffle(sunji)
    print("문제: ",tmp[0])

    for k in range(len(sunji)):
        print(k+1,sunji[k][1])

    n=int(input("정답 ?: ")) 

    word.insert(i,tmp)

    if word[i]==sunji[n-1]:
        correct_cnt+=1
        # print("정답")
    else:
        X.append(word[i])
        # print("오답")
    
print(f"총 문항수 : ",len(word),end=' ')
print(f"맞춘 수: ",correct_cnt)
print("틀린문제",X)
