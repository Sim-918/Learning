#ATM ->N명
#[p1,p2,p3,p4,p5]  N=5
#p1=3 p2=1 p3=4 p4=3 p5=2
#3+(3+1)+(3+1+4)+(3+1+4+3)+(3+1+4+3+2)
#3+4+8+11+13=39

#p2->p5->p1->p4->p3
#1+(1+2)+(1+2+3)+(1+2+3+3)+(1+2+3+3+4)


#p[0]+(p[0]+[1])+(p[0]+p[1]+p[2])+(p[0]+[1]+p[2]+p[3])+(p[0]+[1]+p[2]+p[3]+p[4])

#i=0,1,2,3,4  j=4,3,2,1,0
#  p[i]+                                =sum+=p[i-4]
# (p[i]+p[i+1])+                        =sum+=p[i-3]
# (p[i]+p[i+1]+p[i+2])+                  =sum+=p[i-2]
# (p[i]+p[i+1]+p[i+2]+p[i+3])+          =sum+=p[i-1]
# (p[i]+p[i+1]+p[i+2]+p[i+3]+p[i+4])     =sum+=p[i]
                                #         =sum+=p[j-i] j=4,3,2,1,0
'''
# for i in range(0,5):#i=0,1,2,3,4
#     sum+=Pn[i]
# print(sum)  #----->15

# for i in range(0,4):#i=0,1,2,3
#     sum+=Pn[i]
# print(sum)  #----->10

# for i in range(0,3):#i=0,1,2
#     sum+=Pn[i]
# print(sum)  #----->6

# for i in range(0,2):#i=0,1
#     sum+=Pn[i]
# print(sum)  #----->3

# for i in range(0,1):#i=0
#     sum+=Pn[i]
# print(sum)  #----->1
'''


n=int(input())
Pn=list(map(int,input().split()))
Pn.sort() 
ssum=0
for i in range(0,n):
    for j in range(0,i+1):
        ssum+=Pn[j]
print(ssum)

#i=0 j=0
#i=1 j=0,1
#i=2 j=0,1,2                               
#i=3 j=0,1,2,3
#i=4 j=0,1,2,3,4
