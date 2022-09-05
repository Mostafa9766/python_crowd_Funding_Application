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
        print("---------------------------------_\n")
        registartion_test()
    elif choice == "2":
        print("---------------------------------_\n")
        login_test()
    elif choice =="3":
        print("________________________  Bye ^_*  ____________________________________\n\n")
        exit
    else:
        print("____________________ Invalid Choice Bye ^_* __________________________\n\n")
        exit
start_app()
