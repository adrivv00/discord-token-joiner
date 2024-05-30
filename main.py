
from raducord import *
import requests, tls_client, datetime, threading, random, json, time, websocket
from colorama import Fore
import os
import httpx

#setup
Console.size(80, 25)
start_time = time.time()
print(TextUtils.make_ascii("                  niger", font="graffiti"))

with open("proxies.txt", "w", encoding='utf-8') as f:
    f.write("")

def save_proxies(proxies):
    with open("proxies.txt", "w") as file:
        file.write("\n".join(proxies))

def get_proxies():
    with open('proxies.txt', 'r', encoding='utf-8') as f:
        proxies = f.read().splitlines()
    if not proxies:
        proxy_log = {}
    else:
        proxy = random.choice(proxies)
        proxy_log = {
            "http://": f"http://{proxy}", "https://": f"http://{proxy}"
        }
    try:
        url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"
        response = httpx.get(url, proxies=proxy_log, timeout=60)

        if response.status_code == 200:
            proxies = response.text.splitlines()
            save_proxies(proxies)
        else:
            time.sleep(1)
            get_proxies()
    except httpx.ProxyError:
        get_proxies()
    except httpx.ReadError:
        get_proxies()
    except httpx.ConnectTimeout:
        get_proxies()
    except httpx.ReadTimeout:
        get_proxies()
    except httpx.ConnectError:
        get_proxies()
    except httpx.ProtocolError:
        get_proxies()

def check_proxies_file():
    file_path = "proxies.txt"
    if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
        get_proxies()

check_proxies_file()

request = tls_client.Session(client_identifier="chrome_108",ja3_string="771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2",h2_settings={"HEADER_TABLE_SIZE": 65536,"MAX_CONCURRENT_STREAMS": 1000,"INITIAL_WINDOW_SIZE": 6291456,"MAX_HEADER_LIST_SIZE": 262144},h2_settings_order=["HEADER_TABLE_SIZE","MAX_CONCURRENT_STREAMS","INITIAL_WINDOW_SIZE","MAX_HEADER_LIST_SIZE"],supported_signature_algorithms=["ECDSAWithP256AndSHA256","PSSWithSHA256","PKCS1WithSHA256","ECDSAWithP384AndSHA384","PSSWithSHA384","PKCS1WithSHA384","PSSWithSHA512","PKCS1WithSHA512",],supported_versions=["GREASE", "1.3", "1.2"],key_share_curves=["GREASE", "X25519"],cert_compression_algo="brotli",pseudo_header_order=[":method",":authority",":scheme",":path"],connection_flow=15663105,header_order=["accept","user-agent","accept-encoding","accept-language"])
r = Fore.RESET; c = Fore.MAGENTA; g = Fore.LIGHTBLACK_EX; tokens = open("tokens.txt", "r", encoding="utf8").read().splitlines()

proxies = (random.choice(open("proxies.txt", "r").readlines()).strip()
    if len(open("proxies.txt", "r").readlines()) != 0
    else None)

if ":" in proxies and len(proxies.split(":")) == 4:
    ip, port, user, pw = proxies.split(":")
    proxy = f"http://{user}:{pw}@{ip}:{port}"
else:
    ip, port = proxies.split(":")
    proxy = f"http://{ip}:{port}"

payload = {
    'fingerprint': Discord.get_fingerprint(proxies),
  }



def Headers(token):  
        headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'fr-FR,fr;q=0.9',
        'authorization': token,
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'cookie': '__dcfduid=676e06b0565b11ed90f9d90136e0396b; __sdcfduid=676e06b1565b11ed90f9d90136e0396bc28dfd451bebab0345b0999e942886d8dfd7b90f193729042dd3b62e2b13812f; __cfruid=1cefec7e9c504b453c3f7111ebc4940c5a92dd08-1666918609; locale=en-US',        
        'origin': 'https://discord.com',
        'pragma': 'no-cache',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImZyLUZSIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA3LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlcGVhc2VfY2hhbm5lcCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE1NDc1MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
         }
        return headers


class niger:
    def joiner(self, t, invite):
        if len(tokens) == 0: 
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers, json=payload); token = t.split(".")[0]
                if rr.status_code == 200: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Joined {c}{token}{g}****{r} to {c}.gg/{invite}{r}")
                elif rr.status_code == 400: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[CAPTCHA]   {g}->    {r}Soldier {c}{token}{g}****{r} was captched {c}[RIP]{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass

    def leaver(self, t, server):
        if len(tokens) == 0:
            print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->   {r}Put {c}tokens{r} to {c}data/tokens.txt{r}")
        else:
            headers = Headers(t)
            try:
                rr = request.delete(f'https://discord.com/api/v9/users/@me/guilds/{server}', headers=headers, json=payload); token = t.split(".")[0]
                if rr.status_code == 204: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[SUCCESS]   {g}->   {r}Successfully left {c}{token}{g}****{r}")
                else: print(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {c}[ERROR]     {g}->    {r}Failed {c}{token}{g}****{r}  {g}{rr.text}{r}")
            except: pass


def main():
    Console.clear()
    print(TextUtils.make_ascii("                  niger", font="graffiti"))
    print(f"""
                         {c}«{r}01{c}»{r}  Joiner  {c}«{r}02{c}»{r}  Leaver 
    """)
    nigger = str(input(f"{c}#:{r}>>  "))
    if nigger == "": main()

    # JOINER
    elif nigger == "1":
        Console.clear(); print(TextUtils.make_ascii("                  niger", font="graffiti"))
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Invite Code {g}» {c}"))
        if server == "": main()
        delay = float(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Delay {g}» {c}"))
        if delay == "": main()
        serverinv = server.strip("https://"); invite = serverinv.split("/")[-1]
        Console.clear(); print(TextUtils.make_ascii("                  niger", font="graffiti"))
        raider = niger()
        for t in tokens:
            threading.Thread(target=raider.joiner, args=(t, invite)).start()
            time.sleep(delay)
        exit = input(""); exit = main()
    
    # LEAVER
    elif nigger == "2":
        Console.clear(); print(TextUtils.make_ascii("                  niger", font="graffiti"))
        server = str(input(f"{datetime.datetime.now().strftime(f'{g}%H:%M:%S')}{r}    {r}Guild ID {g}» {c}"))
        if server == "": main()
        Console.clear(); print(TextUtils.make_ascii("                  niger", font="graffiti"))
        raider = niger()
        for t in tokens:
            threading.Thread(target=raider.leaver, args=(t, server)).start()
        exit = input(""); exit = main()
main()



