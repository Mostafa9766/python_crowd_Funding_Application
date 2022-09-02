#!/bin/python

import registartion
from main_menu import menu

def login_test():
    usr_email = input("Email : ")
    password = input("Password : ")
    try:
        usr_file = open('usrs_data.txt','r')
    except Exception as e:
        print(e)
    else:
        usrs = usr_file.readlines()
        for usr in usrs:
            userdata = usr.strip("\n")
            userinfo = userdata.split(":")

            if userinfo[3] == usr_email and userinfo[4] == password:
                print("logged in successfully")
                menu(userinfo[0])
                break
        else:
            print("invalid name or password ,try again but make sure you registered before: ")
            return registartion.registartion_test()

