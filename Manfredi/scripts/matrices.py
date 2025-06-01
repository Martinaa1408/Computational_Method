#use the file TTM.txt per rappresentare una matrice di sostituzione
#leggere una matrice di sostituzione da un file chiamato TTM.txt e accedere ai valori di quella matrice utilizzando due nucleotidi come chiavi.
class Substitutionmatrix:
    def __init__(self, filename):
        '''
        dictionary of dictionaries
            keys: nucleotide
            values: dictionary
                keys: nucleotide
                values: numbers
        '''
        # Apertura del file per la lettura
        with open(filename) as reader:
            # Leggi la prima riga per ottenere i nucleotidi (colonne e righe della matrice)
            line = reader.readline()
            # Rimuovi gli spazi iniziali e finali e separa i nucleotidi in una lista
            characters = line.strip().split()

            # Inizializza il dizionario principale che conterrà la matrice di sostituzione
            self.values = {}

            # Crea una voce nel dizionario per ogni nucleotide (come chiavi)
            #Le chiavi del dizionario principale sono nucleotidi(come 'A', 'T', 'C', 'G').
            #I valori per ogni chiave sono altri dizionari, in cui le chiavi sono sempre i
            #nucleotidi e i valori sono numeri che rappresentano i valori di sostituzione tra i nucleotidi.
            for char in characters:
                self.values[char] = {}

            # Per ogni riga successiva nel file, che contiene i valori della matrice
            for line in reader:
                # Dividi la riga in base agli spazi
                splitted_line = line.strip().split()
                # Il primo elemento della riga è il nucleotide di riferimento (char1)
                char1 = splitted_line[0]

                # Soluzione 1: utilizzo di un indice per associare i valori
                # Itera sui valori della riga a partire dal secondo elemento
                for i in range(1, len(splitted_line)):
                    # Popola il dizionario con i valori
                    self.values[char1][characters[i - 1]] = float(splitted_line[i])

                # Soluzione 2: usando la funzione zip per associare direttamente i nucleotidi ai valori
                # Questa parte è commentata, ma è un'alternativa
                # for char2, val in zip(characters, splitted_line[1:]):
                # self.values[char1][char2] = val

    # Metodo per ottenere un valore dalla matrice usando due nucleotidi come chiavi
    def __getitem__(self, key):
        key1, key2 = key
        # Restituisce il valore corrispondente nella matrice (es. "A", "T")
        return self.values[key1][key2]


# Verifica se il file è eseguito direttamente
if __name__ == "__main__":
    # Creazione dell'oggetto della classe SubstitutionMatrix, passando il nome del file
    matrix = Substitutionmatrix("TTM.txt")

    # Stampa il valore nella matrice per la sostituzione tra 'A' e 'T'
    print(matrix["A", "T"])
    print(matrix["A", "C"])
    print(matrix["A", "G"])
    print(matrix["T", "A"])
    print(matrix["T", "C"])


#    A  T  C  G
# A  2 -1 -1  0
# T -1  2  0 -1
# C -1  0  2 -1
# G  0 -1 -1  2