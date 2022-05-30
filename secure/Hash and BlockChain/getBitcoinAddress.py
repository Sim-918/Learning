import os 
import hashlib 
from hashlib import sha256 as sha
from base58check import b58encode
import ecdsa


def ripemd160(x):
    ret=hashlib.new('ripemd160')
    ret.update(x)
    return ret

def generateBitcoinAddress():
    #개인키 생성 후 지갑에 보관(WIF절차)
    privkey=os.urandom(32)                                          #32비트의 랜덤한 개인키 생성
    fullkey='80'+privkey.hex()                                      #16진수문자열로 변경

    a=bytes.fromhex(fullkey)                                        #16진수로 된 fullkey를 byte 객체로 변환
    sha_a=sha(a).digest()
    sha_b=sha(sha_a).hexdigest()
    c=bytes.fromhex(fullkey+sha_b[:8])

    #WIF(Wallet Import Format)->비트코인 거래를 위한 약식개인키
    WIF=b58encode(c)

    #NO.1 개인키를 이용해 ECDSA 공개키 획득
    signing_key=ecdsa.SigningKey.from_string(privkey,curve=ecdsa.SECP256k1)
    verifying_key=signing_key.get_verifying_key()
    pubkey=(verifying_key.to_string()).hex()

    #NO.2 ECDSA 공개키의 앞부분에 '0x04'를 추가함
    pubkey='04'+pubkey

    #NO.3 2단계에서 얻는 값의 SHA-256해시값을 얻고, 이 해시값에 RIPEMD-160을 적용한 값을 얻음
    #RIPEMD-160은 MD4기반의 해시 알고리즘, 32비트 연산에 최적
    pub_sha=sha(bytes.fromhex(pubkey)).digest()
    encPubkey=ripemd160(pub_sha).digest()

    #NO.4 3단계에서 얻은 값을 '0x00'을 추가
    encPubkey=b'\x00'+encPubkey

    #NO.5 4단계에서 얻은 값의 SHA-256 해시값을 얻음
    chunk=sha(sha(encPubkey).digest()).digest()

    #NO.6 5단계에서 얻는 값의 첫 4바이트를 체크섬이라 정의
    checksum=chunk[:4]

    #NO.7 4단계에서 얻는 encPubkey에 체크섬을 더함
    hex_address=encPubkey+checksum

    #NO.8 7단계에서 얻은 값의 Base58인코딩 한 값을 비트코인 주소로 함
    bitcoinAddress=b58encode(hex_address)

    #WIF와 생성된 비트코인 주소 출력
    print('+++WIF=',WIF.decode())
    print('+++Bitcont Address=',bitcoinAddress.decode())

generateBitcoinAddress()
#########################
# import os
# privkey=os.urandom(32)
# print("privkey=",privkey)
# fullkey='80'+privkey.hex()
# print("fullkey=",fullkey)
# a=bytes.fromhex(fullkey) 
# print("byte Format=",a)                                  
