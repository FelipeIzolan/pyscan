import socket
from threading import Thread
from tqdm import tqdm

print("""
..................
\033[0;31m█▀█\033[0m\033[0;32m█▄█\033[0m\033[0;34m█▀\033[0m\033[1;33m█▀▀\033[0m\033[0;35m▄▀█\033[0m\033[0;36m█▄░█\033[0m
\033[0;31m█▀▀\033[0m\033[0;32m░█░\033[0m\033[0;34m▄█\033[0m\033[1;33m█▄▄\033[0m\033[0;35m█▀█\033[0m\033[0;36m█░▀█\033[0m
..................
  Port scanning   
..................
""")

PROCESS = 25
IP = input("Insert IP: ")
MAX = input("Insert max-range (default: 65535): ") or 65535 
MAX = int(MAX)

progress = tqdm(total=MAX, ncols=55, colour="cyan", bar_format="| {bar} | {percentage:3.0f}% | {elapsed} |")
pp = int(MAX / PROCESS)

THREADs = []
PORTs = []

def every(arr, value):
    for item in arr:
        if item != value:
            return False

    return True

def check(IP, PORT):
    s = socket.socket()
    s.settimeout(0.1)
    c = s.connect_ex((IP, PORT))
    s.close()

    if c == 0: return True
    else: return False 

def thread(start, end, IP, index):
    for PORT in range(start, end):
        progress.update(1)
        if check(IP, PORT): PORTs.append("[🟢] {}:{}".format(IP, PORT))
        # else: PORTs.append("[🔴] {}:{}".format(IP, PORT))
   
    THREADs[index] = True
    if every(THREADs, True):
        progress.close()
        print("\n".join(PORTs))

for i in range(PROCESS):
    start = i * pp
    end = (i + 1) * pp
  
    if PROCESS == i + 1:
        end = end + (MAX - end)

    tr = Thread(target=thread, args=(start, end, IP, i))
    THREADs.append(False)
    tr.start()

