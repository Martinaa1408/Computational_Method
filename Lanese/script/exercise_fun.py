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


def eval_expr(expr):
    operator = '+-'
    numbers = '0123456789'

    parts = ''.join(expr.strip().split())
    if parts == '':
        return None, None

    tot = 0
    num = ""
    sign = 1

    for el in parts:
        if el in numbers:
            num += el
        elif el in operator:
            tot += sign * int(num)
            num = ""
            if el == '+':
                sign = 1
            else:
                sign = -1

    tot += sign * int(num)
    return parts, tot


def main():
    try:
        file_inp = open(in_filename, 'r')
    except FileNotFoundError:
        exit()

    results = ""

    for line in file_inp:
        expr, value = eval_expr(line)
        if expr is None:
            continue
        results += expr + "=" + str(value) + "\n"

    file_inp.close()

    if out_filename == '':
        print(results, end='')
    else:
        with open(out_filename, 'w') as out:
            out.write(results)


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2 and len(argv) != 3:
        exit()

    in_filename = argv[1]
    out_filename = ''
    if len(argv) == 3:
        out_filename = argv[2]

    main()
