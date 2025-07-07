# ============================================
# SCHEMA GUIDA PER ESERCIZI CON CLASSI IN PYTHON
# (SubstitutionMatrix, SequencePair, MultiSequencePair)
# ============================================

# -----------------------------
# ✅ Estendere SubstitutionMatrix
# -----------------------------

# Esempio: override con dizionario + regole personalizzate
class SubstitutionMatrix:
    def __init__(self, filename):
        # Carica la matrice da file
        self.values = {}
        with open(filename) as f:
            chars = f.readline().split()
            for line in f:
                parts = line.strip().split()
                row_char = parts[0]
                for i in range(1, len(parts)):
                    self.values[(row_char, chars[i-1])] = int(parts[i])

# Estensione con override e logica purine/pyrimidine
class Sub(SubstitutionMatrix):
    def __init__(self, filename, override={}):
        super().__init__(filename)
        self.override = override  # esempio: {('A','G'): 3, ('C','T'): -2}

    def __getitem__(self, key):
        # Usa override se presente
        if key in self.override:
            return self.override[key]
        # Regola: +10 se entrambi purine o entrambi pirimidine
        purines = {'A', 'G'}
        pyrimidines = {'C', 'T'}
        a, b = key
        if (a in purines and b in purines) or (a in pyrimidines and b in pyrimidines):
            return 10
        if '-' in key:
            return -5  # penalità per gap
        return self.values[key]

    def gap_penalty(self, pos):
        # Penalità variabile: -2 se pos multiplo di 3, altrimenti -5
        if pos % 3 == 0:
            return -2
        return -5


# -----------------------------
# ✅ Estendere SequencePair
# -----------------------------

class SequencePair:
    def __init__(self, seq1, seq2):
        self.seq1 = seq1
        self.seq2 = seq2

    def smith_waterman(self, matrix):
        F, T = self._create_matrices(matrix)
        max_score = 0
        max_pos = (0, 0)
        for i in range(len(F)):
            for j in range(len(F[0])):
                if F[i][j] > max_score:
                    max_score = F[i][j]
                    max_pos = (i, j)

        # Backtracking per recuperare l’allineamento
        i, j = max_pos
        aln1 = ''
        aln2 = ''
        while T[i][j] != '':
            if T[i][j] == 'd':
                aln1 = self.seq1[j-1] + aln1
                aln2 = self.seq2[i-1] + aln2
                i -= 1
                j -= 1
            elif T[i][j] == 'u':
                aln1 = '-' + aln1
                aln2 = self.seq2[i-1] + aln2
                i -= 1
            elif T[i][j] == 'l':
                aln1 = self.seq1[j-1] + aln1
                aln2 = '-' + aln2
                j -= 1
        return aln1, aln2, max_score

# Estensione: reverse complement + penalità variabile
class Seq(SequencePair):
    def _create_matrices(self, matrix):
        F = []
        T = []
        for i in range(len(self.seq2) + 1):
            F.append([0] * (len(self.seq1) + 1))
            T.append([''] * (len(self.seq1) + 1))

        for i in range(1, len(self.seq2) + 1):
            for j in range(1, len(self.seq1) + 1):
                top = F[i - 1][j] + matrix.gap_penalty(i), 'u'
                left = F[i][j - 1] + matrix.gap_penalty(j), 'l'
                diag = F[i - 1][j - 1] + matrix[self.seq1[j - 1], self.seq2[i - 1]], 'd'
                zero = 0, ''
                F[i][j], T[i][j] = max([top, left, diag, zero], key=lambda x: x[0])
        return F, T

    def reverse_complement(self):
        comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        rev1 = ''
        rev2 = ''
        for c in self.seq1[::-1]:
            rev1 += comp[c]
        for c in self.seq2[::-1]:
            rev2 += comp[c]
        return SequencePair(rev1, rev2)

# -----------------------------
# ✅ MultiSequencePair – Allineamento migliore tra più sequenze
# -----------------------------

from itertools import combinations

class MultiSequencePair:
    def __init__(self, filename):
        self.sequences = []
        with open(filename) as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if lines[i].startswith(">"):
                    self.sequences.append(lines[i+1].strip())
        if len(self.sequences) < 3:
            raise ValueError("Il file deve contenere almeno 3 sequenze")

    def best_alignment(self, matrix):
        best_score = -1
        best_pair = None
        best_alignment = None
        for s1, s2 in combinations(self.sequences, 2):
            pair = SequencePair(s1, s2)
            a1, a2, score = pair.smith_waterman(matrix)
            if score > best_score:
                best_score = score
                best_pair = (s1, s2)
                best_alignment = (a1, a2)
        return best_pair, best_alignment, best_score

# ===============================
# ✅ TIPI DI ESTENSIONE (schema mentale)
# ===============================

# - "Modifica valori della matrice" → sovrascrivi __getitem__
# - "Penalità variabili per posizione" → aggiungi gap_penalty(pos)
# - "Reverse complement" → metodo che trasforma e restituisce nuova SequencePair
# - "Input da fasta" → leggi le sequenze riga dopo riga e salvale in una lista
# - "Coppia migliore" → usa itertools.combinations + score massimo
# - "Smith-Waterman personalizzato" → riscrivi _create_matrices()

# ===============================
# ✅ Pronto per: esercizi Lanese, Manfredi, project exam
# ===============================
