'''
Write a python program that takes a source file containing in each line an arithmetic integer
expression with only sums and subtractions, and computes the results. The name of the
source file is taken as command line parameter. If there is an additional command line
parameter then this is the name of the file where the results will be written, otherwise the
results are printed on the screen.
Input
34+12-2
10-23+1
100+3+12+2
2
Output
34+12-2=44
10-23+1=-12
100+3+12+2=117
2=2   '''

def read_file(filename):
    lines = []
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line != "":
                    lines.append(line)
    except FileNotFoundError:
        print("warning: file not found")
        exit()
    return lines


def write_file(filename, results):
    with open(filename, "w") as f:
        for line in results:
            f.write(line + "\n")


def main():
    lines = read_file(argv[1])
    results = []

    for expr in lines:

        total = 0
        num = ""
        op = "+"   # operatore iniziale

        for ch in expr:

            if ch.isdigit():
                num += ch

            elif ch == "+" or ch == "-":

                if op == "+":
                    total += int(num)
                else:
                    total -= int(num)

                op = ch      # aggiorno operatore
                num = ""

        # aggiungo l'ultimo numero
        if op == "+":
            total += int(num)
        else:
            total -= int(num)

        results.append(expr + "=" + str(total))

    return results


if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2 and len(argv) != 3:
        print("usage: python3 script.py source.txt [output.txt]")
        exit()

    results = main()

    if len(argv) == 3:
        write_file(argv[2], results)
    else:
        for line in results:
            print(line)
