import random
import string
import json
from colorama import Fore, Back, Style
import os
import platform
import re

creds = {}
system= platform.system()



def banner():
    print(Fore.GREEN + str("________              _____                                             "))
    print(Fore.GREEN + str("\______   \___.__.   /     \ _____    ____ _____     ____   ___________ "))
    print(Fore.GREEN + str(" |     ___<   |  |  /  \ /  \\__  \  /    \\__  \  / ___\_/ __ \_  __ \ "))
    print(Fore.GREEN + str(" |    |    \___  | /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/"))
    print(Fore.GREEN + str(" |____|    / ____| \____|__  (____  /___|  (____  /\___  / \___  >__|   "))
    print(Fore.GREEN + str("           \/              \/     \/     \/     \//_____/      \/       "))

banner()

f= open('data.json')
data= json.load(f)

def proccess():
    while True:
        email=input("Enter an email to generate a pass: ")
        if email == "exit":
            f.close()
            break

            # Check if the email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("Invalid email address. Please try again.")
                continue

        if email in data:
            print(Fore.RED +"[-]The email already exists in the database.")
            
        else:
            print("[+]Your email has been added to the database.")
            print("[+]Let's generate your password.")
            range_pass_digits = int(input("How many digits you want your password: "))
            if range_pass_digits <= 0:
                print("Password length must be a positive non-zero integer.")
                continue
            gen_password = "".join(random.choice(string.ascii_letters + string.digits) for i in range(range_pass_digits))
            creds[email] = gen_password
            print(f"[+]Generated password: {gen_password}")
            break
proccess()

def save_values():
    with open('data.json', 'w') as f:
        json.dump(creds, f, indent=2)
save_values()

menu_return= input("Do you want to return to menu? (y/n):")

if menu_return== "y":
    os.system("python menu.py")
elif menu_return=="n":
    if system == "Windows":
        os.system("cls")
    elif system == "Linux":
        os.system("clear")
    proccess()
