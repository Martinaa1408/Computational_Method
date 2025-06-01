#In questo codice viene implementato l'algoritmo Smith-Waterman per l'allineamento locale delle sequenze, che è una variazione dell'algoritmo di Needleman-Wunsch.
#Mentre Needleman-Wunsch esegue un allineamento globale tra due sequenze, Smith-Waterman cerca di trovare l'allineamento ottimale tra due sequenze che possono essere parzialmente allineate (cioè con un segmento allineato, senza bisogno che le sequenze siano completamente allineate).
#Per farlo, si utilizza una matrice di sostituzione e una penalizzazione per i gap.

#La classe SeqPair estende la classe SeqPair definita nel modulo Substitutionmatrix
# per aggiungere nuovi metodi necessari per l'algoritmo Smith-Waterman
from manfredi import Substitutionmatrix, matrices

class SeqPair(Substitutionmatrix.SeqPair):  # Use inheritance to extend the original class with new methods
    def __init__(self, seq1, seq2):
        ''' Questo costruttore chiama il costruttore della classe originale '''
        super().__init__(seq1, seq2)  # Inizializza le sequenze utilizzando il costruttore della classe base

    # Metodo per creare le matrici F e T utilizzate per l'algoritmo Smith-Waterman
    def _create_local_matrices(self, matrix, gap):
        # Crea le matrici F e T (F contiene i punteggi di allineamento, T contiene le direzioni di backtracking)
        F = []  # Matrice dei punteggi
        T = []  # Matrice delle direzioni

        # Inizializza le matrici con dimensioni adeguate
        for row in range(len(self.seq2) + 1):
            F.append([0] * (len(self.seq1) + 1)) # Inizializza la matrice F con 0
            T.append([''] * (len(self.seq1) + 1)) # Inizializza la matrice T con stringhe vuote

        # Riempie il resto delle matrici F e T
        for row in range(1, len(self.seq2) + 1):
            for col in range(1, len(self.seq1) + 1):
                # Calcola i valori per ogni cella (top, left, diagonal, zero)
                '''
                # Version 1 with if elif elif else
                top = F[row-1][col] + gap
                left = F[row][col-1] + gap
                diagonal = F[row-1][col-1] + matrix[self.seq1[col-1], self.seq2[row-1]]

                F[i][j] = max(top, left, diagonal, 0)

                if F[row][col] == 0: # First choice in case of parity
                    pass
                elif F[row][col] == diagonal:
                    T[row][col] = 'd'
                elif F[row][col] == top:
                    T[row][col] = 'u'
                else: #F[row][col] == left:
                    T[row][col] = 'l'
                '''

                # Version 3 with tuples
                top = F[row - 1][col] + gap, 3, 'u'  # Punteggio se il movimento è verso l'alto (up)
                left = F[row][col - 1] + gap, 2, 'l' # Punteggio se il movimento è verso sinistra (left)
                diagonal = F[row - 1][col - 1] + matrix[self.seq2[row - 1], self.seq1[col - 1]], 1, 'd' # Punteggio per il movimento diagonale (diagonal)
                zero = 0, 4, '' # Prima scelta in caso di parità (se il punteggio è 0)
                F[row][col], _, T[row][col] = max(top, left, diagonal, zero) # Calcola il massimo tra i punteggi e aggiorna F e T

        return F, T #restituisce le matrici riempite

    # Metodo che implementa l'algoritmo Smith-Waterman per l'allineamento locale
    def smith_waterman(self, matrix, gap):
        # Crea le matrici F e T utilizzando il metodo _create_local_matrices
        F, T = self._create_local_matrices(matrix, gap)
        aln1 = "" # Sequenza allineata 1
        aln2 = "" # Sequenza allineata 2

        # Trova la posizione di inizio per il backtracking (il massimo punteggio in F)
        max_score = -1
        for row in range(len(self.seq2) + 1):
            for col in range(len(self.seq1) + 1):
                if F[row][col] > max_score:
                    max_score = F[row][col] # Aggiorna il punteggio massimo
                    start_row = row # Memorizza la posizione di inizio (riga)
                    start_col = col # Memorizza la posizione di inizio (colonna)

        row = start_row # Imposta la riga di partenza per il backtracking
        col = start_col  #Imposta la colonna di partenza per il backtracking

        # Ciclo di backtracking finché non raggiungiamo una direzione vuota ('')
        while T[row][col] != '':
            if T[row][col] == 'd': # Se la direzione è diagonale ('d')
                aln1 = self.seq1[col - 1] + aln1 # Aggiungi il carattere da seq1 all'allineamento
                aln2 = self.seq2[row - 1] + aln2 # Aggiungi il carattere da seq2 all'allineamento
                row = row - 1 # Muovi verso l'alto
                col = col - 1 # Muovi verso sinistra
            elif T[row][col] == 'l': # Se la direzione è verso sinistra ('l')
                aln1 = self.seq1[col - 1] + aln1 # Aggiungi il carattere da seq1 all'allineamento
                aln2 = "-" + aln2 # Aggiungi un gap a seq2
                col = col - 1 # Muovi verso sinistra
            else:  # se la direzione è verso l'alto ('u')
                aln1 = "-" + aln1 # Aggiungi un gap a seq1
                aln2 = self.seq2[row - 1] + aln2  #Aggiungi il carattere da seq2 all'allineamento
                row = row - 1 # Muovi verso l'alto

        # Restituisce le due sequenze allineate e il punteggio massimo
        return aln1, aln2, max_score

# Codice principale
if __name__ == "__main__":
    # Crea un oggetto SeqPair con le sequenze da allineare
    myobj = SeqPair("TGA", "GA")  # Inizializza l'oggetto con le sequenze "TGA" e "GA"
    # Stampa le sequenze per verificare l'input
    #print(myobj.seq1, myobj.seq2)
    # Carica la matrice di sostituzione dal file "TTM.txt"
    submat = matrices.Substitutionmatrix("../exam manfredi/2024-02/PAM250.txt")
    # Esegui l'allineamento Smith-Waterman e ottieni le sequenze allineate e il punteggio finale
    aln1, aln2, score = myobj.smith_waterman(submat, -2)
    print(aln1)
    print(aln2)
    print("Score: ", score)

#output:
#GA
#GA
#Score:  4.0
