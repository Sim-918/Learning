import random

word=[['a','에이'],['b','비'],['c','씨'],['d','디'],['e','이'],['f','에프'],]

sunji=random.sample(range(len(word)),4)
sunji_arr=[]

# 선지를 word전체에서 가져옴
for i in sunji:
    sunji_arr.append(word[i])


# 다음 루프 때 만약 ans_arr가 not in하면 루프반복
# 있으면 다음 랜덤 찾기
# len(word)와 len(ans)의 길이가 같아지면 반복문 종료
ans=random.sample(sunji_arr,1)
# ans_arr=[]
# if ans in ans_arr:
#     print("겹침")

print(f"문제-->",ans[0][0])

# ans_arr.append(ans[0][0])
# print(ans_arr)


for i in range(len(sunji_arr)):
    print(f"{i+1}",sunji_arr[i][1])

user_input=int(input("정답: "))-1    # 4

if sunji_arr[user_input][1]==ans[0][1]:
    print("correct")
else:
    print("you dead")









# while True:
#     test=random.sample(word,4)
#     sunji=random.randint(0,3)
#     tmp=test[sunji][0]

#     print(tmp,"의 정답은?")
#     for i in range(4):
#         print(f"{i+1}",test[i][1])

#     user_input=int(input("답: "))-1

#     if user_input==-1:
#         break
#     if sunji==user_input:
#         print("정답")
#     else:
#         print("오답")

    

