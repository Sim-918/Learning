from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA
from os import path
KSIZE=1024

class myDES():#myDES 클래스 정의, myDES에는 암호화를 수행하는 enc()와 복호화를 수행하는 dec() 메소드 정의
    def __init__(self,keytext,ivtext):#클래스 생성자, keytext는 암호키를 생성하기 위한 문자열
        hash=SHA.new()#SHA256.new()->SHA256 객체을 만들고 hash에 할당
        hash.update(keytext.encode('utf-8'))#SHA256해시를 갱신, 사용된 인자는 keytext, 유니코드 문자열을 인자로 받지 않도록
        key=hash.digest()                                      #만약 유니코드 문자열을 받으면 오류발생
        self.key=key[:24]#(Pycryptodome에서 제공하는 3des의 키 크기는 16 or 24바이트),key의 값은 24byte, 키 값을 슬라이싱해 self.key에 할당
        
        hash.update(ivtext.encode('utf-8'))#초기화 벡터->64비트(64비트 암호화 블록크기)
        iv=hash.digest()#초기화벡터를 위한 해시 갱신->hash.digest()로 해시값을 얻은 후 변수 iv에 담음
        self.iv=iv[:8]#iv의 처음 8바이트를 초기화 벡터값으로 할당

    def makeEncInfo(self, filename):#filename으로 지정된 파일 크기를 구한 후
        fillersize=0#fileersize선언
        filesize=path.getsize(filename)#패키지from os import path으로 파일의 크기(byte)를 읽는다.
        if filesize%8!=0:#만약 filesize가 8바이트 배수가 아닐 경우
            fillersize=8-filesize%8#filesize를 8바이트 배수로 만들고 ->fillersize에 값을 할당
        filler='0'*fillersize#filllersize를 8의 배수로 만들기 위해 '0'문자열을 filler로 정의
        header='%d' %(fillersize)#fillersize의 0의 개수의 문자열을 정수로  ex)'00000'->5
        gap=8-len(header)#gap=8-(header의 길이)->header의 크기는 8바이트로
        header+='#'*gap#만약 header에 0의 개수가 5개 이면->5#######

        return header,filler#header, filler리턴
    
    def enc(self,filename):#암호화를 위한 enc함수->filename으로 지정된 파일 내용을 3DES로 암호화 한 후 새로운 파일에 저장하는 함수
        encfilename=filename+'.enc'#파일이름은 plain.txt.enc로
        header,filler=self.makeEncInfo(filename)#makeEncInfo(filename)을 호출하여 헤더와 '0'문자열을 얻고 각각 filler와 header에 담는다.
        des3=DES3.new(self.key,DES3.MODE_CBC,self.iv)#DES3,new(암호키,운영모드,초기화벡터) ※초기화 벡터가 있을 수도 없을 수도있다.
        
        h=open(filename,'rb')#바이너리 읽기 모드로 파일을 오픈
        hh=open(encfilename,'wb+')#바이너리 쓰기 모드로 파일 생성 후 오픈

        enc=header.encode('utf-8')#header를 enc로 바꾸는 작업
        content=h.read(KSIZE)
        content=enc+content
        while content:
            if len(content)< KSIZE:#만약 content의 길이가 KSZIZE(1KB)보다 작다면 
                content+=filler.encode('utf-8')#파일의 끝까지 읽음, content에 0을추가한다는 의미
            enc=des3.encrypt(content)#content를 3DES로 암호화하고 파일에 저장 한 후 
            hh.write(enc)#파일에서 다시 KSIZE만큼 읽어 
            content=h.read(KSIZE)#content에 담음
        h.close()#파일 닫기
        hh.close()#파일 닫기
    
    def dec(self,encfilename):#복호화 dec, encfilename으로 저장된 암호화된 파일 내용을 1KB(KSIZE)씩 읽어 3DES로 복호화 한 후 새로운 파일 만드는 함수
        filename=encfilename+'.dec'#파일이름의 .enc.dec확장자로 만드는 작업
        des3=DES3.new(self.key,DES3.MODE_CBC,self.iv)#DES3,new(암호키,운영모드,초기화벡터) ※초기화 벡터가 있을 수도 없을 수도있다.

        h=open(filename,'wb+')#복호화 된 내용을 저장된 파일을 쓰기 모드로 열고 h로 두고
        hh=open(encfilename,'rb')#암호화된 파일을 읽기 모드로 열고 hh에 할당

        content=hh.read(8)#최초 8바이트를 읽어 3DES로 복호화
        dec=des3.decrypt(content)
        header=dec.decode()
        fillersize=int(header.split('#')[0])#정수로 변환하여 '#'을 구분자로 header를 분리 한 후, 파일 끝부분에 추가된 '0'의 개수를 구함

        content=hh.read(KSIZE)#dec에서 KSIZE를 읽고 content에 담은 후
        while content:#while 진입
            dec=des3.decrypt(content)#content에 내용이 없을 때 까지 수행
            if len(dec)<KSIZE:#만약 dec의 길이가 KSIZE보다 작을 때
                if fillersize!=0:#만약 fillersize가 0이 아니면 
                    dec=dec[:-fillersize]#dec때 추가한 '0'문자열을 제거하고
            h.write(dec)#파일을 읽기
            content=hh.read(KSIZE)
        h.close()
        hh.close()
        
def main():
    keytext='samsjang'
    ivtext='1234'
    filename='plain.txt'
    encfilename=filename+'.enc'

    myCipher=myDES(keytext, ivtext)
    myCipher.enc(filename)
    myCipher.dec(encfilename)

if __name__=='__main__':
    main()
