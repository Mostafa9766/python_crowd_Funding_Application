#!/bin/python

from view import view
def edit(usr_id):
    projects=view(usr_id)
    projectname = input('\nenter projcet name you want to edit: ')
    for p in projects:
        userproject = p.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == projectname and usr_id==userproject[0]:
            print(projects)
            print("__________________________________________________________________________________________________\n")
            choice= input('\n   choose 1)edit project title\n\t2)edit project details\n\t3)edit project targrt\n\t4)edit start date\n\t5)edit end date\n\t6)update all : ')
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

            updatedproject = ":".join(userproject)
            updatedproject = f"{updatedproject}\n"
            projectindex = projects.index(p)
            print(projectindex)
            projects[projectindex] = updatedproject
            break
    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()

