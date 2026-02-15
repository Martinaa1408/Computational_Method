#EXERCISE A
#write a python program that takes from the user strings containing comma-separated integers.
#The program takes a command line parameters an integer threshold and the name of a destination file to write teh results. For each line, the program prints on the destination file the number of pairs of integers in the line whose product is strictly greater than the threshold.
#sample execution:
#threshold: 18
#input:     #output file
#3,4,5      1
#4,4,23,1   3
#-3,8,1     0

def read_filename():
    line = input('insert a line of numbers separated by comma:')
    if line == '':
        return None

    numbers = []
    parts = line.split(',')
    print(parts)

    try:
        for p in parts:
            numbers.append(int(p))
    except:
        print("Please enter only integers.")
        return []   # segnalo errore
    print(numbers)
    return numbers


def compute(numbers, threshold):
    results = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] * numbers[j] > threshold:
                results += 1
    return results


def write_file(filename, result):
    with open(filename, 'a') as writer:   # append
        writer.write(str(result) + '\n')


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 3:
        print('usage python3 script.py threshold output.txt')
        exit()

    threshold = int(argv[2])
    filename = argv[1]


    while True:
        numbers = read_filename()

        if numbers is None:
            break

        if numbers == []:
            continue

        result = compute(numbers, threshold)
        write_file(filename, result)
