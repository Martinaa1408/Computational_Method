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

def read_numbers(input_file):
    """Reads a line of numbers from the input file and returns a list of integers."""
    try:
        file = open(input_file, "r")
        line = file.readline().strip()
        file.close()

        parts = line.split()
        numbers = []
        for num in parts:
            try:
                numbers.append(int(num))
            except ValueError:
                print('Error: invalid line.')
        return numbers

    except FileNotFoundError:
        print('Error: input file not found.')
        exit(1)

def guess_game():
    """Handles the game logic: reads the file, generates possible sums, and prompts user guesses."""
    if len(argv) != 2:
        print("Usage: python script.py input_file")
        exit(1)

    input_file = argv[1]
    numbers = read_numbers(input_file)

    print("Guess the sum of two numbers from the file!")

    possible_sums = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            print(i, j)
            possible_sums.append(numbers[i] + numbers[j])

    while True:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Error: please enter an integer.")
            continue

        if guess in possible_sums:
            print("You win!")
            break
        elif guess > max(possible_sums):
            print("Upper!")
        elif guess < min(possible_sums):
            print("Lower!")
        else:
            print("Try again!")

guess_game()
