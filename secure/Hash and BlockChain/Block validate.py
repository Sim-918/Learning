from ast import Pow
from base64 import decode
from email import header
from hashlib import sha256 as sha
import codecs



#####require little-endian#################
# def stR(num):
#     s=''
#     for i in range(len(num)-1,0,-2):
#         s += num[i-1:i+1]
#     return s
# a='00000000000008a3a41b85b8b29ad444def299fee21793cd8b9e567eab02cd81'
# print(stR(a))

#######131028 floor Block validatePow########
###############131028 block value################
#   prev 39cb4aea452a9a3e3668501d54aa17c83b6205ec51067bf3bd0c000000000000
#   merkle 4790a3b218b8e7052a33d66fdfaf2317f09ecc6aaac51f9104a3fd520b51478d
#   nonce 1113530375
#   bits 438145839
#   time 1308142052

def decodeBitcoinVal(bits):
    decode_hex=codecs.getdecoder('hex_codec')
    binn=decode_hex(bits)[0]
    ret=codecs.encode(binn[::-1],'hex_codec')
    return ret
def getTarget(bits):
    bits=int(hex(bits),16)
    bit1=bits>>4*6
    base=bits&0x00ffffff

    sft=(bit1-0x3)*8
    target=base<<sft
    return target

def validatePoW(header):
    block_version=header[0]
    hashPervBlock=header[1]
    hashMerkleRoot=header[2]
    Time=header[3]
    Bits=header[4]
    nonce=header[5]

    decode_hex=codecs.getdecoder('hex_codec')
    
    bits_str=str(hex(Bits))[2:]
    nonce_str=str(hex(nonce))[2:]
    ts_str=str(hex(Time))[2:]

    header_hex=block_version+hashPervBlock+hashMerkleRoot+decodeBitcoinVal(ts_str).decode()+decodeBitcoinVal(bits_str).decode()+decodeBitcoinVal(nonce_str).decode()
    header_bin=decode_hex(header_hex)[0]

    hash=sha(header_bin).digest()
    hash=sha(hash).digest()
    Pow=codecs.encode(hash[::-1],'hex_codec')

    target=getTarget(Bits)
    target=str(target)
    target='0'*(66-len(target))+target[:]

    print('target\t=',target)
    print('PoW\t=',Pow)

    if int(Pow,16)<=int(target,16):
        print('+++ Accept this Block')
    else:
        print('--- Reject this Block')

###put in the block  value###
#caution: hashprev,merkleroot is little endian and time,bits,nonce is integer
block_version=''
hashPrevBlock=''
hashMerkleRoot=''
Time=                 #only unix timestamp value
Bits=
nonce=

header=[block_version,hashPrevBlock,hashMerkleRoot,Time,Bits,nonce]
validatePoW(header)

#SHA-256(version+prevblockhash+murkleroothash+time+bits+nonce)<=target  ----->block accept
