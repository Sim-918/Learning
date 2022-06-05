############zipcracker############
import zipfile
from threading import Thread

def crackzip(zfile,passwd):
    try:                                                                    
        zfile.extractall(path='/test',pwd=passwd)                          #test dir 에서 zfile의 passwd를 패스워드로 해 zfile의 모든 내용에 압축해제시도
        print('ZIP file extracted successfully! PASS=[%s]'%passwd.decode()) #압축성공
        return True
    except:
        pass
    return False

def main():
    dictfile='dictionary.txt'
    zipfilename='locked.zip'                                            #암호가 걸림 zip파일
    zfile=zipfile.ZipFile(zipfilename,'r')                              #zfile을 읽음
    pfile=open(dictfile,'r')                                            #dictfile파일을 읽음

    for line in pfile.readlines():                                      #pfile을 한 라인씩 읽는다.
        passwd=line.strip('\n')                                         #줄바꿈을 제거하고
        t=Thread(target=crackzip,args=(zfile,passwd.encode('utf-8')))   #passwd에 담는다. 그 후 crackzip함수를 쓰레드로 호출
        t.start()
main()
