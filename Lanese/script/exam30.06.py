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

def main():
    input_file = open(argv[1], 'r')
    words = []

    for line in input_file:
        parts = line.strip().lower().split(',')   
        for p in parts:
            p = p.strip()                         # " program" -> "program"
            if p != '':
                words.append(p)

    input_file.close()

    print(words)

    current_txt = []
    while True:
        user = input('Enter word or prefix (empty to exit): ').strip().lower()
        if user == '':
            print('Goodbye')
            break

        if user in words:
            current_txt.append(user)
            print('Added:', user)
        else:
            suggestions=[]
            for w in words:
                if w[:len(user)]==user:
                    suggestions.append(w)
                    print(suggestions)
            if len(suggestions)>0:
                print('Suggestions:')
                for i in range(len(suggestions)):
                    print(str(i+1),suggestions[i])
                choice=input('Choose (number), p (proposed), d (discard): ').strip().lower()
                if choice=='d':
                    print('discarded')
                    continue
                elif choice=='p':
                    current_txt.append(user)
                    print('added',user)
                    if user not in words:
                        words.append(user)
                else:
                    index=int(choice)-1
                    chosen=suggestions[index]
                    current_txt.append(chosen)
                    print('added',chosen)
            else:
                choice=input('not found. added to a text (y/n)?').strip().lower()
                if choice=='y':
                    current_txt.append(user)
                    print('added',user)
                    if user not in words:
                        words.append(user)
    output_file = open(argv[1], 'w')
    for w in words:
        output_file.write(w + "\n")
    output_file.close()

    print("Current Text:", " ".join(current_txt))
main()
#THREE CASE: words that is equal to the words in the file; prefix of this words, and nothing ''


