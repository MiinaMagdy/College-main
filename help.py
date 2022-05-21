from queue import PriorityQueue
from getpass import getpass
import os
import time
from msvcrt import getch        # for windows users
from textwrap import wrap
import pyttsx3

# record of Student ->     Id + '\t' + Name + '\t' + Age + '\t' + Department + '\t' + Level + '\t' + Password + '\t' + [courses] + '\t\n'
# record of Teahcer ->     Id + '\t' + Name + '\t' + Age + '\t' + Course_name + '\t' + Password + '\t' + [students] + '\t\n'

class bcolors:
    red = '\033[38;5;196m'
    green = '\033[38;5;40m'
    blue = '\033[34m'
    gold = '\033[38;5;220m'
    white = '\33[37m'
    magenta = '\033[35m'
    brown = '\033[38;5;94m'
    bold = '\033[01m'
    reset = '\033[0m'

def SetCo(s):
    lis = {
        bcolors.red: 'red', bcolors.green: 'green', 
        bcolors.blue:'blue', bcolors.gold: 'gold',
        bcolors.magenta : 'magenta', bcolors.brown : 'brown', 
        bcolors.reset : 'reset', bcolors.white: 'white',
    }
    lis = { value:key for key, value in lis.items()}
    print(f'{lis[s]}', end='')

def PutSp(n, ch):
    print(n * str(ch), end='')

students_ids = PriorityQueue()
teachers_ids = PriorityQueue()

existance_student_id = [False for i in range(205)]
existance_teacher_id = [False for i in range(205)]

def sound(sentence):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(sentence)
    engine.runAndWait()

def press_any():
    print()
    SetCo('blue')
    PutSp(30 , ' ')
    print("Press any key to return back...", end = '', flush=True)
    sound("press any key to continue please")
    getch()
    print()
    

def Directing():
    PutSp(30 , ' ')
    SetCo('magenta')
    print('Redicrecting', end='', flush = True)
    for i in range(3):
        print('.', end='', flush = True)
        time.sleep(0.3)
    time.sleep(0.2)
    os.system("cls")
    print()

def Returning():
    print()
    PutSp(30 , ' ')
    SetCo('red')
    print('Returning', end='', flush = True)
    for i in range(3):
        print('.', end='', flush = True)
        time.sleep(0.3)
    time.sleep(0.2)
    os.system("cls")
    print()

def init_student_ids():
    with open("Student.txt", 'r') as student_file:
        for record in student_file:
            fields = record.split('\t')
            existance_student_id[int(fields[0])] = 1
        for i in range(1, 205, 1):
            if not existance_student_id[i]:
                students_ids.put(i)

def init_teacher_ids():
    with open("Teachers.txt", 'r') as teacher_file:
        for record in teacher_file:
            fields = record.split('\t')
            existance_teacher_id[int(fields[0])] = 1
        for i in range(1, 205, 1):
            if not existance_teacher_id[i]:
                teachers_ids.put(i)
                
def table(text , w  , m = 40 ):
    sentence = text
    width = w
    PutSp(m , " ")
    print('+-' + '-' * width + '-+')

    for line in wrap(sentence, width):
        PutSp(m , " ")
        print('| {0:^{1}} |'.format(line, width))
