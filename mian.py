import time


def mian():
    k = [
        {
            'k':99,
            'pq':[
                {'p':13,'q':17,'E':55},
                {'p':19,'q':31,'E':317},
                {'p':23,'q':37,'E':665},
                {'p':29,'q':41,'E':1093},
                {'p':23,'q':43,'E':779},
                {'p':29,'q':43,'E':631},
                {'p':31,'q':43,'E':1247},
                {'p':13,'q':43,'E':403},
                {'p':19,'q':37,'E':265},
                {'p':23,'q':41,'E':483},
                {'p':17,'q':37,'E':491},
            ]
        },
        {
            'k':9999,
            'pq':[
                {'p':503,'q':509,'E':240289},
                {'p':503,'q':541,'E':67327},
                {'p':503,'q':563,'E':218427},
                {'p':521,'q':563,'E':270879},
                {'p':541,'q':563,'E':277043},
                {'p':557,'q':563,'E':179191},
                {'p':521,'q':569,'E':150977},
                {'p':541,'q':569,'E':204659},
                {'p':557,'q':569,'E':186737},
                {'p':23,'q':41,'E':483},
                {'p':523,'q':569,'E':241697},
                {'p':23663,'q':23687,'E':499002979},
                {'p':23663,'q':23719,'E':440644537},
                {'p':23671,'q':23719,'E':265451239},
                {'p':23689,'q':23719,'E':317919649},
                {'p':23663,'q':23743,'E':523050071},
                {'p':23671,'q':23743,'E':550481201},
                {'p':23687,'q':23743,'E':301113629},
                {'p':23719,'q':23743,'E':319600325},
                {'p':23719,'q':23743,'E':319600325},
                {'p':23741,'q':23743,'E':135181049},
                {'p':23677,'q':23687,'E':265644109},
                {'p':569851,'q':569893,'E':93597556411},
                {'p':569869,'q':569893,'E':295033365569},
                {'p':569869,'q':569893,'E':295033365569},
                {'p':569887,'q':569893,'E':21724127005},
                {'p':569851,'q':569939,'E':220980716653},
                {'p':569851,'q':569939,'E':220980716653},
                {'p':569869,'q':569939,'E':240615060733},
                {'p':569893,'q':569939,'E':158125939199},
                {'p':569903,'q':569939,'E':94694338825},
                {'p':569861,'q':569903,'E':49450119631},
                {'p':569869,'q':569927,'E':296656868321},
                {'p':569893,'q':569927,'E':64023926669},
                {'p':26985551,'q':26985583,'E':701359714035323},
                {'p':26985571,'q':26985583,'E':186966363530833},
                {'p':26985559,'q':26985619,'E':81520590026039},
                {'p':26985577,'q':26985619,'E':376598558292431},
                {'p':26985551,'q':26985677,'E':290122345465419},
                {'p':26985559,'q':26985677,'E':270437477906711},
                {'p':26985577,'q':26985677,'E':480035735298941},
                {'p':26985587,'q':26985677,'E':79146167518537},
                {'p':26985659,'q':26985677,'E':182795845354627},
                {'p':26985571,'q':26985659,'E':274798124868997},
                {'p':4771212547,'q':7408868921,'E':15052772997031184561},
                {'p':4868747809,'q':5949670231,'E':16626600218558042753},
                {'p':7373533723,'q':3842610773,'E':6397280705233555615},
                {'p':7408868921,'q':9731236789,'E':29851397866082487941},
                {'p':5949670231,'q':2999999929,'E':10605590135834247289},
                {'p':4868747809,'q':3842610773,'E':3420430098564722699},
                {'p':7373533723,'q':9731236789,'E':40230650765004111245},
                {'p':7408868921,'q':9753236789,'E':23454776869484898807},
                {'p':5949670231,'q':2999999929,'E':11985265811310513161},
                {'p':4771212547,'q':2999999929,'E':12513510076550214601},
                {'p':10691097123712491259,'q':12345678901234567891,'E':102334299169378819062396764814592390933},
                {'p':11111111111111111011,'q':13337779797779999999,'E':61748409571487893182330324516123499987},
                {'p':11138479445180240497,'q':20212223242526272829,'E':89541539236266886837435650863872693369},
                {'p':12345678901234567891,'q':21576695089956874999,'E':151793987040994757605893640217037403783},
                {'p':13337779797779999999,'q':24681012141618202211,'E':217768863431619349612534332877152758001},
                {'p':20212223242526272829,'q':36484957213536676883,'E':123414559702833620248081457075860631115},
                {'p':21576695089956874999,'q':38775788043632640001,'E':334786032549728383876934161260505675711},
                {'p':24681012141618202211,'q':43252003274489855999,'E':760071406822345884412403881800851461851},
                {'p':36484957213536676883,'q':44444444443333332221,'E':1434581645891937663444534049387066185113},
                {'p':10691097123712491259,'q':44444444443333332221,'E':380489192406115331014545740916376343579},
            ]
        },
    ]


    results = []
    count = 0
    for y in k:
        for x in y['pq']:
            Q = ((x['p'] - 1) * (x['q'] - 1))
            N = x['p'] * x['q']
            E = x['E']
            D = calculateD(E, Q)
            passwordObj = encrypt(y['k'], E, N)
            decryptPass = decrypt(passwordObj['password'], D['d'], N)
            result = {
                'k': y['k'],
                'p': x['p'],
                'q': x['q'],
                'N': N,
                'Q': Q,
                'E': E,
                'D': D,
                'passwordObj':passwordObj,
                'decryptPass': decryptPass
            }
            count +=1
            writeAFile(result)
            print(result)
            print('\n --'+ str(count) +'-- \n')
            results.append(result)



def writeAFile(x):
    file = open("results.txt", "a+")
    file.write('k : ' + str(x['k']) + '\n')
    file.write('p : ' + str(x['p']) + '\n')
    file.write('q : ' + str(x['q']) + '\n')
    file.write('N : ' + str(x['N']) + '\n')
    file.write('Q : ' + str(x['Q']) + '\n')
    file.write('E : ' + str(x['E']) + '\n')
    file.write('D : ' + str(x['D']) + '\n')
    file.write('Sifre : ' + str(x['passwordObj']['password']) + '\n')
    file.write('Sifre Sure : ' + str(x['passwordObj']['passwordCreateTime']) + '\n')
    file.write('Sifre Cozulmus : ' + str(x['decryptPass']['number']) + '\n')
    file.write('Sifre Cozulmus Sure : ' + str(x['decryptPass']['passwordDecryptTime']) + '\n')
    file.write('========================================')
    file.write('\n')
    file.close()

def decrypt(password, D, N):
    start_time = time.time()
    number = (password**D)%N
    return {'number':number,'passwordDecryptTime':'{:f}'.format(time.time() - start_time)}

def encrypt(number, E, N):
    start_time = time.time()
    password = (number**E)%N
    return {'password':password,'passwordCreateTime':'{:f}'.format(time.time() - start_time)}

def calculateD(e, Q):
    start_time = time.time()
    d = modinv(e, Q)
    return {'d':d,'dTime':'{:f}'.format(time.time() - start_time)}

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

if __name__ == '__main__':
        mian()