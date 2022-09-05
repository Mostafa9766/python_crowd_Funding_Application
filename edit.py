#!/bin/python
from main_menu import menu
from functions import view
def edit(usr_id):
    projects=view(usr_id)
    projectname = input('\nenter projcet name you want to edit: ')
    for p in projects:
        userproject = p.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == projectname and usr_id == userproject[0]:
            print(projects)
            print("__________________________________________________________________________________________________\n")
            choice= input('\n------- Select from menu to edit  ----------\n  1)Update All\n   2)Edit Project Title\n  3)Edit Project Details\n  4)Edit Project Targrt\n  5)Edit Start Date\n  6)Edit End Date\n')
            
            print("__________________________________________________________________________________________________\n")
            if choice == "1":
                newtitle = input("Enter new project name: ")
                userproject[1] = newtitle
                projectdetails = input("Enter new project details: ")
                userproject[2] = projectdetails
                projecttarget = input("Enter new projct target: ")
                userproject[3] = projecttarget
                projectstart = input("Enter new start date: ")
                userproject[4] = projectstart
                projectend = input("Enter new end date: ")
                userproject[5] = projectend

            elif choice == "2":
                newtitle= input("Enter new project title: ")
                userproject[1]= newtitle

            elif choice == "3":
                projectdetails = input("Enter new project details: ")
                userproject[2]= projectdetails

            elif choice == "4":
                projecttarget = input("Enter new project target: ")
                userproject[3]= projecttarget

            elif choice == "5":
                projectstart = input("Enter new start date: ")
                userproject[4]= projectstart

            elif choice == "6":
                projectend = input("Enter new end date: ")
                userproject[5] = projectend
            else:
                print("invalid input,try with valid option")
                menu(usr_id)
            updatedproject = ":".join(userproject)
            updatedproject = f"{updatedproject}\n"
            projectindex = projects.index(p)
            print(projectindex)
            print(updatedproject)
            projects[projectindex] = updatedproject
            break

    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()
    menu(usr_id)

