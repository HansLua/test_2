from random import randrange, choice
from string import ascii_lowercase
from time import ctime,time

tlds = ('org','edu','net','com','gov')
last9 = [str(x) for x in range(10)]
for i in range(randrange(100,120)):
    dtint = randrange(int(time())-31536000,int(time()))
    dtstr = ctime(dtint)
    llen = randrange(4,8)
    login = ''.join(choice(ascii_lowercase) for j in range(llen))
    dlen = randrange(llen,13)
    dom = ''.join(choice(ascii_lowercase) for j in range(dlen))
    phone = '1' + choice(['3','4','5','7','8']) + ''.join(choice(last9) for j in range(9))
    print("time->{}::email->{}@{}.{}::No->{}-{}-{}::phone->{}".format(
        dtstr,login,dom,choice(tlds),dtint,llen,dlen,phone
    ))
