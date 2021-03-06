from db_helper import DBHelper


def run_application():
    db = DBHelper()    # creating object of the DBHelper class
    run_flag = True
    while run_flag:
        print('\n\n*****WELCOME*****')
        print('Enter 1 to Add a new user')
        print('Enter 2 to Display all users')
        print('Enter 3 to Update a user')
        print('Enter 4 to Delete a user')
        print('Enter 9 to EXIT')
        choice = int(input('\nEnter your choice  '))
        try:
            if choice == 1:
                # create a new user and insert his data
                user_id = int(input('\nEnter User-Id  '))
                user_name = input('\nEnter User-name  ')
                phone_number = input('\nEnter Phone-number  ')
                db.insert_user(user_id, user_name, phone_number)

            elif choice == 2:
                # display all users
                db.fetch_all_data()

            elif choice == 3:
                # update a user
                user_id = int(input('\nEnter User-Id  '))
                new_user_name = input('\nEnter New User-name  ') 
                new_phone_number = input('\nEnter New Phone-number  ')
                db.update_user(user_id, new_user_name, new_phone_number)

            elif choice == 4:
                # delete a user
                user_id = int(input('\nEnter User-Id  '))
                db.delete_user(user_id)
        
            elif choice == 9:
                # exit from the program
                run_flag = False
            else:
                print('Invalid choice !\nTry again')
        except Exception as e:
            print(e)





def main():
    run_application()
main()