from help import *
from student import *

def searchStudent():
    PutSp(20 , ' ')
    SetCo('gold')
    sound("please Enter the ID of the student to search for")
    stu_id = input('Enter the ID of the student to search for:')
    flag = 0
    with open('Student.txt','r') as file:
        for line in file:
            fields = line.split('\t')
            if stu_id == fields[0]:
                PutSp(20 , ' ')
                SetCo('green')
                print('ID\tName\tAge\tDepartment\tLevel\t\tPassword')
                PutSp(20 , ' ')
                print('---------------------------------------------------------------------')
                PutSp(20 , ' ')
                SetCo('gold')
                for i in range(6):
                    if i < 3:
                       print(fields[i] + '\t', end='')
                    else :
                        print(fields[i] + '\t\t' , end = '')
                print('\n')
                flag = 1
        if not flag:
            SetCo('red')
            PutSp(50 , ' ')
            print('Not Found')
            sound("Not Found")
    press_any()
    Returning()
    
    
def Remove_Teacher():
    PutSp(30,' ')
    SetCo('gold')
    sound("please Enter The id you want to delete")
    Id = input('Enter The id To delete: ')
    flag = False
    with open('Teachers.txt', 'r') as TecFile, open('Temp.txt', 'w') as temporary_file:
        for record in TecFile:
            field = record.split('\t')
            if field[0] == Id:
                flag = True
            else:
                temporary_file.write(record)
                
    os.remove('Teachers.txt')
    os.rename('Temp.txt' , 'Teachers.txt')

    if not flag:
        PutSp(50,' ')
        SetCo('red')
        print('teacher Not Found')
        sound("teacher Not Found")
        press_any()
        Returning()
    
    teachers_ids.put(int(Id))
    PutSp(50,' ')
    SetCo('green')
    print('deleted successfully')
    sound("deleted successfully")
    with open('Student.txt', 'r') as student_file, open('Temporary.txt', 'w') as Tempo:
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if Id in fields[6:]:
                fields = [fields[i] for i in range(0, len(fields)) if i < 6 or fields[i] != Id]
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            Tempo.write(record)
            
    os.remove('Student.txt')
    os.rename('Temporary.txt', 'Student.txt')
    press_any()
    Returning()

def delete_student():
    PutSp(30,' ')
    SetCo('gold')
    sound("Enter The id you wante to delete")
    Id = input('Enter The id To delete: ')
    flag = False
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        for record in student_file:
            field = record.split('\t')
            if field[0] == Id:
                flag = True
            else:
                temp_file.write(record)
                
    os.remove('Student.txt')
    os.rename('Temp.txt' , 'Student.txt')
    
    if not flag:
        PutSp(30,' ')
        SetCo('red')
        print('Student Not Found')
        sound("Student Not Found")
        press_any()
        Returning()
        return

    students_ids.put(int(Id))
    PutSp(30,' ')
    SetCo('green')
    print('deleted successfully')
    sound("deleted successfully")
    with open('Teachers.txt', 'r') as teacher_file, open('Temporary.txt', 'w') as Tempo:
        for record in teacher_file:
            fields = record.split('\t')
            fields.pop()
            if Id in fields[5:]:
                fields = [fields[i] for i in range(0, len(fields)) if i < 5 or fields[i] != Id]
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            Tempo.write(record)
            
    os.remove('Teachers.txt')
    os.rename('Temporary.txt', 'Teachers.txt')
    press_any()
    Returning()

def update_student(_id = '-1'):
    PutSp(30,' ')
    SetCo('gold')
    sound("Enter The id To update")
    _id = input('Enter The id To update: ')
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True    
                
                PutSp(30,' ')
                sound("Do you want to change the Name")
                ch = input('Do you want to change the Name (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    PutSp(30,' ')
                    fields[1] = input('\tEnter the new name: ')

                PutSp(30,' ')
                sound("Do you want to change the Age")
                ch = input('Do you want to change the Age (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    PutSp(30,' ')
                    fields[2] = input('\tEnter the new Age: ')

                PutSp(30,' ')
                sound("Do you want to change the Department")
                ch = input('Do you want to change the Department (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    PutSp(30,' ')
                    fields[3] = input('\tEnter the new Department: ')
                     
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            temp_file.write(record)

        if not flag:
            PutSp(50,' ')
            SetCo('red')
            print('Student not found')
            sound("Student not found")
        else:
            PutSp(50,' ')
            SetCo('green')
            print('Student updated successfully')
            sound("Student updated successfully")

    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')
    press_any()
    Returning()

def ctrl_student():
    while 1:
        SetCo('blue')
        table('Admin Page (Control Student)' , 50)
        table("" ,50)
        print()
        PutSp(30,' ')
        SetCo('green')
        print('choose: ')
        table('1- Show All Student ',25)
        table('2- Search Student ',25)
        table('3- Add ',25)
        table('4- Remove ',25)
        table('5- Edit ',25)
        SetCo('red')
        table('6- Return ',25)
        table("",25)
        PutSp(30,' ')
        SetCo('gold')
        Ad_Stud_choice = input('Choice: ')
        if Ad_Stud_choice == '1':
            #show all student
            Directing()
            print()
            read_student()
        elif Ad_Stud_choice == '2':
            #search student
            Directing()
            print()
            searchStudent()
        elif Ad_Stud_choice == '3':
            Directing()
            print()
            write_student()
        elif Ad_Stud_choice == '4':
            #remove
            Directing()
            print()
            delete_student()
        
        elif Ad_Stud_choice == '5':
            #Edit
            Directing()
            print()
            update_student()
        
        elif Ad_Stud_choice == '6':
            #return
            Returning()
            return
                                
