from help import *

def write_student():    #Done
    with open('Student.txt', 'a') as student_file:
        Name = input("Name: ")
        Age = input("Age: ")
        Department = input("Department: ")
        Level = input("Level: ")
        Password = str(getpass("Password: "))
        Id = str(students_ids.get())
        print("\nRegistration Completed ... Your ID is: ", Id)
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
                print('ID\tName\tAge\tDepartment\tLevel\tPassword')
                print('------------------------------------------')
                flag = 0
            fields = record.split('\t')
            for i in range(6):
                print(fields[i] + '\t', end='')
            print()
    if flag:
        print('No Students Found')
    press_any()
    Returning()

def search_student(_id = '-1', _password = '-1'):
    with open('Student.txt', 'r') as student_file:
        for record in student_file:
            fields = record.split('\t')
            if _id == fields[0] and fields[5] == _password:
                return [True, fields]
    return [False, []]

# def delete_student():
#     student_id = input('Enter the id of the student to delete: ')
#     with open('Student.txt', 'r') as student_file, open('Temp.txt', 'w') as temp_file:
#         flag = False
#         for record in student_file:
#             fields = record.split('\t')
#             if student_id == fields[0]:
#                 flag = True    
#             else:
#                 temp_file.write(record)
#         if not flag:
#             print('Student not found')
#         else:
#             print('Student deleted successfully')
#     os.remove('Student.txt')
#     os.rename('Temp.txt', 'Student.txt')

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
            print('Student not found')
        else:
            print('Student updated successfully')
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
                fields[5] = getpass("Enter the new password for " + fields[1] + ": ")
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                ThisStu = record.split('\t')
            temp_file.write(record)
        if not flag:
            print('Student not found')
        else:
            print('Student updated successfully')
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
        print("1- Register")
        print("2- Sign in")
        print("0- Return Back")
        choice = input('Choose: ')
        
        if choice == '0':
            Returning()
            return 
        
        found = 0
        Directing()

        if choice == '1':
            # Register 
            found  = 1
            print("Student Register Page")
            this_student = write_student()

        elif choice == '2':
            # sign in 
            print("Student Sign In Page")
            student_id = input('Enter ID: ')
            student_pass = getpass('Enter Password: ')
            [found, this_student] = search_student(student_id, student_pass)

        if not found:
            print("The ID or the Password is wrong, Please try Aagin")
            press_any()
            Returning()
            return


        stu_choic = '1'
        while stu_choic != '0':
            Directing()
            print('1- Show my Info')
            print('2- Add a new course')
            print('3- Show my courses')
            print('4- Update password')
            print('0- Logout')
            stu_choic = input('Choose: ')
            if stu_choic == '0':
                Returning()
                return
            
            Directing()

            if stu_choic == '1':
                print('ID\tName\tAge\tDepartment\tLevel\tPassword')
                print('------------------------------------------')
                for i in range(6):
                    print(this_student[i] + '\t', end='')
                print()
                press_any()
                Returning()
            elif stu_choic == '2':
                # Add new course
                courses_found = 0
                valid_choice = False
                with open('Teachers.txt', 'r') as teacher_file:
                    courses_list = []
                    for record in teacher_file:
                        fields = record.split('\t')
                        if fields[0] not in this_student[6:]:
                            print(fields[0] + '- ' + fields[3])
                            courses_list.append(fields[0])
                            courses_found += 1
                    if courses_found > 0:
                        print('0- return back')
                        course_choice = input('Choose: ')
                        if course_choice == '0':
                            continue
                        if course_choice in courses_list:
                            valid_choice = True
                            this_student = add_new_course(this_student[0], course_choice)

                    else:
                        print("There is no available courses for you now!")
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
                            print(fields[0] + '- ' + fields[3])
                if no_courses:
                    print('No Courses Found')
                press_any()
                Returning()
                
            elif stu_choic == '4':
                this_student = update_password(this_student[0])