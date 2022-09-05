#!/bin/python
from main_menu import menu
import time


#___________________________view function_____________________
                                                                                                
def view(usr_id):
    try:
        usersprojects = open("projects_data.txt", "r")
    except Exception as e:
        print(e)
    else:
        print("\n_______ All Projects ___________\n")
        projects=usersprojects.readlines()
        for project in projects:
            userproject = project.strip("\n")
            projinfo = userproject.split(":")
            print(projinfo)
        usersprojects.close()
        return projects

#____________________search function______________________________

def search(usr_id):
    projects=view(usr_id)
    projectdate = input('\nWrite project date (dd/mm/yyyy) : ')
    try:
        validate_date = time.strptime(projectdate, '%d/%m/%Y')
        if validate_date:
            for p in projects:
                userproject = p.strip("\n")
                userproject = userproject.split(":")
                if userproject[4] == projectdate:
                    print(userproject)
        else:
            print("\n project not exist, enter valid data :")
            return search(usr_id)

    except ValueError:
        print("Invalid data")
        menu(usr_id)
    menu(usr_id)
#___________________________________Delete Function_____________________________________
def delete(usr_id):
    projects = view(usr_id)
    deleteproject = input('\nenter project you want to delete : ')
    for project in projects:
        userproject = project.strip("\n")
        userproject = userproject.split(":")
        print(userproject)
        if userproject[1] == deleteproject and usr_id==userproject[0]:
            projects.remove(project)
            print(deleteproject,"project was deleted")
            break
        #else: 
         #   print(" project not  exist, make sure this project assigned to your id and try again")
          #  return menu(usr_id)
    else:
        print("you are only autharized to delete your projects")
        menu(usr_id)
    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()
    menu(usr_id)
