import exercise as input

class SubstitutionMatrix(input.SubstitutionMatrix):
    def __init__(self, filename):
        super().__init__(filename)

    def __getitem__(self, key):
        if '-' in key:
            return -5
        else:
            return self.values[key]


class SequencePair(input.SequencePair):
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
                top = F[i - 1][j] + matrix[self.seq1[j - 1], '-'], 'u'
                left = F[i][j - 1] + matrix['-', self.seq2[i - 1]], 'l'
                diagonal = F[i - 1][j - 1] + matrix[self.seq1[j - 1], self.seq2[i - 1]], 'd'
                zero = 0, ''
                F[i][j], T[i][j] = max(top, left, diagonal, zero)
        return (F, T)


if __name__ == "__main__":
    myobj = SequencePair("input.fasta")
    # print("la sequenza 1 da allineare è:", myobj.seq1, "||| con la sequenza 2 che è:", myobj.seq2)
    matrix = SubstitutionMatrix("PAM250.txt")
    print(myobj.smith_waterman(matrix))
