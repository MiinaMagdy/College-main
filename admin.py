from help import *
from ctrl_teacher import ctrl_teacher
from ctrl_student import ctrl_student

def admin():
    while 1:
        Directing()
        SetCo('green')
        table('1- sign in',20)
        SetCo('red')
        table('0- return back',20)
        table("",20)
        SetCo('gold')
        PutSp(30,' ')
        Reg_sign = input('choose: ')

        
        if Reg_sign == '0':
            Returning()
            return
        if Reg_sign != '1':
            SetCo('red')
            print('Choose a number between 0 and 1')
            sound("Choose a number between 0 and 1")
            press_any()
            continue
        Directing()
        SetCo('blue')
        table('Sign In Admin Page\n' , 50 , 40)
        table('' , 50 , 40)
        
        PutSp(50,' ')
        SetCo('brown')
        Id = input('Enter ID: ')
        PutSp(50,' ')
        Password = getpass('Enter Password: ')
        found = (Id == Password and Id == 'Admin')
        if found:
            while 1:
                Directing()
                SetCo('green')
                table('Admin Page\n' , 50 , 30)
                table('' , 50 , 30)
                print()
                PutSp(30,' ')
                print('choose: ')
                table('1- Control Teacher',20)
                table('2- Control Student',20)
                SetCo('red')
                table('0- Log out',20)
                table("",20)
                PutSp(30,' ')
                SetCo('gold')
                Admin_choice = input('Choice: ')
                
                if Admin_choice == '0':
                    Returning()
                    return
                elif Admin_choice == '1':
                    ctrl_teacher()

                elif Admin_choice == '2':
                    ctrl_student()
                
                else:
                    SetCo('red')
                    print('Choose a number between 0 and 2')
                    sound("Choose a number between 0 and 2")
                    press_any()
   
        else:
            print()
            PutSp(40,' ')
            SetCo('red')
            print('Id or Password is wrong please try again!!!')
            sound("yooooohhhh Id or Password is wrond please try again")
            press_any()        
            Returning()
