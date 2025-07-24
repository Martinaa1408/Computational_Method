# smith_waterman_main.py

from A_exam_text import SubstitutionMatrix, SequencePair

# Estensione della classe SequencePair
class MySequencePair(SequencePair):
    
    def __init__(self,seq1,seq2,matrix,gap):
        super().__init__(seq1,seq2,matrix,gap)
        
    def _create_matrices(self):
        '''Smith-Waterman local alignment: compute F and T matrices'''
        n = len(self.seq2) + 1  # righe
        m = len(self.seq1) + 1  # colonne

        # Inizializza le matrici
        self.F = [[0 for _ in range(m)] for _ in range(n)]
        self.T = [["" for _ in range(m)] for _ in range(n)]

        self.best_aln_score = 0
        self.best_aln_start = (0, 0)

        for i in range(1, n):
            for j in range(1, m):
                match = self.matrix[self.seq2[i-1], self.seq1[j-1]]
                diag = self.F[i-1][j-1] + match
                up = self.F[i-1][j] + self.gap
                left = self.F[i][j-1] + self.gap
                self.F[i][j] = max(0, diag, up, left)

                # Tracciamento
                if self.F[i][j] == 0:
                    self.T[i][j] = ''
                elif self.F[i][j] == diag:
                    self.T[i][j] = 'd'
                elif self.F[i][j] == up:
                    self.T[i][j] = 'u'
                elif self.F[i][j] == left:
                    self.T[i][j] = 'l'

                # Aggiorna miglior punteggio
                if self.F[i][j] > self.best_aln_score:
                    self.best_aln_score = self.F[i][j]
                    self.best_aln_start = (i, j)


# Fix costruttori (__init__ e __getitem__) nel modulo originale se non l’hai già fatto:
# class SubstitutionMatrix:
#     def __init__(self, filename):
#         ...
#     def __getitem__(self, key):
#         ...

# class SequencePair:
#     def __init__(self, ...):
#         ...
#     def __str__(self):
#         ...

# Main per il test
if __name__ == "__main__":
    # a. Crea la matrice PAM250
    matrix = SubstitutionMatrix("PAM250.txt")

    # b. Crea oggetto SequencePair con sequenze e gap penalty
    pair = MySequencePair("AAAAACCAACCAAAAA", "RRRRCCCCRRRR", matrix, -5)

    # c. Stampa il risultato
    print(pair)
