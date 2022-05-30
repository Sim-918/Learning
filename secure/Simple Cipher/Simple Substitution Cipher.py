def makeCodebook():

    decbook={'5':'a','2':'b','#':'d','8':'e','1':'f','3':'g','4':'h',\

             '6':'i','0':'l','9':'m','*':'n','%':'o','=':'p','(':'r',\

             ')':'s',';':'t','?':'u','@':'v',':':'y','7':' '}

    encbook={}

    for k in decbook:

        val=decbook[k]

        encbook[val]=k

 

    return encbook,decbook

 

def encrypt(msg,encbook):

    for c in msg:

        if c in encbook:

            msg=msg.replace(c,encbook[c])

 

    return msg

 

def decrypt(msg,decbook):

    for c in mag:

        if c in decbook:

            msg=msg.replace(c,decbook[c])

 

    return msg

 

if __name__=='__main__':
    h=open('plain.txt','rt')#plain파일을 읽기모두로 파일을 오픈 ※plain.txt가 있어야함
    content=h.read()
    h.close()

    encbook,decbook=makeCodebook()
    content=encrypt(content, encbook)

    h=open('encrytion.txt','wt+')#plain파일을 치환해 encrytion.txt로 생성 후 오픈
    h.write(content)
    h.close()
