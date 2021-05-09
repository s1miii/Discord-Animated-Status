import requests
from time import sleep
from colorama import Fore
import json
import os
import emoji

email = input(f'\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RESET}Enter your email address: ')
password = input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RESET}Enter your password: ')

data={'email': email, 'password': password, 'undelete': "false"}
headers={'content-type': 'application/json', 'user-agent': 'Opera/8.70 (X11; Linux x86_64; sl-SI) Presto/2.10.303 Version/12.00'}
r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)

if r.status_code == 200:
    token = r.json()['token']
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.GREEN}Successfully logged in\n{Fore.RESET}')

elif 'PASSWORD_DOES_NOT_MATCH' in r.text:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RED}Invalid password{Fore.RESET}')
    os._exit(0)
    
elif "captcha-required" in r.text:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RED}Discord returned captcha. Try again later{Fore.RESET}')
    os._exit(0)

else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RED}An error has occured{Fore.RESET}')
    os._exit(0)


status = input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTCYAN_EX}] {Fore.RESET}Text you want to display: {Fore.WHITE}')
print(f'\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RESET}Search here: {Fore.WHITE}https://linktr.ee/semmoolenschot {Fore.LIGHTBLACK_EX}(Leave empty if you dont want emoji)')
emoji = emoji.emojize(input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}-{Fore.LIGHTCYAN_EX}] {Fore.RESET}Insert emoji name: {Fore.WHITE}'), use_aliases=True)
print(f'\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RESET}Recommended time is 0.5 - 1.5 {Fore.LIGHTBLACK_EX}(seconds)')
speed = float(input(f'{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}] {Fore.RESET}Delay: {Fore.WHITE}'))

t = token

print(f'\n{Fore.LIGHTCYAN_EX}[{Fore.LIGHTRED_EX}>{Fore.LIGHTCYAN_EX}]{Fore.GREEN} Running')

while True:
    for text in range(0, len(status)+1):
        if emoji != '':
            content = {
                'custom_status': {'text': status[:text], 'emoji_name': emoji}
            }
        else:
            content = {
                'custom_status': {'text': status[:text]}
            }
        requests.patch("https://ptb.discordapp.com/api/v6/users/@me/settings", headers={"authorization": token}, json=content)
        sleep(speed)



