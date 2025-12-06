#EXERCISE B
#Write a python program that takes from file 'guess.txt' a single line containing space-separated integers. 
#The user plays the following  game: he insert a number, and needs to guess the sum of two numbers in the line. 
#If the guess is correct, he is congratulated with 'You win' and the game ends. If the guess is wrong, he has to retry but gets: 'upper' if all possible sums are higher than the guessed number, 'lower' if tehy are all lower and 'try again' otherwise
#sample execution
#input file:
#4 12 13 5
#run
#8
#upper
#22
#try again
#25
#you win

from sys import argv

def read_numbers(filename):
    f = open(filename, "r")
    line = ""
    for l in f:
        line = l.strip()
    f.close()

    parts = line.split()
    numbers = []

    for p in parts:
        numbers.append(int(p))

    return numbers


def main():
    if len(argv) != 2:
        print("Usage: python script.py <input_file>")
        return

    filename = argv[1]
    numbers = read_numbers(filename)

    possible_sums = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            s = numbers[i] + numbers[j]
            possible_sums.append(s)

    min_sum = possible_sums[0]
    max_sum = possible_sums[0]

    for v in possible_sums:
        if v < min_sum:
            min_sum = v
        if v > max_sum:
            max_sum = v

    while True:
        guess_str = input("Enter a number: ")
        try:
            guess = int(guess_str)
        except:
            print("Please enter an integer.")
            continue

        if guess in possible_sums:
            print("You win")
            break
        elif guess < min_sum:
            print("lower")
        elif guess > max_sum:
            print("upper")
        else:
            print("try again")

main()
