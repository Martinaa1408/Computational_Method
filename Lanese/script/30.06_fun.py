"""
Exercise module Lanese

Write a Python program that helps users writing text. In particular,
when the user inserts a (prefix of a) word, it is searched in a given
data structure. If it exists, it is directly added to the text. If it is
the prefix of one or more existing words, the user can choose which
one to insert, or select the proposed word, or discard it and propose
a new one. If it is not a prefix of a given word, then it can choose
whether to select it or discard it. Whenever a word not in the data
structure is selected, it is also added to the data structure. The
program terminates when an empty word is inserted. The list of words
is taken from a file whose name is taken as command line
parameter. Assume the file contains one word per line, and that they
are all lowercase. When the program terminates, the file needs to be
updated.

Example usage:

$ python autocomplete.py words.txt
(Assuming words.txt contains: programming, program, programmer, python, project, simple)

Enter word or prefix (empty to exit): py
Suggestions:
1. python
Choose a suggestion (number), or 'p' for the proposed word, 'd' to discard: 1
Added: python
Current Text: python

Enter word or prefix (empty to exit): prog
Suggestions:
1. programming
2. program
3. programmer
Choose a suggestion (number), or 'p' for the proposed word, 'd' to discard: p
Added: prog
Current Text: python prog
"""

def read_file(filename):
    line = []
    try:
        with open(filename) as reader:
            r = reader.readline()
            while r != '':
                w = r.strip()
                if w != '':
                    line.append(w)
                r = reader.readline()
    except FileNotFoundError:
        print('warning')
        exit()
    return line


def main():
    text = ''

    while True:
        word = input('enter a word or prefix (empty to exit):').strip().lower()

        if word == '':
            break

        suggestions = []

        # Caso 1: parola esatta
        if word in line:
            text += word + ' '
            print('Added:', word)
            print('Current Text:', text.strip())
            continue

        # Caso 2: prefisso
        for l in line:
            if l.startswith(word):   # <-- QUI era l’errore nel tuo
                suggestions.append(l)

        if len(suggestions) > 0:
            print('Suggestions:')
            for i in range(len(suggestions)):
                print(str(i+1), suggestions[i])

            choice = input("Choose number, 'p' proposed, 'd' discard: ").strip().lower()

            if choice == 'd':
                continue

            elif choice == 'p':
                text += word + ' '
                print('Added:', word)
                if word not in line:
                    line.append(word)
                print('Current Text:', text.strip())

            else:
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(suggestions):
                        chosen = suggestions[index]
                        text += chosen + ' '
                        print('Added:', chosen)
                        print('Current Text:', text.strip())

        # Caso 3: nessun prefisso
        else:
            choice = input('Not found. Add to text? (y/n): ').strip().lower()
            if choice == 'y':
                text += word + ' '
                print('Added:', word)
                if word not in line:
                    line.append(word)
                print('Current Text:', text.strip())


def write_file(line, filename):
    try:
        with open(filename, 'w') as writer:
            for l in line:
                writer.write(l + '\n')
    except FileNotFoundError:
        exit()


if __name__ == '__main__':
    from sys import argv
    if len(argv) != 2:
        exit()

    line = read_file(argv[1])
    main()
    write_file(line, argv[1])



