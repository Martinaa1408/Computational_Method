'''Write a python program that takes two filenames from the command
line. It reads from the first file, which contains dates in the format
dd/mm/yyyy (one per line), and for each date in the first file, it
writes on the second file the number of days after 01/01/2000, or
Error in case the format is not correct. Assume all the years have 365
days (i.e., assume there are no leap years).

YOU CANNOT USE LIBRARY FUNCTIONS FOR DATE ELABORATION (e.g., from
datetime, calendar, time or dateutil libraries).

Ex.  

Input file:          Output file:  

01/01/2000      0
02/01/2000      1
31/12/2000      364
01/01/2001      365
15/06/2025      9288
32/01/2000      Error
1/2/2001        Error
12-03-2005      Error
01/01/1999      Error
0A/01/2001      Error '''

from sys import argv

day=[31,28,31,30,31,30,31,31,30,31,30,31]
year_ref=2000
month_ref=1
day_ref=1

input_file=open(argv[1],'r')
output_file = open(argv[2], 'w')
for line in input_file:
    line=line.strip().split('/')
    try:
        if len(line[0])<2 or len(line[1])<2:
            result='Error'
        else:
            for p in range(len(line)):
                line[p] = int(line[p]) #line=[int(p) for p in line]
            if  line[1]>12 or line[1]<1 or line[2]<2000 or line[0]>day[line[1]-1]:
                result='Error'
            else:
                result = ((line[2] - year_ref) * 365 + (sum(day[0:(line[1] - 1)])) + (line[0] - day_ref)) #logic
    except:
        result='Error'
    output_file.write(str(result) + '\n')

input_file.close()
output_file.close()
