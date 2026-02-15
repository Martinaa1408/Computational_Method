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


def read_words():
    words = []
    try:
        input_file = open(filename, 'r')
    except FileNotFoundError:
        exit()

    for line in input_file:
        line = line.rstrip().upper()
        if line == '':
            continue
        words.append(line)

    input_file.close()
    return words


def build_scheme(word):
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'

    text = []
    for ch in word:
        if ch in vowels:
            text.append('+')
        elif ch in consonants:
            text.append('-')
        else:
            text.append('?')
    return text


def apply_letter(word, text, letter):
    for pos in range(len(word)):
        if word[pos] == letter:
            text[pos] = letter
    return text


def play_round(word):
    text = build_scheme(word)
    print(''.join(text))

    tries = 0
    while True:
        user = input('Insert a letter or guess the word:').strip().upper()
        if user == '':
            continue

        tries += 1

        # guess the word
        if len(user) > 1:
            if user == word:
                print('You win! In', tries, 'tries!')
                return
            else:
                print('Nice try! ... but wrong...')
                print(''.join(text))
                continue

        # single letter
        text = apply_letter(word, text, user)
        print(''.join(text))


def main():
    words = read_words()

    i = 0
    while True:
        if i >= len(words):
            i = 0

        word = words[i]
        i += 1

        play_round(word)

        repeat = input('Do you want to play again Y/N? ').strip().upper()
        if repeat != 'Y':
            break


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit()

    filename = argv[1]   # globale
    main()
