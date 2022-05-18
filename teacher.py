from help import *

def SearchTeacher(_id = '-1', _pass = '-1'):
    with open('Teachers.txt', 'r') as InFile:
        flag = 1

        for Tec in InFile:
            fields = Tec.split('\t')
            if _id == fields[0] and _pass == fields[4]:
                return [True, fields]
        
    return [False, []]

def update_Teacher(_id = '-1'):
    with open('Teachers.txt', 'r') as TechFile, open('Temp.txt', 'w') as temp_file:
        flag = False
        for record in TechFile:
            fields = record.split('\t')
            fields.pop()
            if _id == fields[0]:
                flag = True    
                fields[4] = getpass("Enter the new password for " + fields[1] + ": ")
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                ThisTec = record.split('\t')
            temp_file.write(record)
        if not flag:
            print('Teacher not found')
        else:
            print('Teacher updated successfully')
    os.remove('Teachers.txt')
    os.rename('Temp.txt', 'Teachers.txt')
    return ThisTec

def teacher():
    Directing()
    choice = '1'
    while choice != '0':
        #Menu:
        print('Choose: ')
        print(8 * '-')
        print("1- Sign in")
        print("0- Return Back")
        
        Reg = input('Choice: ')
        
        if Reg == '0':
            Returning()
            return
        
        found = 1
        thisTeacher = []
        if Reg == '1':
            Directing()
            print("Teacher Sign In Page")
            print(22 * '-')
            TecID = input('Enter ID: ')
            TecPass = getpass('Enter Password: ')
            [found, thisTeacher] = SearchTeacher(TecID, TecPass)
        
        if not found:
            print("The ID or the Password is wrong, Please try Aagin")
            press_any()
            Returning()
            return
        
        TecCh = '1'
        while TecCh != '0':
            Directing()
            print('1) Show my Info')
            print('2) Show my students')
            print('3) Update password')
            print('0) Logout')
            TecCh = input('Choose: ')
            if TecCh == '0':
                Returning()
                return
            
            Directing()

            if TecCh == '1':
                print('ID\tName\tAge\tCourse\tPassword')
                print('-' * 50)
                print('\t'.join(map(str, thisTeacher[0: 3])) + '\t  ' + thisTeacher[3] + '\t\t    ' +'\t'.join(map(str, thisTeacher[4: 5])))
                press_any()
            
            elif TecCh == '2':
                flag = 0
                with open('Student.txt', 'r') as StuFile:
                    for stu in StuFile:
                        fields = stu.split('\t')
                        if fields[0] in thisTeacher[5:]:
                            flag = 1
                            print(fields[0] + '- ' + fields[1])
                    if not flag:
                        print('There\'s no Students yet.')
                    press_any()
            
            elif TecCh == '3':
                thisTeacher = update_Teacher(thisTeacher[0])