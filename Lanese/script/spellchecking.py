'''Write a python program to do spellchecking. It has two input files, text.txt and dict.txt, and
one output file, output.txt. File dict.txt contains a word per line, and represents the correct
words. File text.txt represents a text, written for simplicity with a word per line as well. File
output.txt is obtained from text.txt as follows. For each word, if the word is correct, it is
copied to output.txt. If it is not, the program asks to the user whether the word should be
considered correct. If so, it is written on output.txt, and from now on it becomes a correct
word. If not, it asks the correct version to the user, and the check for correctness restarts.'''

from sys import argv

dict_file = open(argv[2], 'r')
correct_words = []
for line in dict_file:
    w = line.strip()
    if w != '':
        correct_words.append(w)
dict_file.close()


text_file = open(argv[1], 'r')
output = open(argv[3], 'w')

for line in text_file:
    word = line.strip()
    if word == '':
        continue

   
    while True:
        if word in correct_words:
            output.write(word + '\n')
            break
        else:
            ans = input(f'Is "{word}" correct? (y/n): ').strip().lower()

            if ans == 'y':
                correct_words.append(word)
                output.write(word + '\n')
                break
            else:
                word = input('Insert correct word: ').strip()
           

text_file.close()
output.close()

dict_file = open(argv[2], 'w')
for w in correct_words:
    dict_file.write(w + '\n')
dict_file.close()
