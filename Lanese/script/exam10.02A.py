#EXERCISE A
#write a python program that takes from the user strings containing comma-separated integers. 
#The program takes a command line parameters an integer threshold and the name of a destination file to write teh results. For each line, the program prints on the destination file the number of pairs of integers in the line whose product is strictly greater than the threshold.
#sample execution:
#threshold: 18
#input:     #output file
#3,4,5      1
#4,4,23,1   3
#-3,8,1     0
from sys import argv

# controllo argomenti
if len(argv) != 3:
    print("Usage: python script.py <threshold> <output_file>")
    exit()

threshold = int(argv[1])
filename = argv[2]

f = open(filename, 'w')

while True:
    line = input('Enter numbers separated by comma (empty to stop): ').strip()

    if line == "":
        break

    parts = line.split(',')
    numbers = []

    try:
        for p in parts:
            numbers.append(int(p))
    except ValueError:
        print("Please enter only integers.")
        continue

    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > threshold:
                count += 1

    f.write(str(count))
    f.write("\n")

f.close()
