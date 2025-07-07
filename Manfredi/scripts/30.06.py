from examjune import SequencePair,SubstitutionMatrix
class Seq(SequencePair):
    def backtracking(self, i, j):
        '''Recupera l’allineamento locale a partire dalla cella (i, j), restituendo anche lo score'''
        aligned1 = ''
        aligned2 = ''
        score = self.F[i][j]  # Salva il punteggio dell’allineamento locale
        while self.T[i][j] != '':
            if self.T[i][j] == 'd':
                aligned1 += self.seq1[j - 1]
                aligned2 += self.seq2[i - 1]
                i -= 1
                j -= 1
            elif self.T[i][j] == 'u':
                aligned1 += '-'
                aligned2 += self.seq2[i - 1]
                i -= 1
            elif self.T[i][j] == 'l':
                aligned1 += self.seq1[j - 1]
                aligned2 += '-'
                j -= 1
        return aligned1[::-1], aligned2[::-1], score

    def find_alignments(self, matrix, gap, threshold):
        '''Cerca e ritorna tutti gli allineamenti con punteggio ≥ threshold'''
        self._create_local_matrices(matrix, gap)
        alignments = []

        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                if self.F[i][j] >= threshold:
                    a1, a2, score = self.backtracking(i, j)
                    alignments.append((a1, a2, score))

        return alignments

if __name__ == "__main__":
    matrix = SubstitutionMatrix("PAM250.txt")
    myobj = Seq("PAWHEAE", "HEAGAWGHEE")
    alignments = myobj.find_alignments(matrix, gap=-4, threshold=5)

    for a1, a2, score in alignments:
        print("Score:", score)
        print(a1)
        print(a2)
        print()
