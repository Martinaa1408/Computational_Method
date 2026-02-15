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

def read_numbers_from_line(line):
    parts = line.strip().split()
    if parts == []:
        return []
    numbers = []
    for p in parts:
        numbers.append(int(p))
    return numbers


def has_pair_sum(numbers, n):
    found = False
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == n:
                found = True
                break
        if found:
            break
    return found


def main():
    try:
        input_file = open(filename, 'r')
    except FileNotFoundError:
        exit()

    for line in input_file:
        if line.strip() == '':
            continue

        numbers = read_numbers_from_line(line)
        print(numbers)

        n = int(input('insert a number to guess: '))
        found = has_pair_sum(numbers, n)
        print(found)

    input_file.close()


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit()
    filename = argv[1]
    main()
