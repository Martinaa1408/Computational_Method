from sys import argv

def read_numbers(input_file):
    """Reads a line of numbers from the input file and returns a list of integers."""
    try:
        file = open(input_file, "r")
        line = file.readline().strip()
        file.close()
        numbers = []
        for num in line.split():
            try:
                numbers.append(int(num))
            except ValueError:
                print("Error: invalid number.")
        return numbers
    except FileNotFoundError:
        print("Error: input file not found.")
        exit(1)

def guess_median_sum_game():
    """Game: user guesses the median sum of all possible pairs."""
    if len(argv) != 2:
        print("Usage: python script.py input_file")
        exit(1)

    numbers = read_numbers(argv[1])
    print("Guess the median sum of all pairs from the file!")

    pair_sums = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair_sums.append(numbers[i] + numbers[j])

    pair_sums.sort()
    n = len(pair_sums)
    if n % 2 == 1:
        median_sum = pair_sums[n // 2]
    else:
        median_sum = (pair_sums[n // 2 - 1] + pair_sums[n // 2]) // 2

    while True:
        try:
            guess = int(input("Enter a number: "))
        except ValueError:
            print("Error: please enter an integer.")
            continue

        if guess == median_sum:
            print("You win!")
            break
        elif guess > median_sum:
            print("Upper!")
        elif guess < median_sum:
            print("Lower!")
        else:
            print("Try again!")

guess_median_sum_game()
