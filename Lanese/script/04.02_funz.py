from sys import argv, exit

def load_exams(path):
    f = open(path, "r", encoding="utf-8")
    collections = []
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(";", 1)
            code = parts[0].strip()
            exam = parts[1].strip()
            collections.append((code, exam))
    f.close()
    return collections

def student_exists(info_student, sid):
    for (name, i) in info_student:
        if i == sid:
            return True
    return False

def student_name(info_student, sid):
    for (name, i) in info_student:
        if i == sid:
            return name
    return ""

def exam_exists(collections, code_in):
    for (code, exam) in collections:
        if code == code_in:
            return True
    return False

def exam_title(collections, code_in):
    for (code, exam) in collections:
        if code == code_in:
            return exam
    return ""

def register_student(info_student):
    name = input("Enter Name: ").strip()
    sid = input("Enter ID: ").strip()

    if student_exists(info_student, sid):
        print("Error: ID already exists.")
        return

    info_student.append((name, sid))
    print("Student registered successfully.")

def record_exam_outcome(collections, info_student, passed_exams, tot_praise):
    sid = input("Enter Student ID: ").strip()

    if not student_exists(info_student, sid):
        print("Error: student not found.")
        return tot_praise

    code_in = input("Enter Exam Code: ").strip()

    if not exam_exists(collections, code_in):
        print("Error: exam code does not exist.")
        return tot_praise

    try:
        grade = int(input("Enter Grade (18-30): ").strip())
    except ValueError:
        print("Error: grade must be an integer.")
        return tot_praise

    if not (18 <= grade <= 30):
        print("Error: invalid grade.")
        return tot_praise

    lode = False
    if grade == 30:
        praise = input("Add praise? (y/n): ").strip().lower()
        if praise == "y":
            lode = True
            tot_praise += 1

    passed_exams.append((sid, code_in, grade, lode))
    print("Outcome registered successfully.")
    return tot_praise

def student_report(collections, info_student, passed_exams):
    sid = input("Enter Student ID to search: ").strip()

    name = student_name(info_student, sid)
    if name == "":
        print("Error: student not found.")
        return

    print("\n--- STUDENT REPORT ---")
    print("Name:", name)
    print("ID:", sid)
    print("Passed Exams:")

    somma = 0
    count = 0
    praises_student = 0

    for (i, code, grade, lode) in passed_exams:
        if i == sid:
            title = exam_title(collections, code)

            if lode:
                print(f"- {code} | {title}: {grade} cum laude")
                praises_student += 1
            else:
                print(f"- {code} | {title}: {grade}")

            somma += grade
            count += 1

    if count == 0:
        avg = 0.0
        print("(none)")
    else:
        avg = somma / count

    print("-----------------------")
    print("Average Score:", round(avg, 1))
    print("Total Praises:", praises_student)
    print("-----------------------")

def main():
    if len(argv) != 2:
        print("usage: python3 career_manager.py exams_list.txt")
        exit(1)

    collections = load_exams(argv[1])

    info_student = []
    passed_exams = []
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

        if choice == 1:
            register_student(info_student)

        elif choice == 2:
            tot_praise = record_exam_outcome(collections, info_student, passed_exams, tot_praise)

        elif choice == 3:
            student_report(collections, info_student, passed_exams)

        elif choice == 4:
            print("Exiting program...")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
