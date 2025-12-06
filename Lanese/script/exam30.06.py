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

def load_words(fname):
    words = []
    f = open(fname, "r")
    for line in f:
        line = line.strip()
        if line != "":
            words.append(line)
    f.close()
    return words

def save_word(fname, w):
    f = open(fname, "a")
    f.write(w + "\n")
    f.close()

def is_prefix(pre, w):
    if len(pre) > len(w):
        return False
    for i in range(len(pre)):
        if pre[i] != w[i]:
            return False
    return True

def main():
    fname = argv[1]
    words = load_words(fname)
    text = []

    while True:
        p = input("word/prefix (empty=exit): ").strip()
        if p == "":
            break

        if p in words:
            text.append(p)
            print("Added:", p)
            print("Text:", " ".join(text))
            continue


        suggestions = []
        for w in words:
            if is_prefix(p, w):
                suggestions.append(w)


        if len(suggestions) > 0:
            print("Suggestions:")
            for i in range(len(suggestions)):
                print(i+1, suggestions[i])

            c = input("number / p=prefix / d=discard: ").strip().lower()

            if c == "d":
                continue
            elif c == "p":
                words.append(p)
                save_word(fname, p)
                text.append(p)
            else:
                try:
                    n = int(c)
                    chosen = suggestions[n-1]
                    text.append(chosen)
                except:
                    print("Invalid")
                    continue

   
        else:
            a = input("Add to dictionary? (y/n): ").strip().lower()
            if a == "y":
                words.append(p)
                save_word(fname, p)
                text.append(p)
            else:
                print("Discarded.")

        print("Text:", " ".join(text))

main()
