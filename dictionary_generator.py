import random, string
from colorama import init, Fore

init()
txt = open('codes.txt', 'w+')

blue = Fore.LIGHTCYAN_EX
white = Fore.LIGHTWHITE_EX

for i in range(5000):
    code = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6)).lower()
    print(f"{blue}[{i+1}] Generating code: {white}{code}")
    txt.write(f"{code}\n")

txt.close()

# for line in txt:
#     print(line.replace(" ","").replace("\n",""))