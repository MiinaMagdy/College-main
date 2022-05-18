from help import *
from student import *

def searchStudent():
    stu_id = input('Enter the ID of the student to search for:')
    flag = 0
    with open('Student.txt','r') as file:
        for line in file:
            fields = line.split('\t')
            if stu_id == fields[0]:
                print('ID\tName\tAge\tDepartment\tLevel\tPassword')
                print('------------------------------------------')
                for i in range(6):
                    print(fields[i] + '\t', end='')
                print('\n')
                flag = 1
        if not flag:
            print('Not Found')
    press_any()
    Returning()


def Remove_Teacher():
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
        print('teacher Not Found')
        press_any()
        Returning()
    
    teachers_ids.put(int(Id))
    print('deleted successfully')
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
        print('Student Not Found')
        press_any()
        Returning()
        return

    students_ids.put(int(Id))
    print('deleted successfully')
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
    _id = input('Enter The id To delete: ')
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True    
                
                ch = input('Do you wnat to change the Name (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    fields[1] = input('\tEnter the new name: ')

                ch = input('Do you wnat to change the Age (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    fields[2] = input('\tEnter the new Age: ')

                ch = input('Do you wnat to change the Department (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    fields[3] = input('\tEnter the new Department: ')
                     
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            temp_file.write(record)

        if not flag:
            print('Student not found')
        else:
            print('Student updated successfully')

    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')
    press_any()
    Returning()

def ctrl_student():
    while 1:
        print('Admin Page (Control Student)')
        print('choose: ')
        print('1- Show All Student ')
        print('2- Search Student ')
        print('3- Add ')
        print('4- Remove ')
        print('5- Edit ')
        print('6- Return ')
        Ad_Stud_choice = input('Choise: ')
        if Ad_Stud_choice == '1':
            #show all student
            Directing()
            read_student()
        elif Ad_Stud_choice == '2':
            #search student
            Directing()
            searchStudent()
        elif Ad_Stud_choice == '3':
            #Add
            Directing()
            write_student()
        elif Ad_Stud_choice == '4':
            #remove
            Directing()
            delete_student()
        elif Ad_Stud_choice == '5':
            #Edit
            Directing()
            update_student()
        elif Ad_Stud_choice == '6':
            #return
            Returning()
            return
                                
