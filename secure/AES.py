from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
#3DES 모듈 ->Crypto.Cipher import DES3
#3DES의 암호화키와 초기화 벡터를 만들기위한 모듈->Cypto.Hash import SHA256 as SHA256
#CBC모드를 암호화 하기위해서는 초기화 벡터가 필요
class myAes():
    def __init__(self,keytext,ivtext):
        hash=SHA.new()
        hash.update(keytext,encode('utf-8'))
        key=hash.digest()
        self.key=key[:16]#메시지길이에 상관없이 암호화 가능하도록 메시지 길이는 16바이트 배수로 만들고 이에 대한 헤더정보를 포함하여 암호화

        hash.update(ivtext.encode('utf-8'))
        iv=hash.digest()
        self.iv=iv[:16]
    
    def makeEnabled(self,plaintext):#이 함수에서 padding을 정의
        fillersize=0#fillersize를 0으로 정의
        textsize=len(plaintext)# 만약 plaintex의 길이가 11이면
        if textsize%16!=0:#11%16!=0 16의 배수가 아님 
            fillersize=16-textsize%16# fillersize=15-(11%16) 15-11=4
        
        filler='0'*fillersize#그럼 0000가 filler에 할당
        header='%d'%(fillersize)#header는 fillersize의 0의 개수의 문자열을 정수로 4가됨
        gap=16-len(header)#gap은 16-4=12
        header+='#'*gap#header=header+'#'*gap 이므로 12############ 이런식으로 형성

        return header+plaintext+filler

    def enc(self,plaintext):
        plaintext=self.makeEnabled(plaintext)
        aes=AES.new(self.key,AES.MODE_CBC,self.iv)
        encmsg=aes.encrypt(plaintext.encode())
        return encmsg
    
    def dec(self,ciphered):
        aes=AES.new(self.iv,AES.MODE_CBC,self.iv)
        decmag=aes.decrypt(ciphertext)

        header=decmag[:16].decode()
        fillersize=int(header.split('#')[0])
        if fillersize!=0:
            decmag=decmag[16:-fillersize]
        else:
            decmag=decmag[16:]
        return decmag
# def main():
#     keytext='samsjang'
#     ivtext='1234'
#     msg='python3x'

#     myCipher=myDES(keytext, ivtext)
#     ciphered=myCipher.enc(msg)
#     deciphered=myCipher.dec(ciphered)
#     print('Origainal:\t%s'%msg)
#     print('Ciphered:\t%s'%ciphered)
#     print('Deciphered:\t%s'%deciphered)

#     main()
