ENC=0
DEC=1
#전역변수를 각각 0과1로 정의
def makeDisk(key): #암호키 key를 입력받아 카이사르 암호디스크 생성, enc_disk와 복호화를 위한 
                   #dec_disk를 생성후 return
    keytable=map(lambda x:(chr(x+65),x),range(26))#chr(65)->A chr(66)->B ...25번째(Z)까지
                                                  #keytable=[('A',0)('B',1),('C',2)....('Z',25)]이런식으로 리스트가 형성된다
    key2index={}#생성된 keytable을 {알파벳:문자인덱스}로 사전 자료를 만든다.->key2index={'A':0,'B':1,...'Z':25}
    for t in keytable:
        alphabet, index=t[0],t[1]
        key2index[alphabet]=index

    if key in key2index:
        k=key2index[key]
    else:
        return None,None #None은 값이 아무것도 없는 것

    enc_disk={}#enc_disk의 키는 평문문자고 값은 암호문 문자이다.
    dec_disk={}#dec_disk의 키는 암호문 문자이고 값은 평문문자이다.
    #만약암호키가 B라면 순서대로 B,C,D,E...Z,A가 된다.F면 F,G,H,I...Z,A,B,C,D,E,가 된다.
    for i in range(26):#i=0부터 25까지 반복
        enc_i=(i+k)%26 #이 라인이 Enc(i)=(i+k)mod 26을 구현한 것이다. 파이썬에서 mod의 연산은 %이다.
        enc_ascii=enc_i+65#대문자A는 ascii코드로 65, 그러므로 i를 0부터 순대로대로 더하면 ABC..식으로 코드 형성
        enc_disk[chr(i+65)]=chr(enc_ascii)#만약 key값이 5이면 enc_disk의 key는 ABCDE... 값은 (65+5)=F부터 FGHIJ..
        dec_disk[chr(enc_ascii)]=chr(i+65)#만약 key값이 5이면 19라인대로 반대로 dec_disk의 key는 FGHIJ..값은 ABCDE..

    return enc_disk,dec_disk

def caesar(msg,key,mode):#인자로 입력된 msg를 암호키 key로 암호문을 만들거나 암호문을 평문으로 만든다.mode는 암호화할것인지 복호화할것인지 나타냄
    ret=''#결과를 위해 빈 문자열 ret을 선언

    msg=msg.upper()
    enc_disk,dec_disk=makeDisk(key)#makeDisk(key)를 호출하고 

    if enc_disk is None:#만약 결과가 None이라면 빈 문자열 ret리턴
        return ret
    
    if mode is ENC:#만약mode가 ENC면 enc_disk를
        disk=enc_disk
    if mode is DEC:#만약mode가 DEC면 dec_disk를 변수 disk에 할당
        disk=dec_disk

    for c in msg: #msg의 각 문자 c가 
        if c in disk:#disk의 키로 존재하면 c가 키인 값 ret추가 
            ret +=disk[c]
        else:#키가 존재하지않으면 c를 ret에 추가
            ret +=c
    
    return ret

def main():
    plaintext='ABCDEFGHIJKLMNOPQRSTUVWXYZ'#plaintext가 이 문자열이고
    key='F'#키는 F

    print('Original:\t%s' %plaintext.upper()) #원본 plaintext
    ciphertext=caesar(plaintext, key, ENC)
    print('caesar cipher:\t%s'%ciphertext)#caesar
    deciphertext=caesar(ciphertext, key, DEC)
    print('Deciphered:\t%s' %deciphertext)#Deciphered

if __name__=='__main__':
    main()
