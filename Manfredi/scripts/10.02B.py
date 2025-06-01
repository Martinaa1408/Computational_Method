from exammm import SubstitutionMatrix
from exammm import SequencePair
from exammm import AlignedSequences  # Importiamo AlignedSequences
#oppure: from exammm import SubstitutionMatrix, SequencePair, AlignedSequences

class Seq(SequencePair): #ok
    def __init__(self, seq1, seq2): #ok
        super().__init__(seq1, seq2) #ok

    def alignment(self, matrix, gap, algorithm): #trattare in maniera più intelligente algorithm
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
            start_row, start_col = 0, 0 #difatti non c'è il bisogno di richiamare le lunghezze delle sequenze
            for i in range(len(self.seq1) + 1):
                for j in range(len(self.seq2) + 1):
                    if F[i][j] > max_score:
                        max_score = F[i][j]
                        start_row, start_col = i, j

            i, j = start_row, start_col #indentazione corretta
            aln1 = ""
            aln2 = ""

            while T[i][j] != '': #ricordati il diverso
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

#Verifica dei requisiti della traccia
#Importazione del modulo
#✅ Il codice importa correttamente le classi dal modulo exammm (che sembra corrispondere al file B_exam_text.py).

#Estensione della classe SequencePair
#✅ La classe Seq estende SequencePair e aggiunge il metodo alignment() per calcolare l’allineamento.

#Il metodo alignment() accetta i tre parametri richiesti
#✅ Il metodo alignment() prende in input:

#Un oggetto SubstitutionMatrix per la matrice di sostituzione.
#Un intero negativo come gap penalty.
#Una stringa ("nw" o "sw") per selezionare l’algoritmo.
#Il metodo restituisce un oggetto AlignedSequences
#✅ Il metodo alignment() restituisce correttamente un'istanza di AlignedSequences.

#Main che testa il codice
#✅ Il codice nel blocco if __name__ == '__main__': esegue i seguenti passi:

#Crea un oggetto SubstitutionMatrix caricando PAM250.txt.
#Crea un oggetto Seq con le sequenze AAAAACCCC e RRRRCCCC.
#Calcola sia un allineamento globale (nw) che un allineamento locale (sw).
#Stampa i risultati.

#Objects are an abstraction including both some data and the functions to work on them (called methods)
#A class describes a type of object
#One can define a class and then instantiate objects from it
#We have to define:
# How to create objects (constructor)
# How to work on them (methods)
#Classes are blocks which start with the class keyword, followed by the class name
#They define a number of functions, called methods
#The first parameter of each method is self, which refers to the current object of the class
#Variables prefixed by self are instance variables, there is one copy per object of the class
# The constructor initializes the instance variables of the class
#Instance variables should not be used directly from outside the class, only via methods
#This allows one to change the internal representation of the class without the need to change programs using it
#This is called encapsulation
#You may define classes starting from other classes
#Subclasses have their own constructor
#Subclasses inherit instance variables and methods from the superclass
#Subclasses may have additional instance variables
