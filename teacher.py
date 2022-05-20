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
                PutSp(20 , ' ')   
                fields[4] = getpass("Enter the new password for " + fields[1] + ": ")
                record = ""
                for i in range(len(fields)):
                    record += fields[i] + '\t'
                record += '\n'
                ThisTec = record.split('\t')
            temp_file.write(record)
        if not flag:
            SetCo('red')
            PutSp(50 , ' ')
            print('Teacher not found')
            sound("Teacher not found")
        else:
            SetCo('green')
            PutSp(40 , ' ')
            print('Teacher updated successfully')
            sound("Teacher updated successfully")
    os.remove('Teachers.txt')
    os.rename('Temp.txt', 'Teachers.txt')
    return ThisTec

def teacher():
    Directing()
    choice = '1'
    while choice != '0':
        #Menu:
        SetCo('green')
        table('Choose: ' , 30)
        table("1- Sign in" ,30)
        SetCo('red')
        table("0- Return Back" , 30)
        table("" , 30)
        SetCo('gold')
        PutSp(20 , ' ')
        Reg = input('Choice: ')
        
        if Reg == '0':
            Returning()
            return
        
        found = 1
        thisTeacher = []
        if Reg == '1':
            Directing()
            SetCo('blue')
            SetCo('green')
            table("Teacher Sign In Page", 40)
            table("" , 40)
            PutSp(20 , ' ')
            SetCo('gold')
            TecID = input('Enter ID: ')
            PutSp(20 , ' ')
            TecPass = getpass('Enter Password: ')
            
            [found, thisTeacher] = SearchTeacher(TecID, TecPass)
        
        if not found:
            SetCo('red')
            PutSp(20 , ' ')
            print("The ID or the Password is wrong, Please try Aagin")
            sound("The ID or the Password is wrong, Please try Aagin")
            press_any()
            Returning()
            return
        
        TecCh = '1'
        while TecCh != '0':
            Directing()
            SetCo('green')
            table('1) Show my Info' , 30)
            table('2) Show my students' , 30)
            table('3) Update password' , 30)
            SetCo('red')
            table('0) Logout' , 30)
            table("" , 30)
            SetCo('gold')
            PutSp(20 , ' ')
            TecCh = input('Choose: ')
            if TecCh == '0':
                Returning()
                return
            
            Directing()

            if TecCh == '1':
                PutSp(40 , " ")
                SetCo('brown')
                print('ID\tName\tAge\tCourse\t\tPassword')
                PutSp(40 , " ")
                print('-' * 50)
                PutSp(40 , " ")
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
                        PutSp(50 , ' ')
                        SetCo('red')
                        sound("There is no Students yet")
                        print('There\'s no Students yet.')
                    press_any()
            
            elif TecCh == '3':
                thisTeacher = update_Teacher(thisTeacher[0])
