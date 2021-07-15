# import :
# socket
# time
# requests
# ipdata
# pprint
import socket
import time
red = '\033[0;31m'
wh = '\033[0;37m'

print(red+'''
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////░██████╗░░░░░░░██████╗░░█████╗░░█████╗░██╗░░██╗//////////////////////////////////////
///////////////////////////////////██╔════╝░░░░░░░██╔══██╗██╔══██╗██╔══██╗██║░██╔╝//////////////////////////////////////
///////////////////////////////////██║░░██╗░█████╗██████╔╝███████║██║░░╚═╝█████═╝░//////////////////////////////////////
///////////////////////////////////██║░░╚██╗╚════╝██╔═══╝░██╔══██║██║░░██╗██╔═██╗░//////////////////////////////////////
///////////////////////////////////╚██████╔╝░░░░░░██║░░░░░██║░░██║╚█████╔╝██║░╚██╗//////////////////////////////////////
///////////////////////////////////░╚═════╝░░░░░░░╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝//////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////''')
ch = input(wh + '''
[?] Choose And Enter :
[1] My ip info 
[2] Get ip info
[3] Get Domain info
[4] Username Searcher
[EXIT] "Press >Enter< To exit"
➤''')

if ch == '':
        print("[+] exit done ")
        exit()

elif ch == '1':
    print('''
▒█▀▄▀█ ▒█░░▒█ 　 ▀█▀ ▒█▀▀█ 
▒█▒█▒█ ▒█▄▄▄█ 　 ▒█░ ▒█▄▄█ 
▒█░░▒█ ░░▒█░░ 　 ▄█▄ ▒█░░░ 
by @3b_r
▀█▀ ▒█▄░▒█ ▒█▀▀▀ ▒█▀▀▀█ 
▒█░ ▒█▒█▒█ ▒█▀▀▀ ▒█░░▒█ 
▄█▄ ▒█░░▀█ ▒█░░░ ▒█▄▄▄█ 　   
''')
    hostname = socket.gethostname()
    cr = "[+]"
    print(cr + f" Device name ➤➤➤ {hostname}")
    from requests import get
    ip = get('https://api.my-ip.io/ip').text
    print('[+] Your ip address ➤➤➤ {}'.format(ip))
    pll = "[+]"
    print('''
    [+] info your ip address:
    please wait to get info....
    ''')
    from ipdata import ipdata
    from pprint import pprint
    ipdata = ipdata.IPData('d5c0fc206b3d9c6787081c46b4c974a95cf844131fa3175218158a4f')
    response = ipdata.lookup(ip)
    print(pll, pprint(response))
    time.sleep(3)
elif  ch == "2" :
    print('''
▀█▀ ▒█▀▀█ 
▒█░ ▒█▄▄█ 
▄█▄ ▒█░░░ 
by @3b_r
░▀░ █▀▀▄ █▀▀ █▀▀█ 
▀█▀ █░░█ █▀▀ █░░█ 
▀▀▀ ▀░░▀ ▀░░ ▀▀▀▀''')
    ip = input(str('Enter the ipv4 or ipv6 ➤ '))
    pll = "[+]"
    from ipdata import ipdata
    from pprint import pprint
    ipdata = ipdata.IPData('d5c0fc206b3d9c6787081c46b4c974a95cf844131fa3175218158a4f')
    response = ipdata.lookup(ip)
    print(pll,pprint(response))
