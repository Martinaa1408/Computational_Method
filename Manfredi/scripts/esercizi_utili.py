#Read carefully the module 'exercise.py' and write a new script
#to implement the following requirements:

#1. Import the module.

#2. Extend the class SubstitutionMatrix to accept a second argument
   #to the constructor: a dictionary of overrides in the form:
   #{('A', 'G'): 3, ('C', 'T'): -2}, which updates the internal matrix.


#3. Override the _getitem_ method so that:
   #a. It returns +10 if both characters are purines (A/G) or both are pyrimidines (C/T).
   #b. Else, return the matrix value (including overrides if provided).


#4. Extend the class SequencePair to add a method 'reverse_complement'
   #that returns a new SequencePair object where both sequences
   #have been replaced by their reverse complements.



#5. In the main:
   #a. Create a SubstitutionMatrix from PAM250 and override a few values,
   #b. Read two sequences from 'input.fasta',
   #c. Create their reverse complements,
   #d. Run Smith-Waterman and print the alignment.
#'''

from exercise import SubstitutionMatrix,SequencePair
class Sub(SubstitutionMatrix):
    def __init__(self,filename):
        super().__init__(filename)

    def __getitem__(self,key):
        key1,key2=key
        purines = {'A', 'G'}
        pyrimidines = {'C', 'T'}
        if (key1 in purines and key2 in purines) or (key1 in pyrimidines and key2 in pyrimidines):
            return 10
        if '-' in key:
            return -5
        else:
            return self.values[key]

class Seq(SequencePair):
    def __init__(self, filename):
        with open(filename, 'r') as sequences:
            sequences.readline()
            self.seq1 = sequences.readline().strip()
            sequences.readline()
            self.seq2 = sequences.readline().strip()

    def reverse_complement(self):
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        self.seq1 = self.seq1[::-1]
        self.seq2 = self.seq2[::-1]
        rv1 = ''
        rv2 = ''
        for a, b in zip(self.seq1, self.seq2):
            rv1 += comp[a]
            rv2 += comp[b]
        self.seq1 = rv1
        self.seq2 = rv2
        return SequencePair(self.seq1, self.seq2)

    def _create_matrices(self, matrix):
        F, T = [], []
        for i in range(len(self.seq2) + 1):
            F.append([])
            T.append([])
            for j in range(len(self.seq1) + 1):
                F[i].append(0)
                T[i].append('')

        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                top = F[i - 1][j] + matrix[self.seq2[i - 1], '-'], 'u'
                left = F[i][j - 1] + matrix['-', self.seq1[j - 1]], 'l'
                diag = F[i - 1][j - 1] + matrix[self.seq2[i - 1], self.seq1[j - 1]], 'd'
                zero = 0, ''
                F[i][j], T[i][j] = max(top, left, diag, zero)
        return F, T

if __name__ == "__main__":
    matrix = Sub('PAM250.txt')
    myobj = Seq('input.fasta')
    myobj_r = myobj.reverse_complement()
    print(myobj.smith_waterman(matrix))

#-------------------------------------------------------------------------------------------------------------------------
#''
#Using the provided module 'exam2025.py', write a script that:

#1. Extends SubstitutionMatrix:
   #a. Add a method 'gap_penalty(pos)' that returns -2 if the position is divisible by 3,
      #else returns -5.

#2. Extends SequencePair:
   #a. Override the method _create_matrices so that the gap penalty at each cell (i,j)
      #is computed using matrix.gap_penalty(j) for horizontal gaps and matrix.gap_penalty(i) for vertical gaps.

#3. In the main:
   #a. Use 'PAM250.txt' and 'input.fasta',
   #b. Run Smith-Waterman,
   #c. Print the alignment and final score.
#'''
from exercise import SubstitutionMatrix,SequencePair


class Sub(SubstitutionMatrix):
    def __init__(self,filename):
        super().__init__(filename)

    def gap_penalty(self,pos):
        if pos%3==0:
            return -2
        else:
            return -5
