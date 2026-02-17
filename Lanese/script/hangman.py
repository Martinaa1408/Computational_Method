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

def read_and_transform(filename):

    try:
        with open(filename) as reader:
            for line in reader:
                word = line.strip().upper()
                if word != "":

                    vowels = "AEIOU"
                    mask = ""

                    for ch in word:
                        if ch in vowels:
                            mask += "+"
                        else:
                            mask += "-"

                    return word, mask

    except FileNotFoundError:
        exit()

def main():

    word, mask = read_and_transform(filename)

    tries = 0
    print(mask)

    while True:

        tentative = input("Insert a letter or guess the word: ").strip().upper()

        if tentative == "":
            continue

        tries += 1

        # prova parola intera
        if len(tentative) > 1:

            if tentative == word:
                print("You win! In", tries, "tries!")
                break
            else:
                print("Nice try! ... but wrong...")
                print(mask)
                continue

        # lettera singola
        letter = tentative
        new_mask = ""

        for i in range(len(word)):
            if word[i] == letter:
                new_mask += letter
            else:
                new_mask += mask[i]

        mask = new_mask
        print(mask)

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        exit()

    filename = argv[1]
    main()



