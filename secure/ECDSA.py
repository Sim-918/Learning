# from Crypto.PublicKey import ECC

# def createPEM_ECDSA():
#     key=ECC.generate(curve='P-256')
#     with open('privkey_ecdsa.pem','w') as h:
#         h.write(key.export_key(format='PEM'))
    
#     key=key.public_key()
#     with open('pubkey_esdas.pem','w') as h:
#         h.write(key.export_key(format='PEM'))

# createPEM_ECDSA()

#ECDSA 개인키, 공개키 파일 만들기

from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256 as SHA

def readPEM(pemfile):
    with open(pemfile,'r') as h:
        key=ECC.import_key(h.read())
    return key

def ecdsa_sign(msg):
    privateKey=readPEM_ECC('privkey_ecdsa.pem')
    sha=SHA.new(msg)
    signer=DSS.new(privateKey,'fips-183-3')
    signature=signer.sign(sha)
    return signature

def ecdsa_verify(msg,signature):
    publicKey=readPEM_ECC('pubkey_ecdsa.pem')
    sha=SHA.new(msg)
    verifier=DSS.new(publicKey, 'fips-183-3')
    try:
        verifier.verify(sha, signature)
        print('Authentic')
    except ValueError:
        print('Not Authentic')

def main():
    def createPEM_ECDSA():
        key=ECC.generate(curve='P-256')
        with open('privkey_ecdsa.pem','w') as h:
            h.write(key.export_key(format='PEM'))
        
        key=key.public_key()
        with open('pubkey_esdas.pem','w') as h:
            h.write(key.export_key(format='PEM'))

    createPEM_ECDSA()
    msg='My name is simsungbo'
    signature=ecdsa_sign(msg.encode('utf-8'))
    ecdsa_verify(msg.encode('utf-8'), signature)

    main()
#ECDSA 전자서명
    
