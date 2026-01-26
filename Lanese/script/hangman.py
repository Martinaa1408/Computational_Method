'''Write a python program to play the hangman game. It reads words from a file (whose name is taken as command line parameter), and plays rounds on the hangman game using them till the user asks to stop.
The game works as follows.
The schema of the word obtained by replacing vowels with +, consonants with – and any other symbol with ? is printed on the screen.
The user can insert a letter, or guess the word.
In the first case, all occurrences of the letter in the word are shown, and the game continues.
In the second case, if the guess is correct then the user wins, and the game shows the number of total tries, otherwise the game continues.

Ex. (assuming the first word in the file is CLASSROOM, user input in red)
--+---++-
Insert a letter or guess the word:A
--A---++-
Insert a letter or guess the word:E
--A---++-
Insert a letter or guess the word:O
--A---OO-
Insert a letter or guess the word:S
--ASS-OO-
Insert a letter or guess the word:T
--ASS-OO-
Insert a letter or guess the word:GLASSNOON
Nice try! ... but wrong...
--ASS-OO-
Insert a letter or guess the word:CLASSROOM
You win! In 7 tries!
Do you want to play again Y/N? N

'''

from sys import argv
input_file = open(argv[1], 'r')

guess_word = []
for line in input_file:
    line = line.rstrip().upper()
    if line == '':
        continue
    for p in line:
        guess_word.append(p)

input_file.close()

print(guess_word) #check

vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

# text is the scheme
text = []
for i in range(len(guess_word)):
    if guess_word[i] in vowels:
        text.append('+')
    elif guess_word[i] in consonants:
        text.append('-')
    else:
        text.append('?')

print(''.join(text)) #check scheme

tries = 0
while True:
    user = input('Insert a letter or guess the word:').strip().upper()
    if user == '':
        continue

    tries += 1

    # word
    if len(user) > 1:
        if user == ''.join(guess_word):
            print('You win! In', tries, 'tries!')
            repeat = input('Do you want to play again Y/N?').strip().upper()
            if repeat != 'Y':
                break                   
        else:
            print('Nice try! ... but wrong...')
            print(''.join(text))
            continue               

    # single letter
    for pos in range(len(guess_word)):
        if guess_word[pos] == user:
            text[pos] = user

    print(''.join(text))