elif ch == '3' :
    print('''
▒█▀▀▄ ▒█▀▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀█▀ ▒█▄░▒█ 
▒█░▒█ ▒█░░▒█ ▒█▒█▒█ ▒█▄▄█ ▒█░ ▒█▒█▒█ 
▒█▄▄▀ ▒█▄▄▄█ ▒█░░▒█ ▒█░▒█ ▄█▄ ▒█░░▀█ 
by @3b_r
▀█▀ ▒█▄░▒█ ▒█▀▀▀ ▒█▀▀▀█ 
▒█░ ▒█▒█▒█ ▒█▀▀▀ ▒█░░▒█ 
▄█▄ ▒█░░▀█ ▒█░░░ ▒█▄▄▄█
    ''')
    def get_info_by_domain(domain_name):
        try:
            ip_addr = socket.gethostbyname(domain_name)
            print("ip address ➤➤➤ ", ip_addr)
        except Exception as exp:
            print(exp)
    my_domain = input("[?] Enter a Domain ➤ ")
    get_info_by_domain(my_domain)
    from ipdata import ipdata
    from pprint import pprint
    ipdata = ipdata.IPData('d5c0fc206b3d9c6787081c46b4c974a95cf844131fa3175218158a4f')
    response = ipdata.lookup(socket.gethostbyname(my_domain))
    pll = '[+]'
    print(pll, pprint(response))
elif ch == '4' :
    print('''
▒█░▒█ ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ 
▒█░▒█ ░▀▀▀▄▄ ▒█▀▀▀ ▒█▄▄▀ 
░▀▄▄▀ ▒█▄▄▄█ ▒█▄▄▄ ▒█░▒█ 
by @3b_r
▒█▀▀▀█ ▒█▀▀▀ ░█▀▀█ ▒█▀▀█ ▒█▀▀█ ▒█░▒█ ░░ ▒█▀▀▀ ▒█▀▀█ 
░▀▀▀▄▄ ▒█▀▀▀ ▒█▄▄█ ▒█▄▄▀ ▒█░░░ ▒█▀▀█ ▀▀ ▒█▀▀▀ ▒█▄▄▀ 
▒█▄▄▄█ ▒█▄▄▄ ▒█░▒█ ▒█░▒█ ▒█▄▄█ ▒█░▒█ ░░ ▒█▄▄▄ ▒█░▒█''')
    import requests

    username = input("[?] Enter the username ➤ ")
    url1 = (f"https://www.facebook.com/{username}")
    url2 = (f"https://www.twitter.com/{username}")
    url3 = (f"https://www.tiktok.com/@{username}")
    url4 = (f"https://www.instagram.com/{username}/")
    url5 = (f"https://www.github.com/{username}/")
    url6 = (f"https://www.snapchat.com/add/{username}")
    url7 = (f"https://www.soundcloud.com/{username}")

    rsp1 = requests.get(url1)
    if rsp1.status_code == 200:
        print("[+]  Facebook ➤➤➤" + url1)
    else:
        print("[-] Not Found Facebook !")
    # ----------------------------------------------------------------------------------------------
    rsp2 = requests.get(url2)
    if rsp2.status_code == 200:
        print('[+] Twitter ➤➤➤ ' + url2)
    else:
        print('[-] Not found acc twitter !')
    # -----------------------------------------------------------------------------------------
    rsp3 = requests.get(url3)
    if rsp3.status_code == 200:
        print("[+] Tiktok ➤➤➤ " + url3)
    else:
        print("[-] Not found acc tiktok !")
    # ----------------------------------------------------------------------------------------
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    rsp4 = requests.get(url4, headers=headers)
    if rsp4.status_code == 200:
        print("[+] Instagram ➤➤➤" + url4)
    else:
        print("[-] Not Found Instagram !")
    # -------------------------------------------------------------------------------------------------------
    rsp5 = requests.get(url5)
    if rsp5.status_code == 200:
        print("[+] GitHub ➤➤➤ " + url5)
    else:
        print("[-] Not Found acc GitHub !")
    # -------------------------------------------------------------------------------------------------------
    rsp6 = requests.get(url6)
    if rsp6.status_code == 200:
        print("[+] Snapchat ➤➤➤ " + url6)
    else:
        print("[-] Not Found Snapchat !")
    # ---------------------------------------------------------------------------------------------------------
    rsp7 = requests.get(url7)
    if rsp7.status_code == 200:
        print("[+] Soundcloud ➤➤➤ " + url7)
    else:
        print("[-] Not Found Soundcloud ! ")
    print("[+] Done Searching ")

else:
    print('ENTRY WRONG !')
    exit()
