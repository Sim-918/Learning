# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA

# def rsa_enc(msg):
#     private_key=RSA.generate(1024)
#     public_key=private_key.publickey()
#     cipher=PKCS1_OAEP.new(public_key)
#     encdata=cipher.encrypt(msg)
#     print(encdata)

#     cipher=PKCS1_OAEP.new(private_key)
#     decdata=cipher.decrypt(encdata)
#     print(decdata)

# def main():
#     msg='samsjang loves python'
#     rsa_encrypt(msg.encode('utf-8'))

#     main()

#3-1 RSA공개키 암호

# from Crypto.PublicKey import RSA

# def createPEM():
#     private_key=RSA.generate(1024)
#     h=open('privatekey.pem','wb+')
#     h.write(private_key.exportKey('PEM'))
#     h.close()

#     public_key=private_key.publickey()
#     h=open('publickey.PEM','wb+')
#     h.write(public_key.exportKey('PEM'))
#     h.close()

# createPEM()

#3-2 RSA 개인키,공개키 파일 만들기

# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA
# from Crypto.Hash import SHA256 as SHA

# def readPEM(pemfile):
#     h=open(pemfile,'r')
#     key=RSA.importKey(h.read())
#     h.close()
#     return key

# def rsa_enc(msg):
#     public_key=readPEM('publickey.PEM')
#     cipher=PKCS1_OAEP.new(public_key)
#     encdata=cipher.encrypt(msg)
#     return encdata

# def rsa_dec(msg):
#     private_key=readPEM('privatekey.pem')
#     cipher=PKCS1_OAEP.new(private_key)
#     decdata=cipher.decrypt(msg)
#     return decdata

# def main():
#     msg='samsjang loves python'
#     ciphered=rsa_enc(msg.encode('utf-8'))
#     print(ciphered)
#     deciphered=rsa_dec(ciphered)
#     print(deciphered)

# main()
#3-3 개인키,공개키 파일을 이용한 RSA공개키 암호

from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA

def readPEM(pemfile):
    h=open(pemfile,'r')
    key=RSA.importKey(h.read())
    h.close()
    return key
def rsa_sign(msg):
    private_key=readPEM('privatekey.pem')
    public_key=private_key.publickey()
    h=SHA.new(msg)
    signature=pkcs1_15.new(private_key).sign(h)
    return public_key,signature

def rsa_verify(msg,public_key,signature):
    h=SHA.new(msg)

    try:
        pkcs1_15.new(msg,public_key).verify(h, signature)
        print('Authentic')
    except Exception as e:
        print(e)
        print('Not Authentic')

def main():
    def createPEM():
        private_key=RSA.generate(1024)
        h=open('privatekey.pem','wb+')
        h.write(private_key.exportKey('PEM'))
        h.close()

        public_key=private_key.publickey()
        h=open('publickey.PEM','wb+')
        h.write(public_key.exportKey('PEM'))
        h.close()

    createPEM()
msg='My name is simsungbo'
public_key,signature=rsa_sign(msg.encode('utf-8'))
rsa_verify(msg.encode('utf-8'), public_key, signature)

main()


#3-4 RSA 공개키 서명



    
    
