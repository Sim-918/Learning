import random

word=[['resume','이력서'],['opening','공석,결원'],['applicant','지원자,신청자'],['requirement','필요조건']
      ,['meet','만족시키다']]

# 한개 씩 pop을 하면서 가야됨
break_point=len(word)
answer=random.randint(0,3)

while break_point>0:
    tmp=random.sample(word,1)
    print()


# while True:
#     tmp=random.sample(word,4)  #test중 랜덤하게 중복없이 4개 뽑음
#     answer=random.randint(0,3)    #0,1,2,3

#     print(f"{tmp[answer][0]}의 뜻은?: ")


#     for i in range(4):
#         print(f"{i+1}.{tmp[i][1]}")


#     print()
#     input_data=int(input("정답: "))
#     if input_data==answer+1:
#         print("정답")
#     elif input_data==0:
#         break
#     else:
#         print("오답",answer+1)
    
