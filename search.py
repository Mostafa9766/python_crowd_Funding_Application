#!/bin/python
from view import view
import time

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
            print("\n invalid data, enter a valid data :")
            return search(usr_id)

    except ValueError:
        print("Invalid data")                    
        return search(usr_id)


