#!/bin/python
from main_menu import menu
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
