from msvcrt import putch
from student import student
from teacher import teacher
from admin import admin
from help import *
    
#PutSp(num, 'ch')
#SetCo('color')

def main():
    os.system('cls')
    init_student_ids()
    init_teacher_ids()
    choice = 1
    sound('welcom to every one')
    while choice != 0:
        SetCo('green')
        table("Main Menu" , 50 , 25)
        table("" , 50 , 25)
        print()

        table("  1- Student\n" , 20)
        table("  2- Teacher\n" , 20)
        table("3- Admin\n" , 20)
        SetCo('red')
        table("0- Exit\n" , 20)
        table("" , 20)  
        SetCo('gold')
        PutSp(20 , " ") 
        choice = int(input('Choice: '))
        if choice == 1:
            student()
        elif choice == 2:
            teacher()
        elif choice == 3:
            admin()
        elif choice != 0:
            PutSp(20 , ' ')
            SetCo('red')
            sound("pleaes Choose a number between 0 and 3")
            print('Choose a number between 0 and 3')
            Directing()
    Returning()
    SetCo("gold")
    PutSp(30,' ')
    print("created by Peter Torki, Mina Magdy, Mohamed Ashraf, Eman Mohamed and Eman El-saied")
    sound("created by Peter Torki, Mina Magdy, Mohamed Ashraf, Eman Mohamed and Eman El-saied")
    SetCo("blue")
    
    PutSp(50,' ')
    print('--> Goodbye <--')
    sound('goodbye')

if __name__ == "__main__":
   main()
