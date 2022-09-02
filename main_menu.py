#!/bin/python
def menu(usr_id):
    print("\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project")

    choice = input("\nChoose from menu: \n")
    if choice == "1":
        from create import create
        create(usr_id)
    elif choice == "2":
        from view import view
        view(usr_id)
    elif choice == "3":
        from edit import edit
        edit(usr_id)
    elif choice == "4":
        from delete import delete
        delete(usr_id)
    elif choice == "5":
        from search import search
        search(usr_id)
    else:
        print("\nInvalid choice, try again: ")
    return menu(usr_id)
