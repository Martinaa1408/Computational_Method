
from A_exam_text import SubstitutionMatrix, SequencePair

class MySequencePair(SequencePair):
    
    def __init__(self,seq1,seq2,matrix,gap):
        super().__init__(seq1,seq2,matrix,gap)
        
    def _create_matrices(self):
        '''Smith-Waterman local alignment: compute F and T matrices'''
        for i in range(len(self.seq2) + 1):
            self.F.append([0]*(len(self.seq1) + 1))  
            self.T.append(['']*(len(self.seq1) + 1)) 

        self.best_aln_score = 0
        self.best_aln_start = (0, 0)

        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                diag = self.F[i-1][j-1] + self.matrix[self.seq2[i-1], self.seq1[j-1]],'d'
                up = self.F[i-1][j] + self.gap,'u'
                left = self.F[i][j-1] + self.gap,'l'
                zero=0,''
                self.F[i][j] = max(zero, diag, up, left)

                if self.F[i][j] > self.best_aln_score:
                    self.best_aln_score = self.F[i][j]
                    self.best_aln_start = (i, j)

if __name__ == "__main__":
    matrix = SubstitutionMatrix("PAM250.txt")
    pair = MySequencePair("AAAAACCAACCAAAAA", "RRRRCCCCRRRR", matrix, -5)
    print(pair)
