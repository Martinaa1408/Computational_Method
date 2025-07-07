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
from sys import argv

# Carica le parole esistenti dal file
def load_words(fname):
    words = []
    try:
        f = open(fname, 'r')
        for line in f:
            line = line.strip()
            if line != '':
                words.append(line)
        f.close()
    except:
        print("Errore nel caricamento.")
        exit(1)
    return words

# Aggiungi una parola nuova al file
def append_word(fname, word):
    try:
        f = open(fname, 'a')
        f.write(word + '\n')
        f.close()
    except:
        print("Errore nel salvataggio.")

# Controlla se una parola inizia con un prefisso
def is_prefix(pre, word):
    if len(pre) > len(word):
        return False
    i = 0
    while i < len(pre):
        if pre[i] != word[i]:
            return False
        i = i + 1
    return True

# Loop principale
def autocomplete(words, fname):
    text = []
    while True:
        print("Enter word or prefix (empty to exit):", end=' ')
        pre = input().strip().lower()
        if pre == "":
            break

        found = False
        i = 0
        while i < len(words):
            if words[i] == pre:
                found = True
            i = i + 1

        if found:
            print("Added:", pre)
            text.append(pre)
        else:
            suggestions = []
            i = 0
            while i < len(words):
                if is_prefix(pre, words[i]):
                    suggestions.append(words[i])
                i = i + 1

            if len(suggestions) > 0:
                print("Suggestions:")
                i = 0
                while i < len(suggestions):
                    print(str(i+1) + ". " + suggestions[i])
                    i = i + 1
                print("Choose number, 'p'=propose, 'd'=discard:", end=' ')
                choice = input().strip().lower()
                if choice == 'd':
                    continue
                elif choice == 'p':
                    if pre not in words:
                        words.append(pre)
                        append_word(fname, pre)
                    text.append(pre)
                else:
                    is_num = True
                    i = 0
                    while i < len(choice):
                        if choice[i] < '0' or choice[i] > '9':
                            is_num = False
                        i = i + 1
                    if is_num:
                        num = int(choice)
                        if num >= 1 and num <= len(suggestions):
                            word = suggestions[num - 1]
                            print("Added:", word)
                            text.append(word)
                        else:
                            print("Invalid number.")
                    else:
                        print("Invalid input.")
            else:
                print("No match. Add '" + pre + "'? (y/n):", end=' ')
                yn = input().strip().lower()
                if yn == 'y':
                    words.append(pre)
                    append_word(fname, pre)
                    text.append(pre)
                else:
                    print("Discarded.")
        print("Current text:", ' '.join(text))

# Entry point
def main():
    if len(argv) != 2:
        print("Uso: python autocomplete.py words.txt")
        exit(1)
    fname = argv[1]
    words = load_words(fname)
    autocomplete(words, fname)

main()
