import os
from colorama import Fore, Style
import json


def banner():
	print(Fore.GREEN + str("________              _____                                             "))
	print(Fore.GREEN + str("\______   \___.__.   /     \ _____    ____ _____     ____   ___________ "))
	print(Fore.GREEN + str(" |     ___<   |  |  /  \ /  \\__  \  /    \\__  \  / ___\_/ __ \_  __ \ "))
	print(Fore.GREEN + str(" |    |    \___  | /    Y    \/ __ \|   |  \/ __ \_/ /_/  >  ___/|  | \/"))
	print(Fore.GREEN + str(" |____|    / ____| \____|__  (____  /___|  (____  /\___  / \___  >__|   "))
	print(Fore.GREEN + str("           \/              \/     \/     \/     \//_____/      \/       "))

banner()

print("Main Menu:")

print("1) Vault")
print("2) Password generator")
print("3) Close")

menu_select= input("Select:")

if menu_select== "2":
	os.system('python password_generator.py')
elif menu_select== "3":
	exit()
elif menu_select== "1":
	with open("data.json", "r") as v:
		data = json.load(v)
	#print("".join(repr(data).split("\n")[1:-1]))
	print(data)
	

