############caesar brute force attack############
def makeDisk(k):                  
    dec_disk={}                             #dec_disk는 사전형식으로 정의
    for i in range(26):                     #i는 0~25
        alp=(i+k)%26+65                     #alp를 i(0~25)와 k(1~25)더하고 26으로 나눈 대문자 A아스키코드의 번호 65를 더해서 할당
        dec_disk[chr(alp)]=chr(i+65)        #dec_disk[문자]=i를 더한 알파벳형태
    return dec_disk                         #dec_disk 리턴

def caesar(msg,key):
    ret=''                                  
    msg=msg.upper()                         
    disk=makeDisk(key)                      #attack 함수에서 key값을 얻고 makeDisk에 key값을 넣고 호출한뒤 disk에 할당, makeDisk에서 dec_disk를 반환받았음
    for c in msg:                           
        if c in disk:                       #만약 disk에 c가 있다면 
            ret+=disk[c]                    #반복문을 통해 c를 disk에 계속 리스트타입으로 더함
        else:                               #아니면
            ret+=c                          #ret에 c를 더함
    return ret                              #ret 리턴


def attack(msg):
    for key in range(1,26):                 #key값은 1~25
        decmsg=caesar(msg,key)              #caesar함수에 평문과 키값을 넣어 호출한 뒤 decsmg에 할당
        print('SHIFIT[%d]:%s'%(key,decmsg)) #caesar함수를 통해 리턴된 key와 decmsg출력


if __name__=='__main__':
    msg='UGAMKZMBSMGQAVCU'                  #평문
    attack(msg)                             #attack함수 호출
############frequency_analysis############
# def frequency_analysis(msg):
#     fa={}
#     for c in msg:
#         if c in fa:
#             fa[c]+=1
#         else:
#             fa[c]=1
#     print(sorted(fa.items(),key=lambda x:x[1],reverse=True))

# if __name__=='__main__':
#     msg='asdashglcxmbnvbgn;ghdsa;fj#!@%&%@#%&^%*^@$qweqsadasfjklczxxcb%#^@#$@#$'
#     frequency_analysis(msg)
############zipcracker############
# import zipfile
# from threading import Thread

# def crackzip(zfile,passwd):
#     try:
#         zfile.extractall(path='./test',pwd=passwd)
#         print('ZIP file extracted successfully! PASS=[%s]'%passwd.decode())
#     except:
#         pass
#     return False

# def main():
#     dictfile='dictionary.txt'
#     zipfilename='locked.zip'
#     zfile=zipfile.ZipFile(zipfilename,'r')
#     pfile=open(dictfile,'r')

#     for line in pfile.readlines():
#         passwd=line.strip('\n')
#         t=Thread(target=crackzip,args=(zfile,passwd.encode('utf-8')))
#         t.start()
# main()


###212page~223page skip  233page까지
#5장1번