class Seq(SequencePair):
    def __init__(self, filename):
        with open(filename, 'r') as sequences:
            sequences.readline()
            self.seq1 = sequences.readline().strip()
            sequences.readline()
            self.seq2 = sequences.readline().strip()

    def _create_matrices(self, matrix):
        # crea la matrice
        F = []
        T = []
        # prima riga e prima colonna
        for i in range(len(self.seq2) + 1):
            F.append([0] * (len(self.seq1) + 1))
            T.append((['']) * (len(self.seq1) + 1))
        # restante parte della matrice
        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                top = F[i - 1][j] + matrix.gap_penalty(i), 'u'
                left = F[i][j - 1] + matrix.gap_penalty(j), 'l'
                diagonal = F[i - 1][j - 1] + matrix[self.seq1[j-1],self.seq2[i-1]], 'd'
                zero = 0, ''
                F[i][j], T[i][j] = max(top, left, diagonal, zero)
        return (F, T)


if __name__ == "__main__":
    myobj = Seq("input.fasta")
    matrix = Sub("PAM250.txt")
    print(myobj.smith_waterman(matrix))

#---------------------------------------------------------------------------------------------------------------------
#'''
#Write a script that:

#1. Defines a class MultiSequencePair, extending SequencePair.

#2. In the constructor:
   #a. Accept a fasta file with more than two sequences (minimum 3),
   #b. Store all sequences in a list.

#3. Implement a method 'best_alignment(matrix)' that:
   #a. Computes all pairwise Smith-Waterman alignments,
   #b. Returns the pair of sequences with the highest alignment score and the alignment itself.

#4. In the main:
   #a. Use 'input.fasta' (which now contains at least 3 sequences),
   #b. Use PAM250 for scoring,
   #c. Print the best aligned pair and the score.
#'''
from exercise import SequencePair,SubstitutionMatrix:
from itertools import combinations


class Sub(SubstitutionMatrix):
    def __init__(self, filename):
        super().__init__(filename)

    def __getitem__(self, key):
        if '-' in key:
            return -5
        else:
            return self.values[key]


class Seq(SequencePair):
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def _create_matrices(self, matrix):
        F, T = [], []
        for i in range(len(self.seq2) + 1):
            F.append([0] * (len(self.seq1) + 1))
            T.append([''] * (len(self.seq1) + 1))

        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                top = F[i - 1][j] + matrix[self.seq2[i - 1], '-'], 'u'
                left = F[i][j - 1] + matrix['-', self.seq1[j - 1]], 'l'
                diag = F[i - 1][j - 1] + matrix[self.seq2[i - 1], self.seq1[j - 1]], 'd'
                zero = 0, ''
                F[i][j], T[i][j] = max([top, left, diag, zero], key=lambda x: x[0])
        return F, T


class MultiSequencePair:
    def __init__(self, filename):
        self.sequences = []
        with open(filename) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith(">"):
                    self.sequences.append(lines[i+1].strip())

        if len(self.sequences) < 3:
            raise ValueError("The file must contain at least 3 sequences.")

    def best_alignment(self, matrix):
        best_score = -1
        best_pair = None
        best_alignment = None

        for s1, s2 in combinations(self.sequences, 2):
            pair = SequencePair(s1, s2)
            aln1, aln2, score = pair.smith_waterman(matrix)
            if score > best_score:
                best_score = score
                best_pair = (s1, s2)
                best_alignment = (aln1, aln2)

        return best_pair, best_alignment, best_score


if __name__ == "__main__":
    matrix = SubstitutionMatrix('PAM250.txt')
    multi = MultiSequencePair('input.fasta')
    seqs, alignment, score = multi.best_alignment(matrix)

    print("Best sequence pair:")
    print("Seq1:", seqs[0])
    print("Seq2:", seqs[1])
    print("Best alignment:")
    print("Aln1:", alignment[0])
    print("Aln2:", alignment[1])
    print("Score:", score)

#----------------------------------------------------------------------------------------------------------------




