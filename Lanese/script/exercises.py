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
from sys import argv


file_inp = open(argv[1], 'r')

operator = '+-'
numbers = '0123456789'
results = ""

for line in file_inp:
    parts = ''.join(line.strip().split())

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

    results += parts + "=" + str(tot) + "\n"

file_inp.close()
print(results)
