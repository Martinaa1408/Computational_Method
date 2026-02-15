'''Exam cmBio 18/7/2025

Exercise – Lanese Module

Write a Python program that helps users managing their daily activities (we consider a single day). An activity has a starting time, an end time, and a name. Times are expressed as just hours, between 0 and 24.

0 can only be used as starting time

24 only as end time

The user can, interactively:

add an activity, by specifying all the information. The user gets a warning if the new activity overlaps in time with existing activities (the activity is inserted anyway)

print on the screen all the activities

print on file all the activities (using one line per activity, as comma-separated fields)

read from file all the activities (this will overwrite the current list of activities)

exit from the program

It is not required to sort the activities for printing or saving.
The file name to be used to read and/or write is provided as command line parameter.

Sample execution (with parameter daily_activities.txt):


===== Daily Activity Manager =====
1. Add a new activity
2. Print all activities
3. Save activities to file
4. Load activities from file
5. Exit

Enter your choice (1-5): 1

— Add New Activity —
Enter activity name: Wake up
Enter start time (0-23): 6
Enter end time (1-24): 7
Activity 'Wake up' added!
pgsql
Copy
Edit
Warning: This activity overlaps with existing activity 'Wake up (6 - 7)'
Activity 'Breakfast' added!

===== Daily Activity Manager =====
1. Add a new activity
2. Print all activities
3. Save activities to file
4. Load activities from file
5. Exit

Enter your choice (1-5): 1

— Add New Activity —
Enter activity name: Work
Enter start time (0-23): 8
Enter end time (1-24): 16
Activity 'Work' added successfully!
pgsql
Copy
Edit
===== Daily Activity Manager =====
1. Add a new activity
2. Print all activities
3. Save activities to file
4. Load activities from file
5. Exit

Enter your choice (1-5): 2

— Your Daily Activities —
1. Wake up from 6 to 7
2. Breakfast from 6 to 8
3. Work from 8 to 16  '''

def overlaps(start, end, e_start, e_end):
    return start <= e_end and end >= e_start


def add_activity(activities):
    print('— Add New Activity —')
    name = input('Enter activity name: ')
    start = int(input('Enter start time (0-23): '))
    end = int(input('Enter end time (1-24): '))

    if start < 0 or start > 23 or end < 1 or end > 24 or start >= end:
        print('invalid times')
        return activities

    for act in activities:
        e_name, e_start, e_end = act
        if overlaps(start, end, e_start, e_end):
            print("Warning: overlaps with", e_name, "(", e_start, "-", e_end, ")")

    activities.append((name, start, end))
    print("Activity", name, "added!")
    return activities


def print_activities(activities):
    print('— Your Daily Activities —')
    for i in range(len(activities)):
        name, start, end = activities[i]
        print(str(i+1) + ".", name, "from", start, "to", end)


def save_activities(activities):
    with open(filename, 'w') as writer:
        for act in activities:
            name, start, end = act
            writer.write(name + "," + str(start) + "," + str(end) + "\n")
    print("Activities saved to file", filename)


def load_activities():
    activities = []
    try:
        with open(filename, 'r') as reader:
            for line in reader:
                line = line.strip()
                if line == '':
                    continue
                parts = line.split(',')
                if len(parts) != 3:
                    continue
                name = parts[0]
                start = int(parts[1])
                end = int(parts[2])
                activities.append((name, start, end))
        print("Activities loaded from file", filename)
    except FileNotFoundError:
        print("File not found")
    return activities


def main():
    activities = []

    menu = (
        "\n===== Daily Activity Manager =====\n"
        "1. Add a new activity\n"
        "2. Print all activities\n"
        "3. Save activities to file\n"
        "4. Load activities from file\n"
        "5. Exit\n"
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            activities = add_activity(activities)
        elif choice == '2':
            print_activities(activities)
        elif choice == '3':
            save_activities(activities)
        elif choice == '4':
            activities = load_activities()
        elif choice == '5':
            print("Exit")
            break
        else:
            print("Invalid choice")


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit()

    filename = argv[1]   # globale
    main()
