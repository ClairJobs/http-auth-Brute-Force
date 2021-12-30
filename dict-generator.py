import os

if os.path.exists("result.txt"):
    os.remove("result.txt")
fopen = open('result.txt','w')
for user in open('username.txt'):
    print(user)
    for password in open('password.txt'):
        userpassword = user.replace('\n','') + ':' + password
        fopen.write(userpassword)
fopen.close()
print('Done!')