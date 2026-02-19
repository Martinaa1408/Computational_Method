'''
Write a python program which takes from command line a file name and an optional -d flag.
The file needs to be a file of space-separated integers. The program prints on the screen the
longest strictly increasing sub-sequence. If two strictly increasing sub-sequences have the
same length, it prints the first one. If the optional -d flag is present, it prints instead the
longest strictly decreasing sub-sequence.
Example (without -d)
23 10 13 17 14 18 20 9 11
10 13 17
$ python3 prog.py -d numbers
23 10'''
from sys import argv


def read_filename(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            parts = line.strip().split()
            for p in parts:
                numbers.append(int(p))
    return numbers


def logic(numbers, decreasing):
    # decreasing = False  → cerca crescente
    # decreasing = True   → cerca decrescente

    if len(numbers) == 0:
        return []

    best_seq = [numbers[0]]       # migliore trovata finora
    current_seq = [numbers[0]]    # quella che sto costruendo ora

    for i in range(1, len(numbers)):

        previous = numbers[i - 1]
        current_number = numbers[i]

        if not decreasing:   # caso crescente
            if current_number > previous:
                current_seq.append(current_number)
            else:
                if len(current_seq) > len(best_seq):
                    best_seq = current_seq
                current_seq = [current_number]

        else:  # caso decrescente
            if current_number < previous:
                current_seq.append(current_number)
            else:
                if len(current_seq) > len(best_seq):
                    best_seq = current_seq
                current_seq = [current_number]

    # controllo finale
    if len(current_seq) > len(best_seq):
        best_seq = current_seq

    return best_seq


def main(filename, decreasing):
    numbers = read_filename(filename)
    result = logic(numbers, decreasing)
    print(" ".join(str(x) for x in result))


if __name__ == "__main__":

    if len(argv) == 2:
        filename = argv[1]
        decreasing = False

    elif len(argv) == 3 and argv[1] == "-d":
        filename = argv[2]
        decreasing = True

    else:
        exit()

    main(filename, decreasing)
