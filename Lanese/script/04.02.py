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


from sys import argv, exit

# controllo argomenti SUBITO
if len(argv) != 2:
    print("usage: python3 career_manager.py exams_list.txt")
    exit(1)

# --- leggo file esami ---
file_input = open(argv[1], 'r')
collections = []
for line in file_input:
    line = line.strip()
    if line != '':
        parts = line.split(';')
        code = parts[0].strip()
        exam = parts[1].strip()
        collections.append((code, exam))
file_input.close()

info_student = []   # [(name, id)]
passed_exams = []   # [(id, code, grade, lode)]
tot_praise = 0

while True:
    print("\n--- UNIVERSITY CAREER MANAGER ---")
    print("1. Register Student")
    print("2. Record Exam Outcome")
    print("3. Student Career Report")
    print("4. Exit")

    try:
        choice = int(input("Select an option: ").strip())
    except ValueError:
        print("Invalid option.")
        continue

    # 1) REGISTER
    if choice == 1:
        name = input('Enter Name: ').strip()
        sid = input('Enter ID: ').strip()

        # ID unico
        ok = True
        for (n, i) in info_student:
            if i == sid:
                ok = False

        if ok:
            info_student.append((name, sid))
            print("Student registered successfully.")
        else:
            print("Error: ID already exists.")

    # 2) RECORD EXAM
    elif choice == 2:
        sid = input("Enter Student ID: ").strip()

        # controllo studente esiste
        found_student = False
        for (n, i) in info_student:
            if i == sid:
                found_student = True
        if not found_student:
            print("Error: student not found.")
            continue

        code_in = input("Enter Exam Code: ").strip()

        # controllo exam code esiste
        found_exam = False
        for (code, exam) in collections:
            if code == code_in:
                found_exam = True
        if not found_exam:
            print("Error: exam code does not exist.")
            continue

        # voto
        try:
            grade = int(input("Enter Grade (18-30): ").strip())
        except ValueError:
            print("Error: grade must be an integer.")
            continue

        if not (18 <= grade <= 30):
            print("Error: invalid grade.")
            continue

        lode = False
        if grade == 30:
            praise = input("Add praise? (y/n): ").strip().lower()
            if praise == 'y':
                lode = True
                tot_praise += 1

        # aggiungo risultato (come nel secondo)
        passed_exams.append((sid, code_in, grade, lode))
        print("Outcome registered successfully.")

    # 3) REPORT
    elif choice == 3:
        sid = input("Enter Student ID to search: ").strip()

        # recupero nome studente
        name = ""
        for (n, i) in info_student:
            if i == sid:
                name = n
        if name == "":
            print("Error: student not found.")
            continue

        print("\n--- STUDENT REPORT ---")
        print("Name:", name)
        print("ID:", sid)
        print("Passed Exams:")

        somma = 0
        count = 0
        praises_student = 0

        for (i, code, grade, lode) in passed_exams:
            if i == sid:
                # titolo esame
                title = ""
                for (c, e) in collections:
                    if c == code:
                        title = e

                if lode:
                    print(f"- {code} | {title}: {grade} cum laude")
                    praises_student += 1
                else:
                    print(f"- {code} | {title}: {grade}")

                somma += grade
                count += 1

        if count == 0:
            avg = 0.0
        else:
            avg = somma / count

        print("-----------------------")
        print("Average Score:", round(avg, 1))
        print("Total Praises:", praises_student)
        print("-----------------------")

    # 4) EXIT
    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid option.")
