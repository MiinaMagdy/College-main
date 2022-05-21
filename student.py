from help import *

def write_student():
    with open('Student.txt', 'a') as student_file:
        SetCo('brown')
        PutSp(50 , " ")
        Name = input("Name: ")
        PutSp(50 , " ")
        Age = input("Age: ")
        PutSp(50 , " ")
        Department = input("Department: ")
        PutSp(50 , " ")
        Level = input("Level: ")
        PutSp(50 , " ")
        Password = str(getpass("Password: "))
        PutSp(50 , " ")
        Id = str(students_ids.get())
        SetCo('brown')
        print()
        PutSp(40 , ' ')
        SetCo('green')
        print("Registration Completed ... Your ID is: ", Id)
        sound("Registration Completed Your ID is " + Id)
        press_any()
        this_stu = Id + '\t' + Name + '\t' + Age + '\t' + Department + '\t' + Level + '\t' + Password + '\t\n'
        student_file.write(this_stu)
        Returning()
        
    return this_stu.split('\t')

def read_student():
    flag = 1
    with open('Student.txt', 'r') as student_file:
        for record in student_file:
            if flag:
                SetCo('green')
                PutSp(20,' ')
                print('ID\tName\tAge\tDepartment\tLevel\t\tPassword')
                PutSp(20,' ')
                
                print('---------------------------------------------------------------------')
                flag = 0
            fields = record.split('\t')
            SetCo('gold')
            PutSp(20,' ')
            for i in range(6):
                  if i < 3:
                        print(fields[i] + '\t',end = '')
                  else:
                    print(fields[i] + '\t\t',end = '')
            
            print()
    if flag:
        PutSp(20,' ')
        SetCo('red')
        print('No Students Found')
        sound("hmmmm No Students Found")
    print()
    press_any()
    Returning()
    
    
def search_student(_id = '-1', _password = '-1'):
    with open('Student.txt', 'r') as student_file:
        for record in student_file:
            fields = record.split('\t')
            if _id == fields[0] and fields[5] == _password:
                return [True, fields]
    return [False, []]

