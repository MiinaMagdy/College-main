from help import *


def ctrl_teacher():
    Directing()
    choice = '1'
    while choice != '0':
        SetCo('blue')
        table('Admin Page (Teacher Control)' , 50 , 30)
        table('' , 50 , 30)
        PutSp(50,' ')
        print()
        SetCo('green')
        PutSp(30 , ' ')
        print('Choose : ')
        table('  1- Show All Teachers ',25)
        table('  2- Search Teacher  ',25)
        table('  3- Add ',25)
        table('  4- Remove ',25)
        table('  5- Edit  ',25)
        SetCo('red')
        table('  0- Return ',25)
        table("",25)
        PutSp(30,' ')
        SetCo('gold')
        choice = input('Enter Your Choice : ')
        if choice == '1':
            print()
            Show_All_Teachers()
           
        elif choice == '2':
            print()
            Search_Teacher()
           

        elif choice == '3':
            print()
            Add_Teacher()
          
        elif choice == '4': 
            print()     
            Remove_Teacher()
           
        elif choice == '5':
            print()     
            Edit_Teacher()
           
        elif choice != '0':
            PutSp(30, ' ')
            SetCo('red')
            print('Choose a number between 0 and 5')
            sound("Choose a number between 0 and 5")
            press_any()
            Directing()

    print()
    Returning()

def Show_All_Teachers():
    flag = 1
    with open('Teachers.txt','r') as file:
        for line in file:
            if flag:
                SetCo('green')
                PutSp(30,' ')
                print('ID\tName\tAge\tCouse\tpassword\t')
                PutSp(30,' ')
                print('----\t----\t----\t----\t----\t')
                flag = 0
            thisTeacher = line.split('\t')
            PutSp(30,' ')
            SetCo('gold')
            print(thisTeacher[0]+'\t\t'+thisTeacher[1]+'\t'+thisTeacher[2]+'\t'+thisTeacher[3]+'\t'+thisTeacher[4]+'\t')  
        press_any()
        Returning()

def Search_Teacher():
    PutSp(30,' ')
    SetCo('gold')
    sound("please Enter the ID of Teacher To search")
    Id = input('Enter the ID of Teacher To search ')
    with open('Teachers.txt','r') as file:
        flag = False
        for line in file:
            thisTeacher = line.split('\t')
            if thisTeacher[0] == Id:
                PutSp(30,' ')
                SetCo('green')
                print('ID\tName\tAge\tCouse\tpassword\t')
                PutSp(30,' ')
                print('----\t----\t----\t-----\t------\t')
                PutSp(30,' ')
                SetCo('gold')
                print(thisTeacher[0]+'\t\t'+thisTeacher[1]+'\t'+thisTeacher[2]+'\t'+thisTeacher[3]+'\t'+thisTeacher[4]+'\t')
                flag = True
                break
        if not flag:
            PutSp(50,' ')
            SetCo('red')
            print('Teacher Not Found')
            sound("Teacher Not Found")
    press_any()
    Returning()

def Add_Teacher():
    
    with open('Teachers.txt','a') as file:
        print()
        PutSp(30,' ')
        name = input('Enter The Name: ')
        PutSp(30,' ')
        
        age = input('Enter The Age: ')
        PutSp(30,' ')
        
        course = input('Enter The Course''s Name: ')
        PutSp(30,' ')
        
        password = getpass('Enter The Password: ')
        PutSp(30,' ')
        print()
        Id = str(teachers_ids.get())
        PutSp(30,' ')
        print("Registration Completed ... Your ID is: ", Id)
        sound("Registration Completed ... Your ID is: " + Id)
        
        file.write(Id + '\t' + name + '\t' + age + '\t' + course + '\t' + password + '\t\n')
    press_any()
    Returning()


def Remove_Teacher():
    print()
    PutSp(30,' ')
    sound("please Enter The id To delete")
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
        return
    
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

def Edit_Teacher():
    print()
    PutSp(30,' ')
    sound("please Enter The id To Edit")
    _id = input('Enter The id To Edit: ') 
    with open('Teachers.txt', 'r') as TechFile, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in TechFile:
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
                sound("Do you want to change the Course name")
                ch = input('Do you want to change the Course name (Y / N)? ')
                if ch == 'y' or ch == 'Y':
                    PutSp(30,' ')
                    fields[3] = input('\tEnter the new course name: ')
                     
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
            temp_file.write(record)
        if not flag:
            PutSp(50,' ')
            print('Teacher not found')
            sound("Teacher not found")
        else:
            PutSp(30,' ')
            SetCo('green')
            print('Teacher updated successfully')
            sound("Teacher updated successfully")
    os.remove('Teachers.txt')
    os.rename('Temp.txt', 'Teachers.txt')
    press_any()    
    Returning()
