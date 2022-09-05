#!/bin/python
def menu(usr_id):
    users= open("usrs_data.txt", "r")
    users=users.readlines()
    for user in users:
        user= user.strip("\n")
        userinfo = user.split(":")
        if usr_id == userinfo[0]:
            username=userinfo[1]
            break
    #users.close()
    print(f"\n_______________ Welcome ya {username}____________")
    print("\n\n 1) Create Project \n 2) View All Projects \n 3) Edit Project \n 4) Delete Project \n 5) Search For Project \n 6)Log Out and  Back to exit ")

    choice = input("\nChoose from menu: \n")
    if choice == "1":
        from create import create
        create(usr_id)
    elif choice == "2":
        from functions import view
        view(usr_id)
    elif choice == "3":
        from edit import edit
        edit(usr_id)
    elif choice == "4":
        from functions import delete
        delete(usr_id)
    elif choice == "5":
        from functions import search
        search(usr_id)
    elif choice=="6":
        from start_crowd_funding import start_app
    else:
        print("\nInvalid choice, try again: ")
        menu(usr_id)
