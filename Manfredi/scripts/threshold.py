#Write a script where you:
#1.	Import the module exam_test.py (the file will be provided during the exam)
#2.	Extend the definition of the class SeqPair defining a new method
#a.	Name: smith_waterman
#b.	Parameters: a matrix (type SubstitutionMatrix), a gap score (type int) and a threshold (type int)
#c.	Output: a list of objects, each of type AlnSeq. Each object in the list represents a possible local alignment. The list should contain all the alignments found by the Smith and Waterman algorithm with a score equal to or greater than the threshold parameter.
#3.	Write a test main that reads a threshold parameter from the command line and adopts the defined classes to print to the terminal all the local alignments of two sequences.
#a.	First sequence: "IFYNAVWSA"
#b.	Second sequence: "IFYNAVWSAWWWVYYHAIWPG"
#c.	Substitution matrix: PAM250 (a file that can be read by the class SubstitutionMatrix will be provided during the exam)
#d.	Gap penalty: 5
from sys import argv
from input import SeqPair, SubstitutionMatrix, AlnSeq

class SubstitutionMatrix(SubstitutionMatrix):
    def __init__(self, filename):
        with open(filename) as reader:
            characters = reader.readline().strip().split()
            self.values = {}
            for line in reader:
                line = line.strip().split()
                self.values[line[0]] = {}
                for char in range(1, len(line)):
                    self.values[line[0]][characters[char - 1]] = float(line[char])

    def __getitem__(self, key):
        key1, key2 = key
        return self.values[key1][key2]


class AlnSeq(AlnSeq):
    def __init__(self, s1, s2, score):
        super().__init__(s1, s2, score)

    def __str__(self):
        return self.s1 + '\n' + self.s2 + '\n' + 'Score: ' + str(self.score)


class Seq(SeqPair):
    def __init__(self, s1, s2, threshold):
        super().__init__(s1, s2)
        self.threshold = threshold

    def smith_waterman(self, matrix, gap):
        F, T = self._local_matrices(matrix, gap)
        alignments = []
        start_row,start_col=0,0
        for row in range(1, len(self.s1) + 1):
            for col in range(1, len(self.s2) + 1):
                if F[row][col] >= self.threshold:
                    start_row, start_col = row, col
                    aln1, aln2 = "", ""
                    score = F[row][col]
                    while T[start_row][start_col] != "":
                        if T[start_row][start_col] == '\\':
                            aln1 += self.s1[start_row - 1]
                            aln2 += self.s2[start_col - 1]
                            start_row -= 1
                            start_col -= 1
                        elif T[start_row][start_col] == '-':  # left
                            aln1 += '-'
                            aln2 += self.s2[start_col - 1]
                            start_col -= 1
                        else:
                            aln1 += self.s1[start_row - 1]
                            aln2 += '-'
                            start_row -= 1
                            alignments.append(AlnSeq(aln1[::-1], aln2[::-1], score))
        return alignments


if __name__ == '__main__':
    my_obj = Seq("IFYNAVWSA", "IFYNAVWSAWWWVYYHAIWPG", int(argv[1]))
    submat = SubstitutionMatrix('PAM250.txt')
    alignments = my_obj.smith_waterman(submat, -5)
    for aln in alignments:
        print(aln)
