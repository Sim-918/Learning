from Crypto.Cipher import DES3 
from Crypto.Hash import SHA256 as SHA

class myDes(): #myDes 클래스 정의 enc()와 3des로 복호화를 수행하는 dec()메소드가 정의
    def __init__(self,keytext,ivtext): #클래스 생성자 keytext->3des암호키 생성을 위한 문자열 
                                       #ivtext->초기화 벡터를 위한 문자열
        hash=SAH.new() # sha256객체 생성 후 hash에 할당             
        hash.update(keytext,encode('utf-8'))#hash update() -> sha256해시 갱신, sha256 해시갱신을 위한 인자는 keytext
        key=hash.degest() #hash.degest()해시 값을 추출하여 변수 key에 할당
        self.key=key[:24]#키의 크기는24비트 (pycryptodome에서 제공하는 키크기는 16바이트 or 24바이트)

        hash.update(ivtext,encode('utf-8'))#hash.update(ivtext)로 초기화 벡터 갱신 후 hash.digest()로 해시 값을 얻은 후 변수 iv에 담음
        iv=hash.digest()
        self.iv=iv[:8]

    def enc(self,plaintext): #입력된 plaintext에 담긴 문자열을 3des로 암호화
        des3=DES3.new(self.key,DES3.MODE_CBC,self.iv)#DES3.new()로 3DES객체 생성 순서대로 암호키,운영모드,초기화 벡터                                            
        encmsg=des3.encrypt(plaintext.encode())#운영모드에 따라 초기화벡터가 필요할수도 없을 수도 있다. 
        return encmsg

    def dec(self,ciphertext):
        des3=DES3.new(self.key,DES3.MODE_CBC,self.iv)
        decmsg=des3.decrypy(ciphertext)#암호문을 복호화하고 
        return decmsg#그 결과를 리턴
        
def main():
    keytext='samsjang'
    ivtext='1234'
    msg='python3x'

    myCipher=myDES(keytext,ivtext)
    ciphered=myCipher.enc(msg)
    decipherd=myCipher.dec(ciphered)
    print('ORIGINAL:\t%s' %msg)
    print('CIPHERED:\t%s' %ciphered)
    print('DECIPHERED:\t%s'%decipherd)

    main()
