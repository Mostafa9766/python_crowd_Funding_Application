#!/bin/python
from main_menu import menu
import time


#___________________________view function_____________________
def view(user_id):
    try:
        usersprojects = open("projects_data.txt", "r")
    except Exception as e:
        print(e)
    else:
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
        return search(usr_id)
#_______________________view function_____________________________

def edit(usr_id):
    projects=view(usr_id)
    projectname = input('\nenter projcet name you want to edit: ')
    for p in projects:
        userproject = p.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == projectname and usr_id==userproject[0]:
            print(userproject)
            print("__________________________________________________________________________________________________\n")
            choice= input('\n  choose 1)edit project title\n\t2)edit project details\n\t3)edit project targrt\n\t4)edit start date\n\t5)edit end date\n\t6)update all : \n')
            print("__________________________________________________________________________________________________\n")


            if choice == "1":
                newtitle= input("please enter new project name: ")
                userproject[1]= newtittle
            elif choice == "2":
                projectdetails = input("please enter new project details: ")
                userproject[2]= projectdetails
            elif choice == "3":
                projecttarget = input("please enter new project target: ")
                userproject[3]= projecttarget
            elif choice == "4":
                projectstart = input("please enter new start date: ")
                userproject[4]= projectstart
            elif choice == "5":
                projectend = input("please enter new end date: ")
                userproject[5] = projectend
            elif choice == "6":
                newtitle = input("enter new project name: ")
                userproject[1] = newtitle
                projectdetails = input(" enter new project details: ")
                userproject[2] = projectdetails
                projecttarget = input("enter new projct target: ")
                userproject[3] = projecttarget
                projectstart = input("enter new start date: ")
                userproject[4] = projectstart
                projectend = input("enter new end date: ")
                userproject[5] = projectend
            else:
                print("invalid choice\n")
                menu(usr_id)
         
            updatedproject = ":".join(userproject)
            updatedproject = f"{updatedproject}\n"
            projectindex = projects.index(p)
            print(projectindex)
            projects[projectindex] = updatedproject
            break
        else:
            print("you are only autharized to edit your projects\n")
            menu(usr_id)

    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()
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
        print("you are only autharized to edit your projects")
        return menu(usr_id)
    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()
    menu(usr_id)
