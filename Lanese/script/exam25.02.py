#Write a python program that accepts two command-line parameters: a filename and an option (MIN/MAX/BOTH). The specified file contain space separated
#integers.
#This program should process each line of the file and:
#If the option is MIN or BOTH, calculate the local minima and write them to the min.txt file.
#If the option is MAX or BOTH, calculate the local minima and write them to the max.txt file.
#A local minim is a number that is strictly less than both the preceding and following numbers. If a number is at the begining or end of the line,
#it is considereded a local minimum if it is less than the adjacent number (if present). A local maximum is defined symmetrically, with the condition of
#being strictly greater.

#Example:
#Input file:
# 1 2 1 1 5 3
# 4 2 6 1 4 5 9 1

#Output file min.txt:
#1 3
#2 1 1
#Output file max.txt:
#2 5
#4 6 9

from sys import argv
input_file=open(argv[1],'r')
output_min=open(argv[2],'w')
output_max=open(argv[3],'w')
option=(argv[4]).upper()
numbers=[]
for line in input_file:
    line=line.strip().split()
    if line=='':
        continue
    else:
        for p in line:
            numbers.append(int(p))
local_max = []
local_min = []
# middle numbers
for i in range(1, len(numbers) - 1):
    if numbers[i] > numbers[i + 1] and numbers[i] > numbers[i - 1]:
        local_max.append((numbers[i]))
    elif numbers[i] < numbers[i + 1] and numbers[i] < numbers[i - 1]:
        local_min.append((numbers[i]))
# at beginning
if numbers[0] < numbers[1]:
    local_min.append(numbers[0])
elif numbers[0] > numbers[1]:
    local_max.append(numbers[0])
# at the end
if numbers[-1] > numbers[-2]:
    local_max.append(numbers[-1])
elif numbers[-1] < numbers[-2]:
    local_min.append(numbers[-1])
print(local_min)
print(local_max)

#list comprhension
str_max = ' '.join([str(x) for x in local_max])
str_min = ' '.join([str(x) for x in local_min])

if option == 'MIN':
    output_min.write(str(str_min) + '\n')
elif option == 'MAX':
    output_max.write(str(str_max) + '\n')
else:
    output_min.write(str(str_min) + '\n')
    output_max.write(str(str_max) + '\n')

input_file.close() 
output_min.close()
output_max.close()
