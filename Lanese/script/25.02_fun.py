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



def main():
    filename = argv[1]
    option = argv[2].upper()

    if option != 'MIN' and option != 'MAX' and option != 'BOTH':
        print('warning')
        exit()

    try:
        with open(filename) as reader:

            if option == 'MIN' or option == 'BOTH':
                writer_min = open('min.txt', 'w')
            if option == 'MAX' or option == 'BOTH':
                writer_max = open('max.txt', 'w')

            for line in reader:
                line = line.strip()
                parts = line.split()

                numbers = []
                try:
                    for p in parts:
                        numbers.append(int(p))
                except ValueError:
                    if option == 'MIN' or option == 'BOTH':
                        writer_min.write('\n')
                    if option == 'MAX' or option == 'BOTH':
                        writer_max.write('\n')
                    continue

                local_min = []
                local_max = []

                n = len(numbers)
                if n <= 1:
                    if option == 'MIN' or option == 'BOTH':
                        writer_min.write('\n')
                    if option == 'MAX' or option == 'BOTH':
                        writer_max.write('\n')
                    continue

                # first
                if numbers[0] < numbers[1]:
                    local_min.append(numbers[0])
                elif numbers[0] > numbers[1]:
                    local_max.append(numbers[0])

                # middle
                for i in range(1, n - 1):
                    if numbers[i] < numbers[i - 1] and numbers[i] < numbers[i + 1]:
                        local_min.append(numbers[i])
                    elif numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
                        local_max.append(numbers[i])

                # last
                if numbers[-1] < numbers[-2]:
                    local_min.append(numbers[-1])
                elif numbers[-1] > numbers[-2]:
                    local_max.append(numbers[-1])

                if option == 'MIN' or option == 'BOTH':
                    writer_min.write(' '.join(str(x) for x in local_min) + '\n')

                if option == 'MAX' or option == 'BOTH':
                    writer_max.write(' '.join(str(x) for x in local_max) + '\n')

            if option == 'MIN' or option == 'BOTH':
                writer_min.close()
            if option == 'MAX' or option == 'BOTH':
                writer_max.close()

    except FileNotFoundError:
        exit()


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 3:
        print('warning')
        exit()
    main()
