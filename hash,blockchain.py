################난이도의 따른 nonce값 구하기#############3
# from hashlib import sha256 as sha

# def hashcash(msg,difficulty):
#     nonce=0
#     print('+++Start')
#     while True:
#         target='%s%d'%(msg,nonce)               #target은 현재 Attack at 14PM!0 형태, nonce는 정수형(0,1,2,..)
#         ret=sha(target.encode()).hexdigest()    #target을 해시로 변환 후 ret에 저장

#         if ret[:difficulty]=='0'*difficulty:    #만약 ret이 리스트형식의 00~~~ 이면 찾음
#             print('++++Bingo')
#             print('++++>',ret)
#             print('--->nonce=%d'%nonce)
#             break
#         nonce+=1                                #nonce값이 0부터 계속해서 찾음

# def main():
#     mas='simsungbo'                             #simsungbo의 해시를 
#     difficulty=2
#     hashcash(mas,difficulty)

# main()
####################해시구하기###########################
# from hashlib import sha256

# msg='simsungbo139'
# sha=sha256()
# sha.update(msg.encode('utf-8'))
# ret=sha.hexdigest()
# print('SHA:',ret)


#simsungbo0 ->해시돌림
#simsungbo1
#simsungbo2.... simsungbo139->0087f4b5804b76096946c86dc46e146c522774d8faae9e86f20e7009382ecc13

