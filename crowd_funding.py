#!/bin/python
#import registration
from registartion  import registartion_test
from login import login_test

#from termcolor import colored, cprint
#cprint("choose registration or login : \n 1) Registration \n 2) Login" 'red', attrs=['blink'])

print("𝕮𝖗𝖔𝖜𝖉-𝕱𝖚𝖓𝖉𝖎𝖓𝖌-𝕮𝖔𝖓𝖘𝖔𝖑𝖊-𝕬𝖕𝖕")
print("choose registration or login : \n 1) Registration \n 2) Login")
choice = input("for first login crowd funding app choose Register : \n")

if choice == "1":
    print("regest")
    registartion_test()
elif choice == "2":
    print("log")
    login_test()

