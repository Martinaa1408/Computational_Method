from exam_sept import SequencePair

class ExtendedSequencePair(SequencePair):
    
    def _backtracking(self, start_i, start_j):
        aligned_seq1 = ""
        aligned_seq2 = ""
        i, j = start_i, start_j
        
        while i > 0 or j > 0:
            if self.T[i][j] == '\\':
                aligned_seq1 = self.seq1[j-1] + aligned_seq1
                aligned_seq2 = self.seq2[i-1] + aligned_seq2
                i -= 1
                j -= 1
            elif self.T[i][j] == '|':
                aligned_seq1 = '-' + aligned_seq1
                aligned_seq2 = self.seq2[i-1] + aligned_seq2
                i -= 1
            elif self.T[i][j] == '-':
                aligned_seq1 = self.seq1[j-1] + aligned_seq1
                aligned_seq2 = '-' + aligned_seq2
                j -= 1
            else:
                break
                
        return aligned_seq1, aligned_seq2
    
    def align(self, sub_matrix_file, gap, algorithm):
        self._create_matrices(sub_matrix_file, gap, algorithm)
        
        if algorithm == "nw":
            i, j = len(self.seq2), len(self.seq1)
            score = self.F[i][j]
        else:
            max_score = 0
            max_i, max_j = 0, 0
            for i in range(len(self.F)):
                for j in range(len(self.F[0])):
                    if self.F[i][j] > max_score:
                        max_score = self.F[i][j]
                        max_i, max_j = i, j
            i, j = max_i, max_j
            score = max_score
        
        aligned_seq1, aligned_seq2 = self._backtracking(i, j)
        
        return aligned_seq1, aligned_seq2, score

if __name__ == "__main__":
    seq1 = "AAAAACCAACCAAAAA"
    seq2 = "RRRRCCCCRRRR"
    gap_penalty = -5
    matrix_file = "PAM250.txt"
    
    esp = ExtendedSequencePair(seq1, seq2)
    
    print("=== Needleman-Wunsch Algorithm ===")
    aligned1_nw, aligned2_nw, score_nw = esp.align(matrix_file, gap_penalty, "nw")
    print("Aligned Sequence 1:", aligned1_nw)
    print("Aligned Sequence 2:", aligned2_nw)
    print("Alignment Score:", score_nw)
    print()
    
    print("=== Smith-Waterman Algorithm ===")
    aligned1_sw, aligned2_sw, score_sw = esp.align(matrix_file, gap_penalty, "sw")
    print("Aligned Sequence 1:", aligned1_sw)
    print("Aligned Sequence 2:", aligned2_sw)
    print("Alignment Score:", score_sw)
    print()
    
    print("Scoring Matrix (F) for Needleman-Wunsch:")
    esp._print_matrices()
