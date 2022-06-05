from hashlib import sha256 as sha
import codecs

def decodeBitcoinVal(bits):                     #원래의 bits값을 알아내는 함수->only bits
    decode_hex=codecs.getdecoder('hex_codec')
    binn=decode_hex(bits)[0]
    ret=codecs.encode(binn[::-1],'hex_codec')
    return ret

def getTarget(bits):
    bits=decodeBitcoinVal(bits)
    bits=int(bits,16)
    print('Bits=%x'%bits)
    bit1=bits>>4*6                              #target값을 구함
    base=bits&0x00ffffff

    sft=(bit1-0x3)*8
    target=base<<sft

    print('Target=%x'%target)

Bits='f2b9441a'                                 #현재 bits의 값은 little endian으로 변환 후이다.
getTarget(Bits)

