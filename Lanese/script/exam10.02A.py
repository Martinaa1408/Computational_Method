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

def comma_separated_numbers():
    line = input('Enter numbers separated by comma (empty to stop): ').strip()
    if line == "":
        return None
    parts = line.split(',')
    numbers = []
    for p in parts:
        numbers.append(int(p))
        
    return numbers


def product_over_threshold(numbers, threshold):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > threshold:
                count += 1
    return count


def write_file():
    if len(argv) != 3:
        print("Usage: python script.py <threshold> <output_file>")
        return
    threshold = int(argv[1])
    filename = argv[2]
    f = open(filename, 'w')
    while True:
        try:
            numbers = comma_separated_numbers()
        except ValueError:
            print("Please enter only integers.")
            continue
        if numbers is None:
            break
        count = product_over_threshold(numbers, threshold)
        f.write(str(count))
        f.write("\n")
    f.close()

def main():
    write_file()
main()
