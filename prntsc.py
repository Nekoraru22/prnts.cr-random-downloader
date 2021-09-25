import requests, threading, os
from bs4 import BeautifulSoup
from colorama import Fore, init

# ---------------- # INICIO # ---------------- #
init()
print(Fore.BLACK + " " + Fore.RESET)

proxies = {
  "socks4": "http://91.126.138.135:5678",
}

headers = {
    'authority': 'prnt.sc',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

# ---------------- # FUNCTIONS # ---------------- #
def check_img(data):
    pass

def get_url(code):
    try:
        html = requests.get(f"http://prnt.sc/{code}", headers=headers).text # , proxies=proxies
        soup = BeautifulSoup(html, 'lxml')
        img_url = soup.find_all('img', {'class': 'no-click screenshot-image'})
        return img_url[0]['src']

    except Exception as error:
        print(f"{code} - {error}")

def get_img(url, code, x):
    try:
        response = requests.get(url, headers=headers) # , proxies=proxies
        if response.status_code == 200:
            data = response.content

            check_img(data) # work in progress

            with open(f"images/{code}.png", 'wb') as f:
                f.write(data)
                print(Fore.LIGHTGREEN_EX + f"[{x}] Downloaded code: {code} - " + Fore.LIGHTBLACK_EX + url + Fore.RESET)

        else: print("Page error - " + response.status_code)

    except:
        that = Fore.LIGHTRED_EX + f"[{x}] Code not found: {str(code)} - " + Fore.LIGHTBLACK_EX + str(url) + Fore.RESET
        print(that)
    
def dict_mode():
    x = 1

    for c in open('codes.txt', 'r'):
        code = c.replace(" ", "").replace("\n", "")
        
        if os.path.isfile(f'images/{code}.png'):
            print(Fore.LIGHTRED_EX + f"[{x}] Repeated code: {code}." + Fore.RESET)
        else:
            url = get_url(code)
            threading.Thread(target=get_img, args=[url, code, x]).start()
        x = x + 1

# ---------------- # START # ---------------- #
dict_mode()

# code = "ziqyxq"
# url = get_url(code)
# threading.Thread(target=get_img, args=[url, code]).start()