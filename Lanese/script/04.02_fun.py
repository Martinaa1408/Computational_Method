'''Exercise module Lanese
Write a python program that helps the university managing student
records (for a single degree) and academic careers.
The program allows the user to:

- register a new student, by entering their Full Name and ID Number. ID Number must be unique.

- record the outcome of an exam, by providing Student ID, Exam Code,
and the Grade. The Grade must be between 18 and 30, and in case of
30 may include a Praise (Lode) The program must verify that the Exam
Code exists (see below).

- print the Student Career Report: given a student ID, it will print

--- student information (Full Name and Student ID)
--- list of passed exams (Code, Title, and Grade, including praise)
--- GPA: arithmetic average of the grades ("30 with praise" counts as "30")
--- total count of praises obtained

- exit from the program

The list of exams is available in a file, whose name is taken as
command line parameter. For each exam it contains its Exam Code and its
Title.

Sample Program Interaction

Command to start: python3 career_manager.py exams_list.txt

Content of exams_list.txt:

B01;Genetics
B02;Bioinformatics
B03;Organic Chemistry

Console Interaction:

--- UNIVERSITY CAREER MANAGER ---
1. Register Student
2. Record Exam Outcome
3. Student Career Report
4. Exit

Select an option: 1
Enter Name: Mario Rossi
Enter ID: 12345

Select an option: 2
Enter Student ID: 12345
Enter Exam Code: B01
Enter Grade (18-30): 30
Add praise? (y/n): y
Outcome registered successfully.

Select an option: 2
Enter Student ID: 12345
Enter Exam Code: B02
Enter Grade (18-30): 24
Add praise? (y/n): n
Outcome registered successfully.

Select an option: 3
Enter Student ID to search: 12345

--- STUDENT REPORT ---
Name: Mario Rossi
ID: 12345
Passed Exams:
- B01 | Genetics: 30 cum laude
- B02 | Bioinformatics: 24
-----------------------
Average Score: 27.0
Total Praises: 1
-----------------------

Select an option: 4
Exiting program... '''

'''def read_filename(filename):
    return []
def main():
    menu_str=(
    '\n\n--- UNIVERSITY CAREER MANAGER ---'
    '1. Register Student\n'
    '2. Record Exam Outcome\n'
    '3. Student Career Report\n'
    '4. Exit'
    )
    while True:
        print(menu_str)
        choice=input('Select an option:')
        if choice=='1':
            insert_student()
        elif choice=='2':
            record_exam()

        elif choice=='3':
            print_report()

        elif choice=='4':
            print('Exiting program... ')
            break
        else:
            print('warning message: you must insert an invalid character')
            continue

def insert_student():
    pass
def record_exam():
    pass
def print_report():
    pass



if __name__=='__main__':
    from sys import argv
    if len(argv)!=2:
        exit()

exams=read_filename(argv[1])  #lista exams
main()   -->questo è lo schema base da qui implementi'''

def read_filename(filename):
    exams={}
    try:
        with open(filename) as reader:
            for line in reader:
                line=line.rstrip()
                parts=line.split(';')
                code=parts[0]
                name=parts[1]
                exams[code]=name

    except FileNotFoundError:
        print('file not found')
        exit()
    return exams
#you can read the code and the name like a dictionary: homogeneous view: id unique

def main():
    global exams   # <-- USA il dizionario letto nel __main__, NON lo azzera!
    students = {}
    # id -> student_name

    careers = {}
    # (id, code) -> (exams-name, grade, lode)

    menu_str = (
    '\n\n--- UNIVERSITY CAREER MANAGER ---\n'
    '1. Register Student\n'
    '2. Record Exam Outcome\n'
    '3. Student Career Report\n'
    '4. Exit\n'
    )

    while True:
        print(menu_str)
        choice = input('Select an option:')

        if choice == '1':
            students = insert_student(students)

        elif choice == '2':
            careers = record_exam(exams, students, careers)

        elif choice == '3':
            # stampa nome studente, lista esami,
            # media aritmetica (30L = 30) e numero lodi
            print_report(exams, students, careers)

        elif choice == '4':
            print('Exiting program... ')
            break

        else:
            print('warning message: you must insert a valid character')
            continue


def insert_student(students):
    #cosa mi serve da passare alla funzione: gli studenti

    '''Enter Name: Mario Rossi
    Enter ID: 12345
    '''
    student_name=input('enter name:')
    id=input('enter ID:')
    #gestione id unico-->valutazione errore
    if student_name == '' or id == '':
        print('warning message: empty name or ID')
        return students

        # gestione id unico (sugli studenti, non sugli exams)
    if id in students:
        print('warning message: ID already exists')
        return students
    else:
        students[id] = student_name
        print('Student registered successfully.')
        return students

def record_exam(exams,students,careers):
    '''Enter Student ID: 12345
    Enter Exam Code: B02
    Enter Grade (18-30): 24
    Add praise? (y/n): n
    Outcome registered successfully.
    '''
    id = input('enter ID:')
    if id not in students:
        print('warning message: student ID not found')
        return careers

    code=input('Enter Exam Code: ')
    if code not in exams:
        print('warning message: exam code not found')
        return careers
    grade_str= input('Enter Grade (18-30): ').strip()

    if not grade_str.isdigit():
        print('warning message: grade must be a number')
        return careers
    grade = int(grade_str)

    if grade < 18 or grade > 30:
        print('warning message: grade must be between 18 and 30')
        return careers

    ans = ''
    if grade == 30:
        ans = input('Add praise? (y/n): ').strip().lower()

    lode = (ans == 'y')

    key = (id, code)

    if key in careers:
        print('warning message: exam already recorded for this student')
        return careers

    exam_name = exams[code]

    careers[key] = (exam_name, grade, lode)

    print('Outcome registered successfully.')
    return careers


def print_report(exams, students, careers):
    id = input('Enter Student ID to search: ').strip()

    if id not in students:
        print('warning message: student ID not found')
        return

    report_str = (
            '\n--- STUDENT REPORT ---\n'
            'Name: ' + students[id] + '\n'
            'ID: ' + id + '\n'
            'Passed Exams:\n'
            )

    print(report_str)

    total = 0
    count = 0
    praises = 0

    for (id_key, code), (exam_name, grade, lode) in careers.items():
        if id_key == id:

            if lode:
                print('- ' + code + ' | ' + exam_name + ': ' + str(grade) + ' cum laude')
                praises += 1
            else:
                print('- ' + code + ' | ' + exam_name + ': ' + str(grade))

            total += grade
            count += 1

    if count == 0:
        print('(none)')
        print('-----------------------')
        print('Average Score: 0.0')
        print('Total Praises: 0')
        print('-----------------------')
        return

    avg = total / count

    print('-----------------------')
    print('Average Score:', avg)
    print('Total Praises:', praises)
    print('-----------------------')



if __name__=='__main__':
    from sys import argv
    if len(argv)!=2:
        exit()
    exams=read_filename(argv[1])
    main()
