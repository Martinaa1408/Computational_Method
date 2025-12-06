from exammm import SubstitutionMatrix
from exammm import SequencePair
from exammm import AlignedSequences  

class Seq(SequencePair):
    def __init__(self, seq1, seq2):
        super().__init__(seq1, seq2)

    def alignment(self, matrix, gap, algorithm): 
        F, T = self._create_matrices(matrix, gap, algorithm)

        if algorithm == "nw":
            aln1 = ""
            aln2 = ""
            i = len(self.seq1)
            j = len(self.seq2)

            while i != 0 or j != 0:
                if T[i][j] == 'd':
                    aln1 = self.seq1[i - 1] + aln1
                    aln2 = self.seq2[j - 1] + aln2
                    i -= 1
                    j -= 1
                elif T[i][j] == 'l':
                    aln1 = self.seq1[j - 1] + aln1
                    aln2 = "-" + aln2
                    j -= 1
                else:  # T[i][j] == 'u'
                    aln1 = "-" + aln1
                    aln2 = self.seq2[i - 1] + aln2
                    i -= 1

            return AlignedSequences(aln1[::-1], aln2[::-1], F[-1][-1])

        elif algorithm == "sw":
            max_score = -1
            start_row, start_col = 0, 0 
            for i in range(len(self.seq1) + 1):
                for j in range(len(self.seq2) + 1):
                    if F[i][j] > max_score:
                        max_score = F[i][j]
                        start_row, start_col = i, j

            i, j = start_row, start_col 
            aln1 = ""
            aln2 = ""

            while T[i][j] != '':
                if T[i][j] == 'd':
                    aln1 = self.seq1[i - 1] + aln1
                    aln2 = self.seq2[j - 1] + aln2
                    i -= 1
                    j -= 1
                elif T[i][j] == 'l':
                    aln1 = '-' + aln1
                    aln2 = self.seq2[j-1] + aln2
                    j -= 1
                else:  # 'u'
                    aln1 = self.seq1[i-1] + aln1
                    aln2 = '-' + aln2
                    i -= 1

            return AlignedSequences(aln1[::-1], aln2[::-1], max_score)

if __name__ == '__main__':
    submat = SubstitutionMatrix("PAM250.txt")
    myobj = Seq("AAAAACCCC", "RRRRCCCC")

    result_nw = myobj.alignment(submat, -5, "nw")
    print("Global Alignment (Needleman-Wunsch):")
    print(result_nw)

    result_sw = myobj.alignment(submat, -5, "sw")
    print("Local Alignment (Smith-Waterman):")
    print(result_sw)

