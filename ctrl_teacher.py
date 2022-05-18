from help import *


def ctrl_teacher():
    Directing()
    while True:
        print('Admin Page (Teacher Control)')
        print('Choose : ')
        print('  1- Show All Teachers ')
        print('  2- Search Teacher  ')
        print('  3- Add ')
        print('  4- Remove ')
        print('  5- Edit  ')
        print('  6- Return ')
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            Show_All_Teachers()
        elif choice == 2:
            Search_Teacher()
        elif choice == 3:
            Add_Teacher()
        elif choice == 4:
            Remove_Teacher()
        elif choice == 5:
            Edit_Teacher()
        else:
            Returning()
            return 

def Show_All_Teachers():
   # fil =  open('Teachers.txt','r')
   # if os.path.getsize(file) == 0:
     #   print('File is empty')
    flag = 1
    with open('Teachers.txt','r') as file:
        for line in file:
            if flag:
                print('ID\tName\tAge\tCouse\tpassword\t')
                print('---------------------------------------')
                flag = 0
            thisTeacher = line.split('\t')
            print('\t'.join(map(str, thisTeacher[0: 3])) + '\t  ' + thisTeacher[3] + '\t\t    ' +'\t'.join(map(str, thisTeacher[4: 5])))
        press_any()
        Returning()

def Search_Teacher():
    Id = input('Enter the ID of Teacher To search ')
    with open('Teachers.txt','r') as file:
        flag = False
        for line in file:
            thisTeacher = line.split('\t')
            if thisTeacher[0] == Id:
                print('ID\tName\tAge\tCouse\tpassword\t')
                print('-------------------------------------')
                print('\t'.join(map(str, thisTeacher[0: 3])) + '\t  ' + thisTeacher[3] + '\t\t    ' +'\t'.join(map(str, thisTeacher[4: 5])))
                flag = True
                break
        if not flag:
            print('Teacher Not Found')
    press_any()
    Returning()

def Add_Teacher():
    with open('Teachers.txt','a') as file:
        name = input('Enter The Name: ')
        age = input('Enter The Age: ')
        course = input('Enter The Course''s Name: ')
        password = getpass('Enter The Password: ')
        Id = str(teachers_ids.get())
        print("\nRegistration Completed ... Your ID is: ", Id)
        file.write(Id + '\t' + name + '\t' + age + '\t' + course + '\t' + password + '\t\n')
    press_any()
    Returning()

#Remove Teacher:
# 1) loop for each stu[6 :], write it in a new file
# 2) if id != id_file -> write in new file

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
        return
    
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

def Edit_Teacher():
    _id = input('Enter The id To delete: ') 
    with open('Teachers.txt', 'r') as TechFile, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in TechFile:
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

                ch = input('Do you wnat to change the Course name (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    fields[3] = input('\tEnter the new course name: ')
                     
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            temp_file.write(record)
        if not flag:
            print('Teacher not found')
        else:
            print('Teacher updated successfully')
    os.remove('Teachers.txt')
    os.rename('Temp.txt', 'Teachers.txt')
    press_any()
    Returning()
# def Edit_Teacher():
#     id = input('Enter The id To delete: ') 
#     file = open('Teachers.txt','r')
#     tempFile = open('Tempteacher.txt','w')
#     flag = False
#     for line in file:
#             field = line.split('\t')
#             if field[0] == id:
#                 do = 
#                 age =  input('Enter the age you want to update ')
#                 field[3] = age;
#                 line = field[0] + '\t' + field[1] + '\t' + field[2] +'\t' + field[3] + '\t' + field[4] + '\n'
#                 flag = True
#             tempFile.write(line)
#     file.close()
#     tempFile.close()
#     os.remove('Teachers.txt')
#     os.rename('Tempteacher.txt' , 'Teachers.txt')
#     if not flag:
#         print('Teacher Not Found')
#     else:
#         print('deleted successfully')