def add_new_course(_id = '-1', course_id = 'none'):
    with open('Student.txt', 'r') as student_file, open('Temporary.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True
                fields.append(course_id)
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                this_student = record.split('\t')
            temp_file.write(record)
        if not flag:
            SetCo('red')
            PutSp(50 , ' ')
            print('Student not found')
            sound("hmmm Student not found")
        else:
            SetCo('green')
            PutSp(40 ,' ')
            print('Student updated successfully')
            sound("Student updated successfully")
    os.remove('Student.txt')
    os.rename('Temporary.txt', 'Student.txt')
    press_any()
    Returning()
    return this_student

def update_password(_id = '-1'):
    with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in student_file:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True 
                PutSp(20 , ' ')  
                SetCo('brown') 
                fields[5] = getpass("Enter the new password for " + fields[1] + ": ")
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                ThisStu = record.split('\t')
            temp_file.write(record)
        print()
        if not flag:
            SetCo('red')
            PutSp(50 , ' ')
            print('Student not found')
            sound("hmmm Student not found")
        else:
            SetCo('green')
            PutSp(40 , ' ')
            print('Student updated successfully')
            sound("Student updated successfully")
    os.remove('Student.txt')
    os.rename('Temp.txt', 'Student.txt')
    press_any()
    Returning()
    return ThisStu

def student():
    Directing()
    this_student = []
    choice = '1'
    while choice != '0':
        SetCo('green')
        table("1- Register\n" , 20)
        table("2- Sign in\n" , 20)
        SetCo('red')
        table("0- Return Back", 20)
        table(' ' , 20)
        SetCo('gold')
        PutSp(20 , ' ')
        choice = input('Choose: ')
        
        if choice == '0':
            Returning()
            return 
        
        found = 0
        Directing()

        if choice == '1':
            # Register 
            found  = 1
            SetCo('blue')
            table("Student Register Page\n" , 70 , 20)
            table("" , 70 , 20)
            print()
            this_student = write_student()

        elif choice == '2':
            # sign in 
            table("Student Sign In Page" , 50 , 20)
            table("" , 50 , 20)
            student_id = input('Enter ID: ')
            student_pass = getpass('Enter Password: ')
            [found, this_student] = search_student(student_id, student_pass)

        if not found:
            SetCo('red')
            print("The ID or the Password is wrong, Please try Aagin")
            sound("yooooohhhh The ID or the Password is wrong, Please try Aagin")
            press_any()
            Returning()
            return


        stu_choic = '1'
        while stu_choic != '0':
            Directing()
            SetCo('green')
            table('1- Show my Info' , 30)
            table('2- Add a new course' , 30)
            table('3- Show my courses' , 30)
            table('4- Update password' , 30)
            SetCo('red')
            table('0- Logout' , 30)
            table("" , 30)
            SetCo('gold')
            PutSp(20 , ' ')
            stu_choic = input('Choose: ')
            if stu_choic == '0':
                Returning()
                return
            
            Directing()

            if stu_choic == '1':
                SetCo('brown')
                PutSp(20 , ' ')
                print('ID\tName\tAge\tDepartment\tLevel\tPassword')
                PutSp(20 , ' ')
                print('---------------------------------------------------------')
                PutSp(20 , ' ')
                for i in range(6):
                    if i != 3:
                        print(this_student[i] + '\t', end='')
                    else:
                        print(this_student[i] + '\t\t' , end = ' ')
                press_any()
                Returning()
            elif stu_choic == '2':
                # Add new course
                courses_found = 0
                valid_choice = False
                with open('Teachers.txt', 'r') as teacher_file:
                    courses_list = []
                    SetCo('green')
                    for record in teacher_file:
                        fields = record.split('\t')
                        if fields[0] not in this_student[6:]:
                            PutSp(20 , ' ')
                            print(fields[0] + '- ' + fields[3])
                            courses_list.append(fields[0])
                            courses_found += 1
                    if courses_found > 0:
                        PutSp(20 , ' ')
                        SetCo('red')
                        print('0- return back')
                        PutSp(15 , ' ')
                        SetCo('gold')
                        course_choice = input('Choose: ')
                        if course_choice == '0':
                            continue
                        if course_choice in courses_list:
                            valid_choice = True
                            this_student = add_new_course(this_student[0], course_choice)

                    else:
                        SetCo('red')
                        PutSp(20 , ' ')
                        print("There is no available courses for you now!")
                        sound("There is no available courses for you now!")
                        press_any()
                        Returning()
                        
                if valid_choice:
                    with open('Teachers.txt', 'r') as teacher_file, open('Temp.txt', 'w') as temp_file:
                        for record in teacher_file:
                            fields = record.split('\t')
                            fields.pop()
                            if course_choice == fields[0]:
                                fields.append(this_student[0])
                                record = ""
                                for i in range(len(fields)):
                                    record += fields[i] + '\t'
                                record += '\n'
                            temp_file.write(record)
                    os.remove('Teachers.txt')
                    os.rename('Temp.txt', 'Teachers.txt')
            elif stu_choic == '3':
                # show my courses
                no_courses = True
                with open('Teachers.txt', 'r') as teacher_file:
                    for record in teacher_file:
                        fields = record.split('\t')
                        if fields[0] in this_student[6:]:
                            no_courses = False
                            SetCo('gold')
                            PutSp(20 , ' ')
                            print(fields[0] + '- ' + fields[3])
                if no_courses:
                    PutSp(50 , ' ')
                    SetCo('red')
                    print('No Courses Found')
                    sound("No Courses Found")
                press_any()
                Returning()
                
            elif stu_choic == '4':
                this_student = update_password(this_student[0])
