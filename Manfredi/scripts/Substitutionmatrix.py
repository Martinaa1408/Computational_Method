#Needleman-Wunsch Algorithm (Global Alignment)
#submat è un oggetto della classe SubstitutionMatrix, che contiene la matrice di sostituzione letta da un file esterno (come TTM.txt).
#Viene usato nell'algoritmo di Needleman-Wunsch per calcolare i punteggi di allineamento tra le due sequenze, utilizzando i valori della matrice di sostituzione per determinare la "corrispondenza" tra i nucleotidi o amminoacidi.

from matrices import Substitutionmatrix
class SeqPair:
    def __init__(self, seq1, seq2):
        '''
                Il costruttore della classe. Riceve due sequenze (seq1, seq2) come input
                e le memorizza come attributi dell'oggetto.
        '''
        self.seq1 = seq1
        self.seq2 = seq2

    def _create_matrices(self, matrix, gap):
        '''
                Crea le matrici F e T:
                - F: matrice dei punteggi di allineamento
                - T: matrice che memorizza le direzioni del backtracking ('u' = up, 'l' = left, 'd' = diagonal)

                matrix: la matrice di sostituzione
                gap: penalizzazione per l'inserimento di un gap
        '''
        # Crea matrici vuote F e T (F contiene i punteggi, T le direzioni)
        F = []  # matrix that contains all the values at the end of the execution
        T = []  # only store the traceback

        # Inizializza le matrici con dimensioni adeguate (len(seq2)+1, len(seq1)+1)
        for row in range(len(self.seq2) + 1):  #+1 gap
            F.append([])
            T.append([])  # Aggiungi una nuova riga a T (necessario)
            for col in range(len(self.seq1) + 1):
                F[row].append(0)  # Corrected index assignment # Inizializza F con 0
                T[row].append('') # Inizializza T con stringhe vuote

        # Inizializzazione della prima riga (per i gap orizzontali)
        for col in range(1,len(self.seq1) + 1):
            F[0][col]=gap*col  # Punteggio basato sul gap
            T[0][col]="l"  # Direzione 'l' per left

        # Inizializzazione della prima colonna (per i gap verticali)
        for row in range(1,len(self.seq2) + 1):
            F[row][0]=F[row-1][0] + gap  # Punteggio basato sul gap
            T[row][0]="u" # Direzione 'u' per up

        # Riempie il resto delle matrici F e T
        for row in range(1, len(self.seq2) + 1):
            for col in range(1, len(self.seq1) + 1):
                '''
                    Calcola i valori nelle matrici F e T per ogni cella
                    Versione 3 con Tuples:
                    Usa una tupla per associare i punteggi e la direzione:
                    - Il punteggio per il movimento verticale (up, 'u')
                    - Il punteggio per il movimento orizzontale (left, 'l')
                    - Il punteggio per il movimento diagonale (diagonal, 'd')
                '''

                top=F[row-1][col]+ gap, 3, 'u'  # Punteggio e direzione 'u'
                left=F[row][col-1] + gap, 2, 'l'  # Punteggio e direzione 'l'
                diagonal=F[row-1][col-1] + matrix[self.seq2[row-1], self.seq1[col-1]], 1, 'd'  # Punteggio e direzione 'd'

                # Prende il massimo tra i punteggi e assegna il valore e la direzione corretti
                F[row][col], _, T[row][col] = max(top, left, diagonal)

        return F, T

    def needleman_wunsch(self, matrix, gap):
        '''
                Esegue l'algoritmo Needleman-Wunsch per l'allineamento globale delle due sequenze.
                matrix: la matrice di sostituzione gap: penalizzazione per i gap
        '''

        # Crea le matrici F e T utilizzando il metodo _create_matrices
        F,T= self._create_matrices(matrix, gap)

        # Inizializza le sequenze allineate
        aln1= ""
        aln2= ""

        # Inizia il backtracking dal basso a destra (angolo inferiore destro)
        row=len(self.seq2)
        col=len(self.seq1)

        # Ciclo fino a raggiungere l'angolo in alto a sinistra
        while row!=0 or col!=0:
            # Se la direzione è diagonale ('d'), allinea entrambi i caratteri
            if T[row][col]=='d':
                aln1=aln1+self.seq1[col-1]
                aln2=aln2+self.seq2[row-1]
                row = row - 1
                col = col - 1
            # Se la direzione è verso sinistra ('l'), aggiungi un gap alla sequenza 2
            elif T[row][col]=='l':
                aln1=aln1+self.seq1[col-1]
                aln2=aln2+"-"
                col=col - 1
            # Se la direzione è verso l'alto ('u'), aggiungi un gap alla sequenza 1
            else: # T[i][j] == 'u'
                aln2=aln2+self.seq2[row-1]
                aln1=aln1+"-"
                row=row-1
        # Restituisce le due sequenze allineate e il punteggio finale
        return aln1, aln2, F[-1][-1]


# Esegui l'algoritmo Needleman-Wunsch se il file viene eseguito come script
if __name__ == '__main__':
    # Crea un oggetto SeqPair con le sequenze da allineare
    myobj = SeqPair("TCA", "TA")
    # Carica la matrice di sostituzione da un file chiamato TTM.txt
    submat = Substitutionmatrix("../TTM.txt")
    # Esegui l'allineamento Needleman-Wunsch e ottieni le sequenze allineate e il punteggio finale
    aln1, aln2, score =myobj.needleman_wunsch(submat, -2)
    # Stampa i risultati
    print(aln1)
    print(aln2)
    print("Score: ", score)
#Come funziona l'algoritmo con questa matrice:
#Match (Corrispondenza): I nucleotidi uguali ricevono un punteggio positivo (ad esempio, A-A o T-T hanno un punteggio di +2).
#Mismatch (Sostituzione non corrispondente): I nucleotidi diversi ricevono un punteggio negativo (ad esempio, A-T ha un punteggio di -1).
#Gap penalty: Ogni volta che viene inserito un gap, viene applicata una penalizzazione di -2.

#output:
#ACT
#A-T
#Score:  2.0





