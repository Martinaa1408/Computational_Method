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

from sys import argv
activities=[]
while True:
    choice = int(input('insert a choice (1-5):'))
    if choice==1:
        new_activity=input('insert a new activity:')
        starting_time=int(input('insert the starting time:'))
        end_time=int(input('insert an ending time:'))
        if starting_time<0 or starting_time>23 or end_time<1 or end_time>24 or starting_time>=end_time:
            print('invalid times')
            continue

        for act in activities:
            e_activity,e_start,e_end=act
            if starting_time<=e_end and end_time>=e_start:
                print('warning:overlaps with',e_activity,'(',e_start,'-',e_end,')')
        activities.append((new_activity, starting_time, end_time))
        print('activity', new_activity, 'is added')

    elif choice==2:
        print('— Your Daily Activities —')
        for act in activities:
            print(act[0],'from',act[1],'to',act[2])

    elif choice==3:
        file_output=open(argv[2],'w')
        for act in activities:
            new_activity, starting_time, ending_time=act
            line=new_activity+","+str(starting_time)+"-"+str(ending_time)+'\n'
            file_output.write(line)
        print('the activities are added into file',argv[2])
        file_output.close()

    elif choice==4:
        filename=open(argv[1],'r')
        for line in filename:
            line=line.strip()
            if line=='':
                continue
            parts=line.split(',')
            new_activity=parts[0]
            starting_time=int(parts[1])
            end_time=int(parts[2])
            for act in activities:
                e_activity, e_start, e_end = act
                if starting_time<=e_end and end_time>=e_start:
                    print('warning:',new_activity,'overlaps with',e_activity)
            activities.append((new_activity, starting_time, end_time))
        filename.close()
        print('activities are loaded from file',argv[1])

    elif choice==5:
        print('Exit')
        break







