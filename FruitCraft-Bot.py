import requests
import time
import datetime
import sys

def goldmine():
    cookies = {
        'FRUITPASSPORT': passport,
    }

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)',
        'Host': 'iran.fruitcraft.ir',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '34',
    }

    data = 'edata=Gk4KXVpRXRJDSEMTfmMXSA%3d%3d'

    response = requests.post('http://iran.fruitcraft.ir/cards/collectgold', headers=headers, cookies=cookies,
                             data=data, verify=False)

def buycard():
    cookies = {
        'FRUITPASSPORT': passport,
    }

    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)',
        'Host': 'iran.fruitcraft.ir',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '34',
    }

    data = 'edata=Gk4dSENREVxTRxw%3D'

    response = requests.post('http://iran.fruitcraft.ir/store/buycardpack', headers=headers, cookies=cookies,
                             data=data, verify=False)


def start_bot():
    maining_time = int((int(capacity) / (int(power) / 3600)))
    print('mine time is >> ', maining_time, ' sec')
    goldmine()
    done = 0
    lost = 0
    buy = 0
    for i in range(60000):

        try:
            time.sleep(maining_time)
            goldmine()
            done += 1
            sys.stdout.write('\r'+'Gold Mine Done  '+ str(done) + '  Gold Mine Lost '+ str(lost) + '  Cards Bought ' + str(buy))
            sys.stdout.flush()
        except:
            lost += 1
            sys.stdout.write('\r'+'Gold Mine Done  '+ str(done) + '  Gold Mine Lost '+ str(lost) + '  Cards Bought ' + str(buy))
            sys.stdout.flush()

        if buy == "Y" or buy == "y":
            try:
                buycard()
                sys.stdout.write('\r'+'Gold Mine Done  '+ str(done) + '  Gold Mine Lost '+ str(lost) + '  Cards Bought ' + str(buy))
                sys.stdout.flush()
            except:
                sys.stdout.write('\r'+'Gold Mine Done  '+ str(done) + '  Gold Mine Lost '+ str(lost) + '  Cards Bought ' + str(buy))
                sys.stdout.flush()



passport = input('Enter PassPort >> ')
buy = input('would you buy crystal card ?? (Y/N) >>> ')
power = input('how may is your manner power ? >> ')
capacity = input('how may is your Capacity ? >> ')

start_bot()
