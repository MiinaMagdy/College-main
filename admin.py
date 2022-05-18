from help import *
from ctrl_teacher import ctrl_teacher
from ctrl_student import ctrl_student

def admin():
    while 1:
        Directing()
        print('1- sign in')
        print('0- return back')
        Reg_sign = input('choose: ')

        if Reg_sign == '0':
            Returning()
            return
        if Reg_sign != '1':
            print('Choose a number between 0 and 1')
            press_any()
            continue

        Directing()

        print('Sign In Admin Page\n')
        Id = input('Enter ID: ')
        Password = getpass('Enter Password: ')
        found = 1
        # found = (Id == Password and Id == 'Admin')
        if found:
            while 1:
                Directing()
                print('Admin Page\n')
                print('choose: ')
                print('1- Control Teacher')
                print('2- Control Student')
                print('0- Log out')
                Admin_choice = input('Choice: ')

                if Admin_choice == '0':
                    Returning()
                    return
                elif Admin_choice == '1':
                    Directing()
                    ctrl_teacher()

                elif Admin_choice == '2':
                    Directing()
                    ctrl_student()
                
                else:
                    print('Choose a number between 0 and 2')
                    press_any()
   
        else:
            print('Id or Password is wrond please try again!!!')
            press_any()
            Returning()