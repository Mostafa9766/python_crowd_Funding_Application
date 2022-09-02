#!/bin/python
from view import view
def delete(usr_id):
    projects = view(usr_id)
    deletepro = input('\nenter project you want to delete : ')
    for project in projects:
        userproject = project.strip("\n")
        userproject = userproject.split(":")
        if userproject[1] == deletpro and usr_id==userproject[0]:
            projects.remove(project)
            break
    else:
        print(" project not  exist, try again")
        return delete(usr_id)
    update= open("projects_data.txt", "w")
    update.writelines(projects)
    update.close()
