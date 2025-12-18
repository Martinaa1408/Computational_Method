import os

class SubstitutionMatrix:
    def __init__(self, filename):
        """Read PAM/BLOSUM matrix from a file and store it in a dictionary."""
        self.values = {}
        if not os.path.exists(filename):
            print(f"Error: {filename} not found.")
            return
        with open(filename, 'r') as f:
            header = f.readline().split()
            for line in f:
                parts = line.split()
                if not parts: continue
                row_char = parts[0]
                for col_char, val in zip(header, parts[1:]):
                    self.values[(row_char, col_char)] = int(val)

    def __getitem__(self, key):
        """Allows access via matrix['A', 'G']. Handles gaps with a fixed penalty if requested."""
        char1, char2 = key
        # Custom logic from Feb 25th task: handle gaps explicitly
        if char1 == '-' or char2 == '-':
            return -5 
        return self.values.get((char1, char2), -5)

class AlignmentTool:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.F = None  # Score Matrix
        self.T = None  # Traceback Matrix

    def compute_matrices(self, matrix, gap, mode="global"):
        """
        Integrated Matrix Computation:
        'global' -> Needleman-Wunsch
        'local'  -> Smith-Waterman
        """
        n, m = len(self.seq2) + 1, len(self.seq1) + 1
        self.F = [[0] * m for _ in range(n)]
        self.T = [[""] * m for _ in range(n)]

        # 1. Initialization
        if mode == "global":
            for i in range(1, n):
                self.F[i][0] = self.F[i-1][0] + gap
                self.T[i][0] = "u"  # up
            for j in range(1, m):
                self.F[0][j] = self.F[0][j-1] + gap
                self.T[0][j] = "l"  # left

        # 2. Filling the Matrix
        for i in range(1, n):
            for j in range(1, m):
                match_score = matrix[self.seq2[i-1], self.seq1[j-1]]
                diag = self.F[i-1][j-1] + match_score
                up = self.F[i-1][j] + gap
                left = self.F[i][j-1] + gap

                if mode == "global":
                    score = max(diag, up, left)
                    self.F[i][j] = score
                    if score == diag: self.T[i][j] = "d"
                    elif score == up: self.T[i][j] = "u"
                    else: self.T[i][j] = "l"
                else:  # Local Alignment
                    score = max(0, diag, up, left)
                    self.F[i][j] = score
                    if score == 0: self.T[i][j] = ""
                    elif score == diag: self.T[i][j] = "d"
                    elif score == up: self.T[i][j] = "u"
                    else: self.T[i][j] = "l"

    def traceback(self, start_i, start_j):
        """Recover the alignment starting from a specific cell."""
        aln1, aln2 = "", ""
        i, j = start_i, start_j
        while i > 0 or j > 0:
            if self.T[i][j] == "d":
                aln1 = self.seq1[j-1] + aln1
                aln2 = self.seq2[i-1] + aln2
                i -= 1; j -= 1
            elif self.T[i][j] == "u":
                aln1 = "-" + aln1
                aln2 = self.seq2[i-1] + aln2
                i -= 1
            elif self.T[i][j] == "l":
                aln1 = self.seq1[j-1] + aln1
                aln2 = "-" + aln2
                j -= 1
            else: # Local alignment '0' cell or start
                break
        return aln1, aln2, self.F[start_i][start_j]

    def find_all_local(self, matrix, gap, threshold):
        """Task from June 30th: Find all local alignments above a threshold."""
        self.compute_matrices(matrix, gap, mode="local")
        results = []
        for i in range(len(self.seq2) + 1):
            for j in range(len(self.seq1) + 1):
                if self.F[i][j] >= threshold:
                    results.append(self.traceback(i, j))
        return results

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # 1. Setup Data
    sub_matrix = SubstitutionMatrix("PAM250.txt")
    s1, s2 = "PAWHEAE", "HEAGAWGHEE"
    gap_penalty = -4
    
    tool = AlignmentTool(s1, s2)

    # 2. Global Alignment (Needleman-Wunsch)
    print("--- GLOBAL ALIGNMENT ---")
    tool.compute_matrices(sub_matrix, gap_penalty, mode="global")
    res_g = tool.traceback(len(s2), len(s1))
    print(f"Seq1: {res_g[0]}\nSeq2: {res_g[1]}\nScore: {res_g[2]}\n")

    # 3. Best Local Alignment (Smith-Waterman)
    print("--- BEST LOCAL ALIGNMENT ---")
    tool.compute_matrices(sub_matrix, gap_penalty, mode="local")
    # Find max score position
    max_score = -1
    pos = (0, 0)
    for i in range(len(s2)+1):
        for j in range(len(s1)+1):
            if tool.F[i][j] > max_score:
                max_score = tool.F[i][j]
                pos = (i, j)
    res_l = tool.traceback(pos[0], pos[1])
    print(f"Seq1: {res_l[0]}\nSeq2: {res_l[1]}\nScore: {res_l[2]}\n")
