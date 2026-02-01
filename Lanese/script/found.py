'''Write a python program that takes a source file containing in each line integer numbers separated by spaces. 
For each line of the file, the program asks the user for an integer, say n, and returns true if the line contains two numbers whose sum is n, 
false otherwise. The name of the source file is taken as command line parameter. 
Source file 
23 -2 3 
9 12 23 
1 2 3 4 5 
13 10 12 
Input value 
1 
44 
6 
13 
Result 
True 
False 
True 
False'''



from sys import argv

input_file = open(argv[1], 'r')

for line in input_file:
    if line.strip() == '':
        continue

    line = line.rstrip().split()
    line = [int(p) for p in line]
    print(line)

    n = int(input('insert a number to guess: '))

    found = False
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            somma = line[i] + line[j]
            if somma == n:
                found = True
                break
        if found:
            break

    print(found)
