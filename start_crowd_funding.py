#!/bin/python 
from auth import *
def start_app():
#from termcolor import colored, cprint
#cprint("choose registration or login : \n 1) Registration \n 2) Login" 'red', attrs=['blink'])
    print("\t\t__________________________________________________\n")
    print("\t\t\t---- 𝕮𝖗𝖔𝖜𝖉-𝕱𝖚𝖓𝖉𝖎𝖓𝖌-𝕮𝖔𝖓𝖘𝖔𝖑𝖊-𝕬𝖕𝖕-----")
    print("\t\t__________________________________________________\n")
    print("choose registration or login : \n 1) Registration \n 2) Login \n 3) Exit \n for first login crowd funding app choose Registration \n")
    choice = input("what is your choice? : \n")

    if choice == "1":
        print("_____________________________________\n")
        registartion_test()
    elif choice == "2":
        print("_____________________________________\n")
        login_test()
    elif choice =="3":
        exit
    else:
        print("________ Invalid Choice Bye ^_* _________\n\n")
        exit
start_app()
