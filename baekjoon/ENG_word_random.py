import random

word=[
    ['resume', '이력서'],
    ['opening', '개장, 공석'], 
    ['applicant', '지원자'], 
    ['requirement', '필요조건'],
    ['meet', '만족시키다'],
    ['qualified', '적격의,자격있는'],
    ['candidate', '후보자'],
    ['confidence', '확신'],
    ['highly', '매우'],
    ['professional', '전문적인'],
    ['interview', '면접'],
    ['hire', '고용'],
    ['training', '교육'],
    ['reference', '참조'],
    ['position', '일자리'],
    ['achievement', '성취'],
    ['impressed', '감명을 받은'],
    ['excellent', '훌룡한'],
    ['eligible', '자격이있는'],
    ['identify', '찾아내다, 확인하다'],
    ['associate', '관련시키다'],
    ['condition', '조건'],
    ['employment', '고용'],
    ['lack', '~이 없다'],
    ['managerial', '관리의'],
    ['diligent', '성실한'],
    ['familiar', '익숙한'],
    ['proficiency', '능숙함'],
    ['prospective', '장래의'],
    ['appeal', '매력, 주목을 끌다'],
    ['specialize', '전문화하다'],
    ['apprehensive', '걱정하는'],
    ['consultant', '상담자,조언자'],
    ['entitle', '자격 부여하다'],
    ['degree', '학위'],
    ['payroll', '급료, 임금대장'],
    ['recruit', '모집하다'],
    ['certification', '증명성'],
    ['occupation', '직업'],
    ['wage', '임금, 급료']
]
sunji_list=word*2

cnt=0

# 틀린문제
X=[]

for i in range(len(word)):
    test=[word[i][1]]
    print(f"문제: ",word[i][0])
    tmp=sunji_list[i+1:i+4]
    for j in tmp:
        test.append(j[1])
    random.shuffle(test)
    print(test)
    user_input=int(input())
    if word[i][1]==test[user_input-1]:
        cnt+=1
        print("correct")
    else:
        X.append(word[i])
        print("worn")

print(f"문항수 : ",len(word))
print(f"맞춘 수: ",cnt)
print("틀린문제",X)
