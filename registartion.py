#!/bin/python
import re

from usr_id import *
def registartion_test(usr_id=usr_id()):
    first_name = input("First name : ")
    last_name = input("Last name : ")
    email = input("Email : ")
    password = input("Password : ")
    confirm_password = input("Confirm password : ")
    mobile_phone = input("Mobile phone : ")

    #validation
    if first_name.isdigit() or not first_name or first_name.isspace() or last_name.isdigit() or not last_name or last_name.isspace():
        print("\n name is invalid, please enter  a valid name")
        registartion_test(usr_id)
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
            else:
                print("\nInvalid Password passwords don't match, please enter valid password")
                registartion_test(usr_id)
        else:
            print("Invalid Email, enter valid email")
            registartion_test(usr_id)



    
