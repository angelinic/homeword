

a = input()
b = input()
c = input()
d = input()
e = input()
UserNameA = dict(User = a, cash = 500)
UserNameB = dict(User = b, cash = 500)
UserNameC = dict(User = c, cash = 500)
UserNameD = dict(User = d, cash = 500)
UserNameE = dict(User = e, cash = 500)
UserName=[UserNameA,UserNameB,UserNameC,UserNameD,UserNameE]


def pushCash():
    lit= input()
    for key in range(len(UserName)):
        if UserName[key]['User'] == lit:
            UserName[key]['cash'] += 500
    return (UserName)
print(pushCash())


def valueUser():
    let = input()
    for key in range(len(UserName)):
        if UserName[key]['User'] == let:
            print(UserName[key]['User'], UserName[key]['cash'])
        else :
            print('Error, no such user please try again')
valueUser()


def bankruptUser():
    let = input()
    for key in range(len(UserName)):
        if UserName[key]['User'] == let:
            UserName[key]['cash'] = 0
            print(UserName[key]['User'], str(UserName[key]['cash']) + 'you are bankrupt')
        else:
            print('Error, no such user please try again')
bankruptUser()