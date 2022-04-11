# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import time
import requests
import datetime
import random
import multiprocessing.pool as multiprocessing
import getpass
import json
import threading
import sys
import uuid
import shutil
import zlib
import base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

l1 = '100077'
l2 = '100078'
os.system('rm -rf token.txt')
g = '\x1b[1;92m'
r = '\x1b[1;91m'
w = '\x1b[1;97m'
y = '\x1b[1;93m'
n = '\x1b[1;94m'
gu = '\x1b[1;95m'
sm = '\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')

logo = "\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m   Author      :     MAHDI HASAN     \n'\x1b[1;92m'   Github      :     MAHDI SHUVO  \n'\x1b[1;93m'   FB        :     https://web.facebook.com/m.mahdi.80\n'\x1b[1;94m'   TOOL TYPE   :     PAID COMMANDS\n'\x1b[1;96m'   WAP NUMBER  :     01887408882            \n"
dec = '2'
server = '2'
rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': rsauser,
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
fuck = []
idx = []
oks = []
cps = []

def main_apv():
    imt = '+MAHDI=='
    os.system('clear')
    print logo
    
    try:
        key1 = open('/sdcard/.android.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print '           You dont have subscrption'
        print '           Hello Dear Ya Cammonds Paid Han Or'
        print '           Ap Ke Subscription Nhi Ha Please Ap'
        print '           Admin Sa Rabta Kran Thanks'
        print '           Subscription Kelya Enter Press Kro'
        print '           Or Whatsapp Pa Rabta Kro Thanks'
        print ''
        myid = uuid.uuid4().hex[:10]
        print '         YOUR KEY : ' + myid + imt
        kok = open('/sdcard/.android.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print '           Ya Uper Wale Ap Ke KEY Ha'
        print '           Copy Kar Ka WhatsApp Pa Bhaj Dena'
        print ''
        print ''
        print ''
        print '     Agar Ap Na Subscription Kar Le Ha To'
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+8801887408882')

    r1 = requests.get('https://raw.githubusercontent.com/MAHDI-Shuvo/Mahdipaid1/main/mahdi.text').text
    if key1 in r1:
        main_system()
    else:
        os.system('clear')
        print logo
        print '           You dont have subscrption'
        print '           Hello Dear Ya Cammonds Paid Han Or'
        print '           Ap Ke Subscription Nhi Ha Please Ap'
        print '           Admin Sa Rabta Kran Thanks'
        print '           Subscription Kelya Enter Press Kro'
        print '           Or Whatsapp Pa Rabta Kro Thanks'
        print ''
        print '         YOUR KEY : ' + key1
        print ''
        print '           Ya Uper Wale Ap Ke KEY Ha'
        print '           Copy Kar Ka WhatsApp Pa Bhaj Dena'
        print ''
        print ''
        print ''
        print '     Agar Ap Na Subscription Kar Le Ha To'
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+8801887408882')


def main_system():
    
    try:
        token = open('token.txt', 'r').read()
    except:
        pass

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        m = q['name']
        print ''
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print 'Trun On Data An Then \t'
        print ''
    except:
        print '\x1b[1;91mToken on Chekpiont '
        os.system('rm -rf token.txt')

    os.system('clear')
