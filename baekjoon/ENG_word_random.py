import random

word = []
# 문자열 정리 코드
while True:
    input_1 = input("done 입력 시 종료: ")
    if input_1.lower() == 'done':
        break
    
    word_translation = [x.strip() for x in input_1.split('\t', 1)]
    
    word.append(word_translation)

sunji_list=word*2

correct_cnt=0
now_cnt=len(word)

# 틀린문제
X=[]

for i in range(len(word)):
    print('-'*10)
    print("남은 문항 수:",now_cnt)
    now_cnt-=1
    test=[word[i][1]]
    print(f"문제: ",word[i][0])
    tmp=sunji_list[i+1:i+4]
    for j in tmp:
        test.append(j[1])
    random.shuffle(test)
    for p in range(len(test)):
        print(p+1,test[p])
    user_input=int(input("정답: "))
    if word[i][1]==test[user_input-1]:
        correct_cnt+=1
    else:
        X.append(word[i])


print(f"총 문항수 : ",len(word),end=' ')
print(f"맞춘 수: ",correct_cnt)
print("틀린문제",X)
