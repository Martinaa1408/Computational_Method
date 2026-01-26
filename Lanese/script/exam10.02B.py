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

from sys import argv
input_file=open(argv[1],'r')
collections=[]
for line in input_file:
    line=line.strip().split()
    if line=='':
        continue
    else:
        for p in line:
            collections.append(int(p))
input_file.close()
print(collections)

possible_sum=[]
for i in range(len(collections)):
    for j in range(i+1,len(collections)):
        sum=collections[i]+collections[j]
        possible_sum.append(sum)
print(possible_sum)


while True:
    guess=int(input('insert a number to guess:'))
    if guess in possible_sum:
        print('you win')
        break
    elif guess<min(possible_sum):
        print('upper')
    elif guess>max(possible_sum):
        print('lower')
    else:
        print('try again')
        continue




