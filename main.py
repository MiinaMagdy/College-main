from student import student
from teacher import teacher
from admin import admin
from help import *

# def prints(srtn):
    
#PutSp(num, 'ch')
#SetCo('color')

def main():
    init_student_ids()
    init_teacher_ids()
    choice = 1
    while choice != 0:

        print('Main Menu\n')
        print('1- Student')
        print('2- Teacher')
        print('3- Admin')
        print('0- Exist\n')
        

        choice = int(input('Choice: '))
        if choice == 1:
            student()
        elif choice == 2:
            teacher()
        elif choice == 3:
            admin()
        elif choice != 0:
            print('Choose a number between 0 and 3')
            Directing()
    Returning()
    print('--> Goodbye <--')

if __name__ == "__main__":
    main()
