#!/bin/python
import re
from main_menu import menu
#________________________________________user id____________________________________

def usr_id():
    nid=open(r"usrs_data.txt", 'r')
    lastid = len(nid.readlines())
    nid.close()
    return lastid+1

#________________________________________registartion____________________________________

def registartion_test(usr_id=usr_id()):
    print("________________ Registartion  _______________________\n")
    first_name = input("First name : ")
    last_name = input("Last name : ")
    email = input("Email : ")
    password = input("Password : ")
    confirm_password = input("Confirm password : ")
    mobile_phone = input("Mobile phone : ")

    #validation
    if first_name.isdigit() or not first_name or first_name.isspace() or last_name.isdigit() or not last_name or last_name.isspace():
        print("\n name is invalid, please enter  a valid name")
        return registartion_test(usr_id)

    else:
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email)):
            if password == confirm_password:
                if re.match("^01[0125][0-9]{8}$", mobile_phone):
                    try:
                        usrs_data = open("usrs_data.txt", "a")
                    except Exception as e:
                        print(e)
                    else:
                        user_data =  f"{usr_id}:{first_name}:{last_name}:{email}:{password}:{mobile_phone}\n"
                        usrs_data.write(user_data)
                        usrs_data.close()
                        return login_test()
            else:
                print("\nInvalid Password passwords don't match, please enter valid password")
                return registartion_test(usr_id)
        else:
            print("Invalid Email, enter valid email")
            return registartion_test(usr_id)


#________________________________________login____________________________________

def login_test():
    print("_________________ Enter  Email  & Password to Login _______________________\n")
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
            return login_test()

