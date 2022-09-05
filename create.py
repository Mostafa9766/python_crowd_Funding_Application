#!/bin/python 
import time
from main_menu import menu

def create(usr_id):

    title = input("Project Title : ")
    details = input("Project Details : ")
    totaltarget = input("Total target of Project : ")
    starttime = input("Project Start Date (dd/mm/yyyy) : ")
    endtime = input("Project End Date (dd/mm/yyyy) : ")
#------------------------validate date format-----------------------------
    try:
        validate_start = time.strptime(starttime, '%d/%m/%Y')
        validate_end = time.strptime(endtime, '%d/%m/%Y')

        if validate_start and validate_end:
            try:
                users_projects = open("projects_data.txt", "a")
            except Exception as e:
                print(e)
            else:
                user_data = f"{usr_id}:{title}:{details}:{totaltarget}:{starttime}:{endtime}\n"
                users_projects.write(user_data)
                users_projects.close()
                print('Your project was created successfully')
                return menu(usr_id)
    except Exception as e:
        print(e)
        print("\nInvalid Data, enter valid data")
        create(usr_id)
