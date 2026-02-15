'''#Write a python program that takes from file 'guess.txt' a single line containing space-separated integers.
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
'''

def read_file(filename):
    numbers=[]
    try:
        with open(filename) as reader:
            for line in reader:
                line=line.strip()
                parts=line.split()
                try:
                    for p in parts:
                        numbers.append(int(p))
                except ValueError:
                    print('integers please')
                    continue
    except FileNotFoundError:
        exit()
    print(numbers)
    return numbers

def calculus(numbers):
    sum=[]
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            possible_sum=numbers[i]+numbers[j]
            sum.append(possible_sum)
    return sum

def main():
    while True:
        choice_str=input('insert a number:')
        sum=calculus(numbers)
        if choice_str=='' or not choice_str.isdigit():
            continue
        else:

            choice=int(choice_str)
            if choice in sum:
                print('you win')
                break
            elif choice>max(sum):
                print('lower')
                continue
            elif choice<min(sum):
                print('upper')
                continue
            else:
                print('try again')
                continue


if __name__=='__main__':
    from sys import argv
    if len(argv)!=2:
        print('nooo')
        exit()
    numbers=read_file(argv[1])
    main()
